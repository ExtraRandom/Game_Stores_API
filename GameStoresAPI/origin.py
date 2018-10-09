# import bs4
from GameStoresAPI.shared import Shared
from selenium import webdriver
from selenium.webdriver.common.by import By

import json


"""

Work in progress

"""


class Origin:

    @staticmethod
    def format_url(url):
        return Shared.url_encode(url, [" ", "!"])

    @staticmethod
    def get_search_results(search_term):
        """Gets search results for given term, no pricing info just name and link"""
        base_url = "https://www.origin.com/gbr/en-us/search?searchString="
        url = base_url + Origin.format_url(search_term)

        store_url = "https://www.origin.com/gbr/en-us/store"

        browser = webdriver.Chrome()
        browser.implicitly_wait(10)
        browser.get(url)
        elements = browser.find_elements(By.XPATH, "//li/otkex-hometile")

        for i in range(3):
            t = elements[i].text
            print(t)
            r = Origin.get_url_from_display_name(t)
            print(r)

        browser.close()

        # print(store_url + r)

    @staticmethod
    def get_url_from_display_name(display_name):
        # TODO add some sort of looper that checks through all api's if one fails
        # EA Seems to have 4 api's all returning the same thing
        url = "https://api4.origin.com/supercat/GB/en_GB/supercat-PCWIN_MAC-GB-en_GB.json.gz"

        jdata = json.loads(Shared.get_page_raw(url))

        for i in range(jdata['totalCount']):
            # print(jdata['offers'][i]['i18n']['displayName'])
            # print(jdata['offers'][i])
            if display_name in jdata['offers'][i]['offerPath']:  # jdata['offers'][i]['i18n']['displayName']:
                return jdata['offers'][i]['offerPath']

        return "No Result"
