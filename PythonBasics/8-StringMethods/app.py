course = " Python Programming"
print(course.upper())  # make all letters capital
print(course.lower())  # make all letters lowaercase
print(course.title())  # the first letter in the first word will be capitalised
print(course.strip())  # removes any spaces from the beginning or the end
print(course.rstrip())  # removes any spaces from the end
print(course.lstrip())  # removes any spaces from the beginning
# wil find the starting index of Pro, it will be -1 if nothing is found, it is case sensitive
print(course.find("Pro"))

print(course.replace("P", "-"))  # will replace all capital Ps with -

# will return True if course has Programming word
print("Programming" in course)
print("Programming" not in course)
