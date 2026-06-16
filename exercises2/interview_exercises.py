def most_frequent_element():
  numbers = [1, 3, 2, 3, 4, 3, 5, 1, 1, 1]
  nums_dict = {}

  for number in numbers:
    if number in nums_dict:
      nums_dict[number] += 1
    else:
      nums_dict[number] = 1

  most_frequent_key = 0
  most_frequent_val = 0

  for key, val in nums_dict.items():
    if val > most_frequent_val:
      most_frequent_val = val
      most_frequent_key = key

  print(most_frequent_key)

# most_frequent_element()

def merge_dicts():
  dict1 = {"a": 1, "b": 2, "c": 3}
  dict2 = {"b": 5, "c": 1, "d": 10}

  merged_dict = {}

  for key, val in dict1.items():
    if key in dict2:
      merged_dict.update({key: val + dict2[key]})
    else:
      merged_dict.update({key: val})

  for key, val in dict2.items():
    if key in dict1:
      merged_dict.update({key: val + dict1[key]})
    else:
      merged_dict.update({key: val})

  print(merged_dict)

merge_dicts()