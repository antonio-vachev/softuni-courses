# You are given a secret message you should decipher. To do that, you need to know that in each word:
# •	the second and the last letter are switched (e.g., Holle means Hello)
# •	the first letter is replaced by its character code (e.g., 72 means H)

message = list(input().split(" "))
deciphered_word = []

for word in message:
    word_list = [x for x in word]
    first_letter = []
    for symbol in word:
        if symbol.isnumeric():
            first_letter.append(symbol)
            word_list.remove(symbol)
        else:
            break
    word_list.insert(0, chr(int("".join(first_letter))))
    word_list[1], word_list[-1] = word_list[-1], word_list[1]
    deciphered_word.append("".join(word_list))

message = " ".join(deciphered_word)
print(message)
