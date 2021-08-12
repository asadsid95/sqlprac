# 5. Switch first and last elements

new_list = [45, 60, 60, 60, 90000]


def first_last_list(new_list):

    first_pop = new_list.pop(0)  # 1st element
    last__pop = new_list.pop()  # last element

    last_switch = new_list.insert(0, last__pop)
    first_switch = new_list.append(first_pop)  # to last element

    return new_list


# print(first_last_list(new_list))

# 6. Count # of unique sublists in a list (#93)

new_list1 = [[45, 1], [60, 1], [60, 1], [60, 1], [90000, 2]]


def unique(newlist):
    result = {}
    for sub in newlist:
        result.setdefault(tuple(sub), list()).append(1)

    for a, b in result.items():
        result[a] = sum(b)
    return result


# print(unique(new_list1))

# 7. Reversing a string


def reverse(x):
    return reversed(x)


def reverse1(x):
    output = ''
    for c in x:
        output = c + output
    return output


# print(reverse1('asad'))

# 8. Count int in a mixed list (#106)

list1 = [1, 'abcd', 3, 1.2, 4, 'xyz', 5, 'pqr', 7, -5, -12.22]


def num_sublist(list1):
    cntr = 0
    for elmt in list1:
        if isinstance(elmt, float):
            cntr += 1
    return cntr


# print(num_sublist(list1))

# 9.

# 10.

# -------------- dictionary ------

# 1. Create a dictionary of keys x, y, and z where each key has as value a list from 11-20, 21-30, and 31-40 respectively. Access the fifth value of each key from the dictionary.

dict1 = {'x': [11, 12, 13, 14, 15, 16, 17, 18, 19],
         'y': [21, 22, 23, 24, 25, 26, 27, 28, 29],
         'z': [31, 32, 33, 34, 35, 36, 37, 38, 39]}

for k, v in dict1.items():
    print(v[4])

    # 2.
    # 3.
    # 4.
    # 5.
    # 6.

    # 7.

    # 8.

    # 9.

    # 10.
