import time
# from this import s

from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from DemoQa.TestCases.getText import get_text_after_test

from DemoQa.library.action_lib import highlight, capture_screenshot, logger
from DemoQa.library.config import driver, excel_file_path


# from DemoQa.library import log


def run_test_case_from_excel(sheet_name):
    import time
    import xlrd as xlrd
    from DemoQa.library.config import driver
    from selenium.webdriver.common.by import By
    from DemoQa.library.action_lib import capture_screenshot, highlight
    # from DemoQa.library import log

    # logger = log.get_logger("Functionality")

    try:
        wb = xlrd.open_workbook(excel_file_path)
        sheet1 = wb.sheet_by_name(sheet_name)
        row_count = sheet1.nrows
        column_count = sheet1.ncols

    except Exception as e:
        print(e)
        print("Error while reading excel file : excel based framework")

    for j in range(3, column_count):
        for i in range(1, row_count):
            action = sheet1.cell_value(i, 0)
            locator = sheet1.cell_value(i, 1)
            element_type = sheet1.cell_value(i, 2)
            element_type = element_type.upper()
            value = sheet1.cell_value(i, j)

            # print("action  :" + action)
            # print("locator :" + locator)
            # print("element_type :" + element_type)
            # print("value   : " + value)

            if element_type == "OPEN_URL":
                print("Start function OPEN URL")
                driver.get(value)
                logger.info('logger msg : ' + action)
                print("END function OPEN URL")

            elif element_type == "TEXT":
                input_text(locator, value)

            elif element_type == "LINK":
                click_link(value)

            elif element_type == "VALIDATE_TEXT":
                validate_text(locator, value)

            elif element_type == "PARTIAL_LINK":
                click_partial_link(locator, value)

            elif element_type == "BUTTON":
                click_button(locator)

            elif element_type == "VALIDATE_URL":
                validate_url(value)

            elif element_type == "GET_TEXT_AFTER_TEXT":
                get_text_after_test(sheet_name, locator, value)    # custom function called from another file

            elif element_type == "WAIT":
                time.sleep(value)

            elif element_type == "ALERT":
                try:
                    time.sleep(5)
                    alert = driver.switch_to.alert
                    time.sleep(5)
                    alert.text()
                    if alert.text() == "Book added to your collection.":
                        capture_screenshot()
                        print("if...1 alert Displayed")
                        # logger.info('logger msg : ' + action)
                        alert.accept()
                        print(locator + " : Alert  clicked ")
                        # logger.info('logger msg : ' + action)
                    elif alert.text() == "Book already present in the your collection!":
                        capture_screenshot()
                        print("elif....2 alert Displayed")
                        # logger.info('logger msg : ' + action)
                        alert.accept()
                        print(locator + " : Alert  clicked ")
                        # logger.info('logger msg : ' + action)
                    else:
                        capture_screenshot()
                        print("else......3  alert Displayed")
                        # logger.info('logger msg : ' + action)
                        alert.accept()
                        print(locator + " : Alert  clicked ")
                        # logger.info('logger msg : ' + action)

                except Exception:
                    print("Alert not handled  unknown issue")
                    # logger.info('logger msg : ' + action + " : Alert not handled  unknown issue")

            elif element_type == "SELECT":
                select_from_dropbox(locator, value)

            elif element_type == "":
                print("End of Test case")

            else:
                print(element_type + " : element type given in excel sheet is not matching")

        print(" End of for i loop  :  ******************************************")
    print(" End of function : run_test_case_from_excel=====================================================================")


def select_from_dropbox(locator, value):
    print("function STARTED : validate_url ")
    time.sleep(1)
    try:
        dropdown_element = driver.find_element(By.XPATH, locator)
        highlight(dropdown_element)
        dropdown_element = Select(dropdown_element)
        # highlight(dropdown_element)
        capture_screenshot()
        # select by visible text
        dropdown_element.select_by_visible_text(value)
        # highlight(dropdown_element)
        # highlight(dropdown_element)
        capture_screenshot()
        print(value + " : selected from dropdown")
        time.sleep(1)

    except Exception as e:
        print(e)
        print("exception is selecting item from dropdown box")

    print("function STARTED : wait ")

def wait(value):
    print("function STARTED : wait ")
    time.sleep(5)
    print("function STARTED : wait ")


def validate_url(value):
    print("function STARTED : validate_url ")

    try:
        time.sleep(1)
        current_url = driver.current_url
        expected_url = value
        print("current_url  : " + current_url)
        print("expected_url : " + expected_url)
        if current_url == expected_url:
            print("current url matches expected url ")
        else:
            print("current url is not matching expected url ")

        time.sleep(1)

    except Exception as e:
        print(e)

    print("function ENDS : validate_url ")


def validate_text(locator, value):
    print("function STARTED : validate_text ")
    time.sleep(1)
    try:
        actual_label_element = driver.find_element(By.XPATH, locator)
        actual_label = driver.find_element(By.XPATH, locator).text
        actual_label = actual_label.strip()
        expected_label = value
        expected_label
        print("actual_label   : " + actual_label)
        print("expected_label : " + expected_label)

        if actual_label_element.is_displayed():
            highlight(actual_label_element)
            capture_screenshot()
            # logger.info('logger msg:' + action)
            if actual_label == expected_label:
                print(value + " : text matches ")
                # logger.info('logger msg:' + action + " : label matches")
            else:
                print(value + " : actual text is not matching expected text")
                # logger.info('logger msg:' + action + " : actual label is not matching expected label ")

    except Exception as e:
        print(e)
        print("exception occurred while  matching text  ")
        # logger.info('logger msg:' + action + " :  actual label not found")

    time.sleep(1)
    print("function ENDS : validate_text ")


def click_partial_link(locator, value):
    print("function STARTED : click_partial_link ")
    time.sleep(1)
    partial_link = driver.find_element(By.PARTIAL_LINK_TEXT, value)
    try:
        # Scroll down to partial link
        driver.execute_script("arguments[0].scrollIntoView();", partial_link)
        time.sleep(1)

        # Submit the form
        highlight(partial_link)
        capture_screenshot()
        driver.execute_script("arguments[0].click();", partial_link)
        print("partial link clicked")
        # logger.info('logger msg:' + action)
        time.sleep(1)

    except Exception:
        print(locator + ": partial link was not clicked")
        # logger.info('logger msg : ' + action + " : partial link was not clicked")

    time.sleep(1)
    print("function ENDS : click_partial_link ")


def click_button(locator):
    print("function STARTED : click_button ")
    time.sleep(1)
    try:
        time.sleep(1)
        button = driver.find_element(By.XPATH, locator)
        # Scroll down to login button
        driver.execute_script("arguments[0].scrollIntoView();", button)
        highlight(button)
        capture_screenshot()
        # logger.info('logger msg : ' + action)
        if button.is_displayed():
            # Submit the form
            # capture_screenshot()
            driver.execute_script("arguments[0].click();", button)
            print(locator + " : button clicked")
            # logger.info('logger msg : ' + action)
            # capture_screenshot()
            time.sleep(3)
        else:
            print(locator + " : button not displayed")
            # logger.info('logger msg : ' + action + " : button not displayed")

    except Exception:
        print(locator + " : button is not clicked ")
        # logger.info('logger msg : ' + action + " : button not displayed")

    time.sleep(1)
    print("function ENDS : click_button ")


def click_link(value):
    print("function STARTED : click_link ")
    time.sleep(1)
    try:

        link_element = driver.find_element(By.LINK_TEXT, value)
        highlight(link_element)
        capture_screenshot()
        link_element.click()
        # logger.info('logger msg : ' + action)
        print(value + " : Link clicked ")

    except Exception as e:
        print(e)

    time.sleep(1)
    print("function ENDS : click_link ")


def input_text(locator, value):
    print("function STARTED : input_text ")
    time.sleep(1)
    try:
        text_box = driver.find_element(By.XPATH, locator)
        text_box.send_keys(value)
        highlight(text_box)
        capture_screenshot()
        print(locator + " : entered into textbox")
        # logger.info('logger msg : ' + action)

    except Exception as e:
        print(e)

    time.sleep(1)
    print("function ENDS : input_text ")
