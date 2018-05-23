import requests
import json


class Itad:

    @staticmethod
    def get_plain_from_steam_appid(api_key, app_id):
        url = "https://api.isthereanydeal.com/v02/game/plain/?key={}&shop=steam&game_id={}".format(api_key, app_id)
        resp = requests.get(url)
        data = json.loads(resp.text)
        if data['.meta']['match'] == False:
            return "Error", "App doesn't exist on ITAD"
        else:
            return data['data']['plain']

    @staticmethod
    def get_all_prices(api_key, plain, region="uk"):
        url = "https://api.isthereanydeal.com/v01/game/prices/?key={}&plains={}&region={}".format(api_key, plain, region)
        resp = requests.get(url)
        data = json.loads(resp.text)

        pdata = data['data'][plain]['list']

        return pdata

    @staticmethod
    def get_best_price(api_key, plain, region="uk"):
        url = "https://api.isthereanydeal.com/v01/game/prices/?key={}&plains={}&region={}".format(api_key, plain, region)
        resp = requests.get(url)
        data = json.loads(resp.text)

        price = data['data'][plain]['list'][0]['price_new']
        url = data['data'][plain]['list'][0]['url']
        shop = data['data'][plain]['list'][0]['shop']['name']

        return price, url, shop
