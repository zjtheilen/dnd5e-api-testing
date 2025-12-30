# DnD5e API Tests

This directory contains automated tests for the [DnD5e API](https://www.dnd5eapi.co/), demonstrating API validation, schema checks, and edge case handling using Python and Pytest.

## Purpose

These tests ensure that key endpoints of the DnD5e API behave as expected:

- **Classes** – Verify valid and invalid class requests, positive tests, and schema validation.
- **Spells** – Validate known spells, handle invalid spell indices, and enforce schema consistency.
- **Monsters** – Test exploratory filters, positive tests, and schema validation.

## Technologies

- Python 3.11
- [Pytest](https://docs.pytest.org/)
- [Requests](https://docs.python-requests.org/)

## Test Coverage

| Test File | Description |
|-----------|-------------|
| `test_classes_endpoint.py` | Validates that the classes endpoint returns a correct list. |
| `test_classes_valid_requests.py` | Positive tests for known classes with schema validation. |
| `test_classes_valid_schema_validation.py` | Validates the structure and fields of class responses. |
| `test_class_invalid_endpoint.py` | Checks behavior for invalid class requests (404). |
| `test_spells_invalid_requests.py` | Ensures invalid spell indices return 404. |
| `test_spells_valid_requests.py` | Validates known spells and enforces schema. |
| `test_spells_valid_schema_validation.py` | Validates the structure and fields of spell responses. |
| `test_monsters_exploratory_filters.py` | Tests monsters endpoint with unexpected parameters. |
| `test_monsters_valid_requests.py` | Positive tests for known monsters. |
| `test_monsters_valid_schema_validation.py` | Validates the structure and fields of monster responses. |

## Notable Testing Strategies

- **Parameterized Tests** – Efficiently test multiple inputs using `pytest.mark.parametrize`.
- **Schema Validation** – Ensures API responses contain expected fields and types.
- **Positive Tests** – Verify known good inputs return expected results.
- **Edge Case Handling** – Tests invalid endpoints and unexpected query parameters.
- **Defect Logging** – Phase 4 defect log captures schema discrepancies and unusual API behavior.

## Phase 4 – Observed Defects & Schema Discrepancies

Documented in [`DEFECTS.md`](./DEFECTS.md) (or inline below), including API response snippets and notes on schema issues. Highlights areas where the API differs from expected behavior, optional fields, or variable data types (e.g., `armor_class` as a list vs int).

## Running the Tests

From the project root directory:

```bash
pytest
```

* All tests are independent and can be run individually.
* Include `-v` for verbose output or `-k <pattern>` to run a subset:

```bash
pytest -v -k test_spells_valid_requests
```

## Notes

* The tests are designed for **both regression and exploratory testing**, making it easy to identify new or recurring defects.
* Schema validation functions are implemented in `api_client.py` and resused across tests.
* Positive tests ensure expected API responses remain stable over time.