from bs4 import BeautifulSoup  # for pulling data out of HTML or XML files
import requests
import pandas as pd
import json

URL = "https://en.wikipedia.org/wiki/List_of_largest_banks?utm_medium=Exinfluencer&utm_source=Exinfluencer"
"&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel"
"-SkillsNetworkCoursesIBMDeveloperSkillsNetworkPY0221ENSkillsNetwork23455645-2022-01-01"
FILE_NAME = "bank_market_cap.json"


def extract_bank_row_data(url):
    html_data = requests.get(url).text
    soup = BeautifulSoup(html_data, 'html.parser')
    # print html_data[101:124] -- requested by the exercise
    by_market_cap = soup.find(id="By_market_capitalization").parent
    table = by_market_cap.find_next_sibling(name='table')
    return table


def transform_data(data_source):
    data = pd.DataFrame(columns=["Name", "Market Cap (US$ Billion)"])
    for row in data_source.tbody.find_all('tr'):
        col = row.find_all('td')
        if col:
            name = col[1].text.rstrip('\n')
            market = col[2].text.rstrip('\n')
            data = data.append({"Name": name, "Market Cap (US$ Billion)": market}, ignore_index=True)
    return data


def load_data(data, file_name):
    data.to_json(file_name)


if __name__ == '__main__':
    scraped_table = extract_bank_row_data(URL)
    market_data = transform_data(scraped_table)
    load_data(market_data, FILE_NAME)
    print market_data.head()  # Print 5 first rows
