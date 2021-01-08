from selenium import webdriver
from selenium.webdriver.chrome.options import Options

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
    url = "https://www.tradeskillmaster.com/black-market?realm="
    realms = get_realms()
    params = create_realm_url_param(realms)
    for param in params:
        get_items(param, url)





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
        rows = driver.find_elements_by_tag_name("span")
        for row in rows:
            row = row.get_attribute("innerHTML")
            if len(row) > 0:
                if row[0] == "[":
                    items.append(row)

                if row == "[Swift Zulian Tiger]":
                    print("[Swift Zulian Tiger] HAS BEEN DETECTED at " + param + "!!!")

                if row == "[Reins of the Mighty Caravan Brutosaur]":
                    print("[Reins of the Mighty Caravan Brutosaur] has been detected at " + param)

                if row == "[Swift Razzashi Raptor]":
                    print("[Swift Razzashi Raptor] has been detected at " + param)

                if row == "[Reins of the Plagued Proto-Drake]":
                    print("[Reins of the Plagued Proto-Drake " + param)

                if row == "[Core Hound Chain]":
                    print("[Core Hound Chain] has been detected at " + param)



main()

