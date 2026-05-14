# Clarify Your Language

When writing requirements or specifications, it’s important to clarify the meaning of each word and phrase to avoid ambiguity. Use the following prompts to help ensure your language is precise and well-understood by everyone involved.

---

| Term        | Clarifying Questions                                                                                       |
|-------------|-----------------------------------------------------------------------------------------------------------|
| **The**     | - Why "the" system and not "a" system—could there be multiple integrated systems?<br>- Which part of the system is responsible—frontend, backend, or both?<br>- Is the system unique to this context, or could there be similar systems elsewhere?<br>- Is there a shared responsibility with other systems or teams?<br>- Is the system part of a larger ecosystem or platform? |
| **system**  | - By system is it actually referring to an input field?<br>- If it is a system, is it a new system, or are we updating an existing one?<br>- Does the system include business processes, as well as a programmable system?<br>- Is the system cloud-based, on-premises, or hybrid?<br>- What are the system’s boundaries and interfaces?<br>- Are there dependencies on third-party services or APIs? |
| **should**  | - Is this optional or mandatory?<br>- Does “should” mean it’s nice to have but not required?<br>- Is this a regulatory or compliance requirement?<br>- What are the consequences if this is not implemented?<br>- Is there a priority or ranking for this requirement compared to others? |
| **handle**  | - Does it mean processing, storing, or validating?<br>- What happens if it can’t handle something?<br>- Does handling include logging or auditing actions?<br>- Should the system notify users or admins if it cannot handle something?<br>- Are there fallback or recovery mechanisms in place? |
| **all**     | - Does “all” include every possible input type or only specific ones?<br>- Are there exceptions, like emojis or unsupported characters?<br>- Are there any exclusions or special cases?<br>- Should future input types be considered for scalability?<br>- How will new input types be validated or supported? |
| **user**    | - Are these internal users (admins), external customers, or both?<br>- Does the requirement apply equally to all user roles, or do some roles have different input rules?<br>- Are there accessibility considerations for different user groups?<br>- Are there localization or internationalization requirements?<br>- How are user permissions and authentication managed? |
| **inputs**  | - Are these text inputs, files, or something else?<br>- What formats or sizes are expected?<br>- Are there restrictions on input length or format?<br>- Should inputs be sanitized or validated for security?<br>- Are there default values or optional fields? |
| **efficiently** | - How do we measure efficiency, is there a defined performance requirement?<br>- What is the expected behaviour under heavy load or stress, and are there defined strategies to handle it?<br>- What are the acceptable response times for different operations?<br>- Are there benchmarks or KPIs for efficiency?<br>- How will efficiency be monitored and reported over time? |

---

Use these questions as a checklist when reviewing requirements to ensure clarity and completeness. Address any ambiguous terms or phrases before proceeding with development or implementation to avoid misunderstandings and ensure all parties have a shared understanding of the requirements.
