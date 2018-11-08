import requests
from bs4 import BeautifulSoup

STACK_URL = "https://stackoverflow.com"


def help_me(question):
    try:
        formatted_question = question.replace("help", "").strip()
        raw_html = requests.get(
            f"{STACK_URL}/search?q={formatted_question}").content
        soup = BeautifulSoup(raw_html, "html.parser")
        first_result = BeautifulSoup.find(
            soup, name="div", attrs={'class': 'question-summary search-result'})
        link = first_result.find("a", href=True)
        return f"I found this link which should be of help, check it out :nerd_face:!\n{STACK_URL}{link['href']}"
    except:
        return "Looks like I was unable to help with that one. I am sorry :sad_cowboy:"
