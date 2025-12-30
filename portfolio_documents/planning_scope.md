## Objective:
Gain hands-on experience with API testing by validating the D&D 5e API (https://www.dnd5eapi.co). The goal is to ensure endpoints return correct, consistent, and complete data while practicing structured QA workflows.
### Scope:
* Test endpoints for Classes, Races, Spells, Monsters, and Equipment.
* Focus on verifying:
    * Correct status codes (200 for valid requests, 404/400 for invalid requests)
    * Presence of required fields
    * Data type correctness (strings, integers, arrays, objects)
    * Handling of invalid inputs and edge cases

* Include both functional and exploratory testing.
* Exclude endpoints or features outside core gameplay data (e.g., advanced optional rules, homebrew content) to keep the project manageable.
### Assumptions:
* The API is publicly accessible and does not require authentication.
* Data returned is static and consistent across requests.
* Testing will use Python (requests/httpx) for automation.
### Constraints:
* Limited time: project will focus on a subset of endpoints.
* No backend access; only testing via public API.
* No performance or load testing in this phase.

