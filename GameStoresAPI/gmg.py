import requests
import bs4
from GameStoresAPI.shared import Shared
import json


class GMG:

    """
    @staticmethod
    def get_search_results(term):
        base_url = "https://www.greenmangaming.com/search/"
        f_term = term.replace(" ", "%20")

        full_url = base_url + f_term

        base = bs4.BeautifulSoup(Shared.get_page_raw(full_url), "html.parser")

        tests = base.select('div[class="row search-result"]'.format(term))
        for test in tests:
            print(test)

            if hasattr(test, 'href') is True:

                # print(test.attrs)
                try:
                    check = test.attrs['href']
                    # print(test.attrs['href'])
                except Exception as e:
                    # print("nah")
                    pass
"""

    @staticmethod
    def format_search(search):
        return requests.utils.quote(search)

    @staticmethod
    def get_quick_search_results(term):
        url = "https://api.greenmangaming.com/api/v2/quick_search_results/{}".format(GMG.format_search(term))
        r_data = Shared.get_page_raw(url)
        data = json.loads(r_data)
        base_url = "https://www.greenmangaming.com"

        for game in data["results"]:
            n = game["GameVariantCode"]
            name = str(n).replace("  ", " ").replace("- PC", "")
            url = "{}{}".format(base_url, game["Url"])
            GMG.get_price_from_page(url)
            break

    @staticmethod
    def get_price_from_page(page):
        base_data = bs4.BeautifulSoup(Shared.get_page_raw(page), "html.parser")


        """
        scripts = base_data.select('script')
        end_data = None

        for s in scripts:
            x = str.strip(s.text)
            # print(x, "\n-------\n")
            if x.startswith("var initialSearchResults = "):
                print(x.replace("var initialSearchResults = ", ""))
                break


        """







