# AGENTS.md

## Project Context
This repository contains the source code for the **CS 461 AI Perception System for Robotics**, a project designed to give a robot persistent awareness of its laboratory surroundings. The system integrates RGB-D sensing with modern vision models (such as SAM 2) to track objects, maintain their 3D location and state over time, manage occlusions, and publish world-state data via a reusable ROS2 interface.

## Technology Stack & Conventions
* **Language**: Python 3.10+
* **Core Libraries**: PyTorch, SAM 2, Open3D, NumPy, SciPy
* **Robotics Middleware**: ROS2 (Humble / Iron / Jazzy compatible)
* **Code Style**: PEP 8 compliance for Python, standard ROS2 workspace layout (`src/`, package structure with `setup.py` / `package.xml`).
* **Architecture**: Modular separation between pure perception pipelines (segmentation, 3D projection, tracking) and ROS2 node wrappers.

## Current State (Week 2)
As of Week 2, the codebase is in its foundational scaffolding phase. 
* **Known Elements**: The chosen stack (Python, PyTorch, SAM 2, ROS2, RGB-D), high-level architecture (Backbone and Walking Skeleton defined in the project story map), and general team conventions.
* **Confidentiality & Boundaries**: This is an academic project for Oregon State University CS 461. Code and documentation are subject to academic integrity policies and course collaboration guidelines.

## Future Additions & Ownership
Once code implementation begins, the following sections will be appended to this document by designated team members:

1. **API & Module Interfaces** (Owner: Perception Lead)
   * Detailed signatures and usage examples for the SAM 2 wrapper and 3D state estimation modules.
2. **ROS2 Message Definitions & Topics** (Owner: Integration Lead)
   * Specifications for custom world-state messages, active topic names, and QoS settings.
3. **Testing & Evaluation Guidelines** (Owner: QA / Testing Lead)
   * Instructions for running unit tests, evaluating tracking drift, and benchmarking inference latency on target hardware.
4. **Hardware Setup & Calibration** (Owner: Robotics / Hardware Lead)
   * Camera calibration parameters, extrinsics relative to the robot base frame, and launch procedures.
