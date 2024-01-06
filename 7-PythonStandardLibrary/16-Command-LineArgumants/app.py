import sys

if len(sys.argv) == 1:
    print("Usage: python app.py <password>")
else:
    password = sys.argv[1]
    print("Password", password)
