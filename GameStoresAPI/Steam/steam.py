import bs4
from GameStoresAPI.shared import Shared
import json


class Steam:

    @staticmethod
    def format_search(search_term):
        result = search_term.replace(" ", "%20")
        return result

    @staticmethod
    def search_by_name(name, currency="gbp", language="en"):
        """Search for a game using a given name"""
        base_url = "https://store.steampowered.com/search/?cc={}&l={}&term=".format(currency, language)
        full_url = base_url + Steam.format_search(name)

        base_data = bs4.BeautifulSoup(Shared.get_page_raw(full_url), "html.parser")

        # print(full_url + "\n")

        if base_data.text == "Error":
            print("Error occured whilst getting data")
        else:
            results = len(base_data.select('div[id="search_result_container"] '
                                           'a[class="search_result_row ds_collapse_flag"]')
                          )

            if results < 3:
                range_end = results
                if range_end == 0:
                    return [{"results": False}]
            else:
                range_end = 3

            game_data_list = [{"results": True}]

            for i in range(0, range_end):
                data = base_data.select('div[id="search_result_container"] a[class="search_result_row ds_collapse_flag"]'
                                        '')[i]
                store_url = data.attrs['href']
                # print(store_url)

                title = data.select('span[class="title"]')[0].text
                # print(title)

                if len(data.select('div[class="col search_discount responsive_secondrow"]')[0].text.strip()) != 0:
                    # Game has a discount
                    price = str(data.select('span strike')[0].next_element.next_element.next_element).strip()
                    discount = data.select('div[class="col search_discount responsive_secondrow"] span')[0].text.strip()
                    # print(price, discount)
                else:
                    # Game doesn't have a discount
                    price = data.select('div[class="col search_price responsive_secondrow"]')[0].text.strip()
                    if len(price) == 0:
                        price = "None"
                    discount = "None"
                    # print(price, discount)

                release_date = data.select('div[class="col search_released responsive_secondrow"]')[0].text.strip()
                if len(release_date) == 0:
                    release_date = "None"

                # print(release_date)

                game_data = {"title": title, "price": price, "discount": discount, "release_date": release_date,
                             "store_url": store_url}
                game_data_list.append(game_data)

            return game_data_list

        return 0

    @staticmethod
    def store_page_data(url, currency="gbp"):
        """ """
        #  https://store.steampowered.com/api/appdetails/?appids=271590

        # Check URL is a Steam URL
        if "store.steampowered" not in url:
            return "Error", "URL is not a Steam URL"

        url_split = str(url).split("/")
        app_id = url_split[4]

        url = "https://store.steampowered.com/api/appdetails/?appids={}&cc={}".format(app_id, currency)

        jdata = Shared.get_page_raw(url)
        # print(jdata)

        if jdata == "Error":
            return "Error", "Retrieving page data failed in 'store_page_data'"

        sdata = json.loads(jdata)

        data = sdata[app_id]['data']

        title = data['name']
        desc = data['short_description']

        coming_soon = data['release_date']['coming_soon']
        release_date = data['release_date']['date']

        discount = 0
        price = "N/A"

        if bool(data['is_free']) == False:
            try:
                price = int(data['price_overview']['final']) / 100
                discount = data['price_overview']['discount_percent']
            except KeyError:
                pass

        developers = ", ".join(data['developers'])
        publishers = ", ".join(data['publishers'])

        if len(publishers) == 0:
            publishers = "None"

        return title, desc, coming_soon, release_date, discount, price, developers, publishers





