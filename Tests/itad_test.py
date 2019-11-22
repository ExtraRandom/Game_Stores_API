# from GameStoresAPI.itad import Itad #  as itad
import itad_api_key as iak
from GameStoresAPI.itad_rw import Itad
api_key = iak.key

a_list = ["app/360830", "app/537450", "app/8140"]


test = Itad.search_plain_cache(api_key, "all", "left 4 dead 2")
test2 = Itad.search_plain_cache(api_key, "origin", "battlefield 1942")

print(test)


# t = Itad.get_price_current_best(api_key, Itad.get_plains_from_steam_appids(api_key, a_list))
# j = Itad.get_price_historic_best(api_key, Itad.get_plains_from_steam_appids(api_key, a_list))

# t = Itad.get_plains_from_steam_appids(api_key, a_list)
# j = Itad.get_plains_from_steam_appids(api_key, "app/8140")

# print(t)
# print(j)



# store_inp = "epic"
# store = Itad.check_store_valid(store_inp)
# print(store)
# print(store)
# print(store)

# t = Itad.search_plain_cache(api_key, store_inp, "borderlands")
# print(t)

# print(Itad.get_multiple_current_best_price(api_key, t))

# j = Itad.search_plain_cache(api_key, "origin", "apex")
# print(j)
# ee = (Itad.search_plain_cache(api_key, "gog", "sim city 3000"))
# print(ee)
# print(Itad.search_plain_cache(api_key, "battlenet", "overwatch"))



"""
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

# a_list = ["app/311210", "app/437350", "app/581450"]
a_list = ["app/261640", "app/319090", "app/459080", "app/316410", "app/275690", "app/321430", "app/289881", "app/289880"]

run_this_other_test = False
if run_this_other_test is True:
    for i in range(len(a_list)):
        # resp = itad.get_all_prices(api_key, plain_list[i])
        resp = itad.get_current_best_price(api_key, plain_list[i])
        print(resp)


# resp =
# print(resp)

# print(itad.get_multiple_plains_from_steam_appids(api_key, a_list))
print(itad.get_multiple_historical_best_price(api_key, itad.get_multiple_plains_from_steam_appids(api_key, a_list)))


# print(itad.get_historical_best_price(api_key, "yookalaylee"))  # , "us"))

"""










