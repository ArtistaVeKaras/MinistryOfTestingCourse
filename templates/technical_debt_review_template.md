# Technical Debt Review Template

Use this template to quickly identify, assess, and plan for technical or testing debt in your project.  
_This template is designed to be concise, actionable, and easy to integrate into your workflow._

---

## 1. DEBT IDENTIFICATION

- **Area:**  
  _Which part of the codebase? (e.g., module, feature, test suite)_

- **Type:**  
  _Technical debt / Testing debt / Documentation debt / Process debt_

- **Origin:**  
  _Created (recent shortcuts) / Inherited (legacy or leftover) / Third-party_

- **Description:**  
  _Briefly describe the debt (e.g., "No automation for user login", "Outdated dependencies", "Manual test cases only")._

- **Date Identified:**  
  YYYY-MM-DD

- **Reporter:**  
  Name or team

---

### 2. IMPACT ANALYSIS

- **Development Speed:**  
  _How does this slow down or complicate work? (e.g., slows feedback, increases manual effort)_

- **Stability/Risks:**  
  _Potential for bugs, missed issues, outages, or security vulnerabilities?_

- **Future Changes:**  
  _Does this make future updates, scaling, or onboarding harder?_

- **Business Impact:**  
  _Does this affect customer experience, compliance, or business goals?_

---

### 3. ACTION PLAN

- **Proposed Solution:**  
  _What should be done? (e.g., add tests, refactor, update docs, automate process)_

- **Effort Estimate:**  
  _Small / Medium / Large (or provide time estimate)_

- **Priority:**  
  _High / Medium / Low – Why? (e.g., critical path, high risk, quick win)_

- **Dependencies:**  
  _Does this depend on other work or teams?_

- **Integration:**  
  _How to fit this work into sprints or alongside feature work? (e.g., schedule as a clean-up task, address during code reviews, add to backlog)_

- **Owner:**  
  _Who is responsible for resolving this debt?_

- **Target Resolution Date:**  
  YYYY-MM-DD

---

**Example:**

## 1 DEBT IDENTIFICATION

- Area: Payment Gateway Tests
- Type: Testing debt
- Origin: Inherited
- Description: No automation for payment flows
- Date Identified: 2025-07-07
- Reporter: QA Team

## 2 IMPACT ANALYSIS

- Development Speed: Slows down feedback, manual regression required
- Stability/Risks: Risk of missing critical bugs, possible payment failures
- Future Changes: Harder to safely update payment logic, onboarding new testers is slower
- Business Impact: Payment failures could impact revenue and customer trust

## 3 ACTION PLAN

- Proposed Solution: Create basic automation coverage for key payment flows
- Effort Estimate: Medium (1 sprint)
- Priority: High – critical path for releases
- Dependencies: Requires test environment with payment sandbox
- Integration: Raise as a clean-up task in sprint planning; check if previous attempts exist
- Owner: QA Lead
- Target Resolution Date: 2025-07
