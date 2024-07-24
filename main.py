from library.library import Library


def main():
    library = Library('library.json')
    IN_OR_OUT = {"+": "в наличии", "-": "выдана"}

    while True:
        print("\nВы находитесь в главном меню библиотеки:")
        print("1. Добавить книгу")
        print("2. Удалить книгу")
        print("3. Искать книгу")
        print("4. Показать все книги")
        print("5. Изменить статус книги")
        print("6. Выйти")

        choice = input("Выберите действие: ")

        if choice == '1':
            while True:
                print("Вы находитесь в меню добавления книг")
                print("1. Продолжаем добавлять книгу")
                print("0. Закончили добавлять")
                subchoice = input("Выберите действие: ")
                if subchoice == "1":
                    title = input("Введите название книги: ")
                    author = input("Введите автора книги: ")
                    year = input("Введите год издания книги: ")
                    library.add_book(title, author, year)
                elif subchoice == "0":
                    break
                else:
                    print("Некорректный выбор. Попробуйте снова.")
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
            while True:
                print("Вы находитесь в меню поиска книг")
                print("1. Продолжаем искать книгу")
                print("0. Закончили искать")
                subchoice = input("Выберите действие: ")
                if subchoice == "1":
                    criterion = input("Искать по (id/title/author/year): ").strip().lower()
                    if criterion in ('id', 'title', 'author', 'year'):
                        query = input("Введите поисковый запрос: ").strip().lower()
                        library.search_books(criterion, query)
                    else:
                        print('Нет такого критерия. Выберите из id title author year')
                elif subchoice == "0":
                    break
                else:
                    print("Некорректный выбор. Попробуйте снова.")
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
