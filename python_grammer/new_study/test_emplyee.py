from python_grammer.new_study.employee import Employee
import pytest

@pytest.fixture
def employee():
    employee = Employee("sam","dai",500000)
    return employee

def test_give_default_raise(employee):
    employee.give_raise()
    assert employee.annual_package == 505000

def test_give_default_raise(employee):
    employee.give_raise(60000)
    assert employee.annual_package == 560000