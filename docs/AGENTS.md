# AGENTS.md

Project context, conventions, and constraints for AI tools working in this repo. This file is the cross-tool source of truth: per-tool files (e.g. CLAUDE.md, `.cursorrules`) should point here rather than duplicate it. Where docs exist, this file links to them instead of restating them.

> **Status: Week 2.** There is little code yet. This file records what the team already knows (stack, conventions, confidentiality boundary) and lists what gets added once code exists, with owners.

---

## Project context

### Description

Build an AI perception system that gives a robot persistent awareness of its surroundings. Using RGB-D cameras and modern vision models such as SAM 2, the system will track laboratory objects, maintain their 3D location and state over time, recognize when objects have moved or become hidden, and recover their state after occlusion.

### Problem statement

Robots need more than individual object detections to perform long-running tasks. They need a persistent understanding of their environment: what objects exist, where they are, what changed, and what the robot has already observed. This persistent world model provides the spatial memory needed for more capable autonomous robots.

### Objectives

1. Integrate AI vision models with RGB-D sensing.
2. Track multiple objects and their 3D state over time.
3. Detect changes caused by people or robot actions.
4. Recover object state following occlusion.
5. Publish world-state information through a reusable ROS2 interface.
6. Demonstrate multiple robot behaviors using the same perception service.

### Where to read more

- Project docs: `[link or path: fill in]`
- Architecture / design notes: `[link or path: fill in]`

---

## Stack

- **Language:** Python
- **Vision / AI:** PyTorch, SAM / SAM 2, object tracking
- **Sensing:** RGB-D cameras, 3D geometry
- **Robotics middleware:** ROS2

---

## Conventions

Agree on and fill in as the team settles them. Until then, follow existing patterns in the repo and ask before introducing new ones.

- **Code style / formatting:** `[TBD: e.g. formatter and linter]`
- **Branching and PRs:** `[TBD]`
- **Testing:** `[TBD]`
- **ROS2 interface naming (topics, messages, services):** `[TBD, owner adds once the interface is drafted]`
- **Commit messages:** `[TBD]`

---

## Constraints

### Confidentiality boundary

Team members may use AI tools for brainstorming, writing, coding help, debugging, documentation, and other project work.

- **OK to share with AI tools:** project code and non-sensitive project information, when useful.
- **Never enter into AI tools:** passwords, API keys, private credentials, and any information the project partner has specifically identified as confidential.
- **If something is clearly sensitive or restricted:** confirm before sharing. The **AI Coordinator** is the first point of contact for deciding whether something can be shared with AI.

AI tools working in this repo should not ask for, echo, or write credentials or partner-confidential material into code, docs, logs, or commit messages. If unsure whether something is covered, stop and flag it to the AI Coordinator.

### Technical constraints

- Perception output must be published through a **reusable ROS2 interface**, not tied to a single robot behavior.
- Object state must persist over time and survive occlusion (see Objectives).

---

## To be added once code exists

Owners are proposed by role; confirm and add names.

| Section | What it covers | Owner (role) |
|---|---|---|
| Repo layout | Directory map and where each component lives | Documentation Currency |
| Setup and run commands | Environment setup, build, launch, tests | Documentation Currency |
| ROS2 interface spec | Topics, message types, frame conventions | Documentation Currency |
| Model and data handling | Where weights and sample data live, and what is off-limits | AI Coordinator |
| Testing and CI | How to run tests, what must pass before merge | The Test Suite |
| Known pitfalls | Gotchas AI tools should avoid | Quality Owner |
