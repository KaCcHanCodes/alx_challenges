from mysql.connector import connect, Error

# Replace with your connection details
connection = connect(
    host="localhost",
    user="***",
    passwd="****",
    database="Library" 
)
cursor = connection.cursor()

# cursor.execute("CREATE TABLE IF NOT EXISTS books (id INTEGER AUTO_INCREMENT PRIMARY KEY, title VARCHAR(255), author VARCHAR(255), ISBN VARCHAR(255))")
# cursor.execute("SELECT * FROM books")

def insert_book(title, author, ISBN):
    value = (title, author, ISBN)
    query = "INSERT INTO books (title, author, ISBN) VALUES ( %s, %s, %s)"
    cursor.execute(query, value)
    connection.commit()
    return True

def search_for_book(title):
    value = (f"%{title}%",)
    query = "SELECT * FROM books WHERE title LIKE %s"
    cursor.execute(query, value)
    result = cursor.fetchall()
    if result:
        for books in result:
            print(*books)


def list_all_books():
    cursor.execute("SELECT * FROM books")
    result = cursor.fetchall()
    for book in result:
        holder = print(book)
    return holder

def remove_book(title):
    value = (title)
    query = "DELETE FROM books WHERE title LIKE '%s'"
    cursor.execute(query, value)
    connection.commit()

while True:
    print("Library Codes")
    print("To register a book = 1\nTo search the library for a book = 2\nTo list all books = 3\nTo remove a book from the library = 4\n")

    user_input = int(input("Please enter a corresponding library code: \n"))

    match user_input:
        case 1:
            #The input returned from the user prompt is stored in a list[] container by default
            title = input("Please enter the title of the book: ").split()
            author = input("Please enter the author of the book: ").split()
            ISBn = input("Please enter the ISBN of the book: \n").split()
            
            #Here I am using the .join() function to convert the various lists into strings
            title_ = " ".join(title)
            author_ = " ".join(author)
            ISBn_ = " ".join(ISBn)

            #Passing the variables into the custom function that inserts books tot he library
            val = insert_book(title_, author_, ISBn_)
            if val:
                print("Upload successful\n")
            else:
                print("Upload unsuccessful, please enter the required details (Book title, Book author, and ISBN)\n")

        case 2:
            title = input("What is the title of the book? ").split()
            title_ = " ".join(title)
            search_for_book(title_)
        
        case 3:
            #refers to the func that shows us the details of all stored books
            list_all_books()
            print("")

        case 4:
            title = input("What book would you like to delete? (title) ").split()
            title_ = " ".join(title)
            value = remove_book(title_)
            if val:
                print(f"{title} deleted successfully\n")
        case _:
            print("Invalid code")
    user_response = input("Would you like to access the library again: (Yes/No) \n").lower()
    if user_response == 'yes':
        print("Alright!\n")
    else:
        print("Goodbye!\n")
        break