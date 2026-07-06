def merge_sorted_lists():
    list1 = [1, 7, 8, 10]
    list2 = [2, 4, 6, 8]

    merged = []

    i = 0
    j = 0

    while i < len(list1) and j < len(list2):
        if list1[i] <= list2[j]:
            merged.append(list1[i])
            i += 1
        else:
            merged.append(list2[j])
            j += 1

    if i < len(list1):
        merged.extend(list1[i:])
    if j < len(list2):
        merged.extend(list2[j:])

    return merged


# print(merge_sorted_lists())


def longest_consecutive_run1():
    s = "aabbbbccccddeeeeaacccc"

    pointer = ""
    collection = {}
    temporary = {}

    for item in s:
        if item != pointer and item not in collection:
            pointer = item
            collection[item] = 1
        elif item == pointer and item in collection:
            collection[item] += 1
        elif item != pointer and item in collection:
            if item not in temporary:
                temporary[item] = 1
            else:
                temporary[item] += 1

            if collection[item] < temporary[item]:
                collection[item] = temporary[item]

    max_key = 0
    max_val = 0

    for key, val in collection.items():
        if val > max_val:
            max_val = val
            max_key = key

    return collection, max_key


# print(longest_consecutive_run1())


def longest_consecutive_run2():
    s = "aabbbbccccddeeeeeeaacccccccccc"

    best_key = ""
    best_val = 0

    current_key = ""
    current_val = 0

    for item in s:
        if current_key == item:
            current_val += 1
        else:
            current_key = item
            current_val = 1

        if current_val > best_val:
            best_key = current_key
            best_val = current_val

    return (best_key, best_val)


# print(longest_consecutive_run2())


def two_sum():
    numbers = [2, 1, 3, 4]
    target = 6

    collection = {}
    current_index = 0

    for item in numbers:
        search = target - item

        if search in collection:
            return (collection[search], current_index)

        if item not in collection:
            collection[item] = current_index
            current_index += 1


# print(two_sum())


def first_unique_character():
    s = "aabbccdeffg"

    collection = {}

    for x in s:
        if x not in collection:
            collection[x] = 1
        else:
            collection[x] += 1

    for key, x in enumerate(s):
        if collection[x] == 1:
            return key
        
print(first_unique_character())