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

most_frequent_element()

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

def string_compression():
  s = "aaabbbccdaa"
  # expected "a3b3c2d1a2"

  i = 0
  j = 0
  result = ""

  for l in s:
    j += 1

    if i+1 == len(s):
      result += f"{l}{j}"
      break
    elif s[i+1] != l:
      result += f"{l}{j}"
      j = 0

    i += 1
  
  print(result)

string_compression()

def valid_parentheses():
  s = "(())()"

  lb_pointer = 0
  rb_pointer = 0

  for item in s:
    if item == "(":
      lb_pointer += 1
    elif item == ")":
      rb_pointer += 1
    
    if lb_pointer - rb_pointer < 0:
      return False
  
  if lb_pointer - rb_pointer != 0:
    return False
  else:
    return True

print(valid_parentheses())

def second_most_frequent():
  numbers = [1, 2, 3, 2, 4, 1, 2, 5, 1, 1, 3]
  numbers_dict = {}

  for item in numbers:
    if item in numbers_dict:
      numbers_dict[item] += 1
    else:
      numbers_dict[item] = 1

  max_key = 0
  max_val = 0
  for key, val in numbers_dict.items():
    if val > max_val:
      max_key = key
      max_val = val

  numbers_dict.pop(max_key)

  max_key = 0
  max_val = 0
  for key, val in numbers_dict.items():
    if val > max_val:
      max_key = key
      max_val = val

  print(max_key)

second_most_frequent()