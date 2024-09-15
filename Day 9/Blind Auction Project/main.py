# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary

import art

print(art.logo)
dictionary = {}
is_finished = False

while not is_finished:
    name = input("what is yo name????")
    bid = input("what is yo bid???")
    dictionary[name] = int(bid)
    choice = input("Are there other users who want to bid?")
    if choice == "no":
        is_finished = True

max_name = ""
max_bid = 0
for key in dictionary:
    if dictionary[key] > max_bid:
        max_name = key
        max_bid = dictionary[key]

print(f"The {max_name} with sum of {max_bid} won")