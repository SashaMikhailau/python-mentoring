"""### Task 6.3
Implement The Keyword encoding and decoding for latin alphabet.
The Keyword Cipher uses a Keyword to rearrange the letters in the alphabet.
Add the provided keyword at the begining of the alphabet.
A keyword is used as the key, and it determines the letter matchings of the cipher alphabet to the plain alphabet. 
Repeats of letters in the word are removed, then the cipher alphabet is generated with the keyword matching to A, B, C
etc. until the keyword is used up, whereupon the rest of the ciphertext letters are used in alphabetical order,
excluding those already used in the key.

<em> Encryption:
Keyword is "Crypto"

* A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
* C R Y P T O A B D E F G H I J K L M N Q S U V W X Z
</em>

Example:
```python
 cipher = Cipher("crypto")
 cipher.encode("Hello world")
"Btggj vjmgp"

 cipher.decode("Fjedhc dn atidsn")
"Kojima is genius"
```"""

import string


class Cipher:
    def __init__(self, keyword):
        self.keyword = keyword
        letters = ""
        for letter in keyword.lower() + string.ascii_lowercase:
            if letter not in letters:
                letters += letter
        self.letters = letters

    def decode(self, encoded):
        return Cipher.__convert_word_between_tables(self.letters, string.ascii_lowercase, encoded)

    def encode(self, decoded):
        return Cipher.__convert_word_between_tables(string.ascii_lowercase, self.letters, decoded)

    @staticmethod
    def __convert_word_between_tables(source_table, dest_table, word):
        result = ""
        for letter in word:
            if letter.lower() in source_table:
                letter_index = source_table.index(letter.lower())
                match = dest_table[letter_index]
                result += match.upper() if letter.isupper() else match
            else:
                result += letter
        return result


if __name__ == "__main__":
    cipher = Cipher("Crypto")
    assert cipher.letters == "cryptoabdefghijklmnqsuvwxz"
    assert cipher.encode("Hello world") == "Btggj vjmgp"
    assert cipher.decode("Btggj vjmgp") == "Hello world"
    assert cipher.encode("Kojima is genius") == "Fjedhc dn atidsn"
    assert cipher.decode("Fjedhc dn atidsn") == "Kojima is genius"
    print("Passed")
