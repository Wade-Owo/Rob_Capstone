# AGENTS.md

Project context, conventions, and constraints for AI tools working in this repository.

This is the cross-tool source of truth. Other AI instruction files should point here instead of copying it.

## Project Context

The project is building a persistent AI perception system for robot workspaces. It uses simulated and eventually physical RGB-D observations, computer vision, 3D object state, persistent memory, and ROS 2.

PNNL has provided a USD digital twin of the laboratory environment and associated texture assets. Those assets are external project resources and are not stored in this public repository unless PNNL explicitly approves redistribution.

## Read These First

- `README.md` - clean-clone quickstart and repository layout
- `docs/requirements.md` - requirements, constraints, success metrics, non-goals, open questions
- `docs/design.md` - current architecture, interfaces, production target, deferred decisions
- `docs/risks.md` - project risks and external prerequisites
- `CONTRIBUTING.md` - branch, PR, testing, review, and Definition of Done
- `docs/rfcs/` - proposed and accepted technical decisions

Do not duplicate those documents here.

## Current State

The repository has a minimal Python scaffold and known-result test so CI can run before the full perception pipeline exists.

Current partner-aligned work includes:

- Isaac Sim 6.1 / HPC setup;
- ROS 2 environment setup;
- loading and validating the PNNL-provided digital twin;
- comparing candidate vision models against the actual runtime environment.

The full perception pipeline is not yet implemented.

## Current Stack

- Python
- python -m pytest
- GitHub Actions
- Planned/being evaluated: Isaac Sim 6.1
- Planned: ROS 2 Humble or Jazzy depending on the verified Ubuntu environment
- Planned: PyTorch and a selected vision/segmentation model
- Planned: RGB-D and 3D geometry

## Conventions

- Work on a branch.
- Open a pull request before merging to `main`.
- At least one teammate reviews each pull request.
- Required CI must pass before merge.
- Run `python -m pytest` locally before opening a PR when practical.
- Use short commit messages that explain what changed.
- Update living docs when assumptions or setup change.

## Confidentiality Boundary

AI tools may be used for brainstorming, writing, coding help, debugging, documentation, and other non-sensitive project work.

Never place the following into external AI tools or this public repository:

- passwords;
- API keys;
- private credentials;
- partner-confidential information;
- partner-provided assets that are not approved for redistribution.

If something may be sensitive, stop and ask the AI Coordinator/team before sharing it.

## Important Deferred Decisions

Do not silently make these decisions in code:

- final persistent world-state representation;
- final ROS 2 interface;
- final perception/tracking model;
- final HPC/Isaac Sim/Ubuntu/ROS 2 environment;
- final detection-distance and object-count requirements.

Check `docs/design.md`, `docs/requirements.md`, and `docs/rfcs/` before changing architectural assumptions.
