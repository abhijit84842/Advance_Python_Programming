def palindrome(word):
    reversed_word=word[::-1]
    if reversed_word == word:
        return True
    else:
        return False
print(palindrome("madam"))