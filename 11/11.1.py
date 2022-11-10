class Release:
    def __init__(self, name):
        self.name = name

class Book(Release):
    def __init__(self, name, author, pages):
        super().__init__(name)
        self.author = author
        self.pages = pages
    
    def print_info(self):
        print(f"{self.name} by {self.author}, {self.pages} pages")

class Magazine(Release):
    def __init__(self, name, editor):
        super().__init__(name)
        self.editor = editor
    
    def print_info(self):
        print(f"{self.name}, editor ({self.editor})")


if __name__ == "__main__":
    aku_ankka = Magazine("Aku Ankka", "Aki Hyyppä")
    hytti_nro_6 = Book("Hytti n:o 6", "Rosa Liksom", 200)

    aku_ankka.print_info()
    hytti_nro_6.print_info()