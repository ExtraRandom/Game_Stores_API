from GameStoresAPI.steam import Steam


search_games = ["hotline miami", "euro truck simulator", "wildlands"]

for i in range(0, len(search_games)):
    print(Steam.search_by_name(search_games[i]))


search_urls = ["https://store.steampowered.com/app/209650/Call_of_Duty_Advanced_Warfare__Gold_Edition/",
               "https://store.steampowered.com/app/560130/Pillars_of_Eternity_II_Deadfire/",
               "https://store.steampowered.com/app/300380"]
               #"https://store.steampowered.com/app/857720/Floor_Kids_Original_Soundtrack/",
               #"https://store.steampowered.com/app/789490",
               #"https://store.steampowered.com/app/271590/Grand_Theft_Auto_V/",
               #"https://store.steampowered.com/app/578080/"]
"""
for i in range(0, len(search_urls)):
    print(Steam.store_page_data(search_urls[i]))

"""












