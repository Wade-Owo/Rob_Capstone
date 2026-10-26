# RFC: Training data pipeline

| Field | Value |
| Author | CJ Chavez |
| Date | 2026-10-25 |
| Status | Proposed |
| Decision Date | N/A |
| Deciders | N/A |
| Superseded By | N/A |

## Problem and Context

For the project "Persistent AI World Models for Robot Workspaces/Persistent 3D Scene Understanding for Robot Workspaces", the team is working towards creating a virtual environment where actions taken by automated robotic systems and humans are considered and mapped. This means items in the virtual space that are moved or hidden are understood to be moved or hidden so an accurate portrayal of robotic spaces is developed. These virtual environments can be used to train real world dynamic robot workspaces so that real world items are always tracked and considered in these environments, ensuring effective and safe human-robot interaction. 

The team is currently blocked based on resources available to us and this will determine the routes we can take to developing the virtual environment. We need training data in order to shape the environment and items within. We need to decide the origin of the training data so we can build our starter virtual environment. If the team does nothing then the project can not proceed considering without a way to formulate the virtual environment, we simply won't have one to simulate robot workspaces and the interactable items. 

## Options

### Option A: RGB-D camera origin

We would use an RBG-D camera to capture a real world working environment at Oregon State. This option would allow the team to create a virtual environment based on a real world environment we have access to and make real world decisions directly in front of and outside the view of the RGB-D camera to test how persistent the model is at understanding the changes in the real environment and applying that to the virtual environment. This is beneficial in being able to work on campus and have an environment to compare for verification of accuracy. The cost of this option would primarily come from the development time required to integrate the RBG-D camera with our decided software and how we use the data collected to change into 3D items.

### Option B: Complete simulation and AWS Cloud

We wouldn't consider real world tracking at all but rather virtually create a workspace and its items. All changes that would need to be considered would be done virtually and checked virtually. This option would be benefical in allowing collaboration between the team and our partners at PNNL located in Washington. The cost of this option would primarily come from the learning curve and development to create only a simulated workspace. Additionally, the infrastructure needed for the cloud software needs a lot of compute power and storage to support it which can be a struggle for the team.  

### Option C: Do Nothing

By doing nothing, the team must find an alternative to create a virtual environment to create a 3D robot workspace. This would take more time from the team's timeline and halt software development further. The cost of this option would primarily come from lack of developing software and delaying further milestones. Without a decision on the source of training data, the team lacks a starting point for the virtual environment and what needs to be implemented in these workspaces. 

## Analysis

- Performance: Option A would be beneficial in collecting real world RGB-D data and test the accuracy of virtual environmental changes to real world changes [1]. This can help in verification of object tracking. Option A runs the risk of issues based on camera limitations and sensor noise. Option B would be beneficial in allowing for the team to control the virtual environment collaboratively. Option B runs the risk of not accurately representing a real world environment. Option C would prevent evaluating performance until an alternative is chosen. I'm uncertain about which option would allow for better performance based on the hardware that will be available to the team. 
- Complexity: Option A would be beneficial in reducing complexity in later deployments. The PNNL team has said they'd be willing to test our virtual environment connection to a lab on their campus. With an RGB-D camera a part of our system, the same camera they use on their robots in their lab, there would be less complexity in real world integration [2]. Option A also runs the risk of requiring heavy virtual change to match a real world workspace. Option B would be beneficial in reducing risk between real world and virtual environment dependencies and allow for easier definition of items within the virtual environment. However, an only virtual environment runs the risk of additional software dependencies and increased development complexities [3]. Option C yet again would leave the team without a way to develop a virtual environment. 
- Maintainability: Option A would require camera calibration and maintenance on software used to process RGB-D data. Changes to any physical workspace may also require changes to the virtual environment in the future. Option B would require maintianing the simulation environment, its cloud infrastructure, and its software dependencies. Option C has no maintainability requirements. 
- Security: Option A would allow the team to collect and process data locally, reducing the need for cloud subscriptions. However, with the amount of training data needed, this would require storage whether that be locally or an external drive. Option B runs the risk of additional security considerations based on the cloud software used and how our virtual environments data is stored. Option C has no immediate security risks. 
- Cost: Option A costs include camera integration, data processing, object tracking, and real world to virtual environment testing. However, the PNNL team initially stated they'd provide a RGB-D camera for our implementation and only recently stated we could have it completely virtual. With Option B, there would need to be additional time to develop the simulated environment and configure it to the cloud infrastructure. This doesn't include the actual monetary costs of maintaining this infrastructure for the 3 term of the capstone. Option C has no immediate costs beside developmental time and delayed milestone. 
- Citations:
[1] https://introlab.github.io/rtabmap/ Used to indicate that there are labs that have already developed systems that use RBG-D camera to create virtual environments. This is open sourced and can be a starting point for the team.
[2] https://ieeexplore.ieee.org/document/6162880 Used to demonstrate that camera data can be used for 3D reconstruction of items and camera tracking for virtual environments.
[3] https://docs.isaacsim.omniverse.nvidia.com/latest/installation/requirements.html The requirements of the Isaac sim that the team would be using that is dependent on the AWS cloud infrastructure. This shows just how many software dependencies the team would need to consider for costs. 

## Recommendation and Verification Plan

Which option you propose and why it wins the analysis above. Then, concretely: how will the team know it worked? List the tests, metrics, or acceptance criteria that would detect failure, and when they will be checked.

The option I propose is Option A. Option A considering the known resources available to us and the project timeline is best in developing the team's next steps. While the camera has its own technical costs and risks, it would allow the team to begin development of the virtual environment. 

For verification, the team would confirm the RGB-D camera works to capture and process color and depth data. Then, the team would test that collected data could generate basic 3D representations of our workspace. Based on initial development, we can then test how accurately the initial demo of the system can detect and update changes in the real world to virtual environment. 

Testing and metrics for verification include that system being able to reflect moved items around the virtual environment, removed items in the virtual environment, and hidden items accounted for in the virtual environment. These hidden items are a major test for the system and these hidden items should no longer appear in the virtual environment but be recognized when they do reappear. These three tests of reflection from the real world to the virtual environment are what determines the persistent of the virtual environment for robot workspaces.

## Constraints

There are currently no constraints. The PNNL team has made it clear they want us to build this project as we want to as a team. They have shown us the system they already have and are there to guide us through our own project. They've stated that the work we do is welcome to be a part of our public portfolio.

They have shown us their PNNL simulation which is their IP however they want us to develop through our own methodology our own virtual environment so we know the process of creating a persistent model for robot workspaces. 

## Delegation and Validation

I handed nothing to AI tools. 

We currently have no checks in our repo as we are blocked on software development.

Points I stopped and validated myself were for Options and Analysis. This decision is hard to reverse, it sets the stage for how we complete our project and what other resources we'll need to be successful. I checked that these options are what are most available to us as a team and what the benefits and trade offs are based on notes from team meetings, team correspondence, and further literature review.

What is assessed is in the [AI policy](https://capstone.alexulbrich.com/assignments/introduction/#ai-policy-applies-to-every-assignment).

## Decision

Proposed

My proposed decision is to use the RGB-D camera. PNNL has already agreed to send the team a camera while they have declined sponsoring the subscription needed to do Cloud software. To start software development as soon as we can, RGB-D camera would help in establishing a better plan to proceed. The team has not made a formal decision together.