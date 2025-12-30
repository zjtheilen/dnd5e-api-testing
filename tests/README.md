# DnD5e API Tests

This directory contains automated tests for the [DnD5e API](https://www.dnd5eapi.co/), demonstrating API validation, schema checks, and edge case handling using Python and Pytest.

## Purpose

These tests ensure that key endpoints of the DnD5e API behave as expected:

- **Classes** – Verify valid and invalid class requests, and enforce schema consistency.
- **Spells** – Validate known spells, handle invalid spell indices, and enforce schema consistency.
- **Monsters** – Test exploratory filters, positive requests, and schema validation.

## Technologies

- Python 3.11
- [Pytest](https://docs.pytest.org/)
- [Requests](https://docs.python-requests.org/)

## Test Coverage

| Test File | Description |
|-----------|-------------|
| `test_classes_endpoint.py` | Validates that the classes endpoint returns a correct list. |
| `test_invalid_class_endpoint.py` | Checks behavior for invalid class requests (404). |
| `test_classes_valid_requests.py` | Positive tests for known classes, ensuring correct data is returned. |
| `test_classes_valid_schema_validation.py` | Validates the schema of class responses to ensure expected fields and types. |
| `test_spells_invalid_requests.py` | Ensures invalid spell indices return 404. |
| `test_spells_valid_requests.py` | Positive tests for known spells, checking status codes and response content. |
| `test_spells_valid_schema_validation.py` | Validates the schema of spell responses to ensure expected fields and types. |
| `test_monsters_exploratory_filters.py` | Tests monsters endpoint with unexpected or edge-case query parameters. |
| `test_monsters_valid_requests.py` | Positive tests for known monsters, ensuring correct data is returned. |
| `test_monsters_valid_schema_validation.py` | Validates the schema of monster responses to ensure expected fields and types. |

## Notable Testing Strategies

- **Parameterized Tests** – Efficiently test multiple inputs using `pytest.mark.parametrize`.
- **Schema Validation** – Ensures API responses contain expected fields and types.
- **Edge Case Handling** – Tests invalid endpoints and unexpected query parameters.
- **Positive Testing** – Confirms that valid requests return expected data.

## Running the Tests

From the project root directory:

```bash
pytest
```

This will automatically discover and run all tests in the `tests` directory.