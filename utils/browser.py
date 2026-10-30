from config.config import Config

VIEWPORT = {"width": 1920, "height": 1080}


def new_browser_context(context, storage_state=None):
    """Create a fresh browser context + page on the behave `context`, optionally already logged in."""
    context.browser_context = context.browser.new_context(
        viewport=VIEWPORT, storage_state=storage_state, accept_downloads=True
    )
    context.browser_context.set_default_timeout(Config.DEFAULT_TIMEOUT)
    context.page = context.browser_context.new_page()
