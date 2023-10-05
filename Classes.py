from pydantic import BaseModel


class PublicationModel(BaseModel):
    """
    Модель для публикации
    :param title: Принимает название
    :param year: Принимает год
    :return: Возвращает информацию о публикации
    """
    
    title: str
    year: int

    def __str__(self):
        return f"Название: {self.title}, Год выпуска: {self.year}"


class BookModel(PublicationModel):
    """
    Модель для книги (унаследована от базового класса PublicationModel)
    :param author: Принимает имя автора
    :return: Возвращает информацию о книге
    """

    author: str

    def publication_info(self):
        return f"Автор: {self.author}, {super().__str__()}"


class JournalModel(PublicationModel):
    """
    Модель для журнала (унаследована от базового класса PublicationModel)
    :param editor: Принимает имя редактора
    :return: Возвращает информацию о журнале
    """

    editor: str

    def publication_info(self):
        return f"Редактор: {self.editor}, {super().__str__()}"


class Library:
    """
    Класс "Книга" содержит информацию о книге, включая название, автора и год издания.
    """

    # Конструктор класса
    def __init__(self):
        self._publications: list[PublicationModel] = []

    # Итератор для класса
    def __iter__(self) -> list[PublicationModel]:
        return iter(self._publications)

    def add_publication(self, publication: PublicationModel):
        """
        Добавляет публикацию в список
        :param publication: Принимает публикацию
        """

        self._publications.append(publication)

    def remove_publication(self, publication: PublicationModel):
        # Проверяет наличие публикации в списке и удаляет её, или выводит сообщение о неудаче
        if publication in self._publications:
            self._publications.remove(publication)

        else:
            print(f"Публикация {publication.title} не найдена в библиотеке")

    # Метод для поиска публикаций по автору
    def publications_by_author(self, author: str) -> list[PublicationModel]:
        """
        Возвращает список публикаций, удовлетворяющих заданному автору
        :param author: Принимает имя автора
        :return: Возвращает список публикаций
        """

        return [publication for publication in self._publications if
                isinstance(publication, BookModel) and publication.author == author]

    def publications_by_editor(self, editor: str) -> list[PublicationModel]:
        # Возвращает список публикаций, удовлетворяющих заданному редактору
        return [publication for publication in self._publications if
                isinstance(publication, JournalModel) and publication.editor == editor]

    def save_to_file(self, filename: str):
        """
        Сохраняет информацию о публикациях в файл
        :param filename: Принимает имя файла
        """

        with open(filename, "w") as file:
            for publication in self._publications:
                if isinstance(publication, BookModel):
                    file.write(f"Книга,{publication.title},{publication.author},{publication.year}\n")
                elif isinstance(publication, JournalModel):
                    file.write(f"Журнал,{publication.title},{publication.editor},{publication.year}\n")

    def load_from_file(self, filename: str) -> list[PublicationModel]:
        """
        Загружает информацию о публикациях из файла
        :param filename: Принимает имя файла
        :return: Возвращает список публикаций
        """

        self._publications = []

        with open(filename, "r") as file:
            lines = file.readlines()

            for line in lines:
                parts = line.strip().split(',')
                if len(parts) >= 3:
                    if parts[0] == "Книга":
                        title, author, year = parts[1], parts[2], int(parts[3])
                        book = BookModel(title=title, author=author, year=year)
                        self.add_publication(book)
                    elif parts[0] == "Журнал":
                        title, editor, year = parts[1], parts[2], int(parts[3])
                        journal = JournalModel(title=title, editor=editor, year=year)
                        self.add_publication(journal)
