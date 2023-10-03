from Classes import Library, BookModel, JournalModel

if __name__ == "__main__":
    library = Library()

    book_1 = BookModel(title="Мастер и Маргарита", author="Михаил Булгаков", year=1967)
    book_2 = BookModel(title="Преступление и наказание", author="Федор Достоевский", year=1866)
    journal_1 = JournalModel(title="Наука и Техника", editor="Иван Петров", year=2023)

    library.add_publication(book_1)
    library.add_publication(book_2)
    library.add_publication(journal_1)

    symbol: str = "\n"

    print(f"Список публикаций в библиотеке:\n"
          f"{symbol.join([publication.publication_info() for publication in library])}")

    author_books = library.publications_by_author("Михаил Булгаков")
    print(f"\nКниги автора Михаил Булгаков:\n"
          f"{symbol.join([book.publication_info() for book in author_books])}")

    editor_journals = library.publications_by_editor("Иван Петров")
    print(f"\nЖурналы редактора 'Иван Петров':\n"
          f"{symbol.join([journal.publication_info() for journal in editor_journals])}")

    library.save_to_file("library.txt")

    library.remove_publication(book_1)

    print(f"\nСписок публикаций после удаления:\n"
          f"{symbol.join([publication.publication_info() for publication in library])}")

    library.load_from_file("library.txt")

    print("\nСписок публикаций после загрузки из файла:\n"
          f"{symbol.join([publication.publication_info() for publication in library])}")
