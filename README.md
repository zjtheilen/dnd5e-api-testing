# D&D 5e API Testing

Automated API tests for the [D&D 5e API](https://www.dnd5eapi.co/) using Python and `pytest`.  
This project demonstrates testing best practices, including **positive, negative, exploratory, and parameterized tests**, along with **HTML reporting**.

---

## Project Overview

This repository contains automated tests for various endpoints of the D&D 5e API.  
Testing focuses on:

- Validating correct responses for known endpoints
- Handling invalid or unexpected inputs gracefully
- Exploratory testing of edge cases
- Verifying stability of repeated requests

Technologies used:

- **Python 3.11**
- **pytest** for test execution
- **pytest-html** for HTML test reports
- **requests** library for API calls

---

## Project Structure

```bash
dnd5e-api-testing/
│
├─ tests/
│ ├─ test_classes_endpoint.py
│ ├─ test_invalid_class_endpoint.py
│ ├─ test_spells_endpoint.py
│ ├─ test_spells_multi_requests.py
│ └─ test_monsters_exploratory_filters.py
│
├─ reports/ # Output HTML reports (not committed)
├─ requirements.txt
└─ README.md
```

---

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/zjtheilen/dnd5e-api-testing.git
cd dnd5e-api-testing
```

### 2. Create & Activate Virtual Environment

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Mac/Linux
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### Running Tests

Run all tests:
```bash
pytest
```

Run tests with **HTML** report:
```bash
pytest --html=reports/report.html
```

Reports are saved to the `reports/` directory.

---

### Test Types

* **Functional** – Verify endpoints return correct responses for valid input
* **Regression** - Ensure repeated requests maintain consistent behavior
* **Exploratory** - Identify edge cases and unexpected behavior
* **Negative / Error Handling** - Validate proper handling of invalid endpoints or parameters

---

### Key Features Demonstrated

* API endpoint validation
* Parametrized tests for multiple input scenarios
* Error handling tests for invalid resources
* HTML reporting with `pytest-html`
* Structured, maintainable Python test code
