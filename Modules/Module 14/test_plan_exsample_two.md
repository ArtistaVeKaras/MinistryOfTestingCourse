# Test Plan Example: Mobile Banking App v2.0

## What is a Test Plan?

A test plan is a document that maps out your testing strategy, objectives, resources, and schedule. It defines what you'll test, how you'll do it, and who's responsible for each piece. This blueprint keeps everyone aligned and focused.

---

## 1. Objectives

- Verify all payment functions work across iOS and Android devices.
- Validate that biometric login meets security standards.
- Ensure 99.9% uptime during peak usage periods.
- Confirm user account management features function as intended.
- Ensure push notifications are delivered reliably.

---

## 2. Scope

- **In Scope:**

  - Login functionality
  - Payments (including transfers and bill payments)
  - Account management (view balances, transaction history)
  - Push notifications
  - Biometric authentication (Face ID, fingerprint)

- **Out of Scope:**
  - Marketing content
  - Back-office functions
  - Non-mobile platforms (e.g., web app)

---

## 3. Schedule

- Functional testing: March 1–7
- Performance testing: March 8–10
- Security testing: March 11–14
- User Acceptance Testing (UAT): March 15–20
- Test plan review and sign-off: March 21

---

## 4. Resources

- 2 iOS testers
- 2 Android testers
- 1 performance engineer
- 1 security specialist
- Test environments: Development, Staging, UAT
- Devices: Latest iOS and Android smartphones

---

## 5. Risks & Contingencies

- **Risk:** Third-party payment gateway unavailable  
  **Mitigation:** Confirm scheduled maintenance windows and have backup test accounts.
- **Risk:** Delays in app store approvals  
  **Mitigation:** Submit builds early and maintain communication with app store teams.
- **Risk:** Incomplete test data  
  **Mitigation:** Prepare and validate test data sets in advance.

---

## 6. Entry Criteria

- All requirements and user stories are finalized and approved.
- Test environments are set up and accessible.
- Test data is prepared and available.
- Latest app build is deployed to test environments.

---

## 7. Exit Criteria

- All planned test cases executed.
- All critical and high-priority defects are fixed and verified.
- Test summary report completed and reviewed.
- Stakeholders have signed off on test results.

---

## 8. Version Control

- This document is versioned. Update the version number and changelog with each significant change.
- Store the document in a shared repository for team access.

**Changelog**

| Version | Date       | Author  | Description of Change         |
| ------- | ---------- | ------- | ----------------------------- |
| 1.0     | 2025-06-27 | QA Lead | Initial creation of test plan |
