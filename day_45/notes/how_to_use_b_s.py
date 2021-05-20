from bs4 import BeautifulSoup
# import lxml   # If html.parser does not work

# Without "latin-1" encoding, reading this file will return an error.
# See: https://stackoverflow.com/questions/44251813/unicodedecodeerror-charmap-codec-cant-decode-byte-0x9d-in-position-1010494
with open("website.html", "r", encoding="utf-8") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")
# print(soup.title)
# print(soup.title.string)

# Formats file
# print(soup.prettify())

# prints 1st anchor tag
# print(soup.a)
# Print 1st list element
# print(soup.li)
# Prints 1st paragraph in p tag
# print(soup.p)

# Finds all instances of a requested thing. In this case, finds all anchor tags:
all_anchor_tags = soup.find_all(name="a")
# print(all_anchor_tags)

# for tag in all_anchor_tags:
    # Prints text in all anchor tags
    # print(tag.getText())

    # Use the .get() method to get the value of an attribute (eg. href link):
    # print(tag.get("href"))

# Isolating an element by its id (eg. a h1 tag with an id of "name")
heading = soup.find(name="h1", id="name")
# print(heading)

# Using the same .find() method to isolate an element by its class
section_heading = soup.find(name="h3", class_="heading")
print(section_heading)
# Getting the text from 'section_heading'
# print(section_heading.getText())
# # # The name of the tag in 'section_heading'
# # print(section_heading.name)
# # # Get hold of a value of an attribute
# # print(section_heading.get("class"))


# Using CSS selectors

# .select_one() will give the 1st matching item (.select() will give all matching items in a list)
company_url = soup.select_one(selector="p a")  # p, a = tags

# We can also use .select_one() & .select() to find a id or class
# select an id:
name = soup.select_one(selector="#name")
print(name)

# select a class:
headings = soup.select(selector=".heading")
print(headings)
