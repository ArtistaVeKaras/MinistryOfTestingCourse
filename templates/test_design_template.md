# Test Design Template

A structured template to guide the creation of comprehensive and effective test designs.

---
TODO: remove all the links to the template files once the template is finalized.

## 1. Test Overview

- **Feature/Component:**  
  [Name of feature, user story, or component]

- **Related Ticket/Story ID:**  
  [JIRA/issue tracker reference]

- **Version/Release:**  
  [Version or release number]

- **Author:**  
  [Name]

- **Date:**  
  [YYYY-MM-DD]

- **Reviewed By / Approval:**  
  [Reviewer/approver name & date]

- **Summary:**  
  [Brief overview of what is being tested]

---

## 2. Test Design Checklist

- [ ] Review acceptance criteria and requirements (attach or link)
- [ ] Identify test scenarios and edge cases
- [ ] Define test data requirements
- [ ] Plan test environment needs (specify below)
- [ ] List required mock services/dependencies
- [ ] Consider non-functional requirements (performance, security, usability)
- [ ] Review for test coverage and traceability (see matrix below)
- [ ] Identify automation opportunities (mark in table)
- [ ] Peer review/sign-off

---

## 3. Traceability Matrix

| Requirement/AC ID | Test Case ID(s) | Coverage Status | Notes |
|-------------------|-----------------|-----------------|-------|
|                   |                 |                 |       |

---

## 4. Test Scenarios & Cases

| Test Case ID | Scenario/Description         | Preconditions | Test Steps | Expected Result | Status | Priority | Owner | Automated (Y/N) | Actual Result | Date Executed |
|--------------|------------------------------|--------------|------------|----------------|--------|----------|-------|-----------------|---------------|---------------|
| TC-01        | [Describe scenario]          | [Pre-reqs]   | [Steps]    | [Expected]     | [Open] | [High]   | [Name]| [Y/N]           | [Result]      | [YYYY-MM-DD]  |
| TC-02        |                              |              |            |                |        |          |       |                 |               |               |

---

## 5. Non-Functional Testing

| Area         | Test Description                | Criteria/Threshold | Status | Owner | Notes |
|--------------|--------------------------------|--------------------|--------|-------|-------|
| Performance  | [e.g., response time < 2s]     | [2s]               | [Open] |       |       |
| Security     | [e.g., role-based access]      | [Pass/Fail]        |        |       |       |
| Usability    | [e.g., WCAG 2.1 compliance]    | [Pass/Fail]        |        |       |       |
| Compatibility| [e.g., Chrome, Safari, iOS]    | [List]             |        |       |       |
| Other        | [e.g., reliability, scalability]| [Describe]         |        |       |       |

---

## 6. Test Environment

- **Environment(s):** [e.g., QA, Staging, Production-like]
- **Configuration:** [OS, browser, DB, etc.]
- **Mock Services/Dependencies:** [List]
- **Special Setup/Config:** [Details]

---

## 7. Risks, Blockers & Mitigations

- **Risks:** [Identify risks]
- **Blockers/Dependencies:** [List]
- **Mitigations:** [Proposed mitigations]

---

## 8. References

- **Requirements:** [Link]
- **Designs/Specs:** [Link]
- **Related Docs:** [Link]

---

**Tip:**  
Update this template as the project evolves. Use the traceability matrix to ensure all requirements are covered and results are tracked.

