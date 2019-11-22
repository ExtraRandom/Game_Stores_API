import json
from datetime import datetime
from GameStoresAPI.shared import Shared
import os, time


class Itad:

    def __init__(self):
        self.last_request = None
        # TODO documentation

    @staticmethod
    def __comma_string(str_input):
        if isinstance(str_input, str):
            return True, str_input
        elif isinstance(str_input, list):
            return False, ",".join(str_input)
        else:
            return None, None

    @staticmethod
    def get_plains_from_steam_appids(api_key, app_ids):
        single, apps_str = Itad.__comma_string(app_ids)
        if single is None:
            return None

        url = "https://api.isthereanydeal.com/v01/game/plain/id/?key={}&shop=steam&ids={}" \
              "".format(api_key, apps_str)
        data = Shared.get_json(url)

        if data is "Error":
            return None
        results = []

        if single:
            results.append(data['data'][app_ids])
            return results
        else:
            for i in app_ids:
                results.append(data['data'][i])
            return results

    @staticmethod
    def get_price_current_best(api_key, plains, region="uk"):
        single, plains_str = Itad.__comma_string(plains)
        if single is None:
            return None

        url = "https://api.isthereanydeal.com/v01/game/prices/?key={}&plains={}&region={}&until=" \
              "".format(api_key, plains_str, region)
        data = Shared.get_json(url)

        results = {}

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

        if len(results) == 0:
            return 0
        else:
            return results

    @staticmethod
    def get_price_historic_best(api_key, plains, region="uk"):
        single, plains_str = Itad.__comma_string(plains)
        if single is None:
            return None

        url = "https://api.isthereanydeal.com/v01/game/lowest/?key={}&plains={}&region={}&until=" \
              "".format(api_key, plains_str, region)
        data = Shared.get_json(url)

        results = {}

        for game in data["data"]:
            date = str(datetime.utcfromtimestamp(data["data"][game]["added"])).split(" ")[0]
            game_d = {
                "price": data["data"][game]["price"],
                "date": date,
                "store": data["data"][game]["shop"]["name"]
            }
            results[game] = game_d

        if len(results) == 0:
            return 0
        else:
            return results

    @staticmethod
    def search_plain_cache(api_key, store: str, search_term: str):
        cache_data = Itad.__read_or_update_cache(api_key, store)
        store_check = Itad.verify_store(store)
        t = len(cache_data['data'])
        # print(t)

        hits = []

        searches = []

        search = search_term.split(" ")
        for word in search:
            if Itad.__is_int(word):
                number_broken = [int(n) for n in str(word)]
                number_fixed = ""
                for digit in number_broken:
                    number_fixed = "{}{}".format(number_fixed, Itad.__int_to_roman(digit))
                    number_fixed = number_fixed.lower()
                searches.append(number_fixed)  # searches.append(word)
            else:
                searches.append(word)

        target = len(searches)

        if store_check != "steam,battlenet,gog,origin,uplay,epic":
            for item in cache_data['data'][store]:
                plain = cache_data['data'][store][item]
                counts = 0

                for word in searches:
                    if word in plain:
                        counts += 1

                if counts == target:
                    hits.append(plain)
        else:
            for store_name in cache_data['data']:
                for item in cache_data['data'][store_name]:
                    plain = cache_data['data'][store_name][item]
                    counts = 0

                    for word in searches:
                        if word in plain:
                            counts += 1

                    if counts == target:
                        if plain not in hits:
                            hits.append(plain)

        if len(hits) is not 0:
            return hits
        else:
            return None

    @staticmethod
    def verify_store(store_input):
        store = str(store_input).lower()

        if store in ['steam', 'valve', 'staem']:
            return "steam"
        elif store in ['battlenet', 'bnet', 'blizzard', 'blizz', 'blizznet']:
            return "battlenet"
        elif store in ['gog', 'goodoldgames', 'cdpr']:
            return "gog"
        elif store in ['origin', 'ea', 'orgin', 'orign']:
            return "origin"
        elif store in ['uplay', 'ubisoft', 'ubi', 'usoft', 'play', 'upaly', "youplay"]:
            return "uplay"
        elif store in ['epic', 'egs', 'eipc', 'epci']:
            return "epic"
        elif store in ['all', 'every', 'combined', 'steam,battlenet,gog,origin,uplay,epic']:
            return "steam,battlenet,gog,origin,uplay,epic"
        else:
            return "INVALID"

    @staticmethod
    def __fetch_store_cache(api_key, store):
        url = "https://api.isthereanydeal.com/v01/game/plain/list/?key={}&shops={}".format(api_key, store)
        s_data = Shared.get_json(url)
        if s_data == "Error":
            return None
        else:
            return s_data

    @staticmethod
    def __read_or_update_cache(api_key, store):
        store_name = Itad.verify_store(store)
        if store_name != "INVALID":
            cache_file = os.path.join(Shared.get_cache_folder(), "{}_itadcache.json".format(store_name))
            if os.path.exists(cache_file):
                with open(cache_file, "r") as file_read:
                    cache_data = json.loads(file_read.read())
                cache_time = cache_data['cached_time']
                if (time.time() - cache_time) >= 60 * 60 * 24 * 7:
                    del cache_data
                    new_data = Itad.__fetch_store_cache(api_key, store_name)
                    if new_data is None:
                        return None
                    new_data['cached_time'] = time.time()

                    with open(cache_file, "w") as file_write:
                        json.dump(new_data, file_write, indent=4)
                    return new_data
                else:
                    return cache_data
            else:
                new_data = Itad.__fetch_store_cache(api_key, store_name)
                if new_data is None:
                    return None
                new_data['cached_time'] = time.time()
                with open(cache_file, "w") as file_write:
                    json.dump(new_data, file_write, indent=4)
                return new_data

    @staticmethod
    def __is_int(s):
        try:
            int(s)
            return True
        except ValueError:
            return False

    @staticmethod
    def __int_to_roman(num: int):
        val = [10, 9, 5, 4, 1]
        syb = ["X", "IX", "V", "IV", "I"]
        roman_num = ''
        i = 0
        if num == 0:
            return 0
        while num > 0:
            for _ in range(num // val[i]):
                roman_num += syb[i]
                num -= val[i]
            i += 1
        return roman_num





