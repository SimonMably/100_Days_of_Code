row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# -----------------------------------------------------------------------------
'''
if position == "11":
    map[0][0] = "X"
elif position == "12":
    map[0][1] = "X"
elif position == "13":
    map[0][2] = "X"
elif position == "21":
    map[1][0] = "X"
elif position == "22":
    map[1][1] = "X"
elif position == "23":
    map[1][2] = "X"
elif position == "31":
    map[2][0] = "X"
elif position == "32":
    map[2][1] = "X"
elif position == "33":
    map[2][2] = "X"
else:
    print("Only enter one of these numbers: 11, 12, 13, 21, 22, 23, 31, 32, 33")
'''
# -----------------------------------------------------------------------------
# Will also work:

horizontal = int(position[0])
vertical = int(position[1])

# Instead of:
selected_row = map[vertical - 1]
selected_row[horizontal - 1] = "X"

# We could also do:
'''
map[vertical - 1][horizontal - 1] = "X"
'''

# -----------------------------------------------------------------------------
print(f"{row1}\n{row2}\n{row3}")
