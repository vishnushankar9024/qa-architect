# Business Flows

Discovered deterministically from existing QA Architect artifacts (artifact-first, no repository scanning, no LLM).

## Validation Summary

- **Total flows discovered:** 11
- **Average steps per flow:** 4.36

**Flows per domain**

- Document Management: 1
- Execution and Field: 1
- Integrations: 1
- Notifications: 1
- Project Management: 3
- Quality and Inspection: 1
- User and Access Management: 1
- Vendor Management: 1
- Workflow, Approval and RACI: 1

**Flows per category**

- Activity Flow: 1
- Checklist Flow: 1
- Document Flow: 1
- Integration Flow: 1
- Notification Flow: 1
- Project Flow: 2
- RACI Flow: 1
- Template Flow: 1
- User Management Flow: 1
- Vendor Management Flow: 1

**Highest complexity flows**

- Workstation Execution Flow
- Planner Synchronization Flow
- Project Creation Flow
- Document Approval Flow
- Vendor Approval Flow
- User Creation Flow
- Template Creation Flow

**Highest criticality flows**

- Project Creation Flow
- Project Assignment Flow
- Document Approval Flow
- Vendor Approval Flow

# Document Management

## Document Approval Flow

_FLOW-001 · Document Flow · confidence 0.94_

**Purpose**

Route a Document through review and approval to a final decision.

**Steps**

1. Initiate _(inferred)_
2. Submission
3. Review
4. Approval
5. Closure _(inferred)_

**Complexity:** High

**Criticality:** Critical

**Dependencies**

- _none_

**QA metadata:** steps=5, integration_points=0, document_touchpoints=3, approval_touchpoints=3

# Execution and Field

## Workstation Execution Flow

_FLOW-002 · Activity Flow · confidence 0.99_

**Purpose**

Carry out and complete the work associated with a Workstation.

**Steps**

1. Initiate
2. Assignment
3. Execution
4. Completion
5. Closure

**Complexity:** High

**Criticality:** High

**Dependencies**

- Checklist

**QA metadata:** steps=5, integration_points=0, document_touchpoints=0, approval_touchpoints=0

# Integrations

## Planner Synchronization Flow

_FLOW-003 · Integration Flow · confidence 0.99_

**Purpose**

Exchange and reconcile Planner data with an external system.

**Steps**

1. Mapping
2. Synchronization
3. Notification

**Complexity:** High

**Criticality:** High

**Dependencies**

- Microsoft Project
- Primavera P6
- SMTP Email Gateway

**QA metadata:** steps=3, integration_points=5, document_touchpoints=0, approval_touchpoints=0

# Notifications

## Notification Flow

_FLOW-004 · Notification Flow · confidence 0.82_

**Purpose**

Detect an event and notify the relevant stakeholders for a Notification.

**Steps**

1. Initiate _(inferred)_
2. Notification
3. Closure _(inferred)_

**Complexity:** Low

**Criticality:** Medium

**Dependencies**

- _none_

**QA metadata:** steps=3, integration_points=0, document_touchpoints=0, approval_touchpoints=0

# Project Management

## Project Assignment Flow

_FLOW-005 · Project Flow · confidence 0.98_

**Purpose**

Allocate ownership and responsibility for a Project.

**Steps**

1. Initiate
2. Assignment
3. Delegation
4. Notification _(inferred)_

**Complexity:** Medium

**Criticality:** Critical

**Dependencies**

- _none_

**QA metadata:** steps=4, integration_points=0, document_touchpoints=0, approval_touchpoints=1

## Project Creation Flow

_FLOW-006 · Project Flow · confidence 0.99_

**Purpose**

Capture, validate and activate a new Project.

**Steps**

1. Initiate
2. Submission
3. Review
4. Approval
5. Activation

**Complexity:** High

**Criticality:** Critical

**Dependencies**

- _none_

**QA metadata:** steps=5, integration_points=0, document_touchpoints=0, approval_touchpoints=1

## Template Creation Flow

_FLOW-007 · Template Flow · confidence 0.77_

**Purpose**

Capture, validate and activate a new Template.

**Steps**

1. Initiate _(inferred)_
2. Submission _(inferred)_
3. Review _(inferred)_
4. Approval _(inferred)_
5. Activation _(inferred)_

**Complexity:** High

**Criticality:** High

**Dependencies**

- Project

**QA metadata:** steps=5, integration_points=0, document_touchpoints=0, approval_touchpoints=0

# Quality and Inspection

## Checklist Completion Flow

_FLOW-008 · Checklist Flow · confidence 0.99_

**Purpose**

Fill in, verify and sign off a Checklist.

**Steps**

1. Initiate
2. Completion
3. Review
4. Approval

**Complexity:** Medium

**Criticality:** High

**Dependencies**

- _none_

**QA metadata:** steps=4, integration_points=0, document_touchpoints=0, approval_touchpoints=2

# User and Access Management

## User Creation Flow

_FLOW-009 · User Management Flow · confidence 0.79_

**Purpose**

Capture, validate and activate a new User.

**Steps**

1. Initiate _(inferred)_
2. Submission _(inferred)_
3. Review _(inferred)_
4. Approval _(inferred)_
5. Activation

**Complexity:** High

**Criticality:** High

**Dependencies**

- _none_

**QA metadata:** steps=5, integration_points=0, document_touchpoints=0, approval_touchpoints=0

# Vendor Management

## Vendor Approval Flow

_FLOW-010 · Vendor Management Flow · confidence 0.94_

**Purpose**

Route a Vendor through review and approval to a final decision.

**Steps**

1. Initiate _(inferred)_
2. Submission
3. Review
4. Approval
5. Closure _(inferred)_

**Complexity:** High

**Criticality:** Critical

**Dependencies**

- Project

**QA metadata:** steps=5, integration_points=0, document_touchpoints=0, approval_touchpoints=3

# Workflow, Approval and RACI

## RACI Assignment Flow

_FLOW-011 · RACI Flow · confidence 0.89_

**Purpose**

Allocate ownership and responsibility for a RACI Assignment.

**Steps**

1. Initiate _(inferred)_
2. Assignment
3. Delegation
4. Notification _(inferred)_

**Complexity:** Medium

**Criticality:** High

**Dependencies**

- _none_

**QA metadata:** steps=4, integration_points=0, document_touchpoints=0, approval_touchpoints=0
