# utils/waiter.py

from playwright.sync_api import Page, TimeoutError as PlaywrightTimeoutError

class Waiter:
    def __init__(self, page: Page, timeout: int = 5000):
        """
        :param page: Playwright page instance
        :param timeout: Default timeout in milliseconds
        """
        self.page = page
        self.timeout = timeout
    
    def wait_for_page_load(self):
        try:
            self.page.wait_for_load_state("networkidle", timeout=self.timeout)
        except Exception as e:
            f"[Waiter] Page did not fully load: {e}"

    def wait_for_selector(self, selector: str, state: str = "visible"):
        """
        Waits for a selector to reach a certain state.
        :param selector: CSS or XPath selector
        :param state: 'attached', 'detached', 'visible', or 'hidden'
        """
        try:
            self.page.wait_for_selector(selector, state=state, timeout=self.timeout)
            print(f"[Waiter] Element '{selector}' became {state}")
        except PlaywrightTimeoutError:
            print(f"[Waiter] Timeout: Element '{selector}' did not become {state} within {self.timeout} ms")

    def wait_for_text(self, selector: str, expected_text: str):
        """
        Waits until the given text appears inside the element.
        """
        try:
            self.page.wait_for_function(
                """(selector, expectedText) => {
                    const el = document.querySelector(selector);
                    return el && el.textContent.includes(expectedText);
                }""",
                arg=(selector, expected_text),
                timeout=self.timeout
            )
            print(f"[Waiter] Text '{expected_text}' found in '{selector}'")
        except PlaywrightTimeoutError:
            print(f"[Waiter] Timeout: Text '{expected_text}' not found in '{selector}' within {self.timeout} ms")
