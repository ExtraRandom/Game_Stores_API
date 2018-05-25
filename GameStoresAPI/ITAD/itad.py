import json
from GameStoresAPI.Shared.shared import Shared


class Itad:

    @staticmethod
    def get_plain_from_steam_appid(api_key, app_id):
        """Get Plain from given Steam APP ID

        :param api_key: ITAD API Key
        :param app_id: Steam Game APP ID
        :return: The plain for the given app id or error if it doesn't exist
        """
        url = "https://api.isthereanydeal.com/v02/game/plain/?key={}&shop=steam&game_id={}".format(api_key, app_id)
        data = json.loads(Shared.get_page_raw(url))      # resp = requests.get(url)      # data = json.loads(resp.text)

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
    def get_best_price(api_key, plain, region="uk"):
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
