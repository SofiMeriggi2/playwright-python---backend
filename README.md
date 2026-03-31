# Playwright + Python — API Automation

API test automation project for [Restful Booker](https://restful-booker.herokuapp.com) using Playwright's `APIRequestContext` with Python, a custom API Client pattern, and HTML reporting.

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Playwright](https://img.shields.io/badge/Playwright-latest-green)
![pytest](https://img.shields.io/badge/pytest-9.x-orange)
![CI](https://github.com/SofiMeriggi2/playwright-python---backend/actions/workflows/tests.yml/badge.svg)

---

## Tech Stack

- **Python 3.11**
- **Playwright APIRequestContext** — HTTP client for API testing
- **pytest** — testing framework
- **pytest-html** — HTML reporting
- **GitHub Actions** — CI/CD

---

## Project Structure

```
pw+python_be/
├── clients/
│   └── booking_client.py     # Encapsulates all API endpoints
├── data/
│   ├── payloads.py            # Request bodies for booking operations
│   └── messages.py            # Expected error messages
├── tests/
│   ├── test_auth.py           # Authentication endpoint tests
│   ├── test_booking_get.py    # GET /booking tests
│   ├── test_booking_post.py   # POST /booking tests
│   └── test_booking_put_patch_delete.py  # PUT, PATCH, DELETE tests
├── .github/
│   └── workflows/
│       └── tests.yml          # CI/CD pipeline
├── conftest.py                # Fixtures: API context, auth token, booking lifecycle
├── pytest.ini                 # pytest config, logging, and custom markers
└── requirements.txt           # Project dependencies
```

---

## Test Cases

| ID | Module | Method | Description | Marker |
|---|---|---|---|---|
| TC-01 | Auth | POST | Successful auth returns valid token | `smoke` |
| TC-02 | Auth | POST | Invalid credentials return error message | `negative` |
| TC-03 | Booking | GET | Get all bookings returns a list | `smoke` |
| TC-04 | Booking | GET | Get booking by ID returns correct data | `smoke` |
| TC-05 | Booking | GET | Non-existent booking ID returns 404 | `negative` |
| TC-06 | Booking | POST | Create booking returns bookingid and data | `smoke` |
| TC-07 | Booking | POST | Create booking without required fields returns error | `negative` |
| TC-08 | Booking | PUT | Full update modifies all fields correctly | |
| TC-09 | Booking | PATCH | Partial update modifies only sent fields | |
| TC-10 | Booking | DELETE | Delete booking returns 201 and booking is gone | `smoke` |

---

## Key Design Decisions

**API Client pattern** — `BookingClient` encapsulates all endpoint calls. Tests never build raw requests directly, they call descriptive methods. Same principle as Page Object Model but for APIs.

**Fixture lifecycle** — `created_booking_id` creates a booking before each test and deletes it after via teardown. Tests run in full isolation with no shared state.

**Session-scoped auth** — `auth_token` calls `/auth` once per test session and reuses the token across all tests that need it.

---

## Installation

```bash
# Clone the repository
git clone https://github.com/SofiMeriggi2/playwright-python---backend.git
cd playwright-python---backend

# Create virtual environment
python -m venv venv
source venv/bin/activate      # Mac/Linux
venv\Scripts\activate         # Windows

# Install dependencies
pip install -r requirements.txt
playwright install chromium
```

---

## Running Tests

```bash
# All tests
pytest -v

# Smoke tests only
pytest -m smoke -v

# Negative tests only
pytest -m negative -v

# Single module
pytest tests/test_auth.py -v
```

The HTML report is automatically generated at `reports/report.html` after each run.
Logs are printed live in the terminal showing booking creation, updates, and cleanup.

---

## CI/CD

The pipeline runs automatically on every push to `main`. Check the execution history in the [Actions](https://github.com/SofiMeriggi2/playwright-python---backend/actions) tab.

---

## Part of an Automation Portfolio

This is the second of five automation projects:

| # | Stack | Type |
|---|---|---|
| 1 | Playwright + Python | Frontend |
| 2 | Playwright + Python | API/Backend ← this one |
| 3 | Playwright + TypeScript | Frontend |
| 4 | Playwright + TypeScript | API/Backend |
| 5 | Selenium | Mobile |