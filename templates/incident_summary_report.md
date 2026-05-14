# Incident Summary Report

## What is it?

A concise document that provides an overview of a production incident, including key details, impact, and resolution status.

## Purpose

To communicate the incident's details, track its lifecycle, and enable informed decision-making for stakeholders.

---

## Incident Report Template

| Field             | Description                                                                 |
|-------------------|-----------------------------------------------------------------------------|
| **Incident ID**   | Unique identifier for the incident                                          |
| **Title**         | Brief summary of the incident                                               |
| **Date Reported** | Date when the incident was first reported                                   |
| **Severity**      | Impact level (e.g., Low, Medium, High, Critical)                            |
| **Environment**   | Affected environment(s) (e.g., Production, Staging)                         |
| **Description**   | Detailed description of the incident                                        |
| **Steps to Reproduce** | Step-by-step instructions to reproduce the issue                       |
| **Impact**        | Who/what is affected, business or user impact                               |
| **Status**        | Current status (e.g., Open, In Progress, Resolved, Closed)                  |
| **Assigned To**   | Responsible team or individual                                              |
| **Actions Taken** | Actions performed to investigate or mitigate the incident                   |
| **Resolution**    | How the incident was resolved, or next steps if unresolved                  |
| **Evidence**      | Attach logs, screenshots, videos, or customer complaints (if applicable)    |

---

## Example

### Incident ID: 101

**Title:** System crashes on clicking the "Checkout" button  
**Date Reported:** January 15, 2025  
**Severity:** High  
**Environment:** Staging and Production  
**Description:**  
The system crashes when a user clicks on the "Checkout" button after adding items to the cart.

**Steps to Reproduce:**

1. Add items to the cart.
2. Click the "Checkout" button.
3. Observe the system crash.

**Impact:**  
Affects users attempting to complete a purchase, resulting in potential revenue loss and poor user experience.

**Status:** Open  
**Assigned To:** SRE Team  
**Actions Taken:**  
The development team has debugged the issue and identified that it is caused by database downtime.

**Resolution:** Pending  
**Evidence:**

- Application logs showing database connection errors  
- User complaints submitted via support portal

---

## Tips

- Use this template to ensure consistency and completeness of information.
- Keep the summary concise while focusing on key aspects (impact, severity, actions).
- Include necessary evidence (e.g., logs, screenshots, videos, customer complaints) to support the investigation.
- Update the report as the incident progresses and new information becomes available.
