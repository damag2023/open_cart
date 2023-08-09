import os

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.edge.options import Options

driver = None

@pytest.fixture(scope="class")
def openBrowser(request):
    global driver
    if request.config.getoption('--browser').title() =="Firefox":
        service_obj = Service("C:\\Users\\dines\\geckodriver\\geckodriver.exe")
        options = Options()
        options.log.level = "TRACE"
        driver = webdriver.Firefox(service=service_obj, options=options)
    elif request.config.getoption('--browser').title()=="Edge":
        service_obj = Service("C:\\Users\\dines\\edgedriver\\msedgedriver.exe")
        edge_options = Options()
        edge_options.add_experimental_option('excludeSwitches', ['enable-logging'])
        driver = webdriver.Edge(service=service_obj, options=edge_options)
    else:
        service_obj =Service("C:\\Users\\dines\\chromedriver\\chromedriver.exe")
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        driver = webdriver.Chrome(service=service_obj, options=options)
    driver.maximize_window()
    driver.implicitly_wait(5)
    request.cls.driver = driver
    yield
    driver.close()

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="Chrome")


# def pytest_html_report_title(report):
#     report.title = "OpenCart_TestCase Execution_report"
#
#
# @pytest.hookimpl(hookwrapper=True)
# def pytest_runtest_makereport(item, call):
#     pytest_html = item.config.pluginmanager.getplugin("html")
#     outcome = yield
#     report = outcome.get_result()
#     extra = getattr(report, "extra", [])
#     if report.when == "call":
#         # always add url to report
#         extra.append(pytest_html.extras.url(driver.current_url))
#         xfail = hasattr(report, "wasxfail")
#         if (report.skipped and xfail) or (report.failed and not xfail):
#             # only add additional html on failure
#             report_directory = os.path.dirname(item.config.option.htmlpath)
#             # file_name = str(int(round(time.sleep() *1000)))+".png"
#             file_name = report.nodeid.replace("::", "_") +".png"
#             destinationFile = os.path.join(report_directory, file_name)
#             _capture_screenshot(destinationFile)
#             if file_name:
#                 html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
#                        'onclick="window.open(this.src)" align="right"/></div>' % file_name
#                 extra.append(pytest_html.extras.html(html))
#         report.extra = extra
#
# def _capture_screenshot(name):
#     driver.get_screenshot_as_file(name)