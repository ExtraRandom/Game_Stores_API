from GameStoresAPI.shared import Shared
import json
import os
import time
from datetime import datetime

"""

Work in progress

"""


class Origin:

    @staticmethod
    def __update_cache_and_return_json():
        url = "https://api4.origin.com/supercat/GB/en_GB/supercat-PCWIN_MAC-GB-en_GB.json.gz"

        r_data = Shared.get_page_raw(url)
        if r_data == "Error":
            return json.loads(
                {"success": False}
            )

        jdata = json.loads(Shared.get_page_raw(url))
        jdata["cached_time"] = time.time()
        jdata["success"] = True

        file = os.path.join(os.getcwd(), "origincache.json")
        with open(file, "w") as fw:
            json.dump(jdata, fw, indent=4)

        return jdata

    @staticmethod
    def __get_or_read_cache():
        file = os.path.join(os.getcwd(), "origincache.json")
        if os.path.isfile(file):
            with open(file, "r") as fr:
                cdata = json.loads(fr.read())
            time_then = cdata["cached_time"]
            time_now = time.time()
            if (time_now - time_then) >= 60 * 60 * 24:  # 1 day
                return Origin.__update_cache_and_return_json()
            else:
                return cdata

        else:  # cache doesnt exist
            return Origin.__update_cache_and_return_json()

    @staticmethod
    def search_by_name(display_name):
        jdata = Origin.__get_or_read_cache()

        try:
            display_name = str(display_name).lower()
            # search_items = display_name.split(" ")

            ids = []

            for i in range(jdata['totalCount'] - 1):
                # print(jdata['offers'][i]['i18n']['displayName'])
                # print(jdata['offers'][i]['masterTitle'])

                try:
                    if display_name in str(jdata['offers'][i]['masterTitle']).lower():
                        ids.append(i)
                    elif display_name in str(jdata['offers'][i]['itemName']).lower():
                        ids.append(i)
                    elif display_name in str(jdata['offers'][i]['i18n']['displayName']).lower():
                        ids.append(i)
                except TypeError:   # print("Type Error")
                    continue

            results = []

            for g_id in ids:
                i_price = jdata['offers'][g_id]['countries']['catalogPrice']
                if i_price == None:
                    continue  # skip if price is none (i believe this is origin access vault only versions of games)

                results.append(
                    {
                        "name": jdata['offers'][g_id]['i18n']['displayName'],
                        "desc": jdata['offers'][g_id]['i18n']['shortDescription'],
                        "price": round(float(i_price), 2),
                        "currency": jdata['offers'][g_id]['countries']['countryCurrency'],
                        "dev": jdata['offers'][g_id]['developerFacetKey'],
                        "pub": jdata['offers'][g_id]['publisherFacetKey'],
                        "type": jdata['offers'][g_id]['itemType'],
                        "url_end": jdata['offers'][g_id]['gdpPath']
                    }
                )

            x = {
                "success": True,
                "results": results
            }
            return x
        except Exception as e:
            return {"success": False, "reason": "Args: {}".format(e.args)}


