# Properties of Good Requirements

There are specific criteria that apply to all types of requirements. 
Ensuring these properties helps create clear, actionable, and testable requirements that support successful project delivery.

---

## Key Properties

- **Completeness** — All requirements are defined; nothing important is missing.
- **Correctness** — Requirements accurately reflect stakeholders' needs and expectations.
- **Consistency** — Requirements are free from contradictions and are aligned across all sources.
- **Testability/Verifiability** — Requirements are testable; test cases can be derived from them.
- **Traceability** — Each requirement can be traced back to its origin (stakeholder, business goal, regulation).
- **Clarity** — Requirements are unambiguous and easily understood by all team members.
- **Feasibility** — Requirements can be implemented within existing constraints.

---

![Properties of Good Requirements](/Images/software_requirementes.png)

![How to Test Your Requirements](/Images/how_to_test_requirements.png)

---

## Requirements Testing Ideas

### Completeness

- Check each object against CRUDL (Create, Read, Update, Delete/Deactivate, List).
- Consider negative scenarios and boundary conditions (use cases).
- For complex if-then conditions, ensure all options are described (decision tables).

### Correctness

- Requirements should not contain incorrect or inaccurate information.
- Peer review by subject matter experts helps validate correctness.

### Consistency

- Watch for duplicate requirements in different places—updates may be missed.
- Beware of combined requirements (e.g., "fast, good, and cheap") that may contradict each other.

### Clarity

- Use consistent terminology—define all key concepts.
- Replace vague terms (“beautiful”, “convenient”, “fast”) with measurable parameters.
- Write requirements in simple, direct language—clearly state who does what.

### Testability/Verifiability

- Every requirement should have clear acceptance criteria.
- Acceptance criteria must be accurate and unambiguous.
- QA engineers should be able to write checklists or test cases for each requirement.
- If you can't test a requirement, it's likely not a good requirement.

### Feasibility

- Assess whether the requirement can be implemented within technical, time, and resource constraints.
- QA engineers and developers should collaborate to evaluate feasibility, leveraging technical expertise.

---

**Tip:**  
Regularly review and refine requirements with all stakeholders to ensure they remain 
complete, correct, consistent, clear, testable, traceable, and feasible throughout the project lifecycle.