### 그림으로 배우는 파이썬 기초 문법
### 11.4 도서 관리 프로그램

class Book:
    def __init__ (self, title, price, author, ISBN10):
        self.title = title
        self.price = price
        self.author = author
        self.ISBN10 = ISBN10
        
    def print_info(self):
        print("Title : " , self.title)
        print("Price : " , self.price)
        print("Author : ", self.author)
        print("ISBN10 : ", self.ISBN10)
        
def print_menu():
    print("1) 도서 추가 ")
    print("2) 도서 삭제")
    print("3) 도서 목록 출력")
    print("4) 종료")
    user_input = input("Menu : ")
    return int(user_input)

def add_book(book_list):
    title = input("Title : ")
    price = input("Price : ")
    author = input("Author : ")
    ISBN10 = input("ISBN10 : ")
    book = Book(title, int(price), author, ISBN10)
    book_list.append(book)
    
def print_book(book_list):
    for book in book_list:
        print("-" * 20)
        book.print_info()        
    print("-" * 20)
    
def del_book(book_list):
    ISBN10 = input("ISBN10 : ")
    
    index = None
    for i, book in enumerate(book_list):
        if book.ISBN10 == ISBN10:
            index = i
            break
        
    if index is not None:
        del book_list[index]
    

    
        
def main():
    book_list = []
    while True:
        menu = print_menu()
        if menu == 1:
            add_book(book_list)
        elif menu == 2:
            del_book(book_list)
        elif menu == 3:
            print_book(book_list)
        else:
            break
        
        
main()        
        
        
        

