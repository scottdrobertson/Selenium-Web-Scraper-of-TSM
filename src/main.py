from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import datetime

options = Options()
options.headless = False
options.add_argument("--window-size=1920,1200")
options.add_argument("user-data-dir=C:/Users/User/AppData/Local/Google/Chrome/User Data/Profile 1")
DRIVER_PATH = 'F:/Programming/BMAH/src/chromedriver_win32/chromedriver.exe'

driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)
# driver.get("https://www.tradeskillmaster.com/black-market?realm=EU-khadgar")
# print(driver.page_source)

def main():
    print("Running!")
    return_date()
    url = "https://www.tradeskillmaster.com/black-market?realm="
    realms = get_realms()
    params = create_realm_url_param(realms)
    for param in params:
        get_items(param, url)
    driver.quit()
    return_date()

    # get_items(params, url)

def return_date():
    date = str(datetime.datetime.now().time())
    date = date[:-7]
    print(date)

def get_realms():
    driver.get("https://www.tradeskillmaster.com/black-market?realm=EU-khadgar")
    realms = driver.find_elements_by_tag_name('option')
    # print(len(realms))

    return realms

def create_realm_url_param(realms):
    # remove first and last WebElement list item
    realms.pop(0)
    realms = realms[:-1]

    # Empty list for params
    paramList = []

    for realm in realms:
        # Changing 'realm' from WebElement to plain text
        realm = realm.get_attribute('innerHTML')

        # Checking if realm is EU or US and then appending the region to the empty param variable
        param = ""
        if "(EU)" in realm:
            param = "EU-"
        if "(US)" in realm:
            param = "US-"

        # Concat anything before '(' to param string
        param = param + realm[:realm.index("(")]

        # Remove any ' characters
        param = param.replace("'", "")

        # Replace any spaces with dashes
        param = param.replace(" ", "-")

        # Removing the last dash from the param
        param = param[:-1]

        # Append param to param List
        paramList.append(param)

    return paramList


def get_items(param, url):
    url = url+param
    driver.get(url)

    items = []
    stupidVar = 0

    if "No results found." in driver.page_source:
        stupidVar + 1
    else:
        # time.sleep(3)
        total = len(driver.find_elements_by_xpath("//table/tbody/tr"))


        i = 1
        while i <= total:
            string = "//table/tbody/tr[" + str(i) + "]"


            y = 1
            while y <= 2:
                if y == 1:
                    name = str(driver.find_element_by_xpath(string+"/td[" + str(y) + "]").get_attribute('innerText'))
                    # test = str(driver.find)
                    # print()


                if y ==2:
                    gold = str(driver.find_element_by_xpath(string + "/td[" + str(y) + "]").get_attribute('innerText'))
                    item = name + " is available on " + str(param) + " and the current bid is " + gold


                    if "[Swift Zulian Tiger]" in item:
                        print(item)

                    if "[Reins of the Mighty Caravan Brutosaur]" in item:
                        print(item)

                    if "[Swift Razzashi Raptor]" in item:
                        print(item)

                    if "[Reins of the Plagued Proto-Drake]" in item:
                        print(item)

                    if "[Core Hound Chain]" in item:
                        print(item)

                    if "19902" in item:
                        name = "[Swift Zulian Tiger]"
                        item = name + " is available on " + str(param) + " and the current bid is " + gold
                        print(item)

                    if "163042" in item:
                        name = "[Reins of the Mighty Caravan Brutosaur]"
                        item = name + " is available on " + str(param) + " and the current bid is " + gold
                        print(item)

                    if "44175" in item:
                        name = "[Reins of the Plagued Proto-Drake]"
                        item = name + " is available on " + str(param) + " and the current bid is " + gold
                        print(item)

                    if "115484" in item:
                        name = "[Core Hound Chain]"
                        item = name + " is available on " + str(param) + " and the current bid is " + gold
                        print(item)


                y += 1
            i += 1




        # i = 1
        # while i <= total:
        #     string = "//table/tbody/tr[" + str(i) + "]"
        #     y = 1
        #     while y <= 2:
        #         string + "/td[" + str(y) + "]/a"
        #         row = driver.find_element_by_xpath(string).get_attribute('innerHTML')
        #         print(row)
        #         y +=2
        #         # row = driver.find_element_by_xpath(string).get_attribute('innerHTML')
        #
        #     i += 1





main()

