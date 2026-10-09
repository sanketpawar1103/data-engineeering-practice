# Kafka Developer Workflow

## Overview

Kafka Developer Workflow is a learning project that simulates a software development workflow using Python and Apache Kafka.

The goal is to understand how independent systems communicate through events, how Kafka enables asynchronous communication, and how an event-driven architecture can automate parts of a developer's workflow.

The project uses mocked systems instead of real Jira or GitHub integrations, allowing us to focus on the underlying concepts and implementation.

## Project Idea

The workflow begins when a new development card is added to a mocked Jira system.

1. A new card is created in Jira.
2. Jira publishes a `CardAdded` event to Kafka.
3. A consumer processes the event and finds an available developer.
4. The card is assigned to the developer.
5. The developer's availability and the card's assignment are updated in their respective components.

GitHub integration and additional workflow automation can be introduced in later phases.

## Architecture

The project will initially contain the following components:

* **Jira:** Manages development cards and their assignment status.
* **Developers:** Manages developer identities and availability.
* **Kafka:** Acts as the event backbone for communication between components.
* **Workflow Consumer:** Processes events and coordinates the assignment workflow.

Each component is responsible for its own data and responsibilities. Kafka enables communication between components without requiring direct function calls between them.

## Technology Stack

* Python
* Apache Kafka
* Podman / container-based development
* Docker Compose-compatible container orchestration, where supported

## Development Roadmap

### Phase 1: Domain Foundations

* Implement the Card entity.
* Implement the Jira component.
* Implement the Developer entity.
* Establish basic domain behavior without Kafka.

### Phase 2: Event-Driven Communication

* Introduce Kafka topics and event structures.
* Publish events when cards are added.
* Consume events and process developer assignments.

### Phase 3: Workflow Automation

* Assign cards to available developers.
* Update developer availability.
* Handle scenarios such as no available developers and invalid assignments.

### Phase 4: Containerization

* Containerize the application and its dependencies.
* Configure services to communicate within the container environment.
* Simplify startup so the project can be run from a fresh clone with minimal manual setup.

### Phase 5: Extended Integrations

* Introduce a mocked GitHub component.
* Extend the workflow with additional development events.
* Explore retries, failure handling, and event-driven system design.

## Learning Objectives

* Understand event-driven architecture.
* Implement Kafka producers and consumers in Python.
* Learn how topics, partitions, offsets, and consumer groups work in practice.
* Design components with clear ownership and responsibilities.
* Explore asynchronous communication between independent systems.
* Practise testing, clean code, and containerized application development.

## Project Status

**In progress:** Initial project structure and Python development setup.

The domain components will be implemented first, followed by Kafka integration and workflow automation.
