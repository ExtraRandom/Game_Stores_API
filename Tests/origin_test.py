from GameStoresAPI.origin import Origin
import json

# Origin.get_url_from_display_name("Battlefield™ V")

# test = Origin.get_search_results("fe")

# test = Origin.get_search_results("battlefield 5")


# Origin.test("red")

# print(Origin.search_by_name("apex legends"))

# print(Origin.search_by_name("battlefield"))

print(json.dumps(Origin.search_by_name("battlefield v")))
