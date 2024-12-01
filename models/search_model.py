from models.json_model import JSON


class Search:
    def __init__(self, book_id=None, title=None, author=None, year=None, status=None):
        self.book_id: int = book_id
        self.title: str = title
        self.author: str = author
        self.year: int = year
        self.status: bool = status
        self.loaded_data: dict = JSON().start_json()

    def search_by_id(self) -> int | bool:
        for index, book in enumerate(self.loaded_data['books']):
            if book['id'] == self.book_id:
                return index
            continue
        return False

    def search_by_argument(self, arg_key: str, arg_class: str | int | bool) -> list | bool:
        found_books = []

        def match_check():
            for index, book in enumerate(self.loaded_data['books']):
                if (arg_class in book[arg_key]) or (arg_class == book[arg_key]):
                    found_books.append(self.loaded_data['books'][index])
                continue
            return found_books

        if len(match_check()) == 0:
            return False
        else:
            return found_books

    def match_args(self, argument: str) -> str | int | bool | list:
        match argument:
            case 'id':
                return self.search_by_id()
            case 'title':
                return self.search_by_argument('title', self.title)
            case 'author':
                return self.search_by_argument('author', self.author)
            case 'year':
                return self.search_by_argument('year', self.year)
            case 'status':
                return self.search_by_argument('status', self.status)


if __name__ == '__main__':
    search = Search(status="4t3")
    result = search.match_args('status')
    print(result)
