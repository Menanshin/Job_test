from selene import browser, have, be


class SQLResultPage:
    def validate_table_visible(self):
        browser.element('.w3-table-all').should(be.visible)

    def find_row_by_text(self, text: str):
        return browser.element(f'//table[contains(@class, "w3-table-all")]/tbody/tr[td[contains(text(), "{text}")]]')

    def validate_column_text(self, row, column_index: int, expected_text: str):
        row.element(f'./td[{column_index}]').should(have.text(expected_text))

    def find_all_rows_by_text(self, text: str):
        return browser.all(f'//table[contains(@class, "w3-table-all")]/tbody/tr[td[contains(text(), "{text}")]]')

    def validate_row_count(self, rows, expected_count: int):
        rows.should(have.size(expected_count))
