![PyCharm](https://img.shields.io/badge/pycharm-143?style=for-the-badge&logo=pycharm&logoColor=black&color=black&labelColor=green) 

## Library
### Задание: Разработка системы управления библиотекой

### Описание
1. Необходимо разработать консольное приложение для управления библиотекой книг.
2. Приложение должно позволять добавлять, удалять, искать и отображать книги.
3. Каждая книга должна содержать следующие поля:
 * id (уникальный идентификатор, генерируется автоматически)
 * title (название книги)
 * author (автор книги)
 * year (год издания)
 * status (статус книги: “в наличии”, “выдана”)

### Требования
 1. Добавление книги: Пользователь вводит title, author и year, после чего книга добавляется в библиотеку с уникальным id и статусом “в наличии”.
 2. Удаление книги: Пользователь вводит id книги, которую нужно удалить.
 3. Поиск книги: Пользователь может искать книги по title, author или year.
 4. Отображение всех книг: Приложение выводит список всех книг с их id, title, author, year и status.
 5. Изменение статуса книги: Пользователь вводит id книги и новый статус (“в наличии” или “выдана”).

### Реализация:
1. Для хранения и обработки данных выбран формат json-файла.
При первом запуске программы создается json-файл с указанным именем. Пользователь вводит title, author и year, после чего книга добавляется в библиотеку с уникальным id и статусом “в наличии”. Данные записываются в словарь, который в свою очередь идексируется в обший список, который записывается в файл.
При дальнейших запусках данные загружаются из файла, а после окончания работы файл перезаписывается.
2. Удаление книги: Пользователь вводит id книги, которую нужно удалить. Происходит проверка наличия данного id книги.
После успешной проверки найденный словарь удаляется из списка.
