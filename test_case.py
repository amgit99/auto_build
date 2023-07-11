import sys
import requests
from bs4 import BeautifulSoup


BASE_URL = "https://codeforces.com/contest/"
CONTEST_ID = "1846"
PROBLEM = "A"


def get_current_contest_id():
    url = "https://codeforces.com/api/contest.list"
    response = requests.get(url)

    if response.status_code == 200:
        contests = response.json()["result"]
        for contest in contests:
            if contest["phase"] == "CODING":
                CONTEST_ID = str(contest["id"])
                break


def get_codeforces_input(url):
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        input_div = soup.find("div", class_="input")

        if input_div:
            input_text = input_div.pre
            tests = ""
            for t in input_text: tests = tests + t.text + "\n"
            return tests
        
    return "Failed"


get_current_contest_id()

if(CONTEST_ID != -1):
    problem_url = BASE_URL + CONTEST_ID + "/problem/" + sys.argv[1]
    input_cases = get_codeforces_input(problem_url)

    f = open("../input.txt", "w")
    f.write(input_cases)
    f.close()