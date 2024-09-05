class Book:
    def __init__(self, title):
        self.title = title
        self._contracts = []

    def contracts(self):
        # Return all contracts related to this book
        return self._contracts

    def authors(self):
        # Return all authors associated with this book
        return [contract.author for contract in self._contracts]


class Author:
    def __init__(self, name):
        self.name = name
        self._contracts = []

    def contracts(self):
        # Return all contracts related to this author
        return self._contracts

    def books(self):
        # Return all books associated with this author
        return [contract.book for contract in self._contracts]

    def sign_contract(self, book, date, royalties):
        # Create and return a new contract for the author and book
        contract = Contract(self, book, date, royalties)
        return contract

    def total_royalties(self):
        # Return the sum of all royalties from related contracts
        return sum(contract.royalties for contract in self._contracts)


class Contract:
    all = []

    def __init__(self, author, book, date, royalties):
        # Validate that the author is of type Author
        if not isinstance(author, Author):
            raise Exception("Invalid author type")
        # Validate that the book is of type Book
        if not isinstance(book, Book):
            raise Exception("Invalid book type")
        # Validate that the date is a string
        if not isinstance(date, str):
            raise Exception("Invalid date type")
        # Validate that the royalties is an integer
        if not isinstance(royalties, int):
            raise Exception("Invalid royalties type")

        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties

        # Add contract to author's and book's contract list
        author._contracts.append(self)
        book._contracts.append(self)

        # Add contract to global list of contracts
        self.__class__.all.append(self)

    @classmethod
    def contracts_by_date(cls, date):
        # Return a list of contracts filtered by date and sorted by date
        return sorted([contract for contract in cls.all if contract.date == date], key=lambda contract: contract.date)
