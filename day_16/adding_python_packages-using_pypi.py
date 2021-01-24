
# Module = a single file that someone has written
# Package = two or more of files that someone has written (usually, a lot of
#           files

# * Using PrettyTable to display data in an ASCII table format.
from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = "l"
print(table)














