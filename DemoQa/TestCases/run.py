import time
import xlrd
import logging
import os
from DemoQa.TestCases.excel_based_framework import run_test_case_from_excel
from DemoQa.library.config import driver, excel_file_path
from selenium.webdriver.common.by import By
from DemoQa.library.action_lib import capture_screenshot, highlight
from DemoQa.library import log

# logger = log.get_logger("Functionality")

try:

    wb = xlrd.open_workbook(excel_file_path)
    sheet1 = wb.sheet_by_name("ExecutionYN")
    row_count = sheet1.nrows
    column_count = sheet1.ncols

    for i in range(1, row_count):
        sheet_name = sheet1.cell_value(i, 0)
        ExecutionYN = sheet1.cell_value(i, 1)
        print("sheet_name :" + sheet_name)
        print("ExecutionYN : " + ExecutionYN)
        ExecutionYN = ExecutionYN.upper()

        if ExecutionYN == "YES":
            run_test_case_from_excel(sheet_name)
            print("Execution Started of test case :==========>>>>> " + sheet_name)

except Exception as e:
    print(e)
    print("Error while reading excel file " )

driver.close()
