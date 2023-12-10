"""CS5001_Kaiqi Zhang_Sep/27/2023: This is the working file for Lab3"""

import random
import string
# Part 1

# Step 1: Generate a list of lists
outer_list = []
outer_list_length = random.randint(6, 12)

for how_many_list in range(outer_list_length):

    inner_list_length = random.randint(4, 10)

    inner_list = [random.randint(0, 100) for how_many_items in range(
        inner_list_length)]

    outer_list.append(inner_list)

print(outer_list)


# Step 2: A Pretty-Printer
def pretty_printer(list):
    """This function prints something in a pretty format.

    Args:
        list (_type_): it takes in one parameter which is the list of lists.
    """

    for x in range(len(list)):
        print(list[x], "\n")


pretty_printer(outer_list)

# Step 3: Computing some list things

# max() is to get the biggest item in list;
# pass in additional parameter to specify max in length
print("The longest list is: ", max(outer_list, key=len))
print("The first two put together makes: ", outer_list[0] + outer_list[1])
# List comprehension again: Expression for variable in iterable
print("The square of the first list is:", [n**2 for n in outer_list[0]])
# multiplying is cheaper than expansion
# Nested List comprehension
print("The big numbers are: ", [[value for value in inner_list if value >= 50]
                                for inner_list in outer_list])
print("The maximum numbes are: ", [max(inner_list)
                                   for inner_list in outer_list])


# Part 2
# Step 4:
candidates = ["Madam, I'm Adam!", "Never even or odd", "Never odd or even",
              "Was it a cat I saw?", "Was it a rat I saw?",
              "A man, a plan, a canal: Suez!",
              "A man, a plan, a canal: Panama!",
              "12/12/1212", "12/12/2121", "Borrow or rob?",
              "Step on no pets!", "This is just a kitty"]

# Approach 1
# translator = str.maketrans('', '', string.punctuation + string.whitespace)
# candidate_cleaned = [s.translate(translator).lower() for s in candidates]
# #The maketrans() method returns a mapping table that can be used with the
# translate() method to replace specified characters.

# Approach 2
candidates_cleaned = []
for i in range(len(candidates)):
    candidates_temp = "".join(
        ch for ch in candidates[i] if ch not in string.whitespace +
        string.punctuation)
    candidates_cleaned.append(candidates_temp.lower())

print(candidates_cleaned)

# #Step 5:


def test_palindrome(string):
    n = len(string)
    i = 0
    while (i < (n/2)):
        if (string[i] != string[-i-1]):
            return False
        else:
            i += 1
    return True


print(test_palindrome(candidates_cleaned[0]))
