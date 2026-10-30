"""Login session reuse, the Playwright equivalent of Cypress `cy.session`."""


class AuthSession:
    """Holds the storage state of the first successful login so later scenarios
    can start already authenticated."""

    storage_state = None
