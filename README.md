# Persistent AI World Models for Robot Workspaces

CS 461 capstone project with PNNL.

## Current status

The project is in the setup and integration phase. PNNL has provided the team with a USD digital twin of the lab environment and associated texture assets. The team is working on:

- running Isaac Sim on the HPC environment;
- configuring the ROS 2 environment;
- evaluating vision models that fit the selected Ubuntu, ROS 2, GPU, and Isaac Sim setup;
- defining the first end-to-end perception and world-state path.

The repository currently contains a small Python scaffold and automated test so the team can verify the development workflow and CI before the full perception pipeline exists.

## Quickstart

### Requirements

- Python 3.11 or newer
- pip

### Setup

```bash
git clone https://github.com/Wade-Owo/Rob_Capstone.git
cd Rob_Capstone
python -m venv .venv
```

Activate the virtual environment.

Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

macOS/Linux:

```bash
source .venv/bin/activate
```

Install development dependencies:

```bash
python -m pip install -r requirements-dev.txt
```

Run the tests:

```bash
python -m pytest
```

## Repository layout

- `src/` - current project scaffold and future implementation
- `tests/` - automated tests
- `docs/requirements.md` - requirements, constraints, success metrics, and open questions
- `docs/design.md` - current architecture, interfaces, and production target
- `docs/risks.md` - project risk register and external prerequisites
- `docs/rfcs/` - RFCs and architectural decision proposals
- `CONTRIBUTING.md` - contribution and review process
- `AGENTS.md` - AI/tool context for the repository

## CI

GitHub Actions runs `python -m pytest` on pull requests and pushes to `main`.

## Staging and rollback plan

Until the full perception pipeline exists, changes are exercised against the local/sample-data scaffold and automated tests before merge.

The planned next staging environment is the PNNL-provided digital twin in Isaac Sim once the HPC environment is verified.

A bad change can be undone by reverting the merged pull request or restoring the last known-good commit.

## External digital twin

The PNNL-provided digital twin is an external project asset and is not committed to this public repository. The current package contains a USD scene and associated texture assets. The team will only publish or redistribute those assets if the partner explicitly approves it.
