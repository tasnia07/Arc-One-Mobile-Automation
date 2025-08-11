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


# Task 2: Navigate to HR → My Attendance

def navigate_to_my_attendance():
    hr_xpath = '//android.view.ViewGroup[@content-desc="HR"]'
    hr_element = wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, hr_xpath)))
    hr_element.click()

    attendance_xpath = '//android.view.ViewGroup[@content-desc="My Attendance"]'
    attendance_element = wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, attendance_xpath)))
    attendance_element.click()


# Task 3: Input From Date and To Date (ensure the gap is no more than 1 month)
def pick_from_date():
    # Click From Date field to open date picker
    from_date_field_xpath = '//android.view.ViewGroup[@content-desc=", From"]'
    wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, from_date_field_xpath))).click()

    # Click Previous Month button
    prev_month_btn_xpath = '//android.widget.ImageButton[@content-desc="Previous month"]'
    wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, prev_month_btn_xpath))).click()
    prev_month_btn_xpath2 = '//android.widget.ImageButton[@content-desc="Previous month"]'
    wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, prev_month_btn_xpath))).click()

    # Select date "1 June 2025"
    from_date_xpath = '//android.view.View[@content-desc="01 June 2025"]'
    wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, from_date_xpath))).click()

    # Click OK button to confirm
    ok_btn_xpath = '//android.widget.Button[@resource-id="android:id/button1"]'
    wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, ok_btn_xpath))).click()


def pick_to_date():
    # Click To Date field to open date picker
    to_date_field_xpath = '//android.view.ViewGroup[@content-desc=", To"]'
    wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, to_date_field_xpath))).click()

    # Click Previous Month button
    prev_month_btn_xpath = '//android.widget.ImageButton[@content-desc="Previous month"]'
    wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, prev_month_btn_xpath))).click()
    prev_month_btn_xpath2 = '//android.widget.ImageButton[@content-desc="Previous month"]'
    wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, prev_month_btn_xpath))).click()

    # Select date " 30 June 2025" (assuming already current month, no navigation)
    to_date_xpath = '//android.view.View[@content-desc="30 June 2025"]'
    wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, to_date_xpath))).click()

    # Click OK button to confirm
    ok_btn_xpath = '//android.widget.Button[@resource-id="android:id/button1"]'
    wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, ok_btn_xpath))).click()


# Task 4: Filter by Status: On Leave
def filter_by_status_on_leave():
    # Click the Status dropdown box to open options
    status_dropdown_xpath = '//android.view.ViewGroup[@content-desc="All, , Status"]/android.view.ViewGroup'
    status_dropdown = wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, status_dropdown_xpath)))
    status_dropdown.click()

    # Select the "On Leave" option from the dropdown
    on_leave_option_xpath = '//android.view.ViewGroup[@content-desc="On Leave"]'
    on_leave_option = wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, on_leave_option_xpath)))
    on_leave_option.click()


# Task 5: Validate that the search results appear
def verify_search_results_present():
    search_results_xpath = '//android.widget.HorizontalScrollView/android.view.ViewGroup/android.view.ViewGroup[1]'
    try:
        wait.until(EC.presence_of_element_located((AppiumBy.XPATH, search_results_xpath)))
        print("Search result element is present.")
        return True
    except NoSuchElementException:
        print("No data found.")
        return False


# Task 6: Take a screenshot of the search results
def take_screenshot(file_path):
    success = driver.save_screenshot(file_path)
    print("Screenshot saved successfully")


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


navigate_to_my_attendance()
pick_from_date()
pick_to_date()
filter_by_status_on_leave()
verify_search_results_present()
take_screenshot('search_results03.png')
close_app_via_back()
