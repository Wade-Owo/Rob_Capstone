# RFC: Baseline Goal

| Field | Value |
| --- | --- |
| Author | Wade Owojori |
| Date | 2026-10-24 |
| Status | Proposed |
| Decision Date | (fill when decided) |
| Deciders | (who agreed to the outcome) |
| Superseded By | (link, if applicable) |

## Problem and Context

Our team needs to decide the baseline goal for this project: what we will demo at the end of the 30 weeks and what counts as success. This project is unusual because our partner's (PNNL's) main goal is for us to learn. They already have their solution to the problem and want us to try to tackle it and see if we come up with anything new and useful they can use. We also have no access to PNNL's lab space or robot. We have a digital twin of the lab and one piece of hardware: an RGB-D camera. With fewer resources than the PNNL team, we should not expect to match the robustness of their solution. We need to define a feasible end goal, treating the project description as a guide rather than a spec for the final product.

We need to decide this now because it determines the number and size of the milestones planned to complete the project. If we do nothing, we will not know what we are building toward demoing, and our milestones and development will drift. Once we define what we want to have as our end goal, which we'll be demoing, we can then break that into milestones and what we want to be able to show in each milestone that will eventually converge to our goal.

## Options

### Option A: Train on Simulator, Validate in the Real World

Our perception pipeline uses two models. A YOLO detector finds each object and labels its type (for example, beaker or person). SAM 2 then takes each detection as a prompt, outlines the object precisely, and follows it from frame to frame. Because the outline is exact, each object's 3D position comes from its own depth pixels rather than the table or background inside its box. We fine-tune the YOLO detector on images rendered from the digital twin of the PNNL lab so that it can identify the objects that will be in the lab. SAM 2 works without fine-tuning; we would fine-tune it only if its outlines of our objects turn out poor. We then check whether the model transfers to the real world by gathering physical versions of as many of those objects as we can and running YOLO and SAM 2 on a live feed from the RGB-D camera PNNL is providing. We validate the 3D mapping pipeline in the digital twin as well. For the end-to-end test, the capstone room stands in for the lab. We place the objects around the room, and a team member carries the camera through it to simulate a robot moving through a workspace. As new frames come in, the live 3D map should update and stay accurate. Once we are confident in its performance, this test becomes our demo. People should also appear in the map. The base (not fine-tuned) YOLO model can already detect people, and if a person is holding a lab object that is visible to the camera, the map should place that object with the person.

Costs: we have to source physical stand-ins for the lab objects, collect and label some real images, and budget time to close the sim-to-real gap if accuracy drops on real footage. This is the right choice if PNNL wants a system that works on a real camera feed and we can get enough representative objects.

### Option B: Trust the Simulator

We train, test, and demo everything in the digital twin, and hand that result to the PNNL team. The cost is that we would not know how well a model trained only on simulated images performs on a live camera feed. The benefit is that everything stays digital, no physical lab equipment to find and no real-world data collection. The result may be less reliable, but it is much simpler, and if the twin-trained model works well on PNNL's real robot, it is a much more efficient path than Option A.

### Option C: Do Nothing

Continuing without a concrete baseline goal risks miscommunication with the PNNL team and a scope too large for our 30-week timeline. The cost arrives when we start building software and discover how large the scope is without a goal sized to our time and resources.

## Analysis

**Performance:** The main risk in this decision is that a detector trained only on rendered images loses accuracy on real camera frames, because lighting, textures, sensor noise, and depth artifacts differ from the render. This gap is well documented. The standard mitigations are domain randomization (randomizing textures, lighting, and camera poses when rendering training data) [1][2] and fine-tuning on real labeled images after training on synthetic data [2]. Option B has no way to measure this gap, but Option A measures it directly.

**Depth quality:** The ZED 2i computes depth from stereo, so its depth is noisier than the twin's rendered depth, especially on textureless or reflective surfaces like glassware and metal. Our 3D map is built from that depth, so a pipeline tuned only in the twin can place objects in the wrong spot in the real world even when detection is correct. Only a real-world test catches this.

**People:** Testing a person carrying an object needs real footage unless the twin can simulate people, and only Option A collects real footage.

**Complexity and cost:** Option A adds data collection, labeling, and a test session in the capstone room, but no new software, since the same pipeline runs on twin renders and live frames. Both options need GPU time to render training data from the twin.

**Maintainability:** Option A forces the pipeline to accept twin and live camera input through the same interface, which is also what PNNL would need to plug our work into their own system.

**Security and confidentiality:** The proprietary assets are not included in our copy of the twin, so they limit what we can train on under both options but leave us nothing to protect. The one confidentiality question we know of is whether we may share our copy of the twin outside the team, which matters if we run it on cloud GPUs and applies equally to both options. Real images of the capstone room contain no partner data, so they are easier to store and share.

**What we are uncertain about:** how large the sim-to-real gap will be for these specific objects; how many of the lab objects we can source physically; whether the twin can render people.

**References**

1. J. Tobin et al., "Domain Randomization for Transferring Deep Neural Networks from Simulation to the Real World," IROS 2017, arXiv:1703.06907.
2. J. Tremblay et al., "Training Deep Networks with Synthetic Data: Bridging the Reality Gap by Domain Randomization," CVPR Workshops 2018, arXiv:1804.06516.

## Recommendation and Verification Plan

I propose Option A. It is the only option that measures whether our system works on real camera data, which makes us more confident in the work we present to the PNNL team. Apart from the real-world testing, it is not much more work than Option B. It only becomes more work if the model does not transfer, and in that case Option B would have left us with a final product that does not work without our knowing it.

**Verification plan:**

1. **Detection transfer:** we hand-label a held-out set of real camera frames of our stand-in objects and measure two things: recall (the share of objects in view that the model finds) and precision (the share of its detections that are correct). We should target at least 80% on both, and no more than about 15 percentage points below the same scores on held-out digital twin renders. The object labels come from the YOLO detector, so these scores measure YOLO. SAM 2 only outlines and follows what YOLO finds, so we spot-check its outlines against hand-drawn ones on a sample of the same frames. We take a first measurement early in Milestone 2 and adjust the target with PNNL if it proves unrealistic. Checked at the end of Milestone 2 (winter term).
2. **Localization:** objects placed at tape-measured positions in the capstone room appear in the 3D map within about 10 cm of their true position. Checked at the end of Milestone 2 (winter term).
3. **Persistence:** during a scripted walkthrough where objects are moved, added, and removed, the map reflects each change within a few seconds of it coming into view, unmoved objects keep stable IDs, and objects that are hidden and then reappear keep their IDs and last known positions. The stored world state is checked at the end of Milestone 3 (winter term), and the 3D map display at the end of Milestone 4 (early spring term).
4. **People:** a person walking through the room carrying an object is mapped together with that object. Person detection is checked at the end of Milestone 2, linking the carried object to the person at the end of Milestone 3, and the combined result in the 3D map at the end of Milestone 4.
5. **Final run:** all four checks are repeated in the Milestone 5 test scenarios (objects moving, disappearing, and reappearing) before the final demo at the end of spring term.

**Failure trigger:** if detection transfer still misses its target after one round of domain randomization plus added real images, we raise it with PNNL and decide together whether to fall back to Option B for the demo.

## Constraints

**Data use and IP:** some 3D models in the digital twin are proprietary to one of PNNL's partners, and they are not included in the copy PNNL gives us, so we cannot train on, render, or demo those items.

**Confidentiality:** beyond the proprietary assets, the only restriction we know of is that we may not be allowed to share our copy of the twin outside the team. We need to confirm this with PNNL before running the twin on cloud GPUs.

**Compute:** running the twin needs more GPU power and storage than some of our laptops have, so we may need cloud computing. Without it, we would set up a space at OSU that resembles the PNNL workspace as closely as we can and collect data manually with the camera.

**Licensing:** Ultralytics YOLO models are licensed under AGPL-3.0, which requires releasing the source code of anything built on them that is distributed or offered as a network service, unless the user buys an Ultralytics enterprise license. We need to confirm PNNL is fine with this before committing to YOLO. If not, an Apache-2.0 detector such as RT-DETR or Grounding DINO avoids the issue. SAM 2 is Apache-2.0, so it raises no concern.

## Delegation and Validation

**What I handed to AI tools:** I wrote the Problem and Context, the three options, the recommendation, and the constraint facts myself. I used Claude for five things: suggesting rewordings across every section; drafting the Analysis section, including its citations; drafting the verification plan's checks and numeric targets; writing this delegation and validation based on what I asked it to do; and explaining technical points I was unsure about, which led to adding the YOLO + SAM 2 pipeline description and the AGPL licensing note.

**What checks made that reasonable:** our repo has no code yet, so there are no tests or CI to rely on; CONTRIBUTING.md says the Quality Owner adds them in Sprint 1. The checks that do exist for this document: every AI change was made as a Google Docs suggestion, so nothing entered the RFC until I accepted it; I challenged claims in doc comments before accepting them.

**Where I stopped and validated the result myself, and why:** I checked every place where the AI was supplying facts about our specific project rather than general knowledge, because that is where it could not know the answer. I had the verification plan's milestone timing checked against our Capstone Project Planning Document and reviewed the result. I corrected the confidentiality analysis, which assumed the proprietary assets were in our copy of the twin when they are not. I questioned whether SAM 2 labels objects, which showed we also need a detector (YOLO). I also removed Analysis points that did not help choose between the options.

This decision isn't too hard to reverse. Option A keeps Option B available: if real-world testing fails, we can drop it and demo in the twin. Switching the other way late in the project would be costly, which is part of why A is a better choice. Before proposing it, I checked that the verification checks fit the milestone timeline in our planning document, and that no confidentiality restriction blocks real-world testing, since the proprietary assets are not in our copy of the twin.

## Decision

Proposed. The team has not decided yet; this section will record the outcome, the date, and who chaired the decision.