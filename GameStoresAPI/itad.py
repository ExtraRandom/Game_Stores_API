import json
from datetime import datetime
from GameStoresAPI.shared import Shared
import os, time


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

        data = Shared.get_json(url)
        results = []

        for i in app_id_list:
            results.append(data['data'][i])
        return results

    @staticmethod
    def get_plain_from_steam_appid(api_key, app_id):
        """Get Plain from given Steam APP ID

        :param api_key: ITAD API Key
        :param app_id: Steam Game APP ID
        :return: The plain for the given app id or error if it doesn't exist
        """
        url = "https://api.isthereanydeal.com/v02/game/plain/?key={}&shop=steam&game_id={}".format(api_key, app_id)
        data = Shared.get_json(url)

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
        data = Shared.get_json(url)

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
        url = "https://api.isthereanydeal.com/v01/game/prices/?key={}&plains={}&region={}" \
              "".format(api_key, plain, region)
        data = Shared.get_json(url)

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
        url = "https://api.isthereanydeal.com/v01/game/prices/?key={}&plains={}&region={}" \
              "".format(api_key, plain, region)
        data = Shared.get_json(url)

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
        data = Shared.get_json(url)

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
        count = 0
        for plain in plains:
            if count == 10:
                break
            else:
                count += 1
            if formatted_plains == "":
                formatted_plains = "{}".format(plain)
            else:
                formatted_plains = "{},{}".format(formatted_plains, plain)

        url = "https://api.isthereanydeal.com/v01/game/lowest/?key={}&plains={}&region={}&until=" \
              "".format(api_key, formatted_plains, region)

        data = Shared.get_json(url)

        for game in data["data"]:
            if 'shop' not in data['data'][game]:
                # skip it
                continue
            else:

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
        count = 0
        for plain in plains:
            if count == 10:
                break
            else:
                count += 1
            if formatted_plains == "":
                formatted_plains = "{}".format(plain)
            else:
                formatted_plains = "{},{}".format(formatted_plains, plain)

        url = "https://api.isthereanydeal.com/v01/game/prices/?key={}&plains={}&region={}&until=" \
              "".format(api_key, formatted_plains, region)

        data = Shared.get_json(url)

        if data == "Error":
            return None

        for game in data["data"]:
            if len(data["data"][game]["list"]) == 0:
                # skip it
                pass
            else:
                game_d = {
                            "price": data["data"][game]["list"][0]["price_new"],
                            "url": data["data"][game]["list"][0]["url"],
                            "store": data["data"][game]["list"][0]["shop"]["name"]
                }
                results[game] = game_d

        return results

    @staticmethod
    def check_store_valid(store_inp):
        """Check if given store is a valid store option, allows for some nick names

        :param store_inp: Store to check
        :return: Proper name of store if correct, or 'INVALID' if store wasn't a valid store
        """
        store = str(store_inp).lower()

        if store in ['steam', 'valve', 'staem']:
            return "steam"
        elif store in ['battlenet', 'bnet', 'blizzard', 'blizz', 'blizznet']:
            return "battlenet"
        elif store in ['gog', 'goodoldgames', 'cdpr']:
            return "gog"
        elif store in ['origin', 'ea', 'orgin', 'orign']:
            return "origin"
        elif store in ['uplay', 'ubisoft', 'usoft', 'play', 'upaly']:
            return "uplay"
        else:
            return "INVALID"

    @staticmethod
    def search_plain_cache(api_key, store: str, search_term: str):
        """

        :param api_key: ITAD API Key
        :param store: Name of store to search
        :param search_term: Search term to search with
        :return: list of plains that match the search term, None if failed and 0 if no results
        """

        """
        Potential issue, say you search for 'battlefield v', battlefield vietnam will come up first
        But if you just search for 'battlefieldv' the results are battlefield 5 as one would expect
        So maybe do another check for if the word with no spaces has any exact matches

        This'll work fine for the time being though
        """

        c_data = Itad.__read_or_update_store_cache(api_key, store)
        hits = []

        search = search_term.split(" ")
        search_other = []

        for word in search:
            appd = False
            number = list(filter(str.isdigit, word))
            for num in number:
                search_other.append(Itad.__number_to_roman_numeral(int(num)))
                appd = True
            if appd is False:
                search_other.append(word)

        if search == search_other:
            check_both = False
        else:
            check_both = True

        if len(c_data['data']) == 0:
            return None

        for item in c_data['data'][store]:
            plain = c_data['data'][store][item]

            if check_both is False:
                checker = 0
                for word in search:
                    if word in plain:
                        checker += 1
                if checker == len(search):
                    hits.append(plain)
            else:  # check_both is true
                checker = 0
                other_checker = 0
                for word in search:
                    if word in plain:
                        checker += 1
                for word_o in search_other:
                    if word_o in plain:
                        other_checker += 1

                hit_max = len(search)
                if checker == hit_max or other_checker == hit_max:
                    hits.append(plain)

        if len(hits) is not 0:
            return hits
        else:
            return 0

    @staticmethod
    def __number_to_roman_numeral(number_input: int):
        """https://www.oreilly.com/library/view/python-cookbook/0596001673/ch03s24.html"""
        if number_input is 0:
            return 0

        ints = (1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1)
        nums = ('M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I')
        result = []
        for i in range(len(ints)):
            count = int(number_input / ints[i])
            result.append(nums[i] * count)
            number_input -= ints[i] * count
        return ''.join(result).lower()

    @staticmethod
    def __fetch_store_cache(api_key, store):
        """"""
        s_data = Shared.get_json("https://api.isthereanydeal.com/v01/game/plain/list/?key={}&shops={}"
                                 "".format(api_key, store))
        if s_data == "Error":
            return None
        else:
            return s_data

    @staticmethod
    def __read_or_update_store_cache(api_key, store_name):
        res = Itad.check_store_valid(store_name)
        if res != "INVALID":
            c_file = os.path.join(Shared.get_cache_folder(), "{}_itadcache.json".format(res))
            if os.path.exists(c_file):
                with open(c_file, "r") as fr:
                    c_data = json.loads(fr.read())
                cache_time = c_data['cached_time']
                if (time.time() - cache_time) >= 60 * 60 * 24 * 7:  # 7 days
                    del c_data
                    new_data = Itad.__fetch_store_cache(api_key, store_name)
                    if new_data is None:
                        return None
                    new_data['cached_time'] = time.time()
                    with open(c_file, "w") as fw:
                        json.dump(new_data, fw, indent=4)
                    return new_data
                else:
                    return c_data

            else:  # no file exists
                new_data = Itad.__fetch_store_cache(api_key, store_name)
                if new_data is None:
                    return None
                new_data['cached_time'] = time.time()
                with open(c_file, "w") as fw:
                    json.dump(new_data, fw, indent=4)
                return new_data




