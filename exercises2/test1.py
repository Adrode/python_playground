# DATA STRUCTURES exercises

numbers = [1, 2, 3, 4, 5, 6]

even_times_two = [x * 2 for x in numbers if x % 2 == 0]
# print(even_times_two)

# ---

user = {
    "name": "Adrian",
    "age": 25,
    "city": "Warsaw"
}

# for key, value in user.items():
#   print(f"{key} -> {value}")

# ---

words = ["apple", "banana", "apple", "orange", "banana", "apple"]

fruits = {}

for item in words:
  if item in fruits.keys():
    fruits[item] += 1
  else:
    fruits.update({item: 1})

# print(fruits)

# ---

numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5]

sort = sorted(set(numbers))
# print(sort)

# ---

numbers = [10, 15, 20, 25, 30, 35, 40]

even_odd_dict = {
  "even": [],
  "odd": []
}

for item in numbers:
  if item % 2 == 0:
    even_odd_dict["even"].append(item)
  else:
    even_odd_dict["odd"].append(item)

# print(even_odd_dict)

# ---

text = "programming in python is fun but programming is also challenging"

check = {}

for item in text.split():
  if item not in check:
    check[item] = 1
  else:
    check[item] += 1

for item in text.split():
  if check[item] == 1:
    # print(item)
    break

# ---

words = ["eat", "tea", "tan", "ate", "nat", "bat"]

anagrams = {}

for word in words:
  key = "".join(sorted(word))
  if key in anagrams:
    anagrams[key].append(word)
  else:
    anagrams[key] = [word]

# print(anagrams)

# ---

s = "programming"

keys = {}

for item in s:
  if item in keys:
    keys[item] += 1
  else:
    keys[item] = 1

for item in s:
  if keys[item] == 1:
    print(item)
    break