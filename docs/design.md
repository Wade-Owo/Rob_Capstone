# Technical Design

## System context

The project is a research-oriented perception pipeline for persistent robot workspace awareness. It will take RGB-D observations, identify and track objects, estimate their 3D state, maintain a persistent world model, and expose that state through ROS 2.

PNNL has provided the team with a digital twin package containing a USD lab scene and associated texture assets. The team currently has local access to that package.

## Current system

At Repo Checkpoint 1, the repository contains a small Python scaffold and known-result test used to verify CI. The final perception pipeline has not yet been implemented.

Current tested flow:

```text
sample object state -> update_object(...) -> updated object state -> pytest known-result assertion
```

Planned product flow:

```text
PNNL digital twin in Isaac Sim
        -> simulated RGB-D / scene observations
        -> perception / segmentation
        -> object identity + 3D state
        -> persistent world state
        -> reusable ROS 2 interface
```

## Current integration work

- Wade: investigate running Isaac Sim on HPC and verify the provided digital twin.
- Wade and Arstanbek: establish the ROS 2 environment.
- Carter and Haddy: compare candidate vision models and setup requirements against the selected Isaac Sim, ROS 2, Ubuntu, and GPU environment.
- CJ: maintain project coordination and sprint/status reporting.

## Components

### PNNL digital twin
The partner-provided simulation package contains a USD lab scene and associated texture assets. It is treated as an external project asset and is not committed to this public repository unless redistribution is explicitly approved.

### Isaac Sim / HPC environment
The intended simulation environment is Isaac Sim 6.1 running on the agreed HPC infrastructure.

This has **not yet been validated**. The team still needs to confirm HPC compatibility and successfully open the partner-provided USD scene there.

### RGB-D input
The project will eventually consume synchronized RGB and depth observations from a physical RGB-D camera and/or an approved simulated source. The initial walking skeleton is expected to use simulated scene data.

### Perception
The perception component will run a selected vision model to detect or segment relevant workspace objects. Model selection is currently open and depends partly on environment compatibility.

### Tracking and state update
This component will associate observations with persistent object identities and update state over time.

### Persistent world state
This component stores the current and last-known state of tracked objects. The final representation is intentionally deferred while the team's RFC on world-state representation is still Proposed.

### ROS 2 interface
The final system will expose world-state information through a reusable ROS 2 interface so downstream behavior does not depend directly on perception implementation details.

## Interfaces and contracts

The final ROS 2 topic/message/service names are not yet decided.

The minimum planned object/world-state record contains:

- persistent object identifier;
- semantic label/class;
- 3D position or pose;
- observation timestamp;
- visibility/state information;
- confidence when available.

## Data model

The final data model is intentionally deferred pending the world-state RFC decision.

The current Python scaffold uses a dictionary keyed by object ID only to provide a real testable behavior for CI. It is not the final architectural choice.

## Production target

For this research project, the planned Week 10 walking skeleton is:

```text
PNNL-provided digital twin in Isaac Sim
        -> simulated scene observation
        -> initial perception step
        -> object/world-state update
        -> inspectable output
```

The intended execution target is the HPC environment the team is currently evaluating with PNNL.

The team has the digital twin, but Isaac Sim execution on HPC has not yet been validated. The exact GPU, driver, Ubuntu, CUDA, ROS 2 configuration, and sample-data path remain open until the environment is successfully tested.

**Owner for Isaac Sim/HPC setup:** Wade Owojori  
**ROS 2 setup:** Wade Owojori and Arstanbek Bulanbekov  
**Vision-model compatibility research:** Carter Cripe and Haddy Alnasser  
**Target date to update this section with the verified environment:** 2026-11-08

If the intended HPC environment cannot support Isaac Sim 6.1, the team will raise that result with PNNL and the instruction team and document the agreed equivalent environment or milestone instead of claiming the target is working.

## Staging and rollback

Until the HPC environment is working, changes are exercised using local/sample-data tests and CI.

Once the simulation environment is available, integration changes will be exercised against the PNNL-provided digital twin before they are treated as part of the working pipeline.

Repository changes can be rolled back by reverting the merged pull request or restoring the last known-good commit.

## Decisions deferred on purpose

- Final persistent world-state representation, pending RFC review and prototype validation.
- Final ROS 2 interface shape.
- Final perception/tracking model.
- Final detection-distance and object-count targets.
- Final physical-vs-simulated data mix.

## Open technical questions

- Can Isaac Sim 6.1 run reliably on the assigned HPC GPU/driver stack?
- Does the USD scene resolve all texture and asset paths in the HPC environment?
- Which supported ROS 2/Ubuntu pairing will the team use?
- Which vision model fits the final compute environment?
- What simulated RGB-D/sensor data will be generated from Isaac Sim?
- What quantitative tracking, detection, and occlusion metrics will PNNL expect?
