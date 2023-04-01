import logging
from datetime import datetime, time
import time
from selenium.webdriver.common.by import By
from DemoQa.library.config import driver
from DemoQa.library.config import screenshot_path

logger = logging.getLogger("Functionality")


def by_locator(str, locator):
    if str == 'XPATH':
        return driver.find_element(By.XPATH, locator)
    if str == 'ID':
        return driver.find_element(By.ID, locator)
    if str == 'NAME':
        return driver.find_element(By.NAME, locator)
    if str == 'LINK_TEXT':
        return driver.find_element(By.LINK_TEXT, locator)
    if str == 'PARTIAL_LINK_TEXT':
        return driver.find_element(By.PARTIAL_LINK_TEXT, locator)
    if str == 'CLASS_NAME':
        return driver.find_element(By.CLASS_NAME, locator)
    if str == 'CSS_SELECTOR':
        return driver.find_element(By.CSS_SELECTOR, locator)
    if str == 'TAG_NAME':
        return driver.find_element(By.TAG_NAME, locator)


def web_click(locator):
    try:
        locator.enabled()
        locator.click()
    except Exception:
        print("unable to click")
        capture_screenshot()
        logger.error("Not able to click")


def enter_text(locator, text_to_enter):
    try:
        locator.enabled()
        locator.click()
        locator.send_keys(text_to_enter)
    except Exception:
        print("unable to enter text")
        logger.error("Not able to click")


def capture_screenshot():
    current_datetime = datetime.utcnow().strftime('%Y_%m_%d_%H_%M_%S_%f')
    driver.save_screenshot(screenshot_path + "img" + current_datetime + ".png")
    return capture_screenshot


def highlight(element):
    """Highlights (blinks) a Selenium Webdriver element"""
    # driver = element._parent
    for i in range(1, 6):
        def apply_style(s):
            driver.execute_script("arguments[0].setAttribute('style', arguments[1]);", element, s)

        original_style = element.get_attribute('style')
        apply_style("background: yellow; border: 2px solid red;")
        time.sleep(.3)
        apply_style(original_style)


# def get_excel_row_column_count(sheet_name):
#     try:
#         # wb = xlrd.open_workbook("DemoQa/TestCases/TestSheet.xlsx")  // path not working right now
#         wb = xlrd.open_workbook("C:/Users/ravikumar/PycharmProjects/pythonProject/DemoQa/TestCases/TestSheet.xlsx")
#         sheet1 = wb.sheet_by_name(sheet_name)
#         row_count = sheet1.nrows
#         column_count = sheet1.ncols
#         print("row_count : " + row_count)
#         print("column_Count : " + column_count)
#         return row_count, column_count
#
#     except Exception:
#         print("Error while reading excel file ")
