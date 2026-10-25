# RFC: Choosing a Persistent World-State Representation

| Field | Value |
| --- | --- |
| Author | Haddy Alnasser |
| Date | 2026-10-25 |
| Status | Proposed |
| Decision Date | Not yet decided |
| Deciders | Project 41 team with PNNL partner input |
| Superseded By | None |

## Problem and Context

Our project is building a perception system that allows a robot to remember and understand its surroundings over time. RGB-D camera data and computer vision models such as SAM 2 will identify objects in the workspace, estimate their 3D locations, and track changes. The system then needs somewhere to store that information so the robot can answer questions such as what objects are currently present, where an object was last seen, whether it moved, and whether it is temporarily hidden.

The decision we need to make is how this persistent world state should be represented and stored. This is important to decide early because most of the perception pipeline will eventually depend on this interface. Object tracking, change detection, occlusion recovery, visualization, and ROS2 communication will all read from or write to the world state. Changing the representation later could require changes across several parts of the system.

This is also a real decision that our team has not finalized yet. Our early planning identified storage of the 3D map as a hard-to-reverse decision. The goal is not simply to save coordinates. The representation needs to support objects, their 3D poses and states, timestamps, semantic labels, and eventually relationships between objects and locations.

If we do nothing, individual parts of the project could begin storing object information in their own formats. This would make integration harder later and could create multiple incompatible representations of the same environment.

## Options

### Option A: Simple In-Memory Lookup Table

The first option is a Python-based lookup table or dictionary. Each object would have an ID and fields such as its label, 3D position, last observation time, confidence, and current state.

This would be the simplest option to build and would let the team begin integration quickly. It would also have very little infrastructure overhead.

The main cost is that relationships between objects would have to be added manually, and persistence would require a separate serialization format such as JSON. As the system becomes more complex, a flat structure could become difficult to maintain.

This option would be appropriate if the final system only needs a relatively small number of independent objects and simple position lookups.

### Option B: SQLite Relational Storage

The second option is to represent the world state using SQLite. Objects, observations, locations, and relationships could be stored in tables and queried through SQL.

[SQLite](https://www.sqlite.org/about.html) is serverless, requires very little database administration, and stores the database in a single portable file. It also provides [ACID transactions](https://www.sqlite.org/transactional.html), meaning updates can be committed atomically and recovered consistently after application or system failures.

This would give the project reliable persistence and a well understood query system without requiring a separate database server. It would also make it straightforward to inspect or export stored data.

The tradeoff is that a relational structure may become awkward as relationships between objects become more important. Queries involving many connected entities can require multiple joins and a more rigid schema. This option would be appropriate if persistence and structured historical queries are more important than representing complex spatial relationships.

### Option C: Graph-Based World Model

The third option is a graph-based world model. Objects, locations, and potentially rooms or robot states would be represented as nodes, while relationships such as inside, near, observed by, or previously at would be represented as edges. Each node could also contain properties such as its 3D pose, semantic label, timestamp, and tracking confidence.

This representation is similar to approaches used in robotics research. [Kimera](https://dspace.mit.edu/entities/publication/5c3c1c1f-e2e2-463d-be86-7b2657d1477c) represents dynamic environments using 3D dynamic scene graphs in which nodes represent spatial concepts and edges represent spatial or temporal relationships. [Hydra](https://dspace.mit.edu/entities/publication/2540dea5-c925-439d-92ec-b78405cda4e1) extends this concept into a system that incrementally constructs 3D scene graphs in real time.

Graph representations also match the type of information our project is expected to maintain. Our world state is not only a list of objects. It must also capture how objects relate to locations and how those states change over time.

The main cost is additional implementation complexity. The team would need to define the graph structure carefully and determine how updates, object identity, and persistence work. A full external graph database could also introduce unnecessary infrastructure. A lightweight graph structure implemented within the Python application may therefore be more appropriate than immediately introducing a separate graph database service.

This option would be appropriate if relationships and long-term extensibility are important parts of the final world model.

### Option D: Do Nothing for Now

The final option is to postpone the decision and allow each subsystem to keep whatever representation is easiest during early development.

This minimizes short-term work and may make sense while we are still waiting on hardware and validating the perception pipeline.

The cost is integration risk. If segmentation, tracking, mapping, and ROS2 components each begin depending on different object structures, changing them later could require substantial rework. This option is only reasonable for very early prototypes that do not yet cross component boundaries.

## Analysis

The main tradeoff is simplicity versus long-term structure.

An in-memory lookup table would be easiest to implement and would likely be fast enough for basic object lookup. However, it provides little structure for relationships and would require separate work for reliable persistence.

SQLite provides stronger persistence and transactional guarantees with very little operational overhead. Its single-file design also makes it attractive for a local robotic system. However, the project is specifically intended to represent a changing spatial environment, not just store independent records.

A graph model has greater implementation complexity, but it maps more naturally to the project's longer-term goals. Robotics work on dynamic scene graphs demonstrates that graph representations can combine geometry, semantics, objects, places, and relationships within one world representation. Hydra has also demonstrated that these structures can be constructed incrementally in real time instead of only offline.

Performance is still uncertain because our team has not yet built enough of the perception pipeline to measure the expected size or update rate of the world state. A simple lookup table would probably have lower overhead for basic queries. A graph structure could require additional processing, especially as more relationships are added. However, the additional structure may reduce complexity elsewhere by giving every component a consistent way to access world-state information.

Maintainability is another important consideration. The representation selected now may eventually become an interface shared by segmentation, tracking, mapping, visualization, and ROS2 components. A simple design is useful early, but if it cannot represent the relationships the project later requires, changing it could affect multiple parts of the system.

Security differences between the three main options are relatively small for our current prototype because world-state information is expected to remain within the local robotic system and does not contain credentials. The larger concerns are maintainability, persistence, and compatibility with the rest of the architecture.

Cost is also relatively small for all three options. An in-memory structure and SQLite require no additional hosted infrastructure. A lightweight graph implementation could also remain entirely local. A separate graph database would create additional setup and maintenance costs, which is one reason I would not recommend using one at this stage.

There is still uncertainty because we do not yet know exactly how much information the final world model will need to contain. Because of that, the recommendation should be validated with a small prototype before the team commits deeply to the representation.

## Recommendation and Verification Plan

I recommend Option C: a graph-based world model, initially implemented as a lightweight Python data structure instead of deploying a separate graph database.

This gives us the flexibility of a scene graph without adding unnecessary infrastructure early in the project. Each detected object can be represented as a node containing its ID, class, 3D pose, state, confidence, and timestamps. Relationships can be added later as the system begins representing locations, containment, proximity, or other spatial information.

Before committing to this representation, the team should build a small prototype and compare it with a basic lookup-table implementation.

The recommendation will be considered successful if the prototype can:

1. Add multiple detected objects to the world state.
2. Update an existing object's 3D position without creating a duplicate identity.
3. Preserve the last known state when an object becomes temporarily unobserved.
4. Recover and update the same object when it becomes visible again.
5. Return an object's current and previous state by ID.
6. Publish a simplified representation through a ROS2 interface.
7. Save and reload the world state without losing object identities or relationships.

The team should also measure update and query latency for the graph and lookup-table prototypes using the same simulated scene. If the graph representation creates unacceptable overhead for the expected workload, the team can reconsider before other components depend on it.

This verification plan is important because the choice is difficult to reverse once multiple parts of the project start depending on the same world-state interface. Testing the representation early gives the team a chance to change direction before that happens.

## Constraints

Licensing is not currently a major constraint if we implement the graph structure ourselves using Python and permissively licensed libraries. If we later adopt an external graph technology, its license will need to be reviewed before it becomes a core project dependency.

The system will use RGB-D and simulated environment data. Any PNNL-provided data must remain within the confidentiality rules established with the partner. Our team agreement allows non-sensitive project code and information to be used with approved AI tools, but credentials and partner-confidential material cannot be shared externally.

The representation itself should therefore avoid embedding credentials, restricted configuration values, or unnecessary partner-specific information in stored object records.

IP is also relevant because the architecture and implementation are part of a sponsored capstone project. Before introducing a third-party database or library as a core dependency, the team should confirm that its license and intended use are compatible with the project.

At this point, there do not appear to be additional data-use restrictions that change the storage decision itself, but this could change if PNNL provides confidential datasets or other restricted resources later in the project.

## Delegation and Validation

I used ChatGPT to help identify possible storage approaches, locate technical sources, compare tradeoffs, and organize the first draft of this RFC. I did not delegate the final project decision to the AI tool.

I validated the suggested graph approach against published robotics work on Kimera and Hydra, which use 3D scene graphs for spatial and semantic representations. I also checked SQLite's official documentation for its persistence and transaction behavior rather than relying only on generated descriptions.

I compared the recommendation against our team's own project planning. Our project requires persistent object identities, 3D positions, changes over time, and eventual ROS2 access, so I focused on options that could support those requirements.

Our repository does not yet have automated tests or CI capable of validating this architectural decision. Because of that, the main validation step before committing to the representation will be a small prototype and team review.

The point where I would stop and validate the result myself is before defining the shared world-state interface that other components will depend on. I would verify that object identities persist correctly, that updates do not create duplicate objects, and that the representation can support the ROS2 interface we plan to expose.

This is important because once multiple components depend on the interface, changing the representation would require significantly more work than changing it during the prototype stage.

## Decision

**Proposed**

The team has not yet selected the final world-state representation. This RFC recommends using a lightweight graph-based representation, pending prototype results and review from the team and PNNL partners.

## References

- SQLite. "About SQLite."  
  https://www.sqlite.org/about.html

- SQLite. "SQLite Is Transactional."  
  https://www.sqlite.org/transactional.html

- Rosinol, Antoni, et al. "Kimera: From SLAM to Spatial Perception with 3D Dynamic Scene Graphs." MIT.  
  https://dspace.mit.edu/entities/publication/5c3c1c1f-e2e2-463d-be86-7b2657d1477c

- Hughes, Nathan, et al. "Hydra: A Real-time Spatial Perception System for 3D Scene Graph Construction and Optimization." MIT.  
  https://dspace.mit.edu/entities/publication/2540dea5-c925-439d-92ec-b78405cda4e1
