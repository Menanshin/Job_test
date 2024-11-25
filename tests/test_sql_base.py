import pytest

from pages.sql_page import SQLPage
from pages.sql_result_page import SQLResultPage


@pytest.fixture
def sql_page():
    return SQLPage()


@pytest.fixture
def sql_result_page():
    return SQLResultPage()


def test_contact_name(sql_page, sql_result_page):
    sql_page.open()
    sql_page.validate_default_query()
    sql_page.execute_default_query()

    sql_page.switch_to_result_frame()
    sql_result_page.validate_table_visible()

    row = sql_result_page.find_row_by_text("Giovanni Rovelli")
    sql_result_page.validate_column_text(row, 4, "Via Ludovico il Moro 22")

    sql_page.switch_to_default_content()


def test_customers_in_london_with_js(sql_page, sql_result_page):
    sql_page.open()
    sql_page.validate_default_query()

    sql_page.set_query("SELECT * FROM Customers WHERE city='London';")

    sql_page.switch_to_result_frame()
    sql_result_page.validate_table_visible()

    london_rows = sql_result_page.find_all_rows_by_text("London")
    sql_result_page.validate_row_count(london_rows, 6)

    sql_page.switch_to_default_content()


def test_update_customer_record(sql_page, sql_result_page):
    sql_page.open()
    sql_page.validate_default_query()

    sql_page.set_query("""
        UPDATE Customers
        SET ContactName='John Doe', City='New York', Address='1234 Broadway'
        WHERE CustomerID = 1;
    """)

    sql_page.switch_to_result_frame()
    sql_result_page.validate_table_visible()

    row = sql_result_page.find_row_by_text("John Doe")
    sql_result_page.validate_column_text(row, 2, "John Doe")
    sql_result_page.validate_column_text(row, 3, "New York")
    sql_result_page.validate_column_text(row, 4, "1234 Broadway")

    sql_page.switch_to_default_content()


def test_delete_customer_record(sql_page, sql_result_page):
    sql_page.open()
    sql_page.validate_default_query()

    sql_page.set_query("""
        DELETE FROM Customers
        WHERE ContactName='John Doe' AND City='New York' AND Address='1234 Broadway';
    """)

    sql_page.switch_to_result_frame()
    sql_result_page.validate_table_visible()

    deleted_rows = sql_result_page.find_all_rows_by_text("John Doe")
    sql_result_page.validate_row_count(deleted_rows, 0)

    sql_page.switch_to_default_content()
