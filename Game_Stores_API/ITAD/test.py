import asyncio
from ITAD import itad

api_key = "a04182c5789ab3ed79e2cfeb07e4bc93199145e6"

list = ["app/865430", "app/440"]

run_this_test = False
if run_this_test is True:
    for i in range(len(list)):
        resp = itad.get_plain_from_steam_appid(api_key, list[i])

        if isinstance(resp, tuple):
            print(resp[0], ": ", resp[1])
        else:
            print(resp)

plain_list = ["destinyii", "callofdutywwii"]

for i in range(len(list)):
    #resp = itad.get_all_prices(api_key, plain_list[i])
    resp = itad.get_best_price(api_key, plain_list[i])
    print(resp)

