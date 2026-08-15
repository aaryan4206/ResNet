from flask import Blueprint
from api.classes.dealers import DealerAPI
from api.classes.employees import EmployeeAPI
from api.classes.sales import SalesAPI
from api.classes.menu import MenuAPI
from api.classes.bills import BillingAPI


def create_employees_blueprints(db):
    employees_bp = Blueprint('employees', __name__, url_prefix='/api/employees')

    employee_view = EmployeeAPI.as_view('employee_api', db=db)

    employees_bp.add_url_rule('/', view_func=employee_view, methods=['GET', 'POST'])

    employees_bp.add_url_rule('/<employee_id>', view_func=employee_view, methods=['GET', 'PUT', 'DELETE'])

    return employees_bp


def create_dealers_blueprints(db):
    dealers_bp = Blueprint('dealers', __name__, url_prefix='/api/dealers')

    dealer_view = DealerAPI.as_view('dealer_api', db=db)

    dealers_bp.add_url_rule('/', view_func=dealer_view, methods=['GET', 'POST'])

    dealers_bp.add_url_rule('/<dealer_id>', view_func=dealer_view, methods=['GET', 'PUT', 'DELETE'])

    return dealers_bp


def create_sales_blueprints(db):
    sales_bp = Blueprint('sales', __name__, url_prefix='/api/sales')

    sale_view = SalesAPI.as_view('sales_api', db=db)

    sales_bp.add_url_rule('/', view_func=sale_view, methods=['GET', 'POST'])

    sales_bp.add_url_rule('/<sale_id>', view_func=sale_view, methods=['GET', 'PUT', 'DELETE'])

    return sales_bp


def create_menu_blueprints(db):
    menu_bp = Blueprint('menu', __name__, url_prefix='/api/menu')

    menu_view = MenuAPI.as_view('menu_api', db=db)

    menu_bp.add_url_rule('/', view_func=menu_view, methods=['GET', 'POST'])

    menu_bp.add_url_rule('/<menu_id>', view_func=menu_view, methods=['GET', 'PUT', 'DELETE'])

    return menu_bp


def create_bills_blueprints(db):
    bills_bp = Blueprint('bills', __name__, url_prefix='/api/bills')

    bill_view = BillingAPI.as_view('bill_api', db=db)

    bills_bp.add_url_rule('/', view_func=bill_view, methods=['GET', 'POST'])

    bills_bp.add_url_rule('/<bill_id>', view_func=bill_view, methods=['GET', 'PUT', 'DELETE'])

    return bills_bp