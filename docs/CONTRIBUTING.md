# Contributing

This guide explains how our team will contribute, review, test, and merge work.

## Getting Started

1. Clone the repository.
2. Follow the setup instructions in the README.
3. Create a branch for your work before making changes.
4. Make sure the project runs locally before opening a pull request.

The team does not yet have finalized local test and lint commands. The Quality Owner will add the exact commands to this file during Sprint 1 once the project tooling is finalized.

Passwords, API keys, access tokens, and other credentials should never be committed to the repository.

## Branching and Workflow

Work should be done on a separate branch instead of directly on the main branch.

Branch names should briefly describe the work being done, for example:

- `feature/object-tracking`
- `fix/data-loading`
- `docs/setup-guide`

When work is ready, open a pull request with a short description of what changed and how it was tested.

## Pull Requests and Reviews

At least one other team member should review a pull request before it is merged.

Reviewers should make sure the change works as expected, follows the project structure, includes testing when needed, and does not introduce obvious security or reliability problems.

Pull requests should normally be reviewed within two weekdays so work is not blocked for too long.

## Testing and Linting

Changes should be tested before they are merged.

New or changed functionality should include tests when appropriate, and existing tests should continue to pass.

The Quality Owner will add the team's local test and lint commands and corresponding CI checks during Sprint 1.

## Definition of Done

A contribution is considered done when:

- The change works as expected.
- Relevant tests pass.
- Linting and formatting checks pass once those checks are available.
- At least one other team member has reviewed the pull request.
- Documentation is updated when needed.
- No passwords, API keys, credentials, or other sensitive information are included.
- Required CI checks pass before merging.

The team will use CI checks for testing, linting, and basic security checks.

Any CI gate that does not exist yet will be added during Sprint 1 by the current Quality Owner.

Code should not be merged if a required CI check is failing.

## Contribution Norm

Each team member will complete at least one meaningful piece of accepted work during every sprint.

Work may include code, testing, documentation, design, data preparation, or other project work agreed on by the team.

Code and documentation will live in the repository, while assigned work and project progress will be tracked in Microsoft Project.

Code is accepted once it has been reviewed and merged. Documentation or other non-code work is accepted once it is completed and reviewed by the team when appropriate.

Tasks should be small enough to reasonably finish within a sprint. Team members may pair on larger tasks, but each person should still have a clear contribution.

## Documentation

Documentation should be updated when a change affects setup, project usage, APIs, or expected behavior.

The README and other project documentation should stay accurate enough for another team member to understand how to use the current project.

## Security

Passwords, API keys, access tokens, and other credentials must not be committed to the repository.

If a secret is accidentally committed, the team should notify each other and replace the exposed credential.

## Communication and Help

Questions, blockers, and requests for help should be posted in the CS 461 Teams chat or ROB Capstone group chat.

Team members should acknowledge messages within 24 hours on weekdays when possible.

If someone is blocked, they should bring it up early rather than waiting until the end of the sprint.
