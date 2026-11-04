# Requirements

## Problem statement

The project will build a persistent perception system for a robot workspace. The system should use RGB-D observations and computer vision to identify relevant objects, estimate their 3D state, remember that state over time, detect changes, and make the resulting world state available through ROS 2.

PNNL has provided a USD digital twin of the laboratory environment and associated texture assets. The digital twin is the team's initial simulation environment while physical-camera integration is still being established.

## Functional requirements

### FR1: Load or receive RGB-D scene observations
The system shall accept RGB and depth observations from the selected physical camera or an approved simulated source.

**Acceptance criterion:** The first walking-skeleton pipeline can consume one approved simulated or recorded scene observation without error.

### FR2: Detect or segment relevant objects
The system shall identify relevant workspace objects using a selected vision model such as SAM 2 or another model chosen after compatibility testing.

**Acceptance criterion:** On an agreed sample scene, the pipeline produces at least one object detection or segmentation result with an associated identifier or class.

### FR3: Maintain object identity over time
The system shall maintain a persistent identifier for an object as new observations arrive.

**Acceptance criterion:** Updating an already-known object changes its state without creating a duplicate object identity.

### FR4: Maintain 3D object state
The system shall store the latest known 3D location and state for tracked objects.

**Acceptance criterion:** A known object's stored 3D position can be updated and queried.

### FR5: Preserve state through temporary occlusion
The system shall retain the last known state of an object while the object is temporarily not visible.

**Acceptance criterion:** When a tracked object is absent from one or more observations, its identity and last known state remain available.

### FR6: Expose world-state information through ROS 2
The system shall expose world-state information through a reusable ROS 2 interface.

**Acceptance criterion:** A ROS 2 consumer can receive or request the current world-state representation through the agreed interface.

### FR7: Load the partner-provided simulation environment
The team shall be able to open the PNNL-provided USD digital twin in the agreed Isaac Sim environment once the HPC configuration is available.

**Acceptance criterion:** The scene loads without blocking asset errors and the expected lab geometry and textures are visible or otherwise verified in the runtime.

## Non-functional requirements

- Favor a simple, maintainable design over unnecessary complexity.
- Keep perception, tracking, and world-state components modular enough to test independently.
- Keep repository setup reproducible from a clean clone.
- Do not commit credentials or partner-confidential information.
- Avoid committing partner-provided digital-twin assets to the public repository unless PNNL explicitly approves redistribution.

## Constraints

- The project is sponsored by PNNL and must respect partner confidentiality and redistribution requirements.
- The project is being built from scratch rather than extending an inherited product codebase.
- PNNL has provided a USD digital twin and texture assets, but the team has not yet validated the scene on the intended HPC environment.
- The team is targeting Isaac Sim 6.1 for the current digital-twin work.
- Isaac Sim 6.1 officially supports ROS 2 Humble and Jazzy. NVIDIA recommends Jazzy on Ubuntu 24.04; Humble is supported on Ubuntu 22.04.
- The exact HPC GPU, driver, Ubuntu, CUDA, and ROS 2 configuration still needs to be verified.
- Physical RGB-D hardware availability remains an external dependency.

## Success metrics

Initial walking-skeleton success metrics:

- CI passes on the named checkpoint commit.
- At least one known-result automated test would fail if its covered behavior broke.
- The documented quickstart works from a clean clone.
- The PNNL-provided USD scene can be opened in the agreed Isaac Sim/HPC environment once that environment is available.
- The first end-to-end research pipeline can process an agreed simulated scene observation and produce inspectable object/world-state output.

Later project metrics will cover tracking correctness, occlusion recovery, detection range, object count, and runtime performance after those targets are agreed with PNNL.

## Non-goals

For Repo Checkpoint 1, the project does not attempt to:

- complete the production perception pipeline;
- finalize robot motion planning or control;
- publish the PNNL digital-twin assets;
- finalize the persistent world-state architecture before the RFC decision is complete;
- claim that Isaac Sim/HPC integration is working before it has actually been verified.

## Open questions

- What exact HPC GPU, driver, CUDA, Ubuntu, and Isaac Sim configuration will be used?
- Will the ROS 2 environment use Humble on Ubuntu 22.04 or Jazzy on Ubuntu 24.04?
- What simulated sensor outputs should be produced from the digital twin for the first walking skeleton?
- Which vision model best fits the agreed Isaac Sim, ROS 2, Ubuntu, and GPU environment?
- What detection distance should the system support?
- How many relevant objects should the system handle in a single frame?
- What final ROS 2 message/service interface will expose the world state?
- What final representation will be used for persistent world-state storage?
