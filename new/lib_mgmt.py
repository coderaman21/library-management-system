# .................library management system...................

class library:
    dict={} # class variable
    books=[] # class variable
    def __init__(self,books_list,lib_name):
        self.books_list=books_list
        self.lib_name=lib_name
        library.books=self.books_list[:] # a copy of all books we have in library
        
    def dispay_books(self):
        return self.books_list

    def add_book(self,book):
        self.books_list.append(book)
        library.books.append(book) # adds every new book to the copy of all books we have in library 
        print('Succesfully added')
    
    def lend_book(self,book):
        if book in self.books_list:
            user_name=input(f'You have requested to lend \"{book}\" book,for that kindlly Enter your name :\n') 
            self.books_list.remove(book)
            library.dict[book]=user_name
            print(f'Congrats,you now have \"{book}\" .')
        else :
            if book in library.books:
                print(f'Book \"{book}\" is not available right now. {library.dict[book]} have it.\n')
            else :
                print(f'Sorry, we don\'t have \"{book}\" book.\n')
    
    def return_book(self,book):
        self.books_list.append(book)
        print(f'You succesfully returned \"{book}\".')

ls=['gunaho ka devta','up 65','musafir cafe','nirmala','godan','chaurasi','gaban']
hlib=library(ls,'harry\'s library')

if __name__=='__main__':
    print('''Operations:
    1.display all available books
    2.lend a book
    3.add a book
    4.return book
    5.exit \n''')
    while True:
        try:
            query=int(input('Enter your choice : '))
            if query==1:
                print(f'{hlib.dispay_books()}\n')
            elif query==2:
                book_name=input('Enter the name of book :\n')
                hlib.lend_book(book_name)
            elif query==3:
                book_name=input('Enter the name of book :\n')
                hlib.add_book(book_name)
            elif query==4:
                book_name=input('Enter the name of book :\n')
                hlib.return_book(book_name)
            elif query==5:
                exit()
            else:
                print('Wrong choice.')
        except ValueError:
            print('Your choice should be in numbers only.')
