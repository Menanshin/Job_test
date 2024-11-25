from selene import browser, have, be


class SQLPage:
    def open(self):
        browser.open('/sql/trysql.asp?filename=trysql_select_all')

    def validate_default_query(self):
        browser.element('.CodeMirror-code').should(be.visible).should(have.text("SELECT * FROM Customers;"))

    def set_query(self, query: str):
        escaped_query = browser.driver.execute_script('return JSON.stringify(arguments[0]);', query)
        browser.execute_script(f"""
            document.getElementById("textareaCodeSQL").value = {escaped_query};
            window.editor.getDoc().setValue({escaped_query});
            w3schoolsNoWebSQLSubmit();
        """)

    def execute_default_query(self):
        browser.element('.ws-btn').click()

    def switch_to_result_frame(self):
        iframe = browser.element('iframe#iframeResultSQL').locate()
        browser.driver.switch_to.frame(iframe)

    def switch_to_default_content(self):
        browser.driver.switch_to.default_content()
