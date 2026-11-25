# RFC: Choosing a Persistent World-State Representation

Author: Haddy Alnasser
Date: November 21, 2026
Status: Proposed
Decision Date: Not yet decided
Deciders: Project 41 team with PNNL partner input
Superseded By: None

## Problem and Context

Our Oregon State University capstone team is working with Pacific Northwest National Laboratory (PNNL) on a perception system for a robot workspace. The goal is to help a robot recognize objects in a lab and remember what happened to them, even when the camera moves or an object is temporarily blocked. PNNL is our partner and a potential user of the research results. The immediate consumers are the perception, tracking, and mapping components sharing object information. A future robot would use it to locate objects and detect changes.

The system is planned around RGB-D cameras, which provide color images and depth measurements. Our team currently uses YOLO segmentation to detect objects and visualize predictions on digital-twin images. We also plan to explore Segment Anything Model 2 (SAM 2) for later perception and visualization work. Neither model determines how the world state is stored: other components must associate detections with object identities and 3D locations, then share that information through Robot Operating System 2 (ROS 2), the communication framework for the robot's software. Our November 18 demo showed the initial image-perception path, not a working persistent world model [1]. The current repository has a small function and test confirming that a stored position can be updated without creating another object ID [2].

The decision is how to represent and store persistent world state. Each object needs an ID, class, 3D pose, last-seen time, and visibility state. We may also need relationships: a vial is on a particular table, a bottle was previously at another location, or an object was observed by a camera. A representation chosen now will eventually be used by perception, tracking, mapping, visualization, and ROS 2 interfaces.

Getting the representation wrong matters beyond developer inconvenience. A robot could act on an outdated location, treat a temporarily hidden object as gone, or report two identities for one physical object. Slower or inconsistent updates could make its map disagree with what the camera just saw. We need to make the interface decision before several modules depend on incompatible assumptions. If we do nothing, separate modules may invent their own formats. Replacing those formats after integration would be much harder than changing a small prototype now.

## Options

### Option A: Simple in-memory lookup table

Store objects in a Python dictionary keyed by persistent ID, with fields for class, pose, visibility, time last seen, and confidence. The existing world-state Python module already demonstrates this basic direction [2]. It is simple, quick to test, and needs no database server. For a small scene with only object-by-ID queries, this may be all we need.

Relationships would require extra lists or indices kept synchronized after moves. Persistence and historical queries also need extra code. Choose this if most operations are independent object lookups and relation queries add little value.

### Option B: SQLite relational storage

Store objects, observations, and relationships in tables with IDs linking records. SQLite runs without a separate server and stores data in a portable file [3]. Its transactions can group updates so a partially completed write does not leave the database in an inconsistent state [4]. It also makes historical records and debugging queries easier to inspect.

Costs include schema design, migrations, and joins. A database is not necessarily faster for in-memory updates. Choose this if durable history, reliable recovery after restart, or structured queries matter more than a flexible spatial relationship model.

### Option C: Lightweight graph-based world model

Represent objects and locations as nodes with properties, and relationships such as on, near, and previously at as edges. The graph could initially live in Python memory and serialize to a local file. This matches the type of information we may eventually need. Kimera describes a robotics approach based on spatial and semantic scene graphs [5], and Hydra describes incremental construction of 3D scene graphs [6]. These papers support investigating a graph, but they do not prove one will be best for our smaller system.

Costs include custom edge rules, identity handling, persistence, and lookup overhead. Choose this if the demo and planned queries genuinely depend on relationships changing over time and a prototype shows manageable implementation and runtime cost.

### Option D: Do Nothing for Now

Let each subsystem store whatever it needs while the perception work is still experimental. This avoids blocking image and model tests today. It is a reasonable temporary choice while components have no shared consumers.

After integration, costs include duplicated converters, inconsistent IDs, and unclear state ownership. Choose this only for isolated experiments with a deadline to revisit the decision before shared interfaces are merged. It is not a viable long-term architecture.

### Option E: Reuse an existing graph implementation

Instead of writing all graph operations ourselves, evaluate a maintained graph library or a reusable component from a research implementation such as the systems described by Kimera or Hydra [5, 6]. Reuse could reduce custom code and provide tested operations for adding nodes and traversing edges. It could also help if PNNL expects to extend the work later.

The cost is learning another interface, adapting its data model, checking the license and dependencies, and possibly importing far more mapping functionality than our prototype needs. We have not verified that any specific library fits our ROS 2 and Python environment. Choose this only if a small integration test shows a useful fit and the license, maintenance burden, and deployment requirements are acceptable.

## Analysis

The central tradeoff is how much structure to introduce before we know the final workload. We have a dictionary update test, not a measured graph or integrated tracker [2]. The November 18 demo shows labeled digital-twin images and initial YOLO segmentation, but no world-state performance data [1]. SAM 2 remains planned for later perception and visualization. Changing models should not require changing the stored object representation.

Option A has the smallest setup cost and is a useful baseline. It also makes failures easy to inspect during early testing. If all we need is an object ID and latest pose, the extra machinery of a graph brings little value. Frequent relationship queries demand additional structure and safeguards against stale links.

Option B is the strongest choice for local persistence and audit history. SQLite documents both its serverless model and transactional behavior [3, 4]. That is helpful if losing object history on restart would make the prototype unusable. However, persistence is a separate question from representation. We could use an in-memory graph while writing snapshots to SQLite or JSON later. Choosing one does not automatically require choosing the other.

Option C offers a more direct vocabulary for relationships. The robotics literature shows why spatial and semantic connections matter in world models [5, 6]. Still, a full scene graph is not necessary just because our system has 3D coordinates. We would have to demonstrate that on, inside, or previous location queries are needed and stay correct after movement and occlusion. Stale graph edges would defeat that purpose.

Option E deserves a real check rather than being dismissed. Reusing graph code may save implementation time, but only if the dependency is understandable and practical in our environment. Kimera and Hydra are useful research references, not drop-in dependencies we have already validated [5, 6]. I would first inspect the required runtime, license, and the portion of the implementation we actually need. A heavyweight mapping stack could make the capstone harder to maintain.

Security and cost do not sharply separate A through C for our current local prototype. None requires a paid hosted database, and a local graph is not automatically safer than SQLite. The bigger risks are partner-data exposure, dependencies, and interface changes. For that reason I favor a small graph prototype behind a stable API, with a dictionary comparison and an explicit path to reject the graph. I would not deploy a separate graph server at this stage.

## Recommendation and Verification Plan

I recommend Option C, a lightweight in-memory graph model, but only provisionally. It should expose simple operations to add or update an object, set a relationship, mark an object as unobserved, look up an object, and find objects at a location. Other modules should use this API so switching to Option A or B remains possible.

A starting record would store an object ID, class, pose, visibility state, last-seen timestamp, and confidence. Separate typed edges would connect an object to a location or another object. Each edge would have a type and updated timestamp. For example, moving a vial from one table to another must remove its old on edge, add the new one, and leave other objects unchanged. Out of view must differ from missing. One unseen frame cannot remove an object.

Comparison setup. Before merging a shared state interface, build the same five operations against Option A and Option C. Use a deterministic recorded event stream, not a live model, so detection errors cannot hide storage bugs. Start with 20 objects across three work areas and 100 ordered observations. Include six object moves, six intervals of occlusion followed by reappearance, and at least six changes to on or inside relationships. Keep the object IDs and expected answers in a checked-in test fixture. Run the same workload on the same development machine, with Python and input fixed, and repeat timing tests five times. These are planned, not measured, conditions.

Acceptance and rejection checks:

1. Identity and visibility: All 20 objects retain their IDs across updates. No move creates a duplicate. Occlusion keeps the last known pose. A later observation restores the visible state. Every expected state transition must pass.

2. Relationship correctness: After each of the six relationship changes, the location lookup and an object- history query must return the expected current and previous locations with no stale edges. Test a move while an object is temporarily occluded. This is the key test for the graph recommendation. Basic object lookup alone is not enough.

3. Save and reload: If the chosen representation claims persistence, serialize it, restart a fresh process, and verify the same IDs, states, and relationships. If durable history is deferred, record that limitation instead of calling the prototype persistent across restarts.

4. Performance: Log per-update and relation-query durations with time.perf_counter, then report median and 95th-percentile latency for both prototypes. The provisional ceiling is 100 ms at the 95th percentile for this small, local test. This is a ceiling to investigate, not a measured requirement from PNNL.

5. Integration: Feed one stored world state through a simple ROS 2 message adapter once the ROS 2 package is ready. Verify the subscriber receives the correct IDs, poses, and visibility states. Until then, a JSON export test is an explicit substitute, not proof that ROS 2 works.

The graph is rejected if it fails any identity or relationship test, cannot be kept consistent during movement, or exceeds the latency ceiling after one reasonable fix. If both graph and dictionary pass, the team will compare how much additional code and manual indexing each needs for relationship updates. If the graph provides no clear benefit for the actual queries, we should keep the simpler dictionary behind the same API. SQLite remains the fallback if restart-safe history becomes a requirement. This makes the experiment capable of changing the recommendation instead of merely confirming it.

The Project 41 team should run and review the comparison before merging a shared world-state API. PNNL can comment on whether the chosen queries reflect the lab use case at the next design review. The team makes the decision. Record the test results, chosen alternative, date, and reviewers in this RFC when that happens. A working segmentation demo is encouraging, but it is not evidence that the world-model representation has passed these tests.

## Constraints

PNNL has provided lab simulation assets for the capstone. We should not put those assets, restricted images, credentials, or configuration details into a public repository or an external service without permission. The storage prototype can instead use synthetic IDs and scene events with the same structure as the real workload. This rules out using partner assets as public test fixtures, not the underlying design comparison.

If we adopt a graph library or code from another robotics project, we must check its actual license, transitive dependencies, and redistribution terms before making it part of our repository. Until that check, Option E is an investigation, not an approved dependency. Local Python structures and SQLite avoid a hosted third-party data processor. An external graph service would need a separate confidentiality and deployment review.

The planned model also should not store more visual or personal information than needed. Object class, pose, state, and timestamps are enough for this decision. Raw camera images and identity information about people do not need to be copied into every object record. These constraints favor a narrow API and local, inspectable storage while the team works with PNNL on the data-use boundaries.

## Delegation and Validation

I used ChatGPT to help organize the options, compare their tradeoffs, revise this draft using feedback, and turn the proposed tests into a clearer decision rule. AI suggestions are not evidence that a graph implementation works. For project evidence, the current code and test are identified in the repository [2], and the November 18 team presentation is identified separately [1]. For outside claims, I used the SQLite documentation and the Kimera and Hydra publications already referenced in the earlier draft [3-6]. None constitutes a project benchmark.

I have not completed the head-to-head prototype comparison or accepted the architecture on the team's behalf. The checkpoints that still require human validation are: checking any reused library's license before adopting it. Reviewing the object-and-edge schema before other modules depend on it, and examining actual test failures, latency logs, and ROS 2 outputs before changing this RFC to Accepted. The shared schema is costly to change. Relationship tests could disprove the case for a graph.

The existing repository test is a useful safety net for duplicate IDs, but it does not check edges, persistence, or ROS 2 [2]. We should add focused tests on a branch, run CI, and ask another teammate to review the interface before merging. A failed check should lead to a simpler representation or a revised recommendation, not a claim that the decision was already validated.

## Decision

Status: Proposed. No final representation has been accepted by the team. I recommend a lightweight graph behind a shared interface, conditional on the explicit comparison above. If it does not offer correct and maintainable relationship behavior, the team should choose the simpler dictionary or SQLite alternative. The decision date and final deciders will be updated only after the prototype review.

## References

1. Project 41 team. PNNL progress demonstration, November 18, 2026, (11-17 Demo.pdf). Shows the staged architecture, simulated image set, and segmentation examples

2. Project repository, Wade-Owo/Rob_Capstone (https://github.com/Wade-Owo/Rob_Capstone).

3. SQLite. About SQLite (https://www.sqlite.org/about.html).

4. SQLite. SQLite Is Transactional (https://www.sqlite.org/transactional.html).

5. Rosinol, Antoni, et al. Kimera: From SLAM to Spatial Perception with 3D Dynamic Scene Graphs (https://dspace.mit.edu/entities/publication/5c3c1c1f-e2e2-463d-be86-7b2657d1477c), MIT.

6. Hughes, Nathan, et al. Hydra: A Real-time Spatial Perception System for 3D Scene Graph Construction and Optimization (https://dspace.mit.edu/entities/publication/2540dea5-c925-439d-92ec-b78405cda4e1), MIT.
