""" Task 5.2
Implement a function which search for most common words in the file.
Use `data/lorem_ipsum.txt` file as a example.

```python
def most_common_words(filepath, number_of_words=3):
    pass

print(most_common_words('lorem_ipsum.txt'))
['donec', 'etiam', 'aliquam']


> NOTE: Remember about dots, commas, capital letters etc.
"""


def find_common_words(filepath, number_of_words=3):
    file = open(filepath)
    content = file.read()
    file.close()

    if not content:
        return

    words = content.replace(".", " ").replace(",", " ").split()
    words = [word.strip().lower() for word in words]
    word_count = count_words(words)
    items = [(k, v) for k, v in word_count.items()]
    items.sort(key=lambda item: item[1], reverse=True)
    items = items[:number_of_words]
    result = [word[0] for word in items]
    return result


def count_words(words):
    word_count = {}
    for word in words:
        current_word_count = word_count.get(word)
        if current_word_count:
            word_count[word] = current_word_count + 1
        else:
            word_count[word] = 1
    return word_count


print(find_common_words("data/lorem_ipsum.txt", 3))
