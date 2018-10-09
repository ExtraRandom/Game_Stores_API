import json
from datetime import datetime
from GameStoresAPI.shared import Shared


class Itad:
    # TODO add info method https://itad.docs.apiary.io/#reference/game/info/get-info-about-game

    @staticmethod
    def get_multiple_plains_from_steam_appids(api_key, app_id_list):
        """Get multiple plains from multiple given app id's

        :param api_key: ITAD API Key
        :param app_id_list: List of steam Game APP ID's
        :return: List of plains for the given app id's
        """
        url = "https://api.isthereanydeal.com/v01/game/plain/id/?key={}&shop=steam&ids={}" \
              "".format(api_key, ",".join(app_id_list))

        data = json.loads(Shared.get_page_raw(url))  # print(data)  # d_len = len(data['data'])
        results = []

        for i in app_id_list:  # range(d_len):
            results.append(data['data'][i])  # print(results)
        return results

    @staticmethod
    def get_plain_from_steam_appid(api_key, app_id):
        """Get Plain from given Steam APP ID

        :param api_key: ITAD API Key
        :param app_id: Steam Game APP ID
        :return: The plain for the given app id or error if it doesn't exist
        """
        url = "https://api.isthereanydeal.com/v02/game/plain/?key={}&shop=steam&game_id={}".format(api_key, app_id)
        data = json.loads(Shared.get_page_raw(url))

        if data['.meta']['match'] == False:
            return "Error", "App doesn't exist on ITAD"
        else:
            return data['data']['plain']

    @staticmethod
    def get_plain_from_title(api_key, title):
        """Get plain from given game name (title)

        :param api_key: ITAD API Key
        :param title: Steam Game Title
        :return: The plain for the given title or error if it doesn't exist
        """
        url = "https://api.isthereanydeal.com/v02/game/plain/?key={}&title={}".format(api_key, title)
        data = json.loads(Shared.get_page_raw(url))

        if data['.meta']['match'] == False:
            return "Error", "Title doesn't match anything on ITAD, check spelling"
        else:
            return data['data']['plain']

    @staticmethod
    def get_all_prices(api_key, plain, region="uk"):
        """Get all prices for a given plain

        :param api_key: ITAD API Key
        :param plain: ITAD Plain for game to get prices for
        :param region: Pricing region, Default is UK
        :return: All prices for the given plain
        """
        url = "https://api.isthereanydeal.com/v01/game/prices/?key={}&plains={}&region={}".format(api_key, plain, region)
        data = json.loads(Shared.get_page_raw(url))

        pdata = data['data'][plain]['list']

        return pdata

    @staticmethod
    def get_current_best_price(api_key, plain, region="uk"):
        """Get best price for a given plain

        :param api_key: ITAD API Key
        :param plain: ITAD Plain for game to get best price for
        :param region: Pricing region, Default is UK
        :return: Best price for the given plain
        """
        url = "https://api.isthereanydeal.com/v01/game/prices/?key={}&plains={}&region={}".format(api_key, plain, region)
        data = json.loads(Shared.get_page_raw(url))

        if len(data['data'][plain]['list']) == 0:
            return "Error", "Check plain exists and is correct and try again", "Error"

        price = data['data'][plain]['list'][0]['price_new']
        url = data['data'][plain]['list'][0]['url']
        shop = data['data'][plain]['list'][0]['shop']['name']

        return price, url, shop

    @staticmethod
    def get_historical_best_price(api_key, plain, region="uk"):
        """Get best historical (all time) price for a given plain

        :param api_key: ITAD API Key
        :param plain: ITAD Plain for game to get best price for
        :param region: Pricing region, Default is UK
        :return: Lowest ever price for the given plain
        """
        url = "https://api.isthereanydeal.com/v01/game/lowest/?key={}&plains={}&region={}&until=" \
              "".format(api_key, plain, region)
        data = json.loads(Shared.get_page_raw(url))

        if len(data["data"][plain]) == 5:
            currency = data[".meta"]["currency"]
            price = data["data"][plain]["price"]
            shop = data["data"][plain]["shop"]["name"]

            return currency, price, shop
        else:
            return "Error", "Error", "Error", "Error"

    @staticmethod
    def get_multiple_historical_best_price(api_key, plains, region="uk"):
        """Get best historical price from multiple given plains

        :param api_key: ITAD API Key
        :param plains: List of ITAD Plains
        :param region: Pricing Region, Default is UK
        :return: List of results
        """

        results = {}

        formatted_plains = ""
        for plain in plains:
            if formatted_plains == "":
                formatted_plains = "{}".format(plain)
            else:
                formatted_plains = "{},{}".format(formatted_plains, plain)

        url = "https://api.isthereanydeal.com/v01/game/lowest/?key={}&plains={}&region={}&until=" \
              "".format(api_key, formatted_plains, region)

        data = json.loads(Shared.get_page_raw(url))

        for game in data["data"]:
            date = str(datetime.utcfromtimestamp(data["data"][game]["added"])).split(" ")[0]

            g_results = {
                    "price": data["data"][game]["price"],
                    "date": date,
                    "store": data["data"][game]["shop"]["name"]
                 }

            results[game] = g_results

        return results

    @staticmethod
    def get_multiple_current_best_price(api_key, plains, region="uk"):
        """Get best current best price from multiple given plains

        :param api_key: ITAD API Key
        :param plains: List of ITAD Plains
        :param region: Pricing Region, Default is UK
        :return: List of results
        """

        results = {}

        formatted_plains = ""
        for plain in plains:
            if formatted_plains == "":
                formatted_plains = "{}".format(plain)
            else:
                formatted_plains = "{},{}".format(formatted_plains, plain)

        url = "https://api.isthereanydeal.com/v01/game/prices/?key={}&plains={}&region={}&until=" \
              "".format(api_key, formatted_plains, region)

        data = json.loads(Shared.get_page_raw(url))

        for game in data["data"]:
            game_d = {
                        "price": data["data"][game]["list"][0]["price_new"],
                        "url": data["data"][game]["list"][0]["url"],
                        "store": data["data"][game]["list"][0]["shop"]["name"]
            }
            results[game] = game_d

        return results



