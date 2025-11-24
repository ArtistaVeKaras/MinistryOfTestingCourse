# Managing a Test Plan

## Sections of a Test Plan

What goes into a test plan can vary greatly depending on the context. Regulated industries, like finance,
will likely require more detailed test planning and documented evidence of execution. In contrast, a startup
in a non-regulated industry may use a more minimalist test plan or sometimes no written test plan at all. 
However, there are several key components that most test plans usually include. Let’s explore those in more detail.

---

### Objectives of a Test Plan

The most obvious component of a test plan is the section covering objectives. We ask ourselves what we want to accomplish with our testing. 
Objectives for test plans shouldn’t be abstract; they need to be **specific, measurable, achievable, relevant, and time-bound (SMART criteria)**.

**Examples of objectives for an online shop:**

- **Planning and execution:**  
  - What will be tested  
  - Requirements and code coverage  
  - Early test involvement  
  - Bug recording and management  
  - Functional and quality characteristics (meeting requirements)  
  - *Example:* Verify core e-commerce functionalities to ensure users can browse products, add them to the cart, change quantities, remove items, and that the calculation of taxes, total, and shipping costs is valid.
  - Validate the checkout process to ensure users can complete purchases, receive confirmations, and apply discounts.
  - Verify user account management, including registration, password reset, profile management, and order history.
  - Validate product search and filtering to ensure customers can find and sort products.
  - Test inventory management to ensure accurate stock display and proper handling of out-of-stock items.

- **Usability and user experience:**  
  - Ensure user navigation is intuitive and the interface is clear and consistent.
  - Validate responsiveness across devices (phones, tablets, laptops).
  - Test for accessibility to ensure compliance with WCAG (Web Content Accessibility Guidelines).

- **Performance:**  
  - Validate website load times and performance under heavy traffic.
  - Test database performance for efficient queries and high transaction volumes.
  - Validate server stability under expected loads.

- **Security:**  
  - Validate secure payments and check for vulnerabilities.
  - Ensure user data protection and encryption.
  - Validate access control for proper user permissions.

- **Integration of third-party software:**  
  - Verify payment processor integration.
  - Test integration with shipping providers for order tracking.
  - Validate inventory management system integration.

---

### Defining the Scope for a Test Plan

Clearly define what will be tested and, just as importantly, what will not be tested. This prevents scope creep and helps manage stakeholder expectations.

**Examples of scope boundaries:**

- **Functional boundaries:**  
  - *In scope:* Shopping cart features (add/remove products, calculate totals).  
  - *Out of scope:* Cancelling orders or post-purchase reviews.

- **Modules:**  
  - *In scope:* User authentication (registration, login, password reset).  
  - *Out of scope:* Product administration.

- **Workflows:**  
  - *In scope:* Customer checkout process.  
  - *Out of scope:* Post-purchase review submission.

- **Third-party add-ons:**  
  - *In scope:* Payment plugin integration points.  
  - *Out of scope:* Internal workings of the payment processor.

- **Data boundaries:**  
  - *In scope:* Customer billing/shipping addresses.  
  - *Out of scope:* Profile images.

- **User boundaries:**  
  - *In scope:* Admin dashboard features for admins.  
  - *Out of scope:* Features for other user roles.

---

### Entry and Exit Criteria in a Test Plan

**Entry criteria** are conditions that must be met before testing can start. **Exit criteria** define when planned testing activities are considered complete. These should be clear and unambiguous, similar to Definition of Ready (DoR) and Definition of Done (DoD) but specific to testing.

**Examples:**

- **Entry Criteria:**
  - Test environment is set up according to requirements.
  - Required hardware and software are installed and operational.
  - Test components are accessible over the network.
  - Test data is created, available, and covers all scenarios.
  - Sensitive data is anonymised or masked.
  - All appropriate tests have been run and passed.
  - Version designations and their content are known.

- **Exit Criteria:**
  - All planned tests for the sprint or test period have been executed.
  - Target code coverage (e.g., 80%) is achieved.
  - All top-priority requirements have been tested.
  - All critical and high-priority bugs are fixed.
  - Regression tests are in place for resolved issues.
  - Any accepted or mitigated bugs are recorded and managed.
  - Stakeholders have formally signed off the release.
  - User acceptance testing is finished and approved by the customer.

---

### Including Risks in a Test Plan

This section should cover potential issues that could impact testing and include mitigation plans. 
Risk analysis helps focus testing on high-risk areas.

**Benefits of documenting risks:**

- Proactively identify potential problems before they impact the project.
- Prioritise what to test first and more deeply.
- Understand and mitigate risks early.
- Reduce costs by avoiding more expensive fixes later.

---

### Timelines in a Test Plan

Include realistic timelines, milestones, and deadlines for testing. Consider dependencies on development activities
and update the timeline as needed. Communicate any changes to all stakeholders promptly.

---

### Resources and People in a Test Plan

Identify the resources and people (or roles) required to execute the test plan. 
This includes the number of testers, required environments, tools, and test data. 
This section is more common in larger projects.

---

### Test Strategy in a Test Plan

Outline the overall approach to testing, including types of testing (functional, non-functional), 
levels (unit, integration, end-to-end), and methodologies. The test strategy may be a separate document
but should be referenced in the test plan.

---

### Updating a Test Plan

Test plans are living documents and must be updated as circumstances change. 
Updates may be significant or minor. Always update the test plan to keep it relevant and useful.

**Common reasons for updating test plans:**
- Changes in requirements or scope
- New risks identified
- Timeline adjustments
- Resource changes

---

### Version Control in a Test Plan

When updating the test plan, it’s crucial to use version control to track changes and ensure 
everyone is working with the latest version. Automated tools (e.g., Git, SharePoint) allow 
for tracking revisions and reverting to previous versions. Alternatively, issue documents 
with a new version number and maintain a changelog.

**Best practices:**
- Update the version number with each significant change (e.g., 1.1, 1.2, 2.0).
- Record the date and summary of changes in a changelog section.
- Store the document in a shared repository for team access.
- Agree on a simple versioning convention for consistency.

---