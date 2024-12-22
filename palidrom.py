def palid(name):
    name=name.lower()
    name=''.join(char for char in name if char.isalnum())
    return name==name[::-1]
name=input("Enter Any String to check is palidrom or not ::")
if palid(name):
    print("This is Palidroma String")
else:
    print("This is not Palidroma String")
    