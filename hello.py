
import bookSdk
from book import Book
def print_menu():
	
	print(""" choose an option:
		1.print all books
		2.add a book 
		3. update a book
		4. delete a book
		""")
while True:

	
	print_menu()
	response = int(input())
	if response ==1:
		for book in bookSdk.get_books():
			print(book)
	
	elif response ==2:
		print("name of the  book")
		title =input()
		print("number of pages ")
		pages=input()
		book=Book(title,pages)
		bookSdk.add_book(book)
	elif response ==3:
		print("Title?")
		title = input()
		print("Pages?")
		pages =input()
		bookSdk.delete_book(Book(title, pages))
		print("new title ")
		new_title=input()
		print("new pages")
		new_pages=input()
		bookSdk.update_book(book,new_title,new_pages)
	elif response == 4:
		print("delete a book ")
	else:
		print("thankyou for using our application")
		break
		
		
		
			
