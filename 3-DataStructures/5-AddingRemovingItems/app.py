letters = ["a", "b", "c"]

# Adding
letters.append("d")  # adds "d" to the end
letters.insert(0, "-")  # adds "-" at index 0

# Remove
letters.pop()  # deletes the last item "d"
letters.pop(0)  # deletes the item at index 0
letters.remove("b")  # deletes first occurence of "b"
del letters[0:3]  # delete statement deletes a range of items
letters.clear()  # deletes all items in a list
