Observed Defects & Schema Discrepancies

This document captures issues, inconsistencies, and notable observations discovered while executing automated tests against the DnD5e API during **Phase 4 – Test Execution & Defect Documentation**.

All findings were discovered through automated Pytest runs and exploratory validation.

---

## Overview

- **API Tested:** https://www.dnd5eapi.co/
- **Test Framework:** Pytest (Python 3.11)
- **Test Types Executed:**
  - Positive functional tests
  - Negative tests
  - Schema validation
  - Exploratory tests

---

## Defect & Discrepancy Log

### 1. Classes Endpoint – Optional `spellcasting` Field

**Endpoint:**  
`GET /api/2014/classes/{index}`

**Description:**  
The `spellcasting` field is not present for non-spellcasting classes such as `fighter`.

**Expected:**  
All class responses contain the same schema, or optional fields are clearly documented.

**Actual:**  
- Spellcasting classes (e.g., `wizard`, `cleric`) include `spellcasting`
- Martial classes (e.g., `fighter`) omit this field entirely

**Impact:**  
Schema validation must account for conditional fields based on class type.

**Resolution / Test Adjustment:**  
Schema assertions updated to treat `spellcasting` as optional rather than required.

**Status:**  
Documented – expected behavior, not a breaking defect

---

### 2. Spell Responses Contain Class-Specific Fields

**Endpoint:**  
`GET /api/2014/spells/{index}`

**Description:**  
Spell responses contain a `classes` array referencing class resources, but do not include class-level fields such as `hit_die`, `saving_throws`, etc.

**Expected:**  
Spell schemas remain distinct from class schemas.

**Actual:**  
An incorrect schema assertion was initially applied, assuming class fields existed in spell responses.

**Impact:**  
False-negative test failures during schema validation.

**Resolution / Test Adjustment:**  
Separate schema validators created for:
- Spells
- Classes
- Monsters

**Status:**  
Resolved via test correction

---

### 3. Monsters Endpoint Accepts Unknown Query Parameters

**Endpoint:**  
`GET /api/2014/monsters?{unexpected_param}`

**Description:**  
The monsters endpoint does not reject or error on unknown query parameters.

**Expected:**  
API may return validation errors or ignore invalid parameters explicitly.

**Actual:**  
- Unknown parameters are silently ignored
- Valid response is still returned with HTTP 200

**Impact:**  
Could lead to silent failures or false assumptions by API consumers.

**Resolution:**  
Documented as exploratory behavior; tests assert stability rather than failure.

**Status:**  
Observed behavior – no functional defect

---

### 4. Consistent Error Handling for Invalid Resource Indices

**Endpoints Tested:**  
- `/classes/{invalid}`
- `/spells/{invalid}`
- `/monsters/{invalid}`

**Observation:**  
All tested endpoints correctly return:

- HTTP Status: `404`
- JSON error payload

**Status:**  
No defect – behavior matches expectations

---

## General Observations

- API responses are stable and consistent across repeated executions.
- Schema variance is primarily due to **optional or conditional fields**, not malformed data.
- Error handling for invalid resources is reliable.
- Exploratory testing revealed lenient query parameter handling.

---

## Testing Takeaways

- Schema validation should reflect **real-world API flexibility**, not rigid assumptions.
- Exploratory testing is essential to uncover undocumented behaviors.
- Parameterized tests significantly reduced duplication and improved coverage.

---

## Phase Status

**Phase 4 – Test Execution & Defect Documentation:**  
**Completed**

Next planned phase:
**Phase 5 – Regression & Exploratory Testing**

---

*This document is intended for inclusion in the `/tests` directory as supporting QA documentation.*
