from selenium.webdriver.support.ui import Select
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import expected_conditions as expected
from selenium.webdriver.support.wait import WebDriverWait
from bs4 import BeautifulSoup
from datetime import date, datetime


ERROR_MSG = f"Something went wrong, please make sure that your date is formatted *D/M/Y* (day-month-year), for example today's date would be *{datetime.today().strftime('%d/%m/%y')}*"

DIBS_URL = "https://queensu.evanced.info/dibs/Login"


def check(command, username, password):

    given_date = parse_command(command)
    days = None
    try:
        if(given_date):
            days = (datetime.strptime(given_date, "%d/%m/%y") -
                    datetime.strptime(datetime.today().strftime("%d/%m/%y"), "%d/%m/%y")).days
            if days < 0 or days > 7:
                return "Please choose a date within the next 7 days"
    except:
        return ERROR_MSG

    # Load the D!Bs Home page
    options = Options()
    options.add_argument('-headless')

    browser = Firefox(executable_path='geckodriver', options=options)
    browser.get(DIBS_URL)

    # Log in
    browser.find_element_by_id("txtUsername").send_keys(username)
    browser.find_element_by_id("pwdPassword").send_keys(password)
    browser.find_element_by_id("btnLoginSubmit").click()

    # Select the time
    time_select = Select(browser.find_element_by_id("SelectedTimeSort"))
    time_select.select_by_index(1)

    if(given_date):
        date_select = Select(browser.find_element_by_id("SelectedSearchDate"))
        date_select.select_by_index(days)

    browser.find_element_by_class_name("btn-large").click()
    html = browser.page_source
    browser.quit()

    soup = BeautifulSoup(html, "html.parser")
    return f'This is what I found for {(given_date or "today")} :calendar:\n' + create_response(soup)


def create_response(soup):
    room_tags = soup.find_all(name="div", attrs={'class': 'title'})
    room_times = []
    room_spaces = []
    for tag in room_tags:
        room_times.append(tag.contents[0].replace("\n", "").strip())
        room_spaces.append(tag.contents[1].contents[1].contents[0])

    response = ""
    for i, time in enumerate(room_times):
        response += f'*{time}*\t-\tSpaces: {room_spaces[i]}\n'
    return response


def parse_command(command):
    splitted = command.split(" ")
    if len(splitted) is not 2:
        return None
    return splitted[1]
