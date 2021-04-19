import pytest
import time

from module_4.business import *

@pytest.mark.smoke
def test_add_employee(alex, jane, fruits_company):
    time.sleep(2)
    new_employees = [alex, jane]
    for employee in new_employees:
        employee.join_company(fruits_company)
        print(f'{employee}')
    assert alex, jane in fruits_company.employees

@pytest.mark.smoke
def test_do_work_engineer(hired_alex):
    engineer_money = 0
    hired_alex.do_work()
    engineer_money = hired_alex.get_money()
    assert engineer_money == 10

@pytest.mark.smoke
def test_do_work_manager(hired_jane):
    manager_money = 0
    hired_jane.do_work()
    manager_money = hired_jane.get_money()
    assert manager_money == 12

def test_already_hired(hired_alex, fruits_company, doors_company):
    hired_alex.join_company(doors_company)
    assert ("Sorry we cannot hire you because you are employeed to "
                  f"{fruits_company}")
@pytest.mark.skip
def test_skip(hired_alex, fruits_company):
    hired_alex.get_money()
    assert manager_money == 10

def test_become_unemployed(hired_alex, fruits_company):
    hired_alex.become_unemployed(fruits_company)
    assert hired_alex.company == None and hired_alex not in fruits_company.employees

@pytest.mark.smoke
def test_go_bankrupt(hired_bill, doors_company):
    doors_company.go_bankrupt()
    assert doors_company.get_money() == 0 and len(
        doors_company.employees) == 0 and hired_bill not in \
           doors_company.employees

@pytest.mark.smoke
def test_make_a_party(hired_jane, fruits_company):
    company_money = fruits_company.get_money()
    employee_money = hired_jane.get_money()
    fruits_company.make_a_party()
    assert fruits_company.get_money() == company_money - (len(
                fruits_company.employees)*5) and hired_jane.get_money() == \
           employee_money + 5
