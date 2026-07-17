# API Automation – restful-booker

![API Tests](https://github.com/PartlyClaudie/Me-Vs-restful-booker/actions/workflows/tests.yml/badge.svg)

Automated API tests for https://restful-booker.herokuapp.com
using pytest and requests.

## Why this project
Second project in my testing portfolio — moving from manual testing
into automation, starting with API-level tests since they're fast,
stable, and don't depend on UI rendering.

## Tech stack
- Python
- pytest
- requests

## Coverage
- **Auth** — token creation with valid/invalid credentials
- **Booking CRUD** — create, read, update, delete
- **Negative cases** — invalid ID, missing auth token, malformed
  request body

## Key finding
Found a real API defect: sending a booking request without a
required field causes a `500 Internal Server Error` with a
plain-text body, instead of a proper `400` validation error. Full
writeup in the manual testing repo — see
[BUG-002](https://github.com/PartlyClaudie/Me-Vs-the-internet/blob/main/bug-reports/BUG-002-missing-field-500-error.md).

## Setup
\`\`\`bash
python -m venv venv
source venv/Scripts/activate   # Windows Git Bash
pip install -r requirements.txt
\`\`\`

## Run tests
\`\`\`bash
pytest tests/ -v
\`\`\`

## Lessons learned
- restful-booker returns `200` (not `401`) on failed auth, and `201`
  (not `200`) on successful delete — reinforced verifying real API
  behavior instead of assuming standard HTTP conventions.
- A test that calls `.json()` on a response without checking the
  content type first will crash on non-JSON error responses —
  learned this the hard way when a 500 error came back as plain text.
- Extracted shared setup (base URL, auth token, booking payload,
  created booking) into pytest fixtures to remove duplication across
  test files.

## Related portfolio projects
- [Manual test cases & bug reports](https://github.com/PartlyClaudie/Me-Vs-the-internet)
- [UI automation (Playwright)](https://github.com/PartlyClaudie/Me-Vs-Playwright)