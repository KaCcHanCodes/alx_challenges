#book = {'title': "How they started: Global brands", 'author': "David lester", 'genre': "Business"}
#x = book.get('genre')
#print(x)

book = {'title': "", 'author': "", 'genre': ""}

title = input("Please enter the title of your favorite book: ")
author = input("Please enter the name of the author: ")
genre = input("What is the book's genre? ")

for items in title:
    book['title'] += items
for items in author:
    book['author'] += items
for items in genre:
    book['genre'] += items

print(book)