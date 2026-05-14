# 📑 Feature Regression Testing Template (RCRCRC)

## 1. Feature Overview

- **Feature Name:**
- **Version Change (e.g., v1 → v2):**
- **Description of Change:**

---

## 2. RCRCRC Categories

### 🆕 Recent

*What new areas of code need testing?*
-  

### ⭐ Core

*What essential functions must continue to work?*
-  

### ⚠️ Risky

*What features/areas are inherently more risky?*
-  

### 🔧 Configuration-Sensitive

*What depends on environment settings?*
-  

### 🛠️ Repaired

*What code changed to fix defects (possible regressions)?*
-  

### 🔄 Chronic

*What typically breaks and needs repeated testing?*
-  

---

## 3. Test Plan

- **Organize tests by category**
- **Prioritize by risk level**
- **Create test cases/charters**
- **Execute systematically**
- **Document findings & new risks**

---

## 4. Pro Tips

- Keep test plan as a **living document**
- Collaborate with developers for technical impacts
- Automate repeatable scenarios
- Track time spent per category

---

# ✅ Examples

### Example 1: Task Manager – Adding Priority Feature

**Feature Overview**
- Name: Task Manager Priority
- Change: v1 (simple tasks) → v2 (priority dropdown + color coding)
- Description: Introduced priority system with visual indicators

**RCRCRC Application**
- Recent: Priority dropdown, color-coded tasks
- Core: Task addition, list display
- Risky: Multiple priority changes, large task lists
- Configuration-Sensitive: Browser compatibility, accessibility settings
- Repaired: Ensure previous bug fixes still hold
- Chronic: Data persistence, UI stability

---

### Example 2: E-Commerce – Discount Code Feature

**Feature Overview**
- Name: Discount Code Application
- Change: v1 (checkout without discounts) → v2 (discount code input + validation)
- Description: Added discount field with validation and recalculation of totals

**RCRCRC Application**
- Recent: Discount input field, recalculation logic
- Core: Checkout flow, payment processing
- Risky: Multiple discounts stacking, edge cases (expired codes)
- Configuration-Sensitive: Currency formats, regional tax rules
- Repaired: Ensure past checkout bugs remain fixed
- Chronic: Cart persistence, order summary accuracy

---