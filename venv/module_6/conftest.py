import pytest
from datetime import datetime
from py.xml import html
from module_4.business import *

@pytest.fixture(autouse=True)
def get_test_name(request):
    print(request.node.name)

@pytest.fixture(scope='session')
def fruits_company():
     return Company('Fruits', address='Ocean street, 1')

@pytest.fixture(scope='session')
def doors_company():
     return Company('Windows and doors', address='Mountain ave. 10')

@pytest.fixture(scope='session')
def alex():
    return Engineer('Alex', 55)

@pytest.fixture(scope='session')
def bill():
    return Engineer('Bill', 20)

@pytest.fixture(scope='session')
def jane():
    return Manager('Jane', 30)

@pytest.fixture(scope='session')
def hired_jane(jane, fruits_company):
    jane.join_company(fruits_company)
    return jane

@pytest.fixture(scope='session')
def hired_alex(alex, fruits_company):
    alex.join_company(fruits_company)
    return alex

@pytest.fixture(scope='session')
def hired_bill(bill, doors_company):
    bill.join_company(doors_company)
    return bill

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    setattr(report, "duration_formatter", "%H:%M:%S.%f")

def pytest_html_results_table_row(report, cells):
    if report.skipped:
        del cells[:]


@pytest.hookspec(firstresult=True)
def pytest_sessionfinish(session, exitstatus):

    print("\n+++++++++++++++++++++++++++++++++++++++++++++")
    print('\n-----Pytest Session Ended')
    print("\n+++++++++++++++++++++++++++++++++++++++++++++")

def pytest_report_teststatus(report, config):
    if report.when == "call":
        print("duration reported immediately after test execution:",
              report.duration)

def pytest_terminal_summary(terminalreporter, exitstatus, config):
    for reps in terminalreporter.stats.values():
        for rep in reps:
            if rep.when == "call":
                print("duration reported after all tests passed:", rep.nodeid,
                      rep.duration)

