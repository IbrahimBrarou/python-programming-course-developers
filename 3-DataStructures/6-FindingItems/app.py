letters = ["a", "b", "c"]
letters.index("a")  # returns 0
letters.index("d")  # returns ValueError: d is not in list

if "d" in letters:
    print(letters.index("d"))

letters.count("d")  # returns 0
