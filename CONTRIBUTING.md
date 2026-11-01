# Contributing

This guide explains how the team contributes, reviews, tests, and merges work.

## Getting Started

1. Clone the repository.
2. Follow the setup instructions in `README.md`.
3. Create a branch before making changes.
4. Run the relevant tests locally.
5. Open a pull request when the change is ready.

Install test dependencies:

```bash
python -m pip install -r requirements-dev.txt
```

Run the current test suite:

```bash
python -m pytest
```

Passwords, API keys, access tokens, and other credentials must never be committed.

## Branching and Workflow

New work should be done on a separate branch instead of directly on `main`.

Examples:

- `feature/object-tracking`
- `fix/data-loading`
- `docs/checkpoint-1`

When work is ready, open a pull request with a short description of what changed and how it was tested.

## Pull Requests and Reviews

At least one other team member should review a pull request before it is merged.

Reviewers should check that the change works, follows the project structure, includes appropriate testing, updates documentation when needed, and does not introduce obvious security, confidentiality, or reliability problems.

Pull requests should normally be reviewed within two weekdays.

Required CI must pass before merge.

## Testing and CI

GitHub Actions runs the current `python -m pytest` suite on pull requests and pushes to `main`.

The current test suite begins with a small known-result world-state behavior so CI is real even before the full perception pipeline exists.

As product code is added, tests should be added for changed behavior rather than leaving CI as a scaffold-only check.

## Definition of Done

A contribution is considered done when:

- the change works as expected;
- relevant tests pass;
- required CI checks pass;
- at least one teammate has reviewed the pull request;
- documentation is updated when setup, interfaces, architecture, or expected behavior changes;
- no credentials or partner-confidential information are included;
- the change is merged through the reviewed pull request.

## Contribution Norm

Each team member owns at least one meaningful accepted piece of work during every sprint.

Work may include code, testing, documentation, design, data preparation, environment setup, or other agreed project work.

Code and repository documentation live in GitHub. Sprint tasks and status live on the team's project board.

Pairing is allowed, but each person's contribution should remain identifiable.

## Documentation

Keep the following living docs current:

- `docs/requirements.md`
- `docs/design.md`
- `docs/risks.md`
- `README.md`
- `CONTRIBUTING.md`
- `AGENTS.md`

Architectural proposals and decisions live under `docs/rfcs/`.

## Security and Partner Assets

Never commit credentials.

Do not commit partner-confidential material or the PNNL-provided digital-twin assets unless PNNL explicitly approves public redistribution.

If a secret is accidentally committed, notify the team and revoke or rotate it.

## Communication and Help

Raise blockers early in the team communication channels rather than waiting until the end of the sprint.
