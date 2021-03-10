import pandas as pd

squirrel_data = pd.read_csv(
                "2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

squirrel_colours = {
    "Fur Colour": ["Grey", "Cinnamon", "Black"],
    "Count": [0, 0, 0]
}

for colour in squirrel_data["Primary Fur Color"]:
    if colour == "Gray":
        squirrel_colours["Count"][0] += 1
    elif colour == "Cinnamon":
        squirrel_colours["Count"][1] += 1
    elif colour == "Black":
        squirrel_colours["Count"][2] += 1

squirrel_colour_data = pd.DataFrame(squirrel_colours)
print(squirrel_colour_data)
squirrel_colour_data.to_csv("squirrel_count.csv")
