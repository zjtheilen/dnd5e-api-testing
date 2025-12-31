## Objective:
Create structured test cases for selected D&D API endpoints to verify correct functionality, data integrity, and error handling. Ensure tests are repeatable and clearly documented for both manual review and automated execution.

### Endpoints Selected:
* Classes (/api/classes)
* Races (/api/races)
* Spells (/api/spells)
* Monsters (/api/monsters)
* Equipment (/api/equipment)

### Test Types Applied:
* Functional Testing: Validate endpoint responses against expected status codes, required fields, and correct data types.
* Regression Testing: Ensure repeated requests return consistent results, and no existing functionality breaks when new requests are tested.
* Exploratory Testing: Perform unscripted requests to discover unexpected API behavior or edge cases.
Example Test Case Structure:

| Test Case ID | Endpoint | Test Type | Steps | Expected Result | Notes |
| ------------ | -------- | --------- | ----- | --------------- | ----- |
| TC-001 | /api/classes | Functional | Send GET request | Status 200, list of classes returned, each object contains index, name, hit_die | Validate all required fields present |
| TC-002 | /api/classes/invalid | Functional | Send GET request with invalid class | Status 404 or error message | Validate API handles invalid input gracefully |
| TC-003 | /api/spells | Regression | Send GET request multiple times | Response consistent across requests | Check data consistency |
| TC-004 | /api/monsters | Exploratory | Test filtering or unexpected parameters | Status handled correctly, no crashes | Identify edge cases |

### Test Artifacts Planned:
* Detailed test case documentation (ID, endpoint, test type, steps, expected result, notes)
* Notes on assumptions, scope decisions, and limitations
* Mapping of test cases to endpoint functionality

### Tools & Skills Demonstrated:
* Test case design for APIs
* Functional, regression, and exploratory testing
* Planning for automated test scripts in Python (or Playwright, if preferred)
* Documentation best practices for QA workflows

## Implementation Status
Automated test coverage currently includes:
- Classes
- Spells
- Monsters

Races and Equipment remain planned but were deprioritized to focus on deeper schema validation, exploratory testing, and defect documentation for core endpoints.
