Test automation project developed using Playwright, Cucumber (Behave), and Python.

It contains the login tests plus the Mobile Reports UI tests ported from the Cypress/TypeScript project `ui-auto-tests`.

## Setup
1. `pip install -r requirements.txt` and `playwright install chromium`
2. Copy `.env.example` to `.env` and fill in the credentials.

## Running
- All: `behave`
- One feature: `behave features/home_page_from_url.feature`
- Headed: set `HEADLESS=false`

## Notes
- Features ending in `_from_explorer` / `_from_url` are tagged `@from_explorer` / `@from_url`; the former render the mobile report inside an iframe.
- Scenarios tagged `@commented_out_in_cypress` were commented out in the source project. Exclude them with `behave --tags=-commented_out_in_cypress`.
- Test data lives in `test_data/`; shared constants in `config/constants.py`.
