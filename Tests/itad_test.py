from GameStoresAPI.itad import Itad as itad
import itad_api_key as iak

api_key = iak.key

# a_list = ["app/360830", "app/537450", "app/8140"]
t_list = ["call of duty world at war", "mass effect 2", "pillars of eternity", "battlefield 5"]

run_this_test = False
if run_this_test is True:
    # for i in range(len(list)):
    for i in range(len(t_list)):

        # resp = itad.get_plain_from_steam_appid(api_key, list[i])
        resp = itad.get_plain_from_title(api_key, t_list[i])

        if isinstance(resp, tuple):
            print(resp[0], ": ", resp[1])
        else:
            print(resp)

plain_list = ["battlefieldv", "destinyii", "callofdutywwii", "darksoulsremastered"]

a_list = ["app/311210", "app/437350", "app/581450"]


run_this_other_test = False
if run_this_other_test is True:
    for i in range(len(a_list)):
        # resp = itad.get_all_prices(api_key, plain_list[i])
        resp = itad.get_current_best_price(api_key, plain_list[i])
        print(resp)


# resp =
# print(resp)

print(itad.get_multiple_plains_from_steam_appids(api_key, a_list))
print(itad.get_multiple_current_best_price(api_key, itad.get_multiple_plains_from_steam_appids(api_key, a_list)))


# print(itad.get_historical_best_price(api_key, "yookalaylee"))  # , "us"))







