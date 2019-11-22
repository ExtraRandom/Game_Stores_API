from GameStoresAPI.playstation import Playstation

test_urls = ["https://store.playstation.com/en-gb/product/EP0002-CUSA02624_00-BLACKOPS3GAME000"
             # "https://store.playstation.com/en-gb/product/EP0002-CUSA05282_00-CODIWPREORDER001",
             # "https://store.playstation.com/en-gb/product/EP0002-BLES00354_00-DISCONLYPARENT00",
             # "https://store.playstation.com/en-gb/product/EP0001-CUSA00773_00-ASOBOMONOPOLY000",
             # "https://store.playstation.com/en-gb/product/EP9000-PCSF00570_00-BORDERLANDS2PSV1"]
             ]

# for url in test_urls:
#    print(Playstation.get_page_data(url))


print(Playstation.search_games("gravity rush", ["ps4"]))
# print(Playstation.search_games("spider man", ["ps4"]))


"""
valid_platforms = ["ps4", "ps3", "vita", "psp"]
valid_content_types = ["games", "bundles", "addons", "themes", "other_extras", "timed_trials"]
"""

