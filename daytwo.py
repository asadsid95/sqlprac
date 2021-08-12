# Number of exercises completed:

'''
Types of Data structutres:
        1. List
        2. Tuple
        3. Dictionary
        4. Set
        5. Array
        6. Linked list
        7. Queue
'''

'''
Functions to do:
1. + / - / * elements
2. Finding specific values (small / largest value)
3. Index specific (ref. + manipulation)
'''

# ---------------------  List ------------------

# 1. Finding smallest number in a list


first_list = [44, 6, 7, 10, -3.5]


def list_smallest_number(list):

    min = list[0]  # integer value

    for a in list:
        if a < min:
            min = a
    return min


def smallest_number_list(list):
    initial_min = list[0]

    for a in list:
        if a < initial_min:
            initial_min = a
    return initial_min


# print(list_smallest_number(first_list))
# print(smallest_number_list(first_list))

# tldr; use 1st element of [] as reference (ref). value
# alt approach: start with 0 -> look into global vs local variable

# 2. Copy/clone a list

copy_list = list(first_list)
# print(copy_list)

# 3. Find & place item at back of list

# print(first_list.pop(first_list.index(10)))


def switched(item):

    first_list.append(first_list.pop(first_list.index(item)))

    return first_list


print(switched(10))

# 4. Removing duplicates in list

new_list = [45, 60, 60, 60, 90]


def rm_dupl(nlist):
    dupl_less = list(dict.fromkeys(nlist))

    return dupl_less


print(rm_dupl(new_list))

# 5. Switch first and last elements

# 6. Count # of sublists containing a number (93)

# 7.

# 8.

# 9.

# 10.

# -------------- Tuple ------

# 1.
# 2.
# 3.
# 4.
# 5.
# 6.

# 7.

# 8.

# 9.

# 10.
