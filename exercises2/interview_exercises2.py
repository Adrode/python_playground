def merge_sorted_lists():
    list1 = [1, 7, 8, 10]
    list2 = [2, 4, 6, 8]

    merged = []

    i = 0       # 1 1 1 1 2 3 3
    j = 0       # 0 1 2 3 3 3 4 
    counter = 0 # 1 2 3 4 5 6 7

    while i < len(list1) and j < len(list2):
        if list1[i] <= list2[j]:
            merged.append(list1[i])
            i += 1
        else:
            merged.append(list2[j])
            j += 1
        print(f"{counter}. {merged}")
        counter += 1

    if i < len(list1):
        merged.extend(list1[i:])
    if j < len(list2):
        merged.extend(list2[j:])

    return merged

print(merge_sorted_lists())