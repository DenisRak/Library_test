import json


class Library:

    def __init__(self, filename):
        """Инициализация объекта."""
        self.filename = filename
        self.books = self.load_data()

    def load_data(self):
        """Загрузка данных из файла."""
        try:
            with open(self.filename, 'r', encoding='utf-8') as file:
                return json.load(file)
        except FileNotFoundError:
            self.save_data([])  # Если файл не найден, создаем его
            return []

    def save_data(self, data: list):
        """Сохранение данных в файл."""
        with open(self.filename, 'w') as file:
            json.dump(data, file, indent=4, ensure_ascii=False)
            
    def generate_id(self):
        """Генерация ID"""
        if self.books:
            return max(book['id'] for book in self.books) + 1
        return 1

    def add_book(self, title: str, author: str, year: str) -> dict:
        """Добавление книги в библиотеку"""
        new_book = {
            'id': self.generate_id(),
            'title': title,
            'author': author,
            'year': year,
            'status': 'в наличии'
        }
        self.books.append(new_book)
        self.save_data(self.books)
        print(f"Книга '{title}' добавлена в библиотеку.")
        return new_book

    def delete_book(self, book_id: int) -> bool:
        """Удаление книги по ID"""
        book_to_delete = next((filter(lambda x: x['id'] == book_id, self.books)))
        self.books.remove(book_to_delete)
        self.save_data(self.books)
        print(f"Книга с ID {book_id} удалена.")
        return True


    def search_books(self, criterion: str, query: str) -> list:
        """Поиск книги по заданному критерию"""
        results = [book for book in self.books if query.lower() in str(book[criterion]).lower()]
        if results:
            for book in results:
                self.print_book(book)
        else:
            print("Книги не найдены.")
        return results

    def display_books(self) -> list:
        """Вывод всех книг библиотеки"""
        if self.books:
            for book in self.books:
                self.print_book(book)
        else:
            print("В библиотеке нет книг.")
        return self.books

    def change_status(self, book_id: int, new_status: str) -> str:
        """Изменение статуса книги"""
        book_to_change = next((book for book in self.books if book['id'] == book_id))
        book_to_change['status'] = new_status
        self.save_data(self.books)
        print(f"Статус книги с ID {book_id} изменен на '{new_status}'.")
        return new_status


    @staticmethod
    def print_book(book):
        """Вывод информации об одной книге"""
        print(f"ID: {book['id']}, Название: {book['title']}, Автор: {book['author']}, Год: {book['year']}, Статус: {book['status']}")

    def check_id(self, book_id):
        list_id = (el['id'] for el in self.books)
        return book_id in list_id

def main():
    library = Library('library.json')
    IN_OR_OUT = {"+": "в наличии", "-": "выдана"}

    while True:
        print("\nМеню библиотеки:")
        print("1. Добавить книгу")
        print("2. Удалить книгу")
        print("3. Искать книгу")
        print("4. Показать все книги")
        print("5. Изменить статус книги")
        print("6. Выйти")

        choice = input("Выберите действие: ")

        if choice == '1':
            title = input("Введите название книги: ")
            author = input("Введите автора книги: ")
            year = input("Введите год издания книги: ")
            library.add_book(title, author, year)
        elif choice == '2':
            try:
                book_id = int(input("Введите ID книги для удаления: "))
                if library.check_id(book_id):
                    library.delete_book(book_id)
                else:
                    print(f"Книга с ID {book_id} не найдена.")
            except ValueError:
                print("ID должен быть числом")
        elif choice == '3':
            criterion = input("Искать по (id/title/author/year): ").strip().lower()
            if criterion in ('id', 'title', 'author', 'year'):
                query = input("Введите поисковый запрос: ").strip().lower()
                library.search_books(criterion, query)
            else:
                print('Нет такого критерия. Выберите из id title author year')
        elif choice == '4':
            library.display_books()
        elif choice == '5':
            try:
                book_id = int(input("Введите ID книги для изменения статуса: "))
                if library.check_id(book_id):
                    new_status = IN_OR_OUT.get(input("Введите новый статус (в наличии - '+'/выдана - '-'): "))
                    if new_status:
                        library.change_status(book_id, new_status)
                    else:
                        print("Некорректный статус. Попробуйте снова.")
                else:
                    print(f"Книга с ID {book_id} не найдена.")
            except ValueError:
                print("ID должен быть числом")
        elif choice == '6':
            break
        else:
            print("Некорректный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()
