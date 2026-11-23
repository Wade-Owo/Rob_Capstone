# RFC: Training data pipeline

Project 41: Persistent AI World Models for Robot Workspaces/Persistent 3D Scene Understanding for Robot Workspaces

CJ Chavez <chavezco@oregonstate.edu>

| Field | Value |
| --- | --- |
| Author | CJ Chavez |
| Date | 2026-10-25 |
| Status | Proposed |
| Decision Date | N/A |
| Deciders | N/A |
| Superseded By | N/A |

## Problem and Context

For Project 41,  "Persistent AI World Models for Robot Workspaces/Persistent 3D Scene Understanding for Robot Workspaces", the team is working towards developing a persistent representation of a real-world robot workspace. The goal is to create a system that can recognize objects, track changes in their positions, and maintain information about objects even when temporarily hidden from view. This is important work for robotic systems as they stay in dynamic environments where human and robots are interacting within the same space. By maintaining an accurate representation of the workspace, a robotic system can make decisions based on current observations and past information.

To create this system, the team needs to collect and process information about the environment. This includes identifying objects from images, using depth information to estimate their positions in 3D space and updating their representation when changes happen. The data collected and processed through this pipeline will establish the foundation for testing object detection and tracking. Without a reliable source of data, the team cannot fully evaluate whether its world model accurately represents the changes in the workplace.

The decision addressed in this RFC is whether the team should use real-world RGB-D camera data to establish its initial workspace, create a fully simulated environment using cloud-based software, or combine real-world data collection with simulation. This decision determines the resources, software dependencies, and development methods needed to build and evaluate the system. 

The team is currently considering these approaches based on resources available through OSU and our project partners at PNNL. PNNL has agreed to provide an RGB-D camera, making real-world data collection a feasible starting point. However, developing a fully simulated environment could provide additional flexibility for creating and modifying workspaces without dependending on physical objects or camera observations. 

## Options

### Option A: RGB-D camera origin

We would use an RBG-D camera to capture a real world working environment at Oregon State. This option would allow the team to create a virtual environment based on a real world environment we have access to and make real world decisions directly in front of and outside the view of the RGB-D camera to test how persistent the model is at understanding the changes in the real environment and applying that to the virtual environment. This is beneficial in being able to work on campus and have an environment to compare for verification of accuracy. The cost of this option would primarily come from the development time required to integrate the RBG-D camera with our decided software and how we use the data collected to change into 3D items.

### Option B: Complete simulation and AWS Cloud

We wouldn't consider real world tracking at all but rather virtually create a workspace and its items. All changes that would need to be considered would be done virtually and checked virtually. This option would be benefical in allowing collaboration between the team and our partners at PNNL located in Washington. The cost of this option would primarily come from the learning curve and development to create only a simulated workspace. Additionally, the infrastructure needed for the cloud software needs a lot of compute power and storage to support it which can be a struggle for the team.  

### Option C: Hybrid RGB-D Camera and Simulation

We would combine real-world RGB-D camera data with a simulated environment. The team would initially capture a physical workspace using the RGB-D camera and use this information to establish the objects and their positions in the virtual environment. Once the inital environment is created, the team could expand it through simulation by introducing additional objects, updating the workspace, or establishing difficult test cases. This option would allow the team to use real-world data for initial development while maintaining the flexibility of a simulated environment. Additionally, it supports testing how well the system responds to changes beyond the original workspace. The cost of this option would come from the additional development time. The team would need to verify changes are consistent in real life and in the simulated environment. 

### Option D: Do Nothing

By doing nothing, the team must find an alternative to create a virtual environment to create a 3D robot workspace. This would take more time from the team's timeline and halt software development further. The cost of this option would primarily come from lack of developing software and delaying further milestones. Without a decision on the source of training data, the team lacks a starting point for the virtual environment and what needs to be implemented in these workspaces. 

## Analysis

- Performance: Option A would be beneficial in collecting real world RGB-D data and test the accuracy of virtual environmental changes to real world changes [1]. This is beneficial because object tracking and persistence are central requirements of the project. However, the accuracy of this approach depends on the quality of the camera observations and the software used to process them. RGB-D cameras can produce incomplete or noisy depth measurements, and objects may become difficult to detect when they overlap or move outside the camera's field of view. These limitations would need to be considered when evaluating the accuracy of the workspace representation. Option B would allow the team to create controlled testing conditions where object positions and movements are already known. This would make it easier to compare expected and observed behavior without introducing camera noise. However, a system that performs well in simulation may not achieve the same performance with real-world observations. This is a concern because the project's goal includes understanding dynamic physical workspaces rather than only simulated environments. Option C could combine the advantages of both approaches by using real-world observations to establish the workspace and simulation to create additional testing scenarios. However, this would introduce additional integration requirements and would not eliminate the need to verify the accuracy of real-world tracking. Option D would prevent the team from collecting meaningful performance measurements until a development approach is selected.
- Complexity: Option A would be beneficial in reducing complexity in later deployments. The PNNL team has said they'd be willing to test our virtual environment connection to a lab on their campus. With an RGB-D camera a part of our system, the same camera they use on their robots in their lab, there would be less complexity in real world integration [2]. Option A also runs the risk of requiring heavy virtual change to match a real world workspace. Option B would be beneficial in reducing risk between real world and virtual environment dependencies and allow for easier definition of items within the virtual environment. However, an only virtual environment runs the risk of additional software dependencies and increased development complexities [3]. Option C would require integrating both the RGB-D perception pipeline and simulation software. While this provides more flexibility, maintaining consistency between the real-world and simulated environments would increase development complexity. Option D yet again would leave the team without a way to develop a virtual environment. 
- Maintainability: Option A would require camera calibration and maintenance on software used to process RGB-D data. Changes to any physical workspace may also require changes to the virtual environment in the future. Option B would require maintianing the simulation environment, its cloud infrastructure, and its software dependencies. Option C would require maintaining both systems and ensuring that updates to one do not affect the other. This could increase the workload for the team, especially if the software components are updated independently. Option D has no maintainability requirements. 
- Security: Option A would allow the team to collect and process data locally, reducing the need for cloud subscriptions. However, with the amount of training data needed, this would require storage whether that be locally or an external drive. Option B runs the risk of additional security considerations based on the cloud software used and how our virtual environments data is stored. Option C would combine these concern because real-world camera data could be transferred into a simulated environment. The team would need to ensure that data is handled securely across both systems. Option D has no immediate security risks. 
- Cost: Option A costs include camera integration, data processing, object tracking, and real world to virtual environment testing. However, the PNNL team initially stated they'd provide a RGB-D camera for our implementation and only recently stated we could have it completely virtual. With Option B, there would need to be additional time to develop the simulated environment and configure it to the cloud infrastructure. This doesn't include the actual monetary costs of maintaining this infrastructure for the 3 term of the capstone. Option C would combine the development costs of both approaches, requiring additional time for integration, testing, and maintenance. While this approach could provide more testing opportunities, it may be able to be done within the remaining capstone timeline. Option D has no immediate costs beside developmental time and delayed milestone. 
- Citations:
- [1] https://introlab.github.io/rtabmap/ Used to indicate that there are labs that have already developed systems that use RBG-D camera to create virtual environments. This is open sourced and can be a starting point for the team.
- [2] https://ieeexplore.ieee.org/document/6162880 Used to demonstrate that camera data can be used for 3D reconstruction of items and camera tracking for virtual environments.
- [3] https://docs.isaacsim.omniverse.nvidia.com/latest/installation/requirements.html The requirements of the Isaac sim that the team would be using that is dependent on the AWS cloud infrastructure. This shows just how many software dependencies the team would need to consider for costs. 

## Recommendation and Verification Plan

I recommend Option A, using the RGB-D camera as the initial source of real-world workspace data. This approach is the most feasible basedo n the resources currently available to the team and the remaining project timeline. PNNL has agreed to rpovide the camera, allowing the team to begin developing a perception pipeline without first establishing a compelte cloud-based simulation environment. While this approach introduces technical challenges involving camera calibration, depth processing, and object tracking these challenges are directly related to the project's intended functionality. 

For verification, the process would begin by confirming that the RGB-D camera can capture usable color and depth information. The team would then process the collected observations to identify objects and estimate their positions in 3D space. The resulting workspace representation would serve as the baseline for evaluating whether the system can accurately reflect changes in the physical environment. 

Once the initial workspace is established, the team would conduct controlled tests involving object movement, removal, and occlusion. For movement testing, objects would be placed in known positions and then moved to new locations. The system should recognize the objects and update their recorded positions. The team would compare estimated positions against referenc emasuremtns to calculate position error. 

For removal testing, an object would be taken out of the workspace. The team would evaluate whether the system correctly updates its recorded state rather than continuing to treat the object as visible or assigning its identity to another object. Because an object leaving the camera's view does not necessarily mean it has been removed from the workspace, the system should distinguish between observations and uncertain object states.

For occlusion testing, an object would be temporarily hidden behind another object and later revealed. The system should retain information about the hidden object's identity and last known position while indicating that the object is not currently visible. When the object reappears, the team would evaluate whether the system associated the new observation with the previously tracked object rather than treaitng it as an entirely new object. 

The team would record the results of these test, including object detection accuracy, position error, identity recovery after occlusion, and the time required to update the world model. These measurements would help determine whether the selected data pipeline supports the project's persistence requirements. Any failure would be documented so the team could identify whether the problem originates from camera observations, perception processing, or the world-state representation.

## Constraints

The main constraints affecting this decision involve software licensing, data use, intellectual property, and confidentiality.

**Licensing:** Option A would require software to process RGB-D data and generate 3D representations. The team must verify that the selected libraries and frameworks allow their intended use. Option B would introduce additional licensing considerations through simulation software and cloud services.

**Data Use:** Option A would involve collecting real-world images and depth information at Oregon State. The team must consider what information is captured and stored, particularly if individuals appear in the camera's view. Any external datasets must also be reviewed for usage restrictions.

**Intellectual Property:** PNNL has shown us its existing simulation, which is its intellectual property. While PNNL encourages us to develop our own approach and permits our work to be included in public portfolios, we must ensure our implementation does not reproduce restricted components of its system.

**Confidentiality:** Although PNNL permits public portfolio use, the team should verify that any shared code, datasets, or demonstrations do not contain restricted information belonging to PNNL.

These constraints favor Option A because the team can collect its own data and develop an independent implementation while limiting dependencies on partner-owned systems. However, software licenses and data permissions must still be verified before implementation. 

## Delegation and Validation

The use of AI tools for this assignment is governed by the AI policy established for the Oregon State University capstone course. The policy permits AI assistance with tasks such as researching options, drafting sections, and improving technical arguments, but requires students to verify the resulting work and remain responsible for their conclusions.

For this RFC, AI assistance was used to help organize and revise the written discussion of the available options and verification plan. The recommendation itself was based on the team's available resources, project requirements, meeting discussions, and external technical documentation. AI-generated suggestions were not treated as verified technical evidence.

The most important points requiring independent validation are the feasibility of the RGB-D camera pipeline, the resource requirements of the simulation approach, and the proposed methods for testing object persistence. These decisions influence the software the team will develop and could require substantial rework if the assumptions are incorrect.

The team will validate the selected approach through camera integration tests, perception evaluations, and controlled object tracking experiments. These checks are particularly important because successful object detection alone does not demonstrate that a system can maintain object identities and positions when objects are temporarily hidden or moved.

The proposed acceptance criteria will also need to be reviewed against the capabilities of the available hardware and the requirements of the project. This ensures that the final recommendation is supported by technical evidence rather than assumptions about system performance.

What is assessed is in the [AI policy](https://capstone.alexulbrich.com/assignments/introduction/#ai-policy-applies-to-every-assignment).

## Decision

Status: Proposed

The recommended decision is to use the RGB-D camera as the initial source of real-world workspace data for the project. This approach is supported by the resources currently available to the team, the project's requirements for real-world object tracking, and the development time remaining in the capstone.

PNNL has agreed to provide the team with an RGB-D camera but has not agreed to sponsor the cloud subscription needed for the proposed simulation approach. As a result, Option A provides a more accessible starting point while allowing the team to focus on implementing and verifying the core functionality of a persistent world model.

The hybrid approach remains a possible future extension if additional development time and computing resources become available. However, it is not recommended as the initial approach because it would introduce additional integration and maintenance requirements.

This recommendation has not yet been formally accepted by the team. The RFC will be updated when a decision is reached.
