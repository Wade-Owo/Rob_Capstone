# Risk Register

This is the project's single risk register.

| Rank | Risk / external prerequisite | Owner | Status / mitigation |
| --- | --- | --- | --- |
| High | Isaac Sim 6.1 has not yet been verified on the intended HPC hardware/software environment. | Wade Owojori | Check GPU/driver/OS compatibility, start Isaac Sim, then test the partner-provided USD scene. Target update: 2026-11-08. |
| High | The PNNL-provided USD scene may have texture or asset references that do not resolve after moving to HPC. | Wade Owojori | Load the scene on HPC and verify expected geometry/textures before building integration work around it. |
| High | The Week 10 execution environment is not yet fully verified. | CJ Chavez | Record the actual working compute target in `docs/design.md` once the Isaac Sim/HPC check is complete; escalate early if an equivalent milestone is needed. |
| High | The full end-to-end perception pipeline does not exist yet. | Haddy Alnasser | Use a real tested scaffold for CI now, then replace it incrementally with real components as the environment comes online. |
| Medium | Isaac Sim, Ubuntu, ROS 2, GPU/CUDA, and vision-model requirements may conflict. | Carter Cripe / Haddy Alnasser | Compare candidate vision-model requirements only after the HPC/ROS environment is known; avoid committing to a model that does not fit the runtime. |
| Medium | Physical RGB-D camera delivery/integration may be delayed. | CJ Chavez | Continue initial development using the provided digital twin and simulated data. |
| Medium | The persistent world-state representation is still open and could cause rework if downstream components depend on it too early. | Haddy Alnasser | Complete RFC review and prototype validation before treating the representation as stable. |
| Medium | Prior direct commits to `main` weaken review traceability. | CJ Chavez | From this checkpoint forward, use branches, reviewed PRs, and passing CI before merge. Do not rewrite history. |
| Low | Partner-provided assets or confidential information could be published accidentally through the public repository or external AI tools. | Wade Owojori | Keep the digital twin and any restricted partner material outside the public repository unless redistribution is explicitly approved. |

## External prerequisites

| Prerequisite | Owner / requester | Status |
| --- | --- | --- |
| PNNL digital twin package | PNNL provided; team has local access | Available |
| Isaac Sim 6.1 on HPC | Wade Owojori | Not yet verified; target update 2026-11-08 |
| ROS 2 environment | Wade Owojori and Arstanbek Bulanbekov | Setup in progress |
| Physical RGB-D camera | CJ Chavez coordinating with partner/instructors | Delivery/integration pending |
| Final environment details for model selection | Carter Cripe and Haddy Alnasser depend on HPC/ROS result | Pending |
