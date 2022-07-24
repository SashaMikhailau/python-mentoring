"""### Task 6.7

Implement a Pagination class helpful to arrange text on pages and list content on given page. 
The class should take in a text and a positive integer which indicate how many symbols will be allowed per each page (take spaces into account as well).
You need to be able to get the amount of whole symbols in text, get a number of pages that came out and method that accepts the page number and return quantity of symbols on this page.
If the provided number of the page is missing print the warning message "Invalid index. Page is missing". If you're familliar with using of Excpetions in Python display the error message in this way.
Pages indexing starts with 0.

Example:
```python
 pages = Pagination('Your beautiful text', 5)
 pages.page_count
4
 pages.item_count
19

 pages.count_items_on_page(0)
5
 pages.count_items_on_page(3)
4
 pages.count_items_on_page(4)
Exception: Invalid index. Page is missing.
```
Optional: implement searching/filtering pages by symblos/words and displaying pages with all the symbols on it.
If you're querying by symbol that appears on many pages or if you are querying by the word that is splitted in two return an array of all the occurences.

Example:
```python
 pages.find_page('Your')
[0]
 pages.find_page('e')
[1, 3]
 pages.find_page('beautiful')
[1, 2]
 pages.find_page('great')
Exception: 'great' is missing on the pages
 pages.display_page(0)
'Your '
```"""
import math


class Pagination:
    def __init__(self, text, symbols_per_page):
        self.text = text
        self.symbols_per_page = symbols_per_page
        self.page_count = math.ceil(len(text) / symbols_per_page)

    def count_items_on_page(self, page_index):
        self.__validate_page_index(page_index)
        if page_index == self.page_count - 1:
            return len(self.text) % self.symbols_per_page
        return self.symbols_per_page

    def find_page(self, search_term):
        search_term_length = len(search_term)
        start_index = 0
        max_index = len(self.text) - search_term_length
        result = set()
        while start_index in range(0, max_index + 1):
            start_index = self.text.find(search_term, start_index)
            if start_index >= 0:
                result.add(self.get_page_by_char_index(start_index))
                end_index = start_index + search_term_length - 1
                result.add(self.get_page_by_char_index(end_index))
                start_index = end_index + 1
        if len(result) == 0:
            raise LookupError(f"'{search_term}' is missing on the pages")
        return sorted(list(result))

    def get_page_by_char_index(self, char_index):
        return char_index // self.symbols_per_page

    def __validate_page_index(self, page_index):
        if page_index not in range(0, self.page_count):
            raise AttributeError("Invalid index. Page is missing.")

    def display_page(self, page_index):
        items_on_page = self.count_items_on_page(page_index)
        start_index = page_index * self.symbols_per_page
        return self.text[start_index: start_index + items_on_page]


if __name__ == "__main__":
    pages = Pagination('Your beautiful text', 5)
    assert pages.page_count == 4
    assert pages.count_items_on_page(0) == 5
    assert pages.count_items_on_page(3) == 4
    # pages.count_items_on_page(4) throws error
    assert pages.find_page('Your') == [0]
    assert pages.find_page('e') == [1, 3]
    assert pages.find_page('beautiful') == [1, 2]
    # assert pages.find_page('great') throws exception
    assert pages.display_page(0) == 'Your '
    assert pages.display_page(3) == 'text'
    # assert pages.display_page(4) throws exception

    print("Passed")
