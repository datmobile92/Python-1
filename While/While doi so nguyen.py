correctname = "John"

while True:
    name = input("Your Name")
if correctname == name:
    print('Its you')
elif correctname != name:
    print("Fail")
else:
    print("Nothing")