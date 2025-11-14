class Book:
    page_material = 'бумага'
    has_text = True

    def __init__(self, name, author, pages, reserved=False):
        self.name = name
        self.author = author
        self.pages = pages
        self.reserved = reserved

    def __str__(self):
        status = ", зарезервирована" if self.reserved else ""
        return (f"Название: {self.name}, Автор: {self.author}, страниц: {self.pages}, "
                f"материал: {self.page_material}{status}")


book1 = Book('Идиот', 'Достоевский', 500, reserved=True)
book2 = Book('Война и мир', 'Толстой', 3000)
book3 = Book('Судьба человека', 'Шолохов', 30)
book4 = Book('Тарас Бульба', 'Гоголь', 1500)
book5 = Book('Анна Каренина', 'Толстой', 1000)


print(book1)
print(book2)
print(book3)
print(book4)
print(book5)


class SchoolBook(Book):

    def __init__(self, name, author, pages, sub, room, task, reserved=False):
        super().__init__(name, author, pages, reserved=False)
        self.sub = sub
        self.room = room
        self.task = task

    def __str__(self):
        status = ", зарезервирована" if self.reserved else ""

        return (f"Название: {self.name} , Автор: {self.author}, страниц: {self.pages}, предмет: {self.sub}, "
                f"класс: {self.room}{status}")


school_book1 = SchoolBook('Идиот', 'Достоевский', 500, 'Литература', 8, True,
                          reserved=True)
school_book2 = SchoolBook('Война и мир', 'Толстой', 3000, 'Чтение', 10, False)
school_book3 = SchoolBook('Судьба человека', 'Шолохов', 30, 'Художественное чтение', 7,
                          True)


print(school_book1)
print(school_book2)
print(school_book3)
