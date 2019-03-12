from GameStoresAPI.origin import Origin
import json

# print(Origin.search_by_name("apex legends"))

# print(Origin.search_by_name("battlefield"))

# print(json.dumps(Origin.search_by_name("battlefield v")))

test = Origin.search_by_name("apex legends")
print(json.dumps(test))
