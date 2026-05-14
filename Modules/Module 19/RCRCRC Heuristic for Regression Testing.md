# RCRCRC Heuristic for Regression Testing

The RCRCRC heuristic, introduced by Rahul, is a powerful mnemonic that helps guide effective regression testing. It provides a structured approach to identify what areas to focus on during testing.

## What is RCRCRC?

RCRCRC stands for:

- **R**ecent Changes
- **C**ore Functionality
- **R**isky Areas
- **C**onfiguration-Sensitive Areas
- **R**epaired Features (previous bugs)
- **C**hronic Problem Areas

## How to Use RCRCRC

### 1. Recent Changes

- Focus on recently modified or added features
- New code is more likely to contain defects
- Check integration points with existing functionality

### 2. Core Functionality

- Test the most critical features that users depend on
- Identify the "must work" paths through the application
- Ensure basic user journeys function correctly

### 3. Risky Areas

- Target complex or poorly understood code
- Areas with many dependencies
- Features with a history of issues

### 4. Configuration-Sensitive Areas

- Test different configurations and environments
- Check feature flags and toggles
- Verify backward compatibility

### 5. Repaired Features

- Retest previously fixed bugs
- Check for regression in related areas
- Verify the fix doesn't introduce new issues

### 6. Chronic Problem Areas

- Focus on components with a history of failures
- Areas that frequently require hotfixes
- Known fragile parts of the system

## Best Practices

- Use RCRCRC as a thinking tool, not a strict checklist
- Prioritize tests based on risk and impact
- Document your test coverage and decisions
- Update your test strategy as the system evolves

## When to Apply RCRCRC

- Before releases or deployments
- After significant code changes
- When planning test cycles with limited time
- To identify test cases for automation