from datetime import datetime
from selenium import webdriver


#####################
# from webdriver_manager.chrome import ChromeDriverManager
# # driver = None
# global driver
# driver = webdriver.Chrome(ChromeDriverManager().install())
#######################



current_datetime = datetime.utcnow().strftime('%Y_%m_%d_%H_%M_%S_%f')
url = "https://demoqa.com/login"
screenshot_path = "../screenshots/"
chromedriver_path = "../driver/chromedriver.exe"
excel_file_path = "D:/pythonFinalAssignment/DemoQa/TestCases/TestSheet.xlsx"
driver = webdriver.Chrome(chromedriver_path)
driver.maximize_window()

RESULT_PATH = screenshot_path
# RESULT_PATH = RESULT_PATH + "HTML_reports_"+ current_datetime
# logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')
# logging.basicConfig(level=logging.DEBUG)

