#------------- Beautiful Soup -----------------#
from bs4 import BeautifulSoup
# import lxml

# # add the encdoing param so you dont get any errors with unicode characters like emojis and stuff like that
# with open("website.html", encoding="utf8") as file:
#     contents = file.read()

# # making soup
# # first specify the file content, nect the parser that help understand the lang the content is structured in
# soup = BeautifulSoup(markup=contents, features="html.parser")

# # getting the string in the title tag
# print(soup.title.string)

# # prints the indented version of the html
# # print(soup.prettify())

# # getting the anchor tag - Note it only gets the first item it has found
# print(soup.a)

# # Getting all instances of a tag
# all_anchor_tag = soup.find_all(name="a")

# # getting only the text
# for tag in all_anchor_tag:
#     # print(tag.getText())  # gets only the text
#     print(tag.get("href"))  # gets the value of the specified attribute

# # gets and item using any attribute
# # applies to when there is only one of that item esle use find all
# heading = soup.find(name="h1", id="name")
# print(heading)
# section_heading = soup.find(name="h3", class_="heading")
# print(section_heading.get("name"))

# # this gets the anchor tag that is within a paragraph tag
# company_url = soup.select_one(selector="p a")
# print(company_url)

# # it is not restricted to only tags, also works with css selectors like ids and classes etc.
# name = soup.select_one(selector="#name")
# print(name)

# # returns a list of all possible items that have a class of heading
# headings = soup.select(".heading")
# print(headings)
