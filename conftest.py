import os
import pytest
from datetime import datetime

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.firefox.service import Service as FirefoxService

from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from utils.LoginPage import login
from utils.excel_reporter import add_result, generate_excel_report


# =========================
# CLI OPTION
# =========================
def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="chrome, edge o firefox"
    )


# =========================
# CONFIG REPORTS
# =========================
def pytest_configure(config):

    os.makedirs("reports", exist_ok=True)
    os.makedirs("screenshots", exist_ok=True)

    fecha = datetime.now().strftime("%Y%m%d_%H%M%S")

    config.option.htmlpath = f"reports/report_{fecha}.html"
    config.option.self_contained_html = True


# =========================
# DRIVER FIXTURE
# =========================
@pytest.fixture
def driver(request):

    browser = request.config.getoption("--browser")

    if browser == "chrome":
        options = webdriver.ChromeOptions()
        options.add_argument("--incognito")
        options.add_argument("--start-maximized")

        driver = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install()),
            options=options
        )

    elif browser == "edge":
        options = webdriver.EdgeOptions()
        options.add_argument("--start-maximized")

        driver = webdriver.Edge(
            service=EdgeService(EdgeChromiumDriverManager().install()),
            options=options
        )

    elif browser == "firefox":
        options = webdriver.FirefoxOptions()
        options.add_argument("--width=1920")
        options.add_argument("--height=1080")

        driver = webdriver.Firefox(
            service=FirefoxService(GeckoDriverManager().install()),
            options=options
        )

    else:
        raise ValueError("Browser no soportado")

    driver.implicitly_wait(5)

    yield driver
    driver.quit()


# =========================
# LOGIN FIXTURE
# =========================
@pytest.fixture
def login_in_driver(driver):
    login(driver)
    return driver


# =========================
# HOOK: RESULT + SCREENSHOT + EXCEL
# =========================
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):

    outcome = yield
    rep = outcome.get_result()

    if rep.when != "call":
        return

    tc_marker = item.get_closest_marker("tc")
    tc_id = tc_marker.args[0] if tc_marker else item.nodeid

    driver = item.funcargs.get("driver")

    if rep.failed:

        add_result(tc_id, False, error=str(rep.longrepr))

        if driver:
            screenshot = f"screenshots/{item.name}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
            driver.save_screenshot(screenshot)

    else:
        add_result(tc_id, True)


# =========================
# FINAL REPORT
# =========================
def pytest_sessionfinish(session, exitstatus):
    generate_excel_report()