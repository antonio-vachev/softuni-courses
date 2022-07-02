all_books = input().split("&")

while True:
    command = input().split(" | ")
    if "Done" in command:
        break
    elif "Add Book" in command:
        if command[1] not in all_books:
            all_books.insert(0, command[1])
    elif "Take Book" in command:
        if command[1] in all_books:
            all_books.remove(command[1])
    elif "Swap Books" in command:
        if command[1] in all_books and command[2] in all_books:
            book_a_index = all_books.index(command[1])
            book_b_index = all_books.index(command[2])
            all_books[book_a_index], all_books[book_b_index] = all_books[book_b_index], all_books[book_a_index]
    elif "Insert Book" in command:
        if command[1] not in all_books:
            all_books.append(command[1])
    elif "Check Book" in command:
        if int(command[1]) <= len(all_books):
            print(all_books[int(command[1])])

print(", ".join([str(x) for x in all_books]))


