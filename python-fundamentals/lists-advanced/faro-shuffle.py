# A faro shuffle is a method for shuffling a deck of cards, in which the deck is split exactly in half. Then the
# cards in the two halves are perfectly interleaved, such that the original bottom card is still on the bottom and
# the original top card is still on top. For example, faro shuffling the list ['ace', 'two', 'three', 'four', 'five',
# 'six'] once, gives ['ace', 'four', 'two', 'five', 'three', 'six'] Write a program that receives a single string (
# cards separated by space) and on the second line receives a count of faro shuffles that should be made. Print the
# state of the deck after the shuffle. Note: The length of the deck of cards will always be an even number.

# Example of input:
# a b c d e f g h
# 5

cards = input().split(" ")
shuffles = int(input())

index_a = int(len(cards)/2)

for shuffle in range(shuffles):
    half_a = cards[:index_a]
    half_b = cards[index_a:]
    cards = []
    for index, card in enumerate(half_a):
        cards.append(card)
        cards.append(half_b[index])

print(cards)

