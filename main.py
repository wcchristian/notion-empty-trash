from selenium import webdriver
import selenium.webdriver.support.ui as ui
import time
import sys
import config
from selenium.common.exceptions import ElementClickInterceptedException, StaleElementReferenceException, TimeoutException

browser = webdriver.Chrome(config.chrome_driver_location)
browser.get(config.landing_page)
browser.add_cookie({"name":"token_v2","domain":"notion.so","value":config.token_v2})
browser.add_cookie({"name":"notion_user_id","domain":"notion.so","value":config.notion_user_id})
browser.add_cookie({"name":"notion_users","domain":"notion.so","value":config.notion_users})

# Nav to landing page after adding login cookies
browser.get(config.landing_page)
wait = ui.WebDriverWait(browser, 20)

# Click the trash in the sidebar
trash_can = wait.until(lambda browser: browser.find_element_by_class_name("sidebarTrash"))
trash_can.click()

# Get all of the items for perma delete
try:
    trashable_items = wait.until(lambda browser: browser.find_elements_by_class_name("trash"))
except TimeoutException:
    browser.close()
    sys.exit()

i = 0
# as long as there are trashable items left
while trashable_items.__len__():
    # refresh trashable item list
    try:
        trashable_items = wait.until(lambda browser: browser.find_elements_by_class_name("trash"))
    except TimeoutException:
        break
    
    # click trash then confirm for each trashable item.
    for item in trashable_items:
        try:
            item.find_element_by_xpath("..").click()
        except (StaleElementReferenceException, ElementClickInterceptedException):
            continue
        delete_button = wait.until(lambda browser: browser.find_element_by_xpath("//*[text()='Yes. Delete this page']"))
        delete_button.click()
        i += 1
        print('Deleted '+str(i))

# Close the browser
browser.close()