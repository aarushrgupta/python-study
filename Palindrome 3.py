word = input("Type a word: ")
word2 = len(word) - 1
reversed_word = ""

while (word2 >= 0):
    reversed_word = reversed_word + word[word2]
    print(reversed_word)
    word2 = word2 -1
print("****************************")
print(word)
print("****************************")
print(reversed_word)
print("****************************")


if word == reversed_word:
    print("It is a palindrome")
else:
    print("It is not a palindrome")
