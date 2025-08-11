from typing import Any, Dict

from appium import webdriver
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# Task 1: Launch the ABC Company mobile app
# Set Desired Capabilities
cap: Dict[str, Any] = {
    "platformName": "Android",
    "appium:platformVersion": "11",
    "appium:deviceName": "fb82c273",
    "appium:automationName": "UiAutomator2",
    "appium:autoLaunch": True,
    "appium:appWaitActivity": "*.*",
    "appium:noReset": "true",
    "appium:ignoreHiddenApiPolicyError": "true",
    "appPackage": "com.arcone.arcone",
    "appActivity": ".MainActivity"

}

# Start Appium Session
url = 'http://127.0.0.1:4723'
driver = webdriver.Remote(url, options=AppiumOptions().load_capabilities(cap))
wait = WebDriverWait(driver, 50)


# Task 2: Navigate to HR → Check-IN

def navigate_to_check_in():
    hr_xpath = '//android.view.ViewGroup[@content-desc="HR"]'
    hr_element = wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, hr_xpath)))
    hr_element.click()

    checkin_xpath = '//android.view.ViewGroup[@content-desc="Check-IN"]'
    checkin_element = wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, checkin_xpath)))
    checkin_element.click()


# Task 3: Complete the check-in process
def take_camera_picture():
    shutter_xpath = '//android.widget.ImageView[@resource-id="com.oppo.camera:id/shutter_button"]'
    wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, shutter_xpath))).click()

    confirm_xpath = '//android.widget.ImageView[@resource-id="com.oppo.camera:id/done_button"]'
    wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, confirm_xpath))).click()


def fill_form_select_log_type():

    log_type_in_xpath = '//android.view.ViewGroup[@content-desc="IN, Log Type"]/android.view.ViewGroup[1]'
    wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, log_type_in_xpath))).click()

    in_xpath = '//android.view.ViewGroup[@content-desc="IN"]'
    wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, in_xpath))).click()
    checkin_btn_xpath = '//android.view.ViewGroup[@content-desc="Check-IN"]'
    wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, checkin_btn_xpath))).click()

    ok_btn_xpath = '//android.view.ViewGroup[@content-desc="OK"]'
    wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, ok_btn_xpath))).click()

    # Task 4: Navigate to HR -> Leave Application
    leave_application_xpath = '//android.view.ViewGroup[@content-desc="Leave Application"]'
    leave_application_element = wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, leave_application_xpath)))
    leave_application_element.click()


# Task5: Create a new leave application by filling all required fields
def create_leave_application():
    xpath_icon_menu = '//android.view.ViewGroup[@content-desc=""]'
    xpath_add_application = '//android.view.ViewGroup[@content-desc="+, Application"]'
    xpath_leave_type_dropdown = '//android.view.ViewGroup[@content-desc=", Leave Type*"]/android.view.ViewGroup'
    xpath_leave_type = '//android.view.ViewGroup[@content-desc="Leave Without Pay"]'

    xpath_from_date_picker = '//android.view.ViewGroup[@content-desc=", From Date*"]'
    xpath_year_header = '//android.widget.TextView[@resource-id="android:id/date_picker_header_year"]'
    xpath_select_year = '//android.widget.TextView[@resource-id="android:id/text1" and @text="2029"]'
    xpath_next_month = '//android.widget.ImageButton[@content-desc="Next month"]'
    xpath_from_day = '//android.view.View[@content-desc="21 September 2029"]'
    xpath_ok_button = '//android.widget.Button[@resource-id="android:id/button1"]'

    xpath_to_date_picker = '//android.view.ViewGroup[@content-desc=", To Date*"]'
    xpath_to_day = '//android.view.View[@content-desc="23 September 2029"]'

    xpath_apply_button = '//android.view.ViewGroup[@content-desc="Apply"]'
    xpath_ok_confirm = '//android.view.ViewGroup[@content-desc="OK"]'

    wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, xpath_icon_menu))).click()
    wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, xpath_add_application))).click()
    wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, xpath_leave_type_dropdown))).click()
    wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, xpath_leave_type))).click()

    wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, xpath_from_date_picker))).click()
    wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, xpath_year_header))).click()
    wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, xpath_select_year))).click()
    wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, xpath_next_month))).click()

    wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, xpath_from_day))).click()
    wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, xpath_ok_button))).click()

    wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, xpath_to_date_picker))).click()
    wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, xpath_to_day))).click()
    wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, xpath_ok_button))).click()

    wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, xpath_apply_button))).click()
    wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, xpath_ok_confirm))).click()
    wait.until(EC.invisibility_of_element_located((AppiumBy.XPATH, xpath_ok_confirm)))


# Task 6: Take a screenshot of the results
def take_screenshot(file_path):
    success = driver.save_screenshot(file_path)
    print(
        "Screenshot saved successfully")


# Task 7: Close the app
def close_app_via_back():
    # Press back button 3 times
    for _ in range(3):
        driver.back()

    # Wait for the "OK" button dialog to appear
    ok_button_xpath = '//android.view.ViewGroup[@content-desc="OK"]'
    ok_button = wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, ok_button_xpath)))

    # Click on the "OK" button to close the dialog
    ok_button.click()
    print("App closed by pressing back 3 times and confirming with OK.")


navigate_to_check_in()
take_camera_picture()
fill_form_select_log_type()
create_leave_application()
take_screenshot('leave_application05.png')
close_app_via_back()
