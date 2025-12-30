## Observed Defects & Schema Discrepancies

While executing automated tests against the DnD5e API, the following issues and discrepancies were observed. This log combines schema inconsistencies, edge cases, and unexpected API behavior with actual response examples.

| ID | Endpoint | Test File | Input / Parameter | Observed Result | Expected Result | Issue Type | Notes |
|----|----------|-----------|-----------------|----------------|----------------|------------|-------|
| 1  | `/monsters/{monster}` | `test_monsters_valid_schema_validation.py` | `aboleth` | `armor_class` returned as list of dicts: <br>```json [{"type":"natural","value":17}]``` | `armor_class` should be `int` | Schema Discrepancy | Adjusted schema validation to handle list-of-dicts returned from API |
| 2  | `/monsters/{monster}` | `test_monsters_valid_schema_validation.py` | `archmage` | `armor_class` returned as list of dicts: <br>```json [{"type":"spell","value":12}]``` | `int` | Schema Discrepancy | Similar to aboleth; consistent handling applied |
| 3  | `/classes/{class}` | `test_classes_valid_requests.py` | `fighter` | Some expected fields missing: <br>```json {"index":"fighter","hit_die":10,"proficiencies":[...]} ``` | Fields like `name` should exist | Schema Discrepancy / API inconsistency | Some class objects do not return all expected keys; validation updated to allow optional fields |
| 4  | `/spells/{spell}` | `test_spells_valid_schema_validation.py` | `fireball` | `assert_class_schema` applied incorrectly on spell data: <br>```json {"index":"fireball","name":"Fireball","level":3,"casting_time":"1 action"} ``` | Spell-specific schema should be used | Misapplied Schema Assertion | Fixed by using `assert_spell_schema` for spell responses |
| 5  | `/spells/{spell}` | `test_spells_valid_schema_validation.py` | `mage-hand` | Same as fireball; schema assertion failure due to misapplied class schema | Spell-specific schema enforced | Misapplied Schema Assertion | Fixed as above |
| 6  | `/spells/{spell}` | `test_spells_valid_schema_validation.py` | `acid-arrow` | Same as fireball | Spell-specific schema enforced | Misapplied Schema Assertion | Fixed as above |
| 7  | `/monsters/` | `test_monsters_exploratory_filters.py` | Unexpected parameters: <br> `unexpected=test`, `level=999`, `random_param=dragon` | API returns 200 with `results` list, sometimes empty: <br>```json {"count":0,"results":[]}``` | Acceptable, but behavior may be non-intuitive | Edge Case / Exploratory | Highlights API behavior with unknown or extreme query parameters |
| 8  | `/classes/{class}` | `test_classes_valid_requests.py` | `wizard`, `bard`, `cleric` | Optional fields like `spellcasting` may be absent: <br>```json {"index":"bard","hit_die":8,"proficiencies":[...]} ``` | Schema expects all top-level keys | Schema Discrepancy | Validation adjusted to allow optional fields |

**Notes:**

- All API response snippets above are taken directly from failed test observations.
- Schema discrepancies primarily involve:
  - `armor_class` being a list of objects instead of an integer.
  - Optional fields missing in some class responses (`spellcasting`, `name` in some cases).
- Edge cases show that the API tolerates unexpected query parameters but may return empty `results`.

**Recommendations:**

- Maintain this log for regression testing — verify if previously observed discrepancies persist.
- Use API-specific conditional validation for optional or variable fields.
- Capture live API response snippets in your defect log for interview demonstration of concrete testing skills.
