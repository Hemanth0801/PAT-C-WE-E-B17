from playwright.sync_api import TimeoutError


class LoginPage:

    def __init__(self, page):

        self.page = page

        self.email_input = page.locator("//input[@placeholder='Enter your mail']")
        self.password_input = page.locator("(//input[@type='password'])[1]")
        self.signin_button = page.locator("//button[@type='submit']")

    def validate_username_box(self):

        try:
            self.email_input.wait_for(state="visible", timeout=5000)
            return True

        except:
            return False

    def validate_password_box(self):

        try:

            self.password_input.wait_for(state="attached", timeout=5000)

            return self.password_input.is_visible()

        except:

            return False

    def validate_submit_button(self):

        return self.signin_button.count() > 0

    def login(self, username, password):

        try:

            self.email_input.wait_for(state="visible", timeout=5000)
            self.email_input.fill(username)

            self.password_input.wait_for(state="visible", timeout=5000)
            self.password_input.fill(password)

            self.signin_button.wait_for(state="visible", timeout=5000)
            self.signin_button.click()

        except TimeoutError:

            print("Element not found")

    def logout(self):

        try:
            popup_close = self.page.locator("button[aria-label='close']")

            if popup_close.count() > 0:
                popup_close.click()

            self.page.wait_for_timeout(2000)

            profile_menu = self.page.locator("//div[contains(@class,'user-profile')]")

            profile_menu.wait_for(state="visible", timeout=10000)

            profile_menu.click()

            logout_btn = self.page.locator("text=Logout")

            logout_btn.wait_for(state="visible", timeout=10000)

            logout_btn.click()

        except Exception as e:

            print("Logout failed:", e)