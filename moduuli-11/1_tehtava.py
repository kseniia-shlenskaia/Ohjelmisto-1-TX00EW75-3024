class Publication:
    def __init__(self, name):
        self.name = name

class Book(Publication):
    def __init__(self, name, author, page_count):
        self.author = author
        self.page_count = page_count
        super().__init__(name)

    def print_information(self):
        print(f"{self.name} (author {self.author}, {self.page_count} pages).")


class Magazine(Publication):
    def __init__(self, name, chief_editor):
        self.chief_editor = chief_editor
        super().__init__(name)

    def print_information(self):
        print(f"{self.name} (chief editor {self.chief_editor}).")

magazine = Magazine('Donald Duck', 'Aki Hyyppä')
book = Book('Compartment No. 6', 'Rosa Liksom', 192)

magazine.print_information()
book.print_information()
