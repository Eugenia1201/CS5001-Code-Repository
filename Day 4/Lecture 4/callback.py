" Testing callback function by sorting on last letter "


def reverse_order(a_string):
    return a_string[::-1]


string_function = reverse_order

print("abcde")
print(string_function("abcde"))


strings_to_sort = ["au", "bt", "cs", "dr"]

print(strings_to_sort)
print(sorted(strings_to_sort))
print(sorted(strings_to_sort, key=reverse_order))
