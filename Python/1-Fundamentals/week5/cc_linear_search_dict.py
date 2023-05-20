def linear_search_dictionary(dict, target_value):
    for key, value in dict.items():
        if value == target_value:
            print(f"{value} was found in the dictionary and the key is: {key}")
            return key
    print(f"{target_value} not found in dictionary.")
    return None


dic = {
    "james": "peach",
    "tiger": "stripe",
    "bruce": "willis",
    }

linear_search_dictionary(dic, "peter")