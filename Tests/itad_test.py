from GameStoresAPI.ITAD.itad import Itad as itad
import itad_api_key as iak

api_key = iak.key

list = ["app/865430", "app/440", "app/570940"]
t_list = ["call of duty world at war", "mass effect 2", "pillars of eternity", "ca ll of duty ww 2"]

run_this_test = True
if run_this_test is True:
    # for i in range(len(list)):
    for i in range(len(t_list)):

        # resp = itad.get_plain_from_steam_appid(api_key, list[i])
        resp = itad.get_plain_from_title(api_key, t_list[i])

        if isinstance(resp, tuple):
            print(resp[0], ": ", resp[1])
        else:
            print(resp)

plain_list = ["destinyii", "callofdutywwii", "darksoulsremastered"]

for i in range(len(list)):
    # resp = itad.get_all_prices(api_key, plain_list[i])
    resp = itad.get_best_price(api_key, plain_list[i])
    print(resp)

