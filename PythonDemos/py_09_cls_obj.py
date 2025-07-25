class Book:
    def __init__(self, title, author,year):
        self.title=title
        self.author=author
        self.year=year
    def dispaly_book_details(self):
        print(f"The Booke Details are {self.title}, {self.author},{self.year}")


obj1=Book("How to become an Effective Leader","Mamidi Jayansh",2043)
obj1.dispaly_book_details()