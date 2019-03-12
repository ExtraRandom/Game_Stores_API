from GameStoresAPI.playstation import Playstation

test_urls = ["https://store.playstation.com/en-gb/product/EP0002-CUSA02624_00-BLACKOPS3GAME000"
             # "https://store.playstation.com/en-gb/product/EP0002-CUSA05282_00-CODIWPREORDER001",
             # "https://store.playstation.com/en-gb/product/EP0002-BLES00354_00-DISCONLYPARENT00",
             # "https://store.playstation.com/en-gb/product/EP0001-CUSA00773_00-ASOBOMONOPOLY000",
             # "https://store.playstation.com/en-gb/product/EP9000-PCSF00570_00-BORDERLANDS2PSV1"]
             ]

for url in test_urls:
    print(Playstation.get_page_data(url))


print(Playstation.search_games("call of duty", ["ps4"]))
print(Playstation.search_games("spider man", ["ps4"]))

# Not the best code but its only for testing so I'm not too bothered

test_game_names = ["ratchet clank 2",  # 1
                   "call of duty",  # 2
                   "bacon",  # 3
                   "star wars",  # 4
                   "something that doesnt exist"]  # 5

test_platforms = [["ps3"],  # 1
                  ["ps3", "ps4"],  # 2
                  ["ps3", "ps4", "vita", "psp"],  # 3
                  ["ps4"], # 4
                  ["error 404 platform not found", "not a real platform"]]  # 5

test_content_types = [["games", "bundles"],  # 1
                      ["themes"],  # 2
                      ["games", "bundles", "addons", "themes", "other_extras", "timed_trials"],  # 3
                      ["games", "bundles", "themes"],  # 4
                      ["not a real content type"]]  # 5

# for i in range(0, len(test_game_names)):
#    bs4_url = Playstation.format_url(test_content_types[i], test_platforms[i], test_game_names[i])
#    print(Playstation.get_data(bs4_url))

"""
valid_platforms = ["ps4", "ps3", "vita", "psp"]
valid_content_types = ["games", "bundles", "addons", "themes", "other_extras", "timed_trials"]
"""

