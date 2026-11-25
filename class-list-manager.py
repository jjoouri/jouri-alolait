# Class List Manager - Group 1
# MIS 211 Bonus Assignment (GitHub Teamwork)

names = ["Sara", "Noura", "Lama", "Reem", "Amal", "Lama"]


# ===== Each student adds her function BELOW this line =====
# Written by: [jouri] (task 1)
def count_names(names):
    count = 0                       # variable: how many names we counted so far
    for name in names:              # loop: go through every name in the list
        count = count + 1
    return count

# ===== Each student adds her function ABOVE this line =====


def main():
    print("Welcome to the Class List Manager!")
    print("Class list:", names)
    # Each student calls her function here, for example:
    # print("Number of names:", count_names(names))


main(   print("Number of names:", count_names(names)))
