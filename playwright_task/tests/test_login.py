from playwright_task.pages.login_page import LoginPage


def test_successful_login(browser_setup):

    page = browser_setup

    login = LoginPage(page)

    login.login("nasinahemanth0801@gmail.com", "Hemu@0801")

    page.wait_for_timeout(5000)

    assert "dashboard" in page.url.lower() or "zenclass" in page.url.lower()


def test_unsuccessful_login(browser_setup):

    page = browser_setup

    login = LoginPage(page)

    login.login("incorrect@gmail.com", "wrong@password")

    page.wait_for_timeout(3000)

    assert "login" in page.url.lower()


def test_validate_username_box(browser_setup):

    page = browser_setup

    login = LoginPage(page)

    assert login.validate_username_box() is True


def test_validate_password_box(browser_setup):

    page = browser_setup

    login = LoginPage(page)

    assert login.validate_password_box() is True


def test_validate_submit_button(browser_setup):

    page = browser_setup

    login = LoginPage(page)

    assert login.validate_submit_button() is True


def test_logout(browser_setup):

    page = browser_setup

    login = LoginPage(page)

    login.login("nasinahemanth0801@gmail.com", "Hemu@0801")

    page.wait_for_timeout(5000)

    assert "dashboard" in page.url.lower()