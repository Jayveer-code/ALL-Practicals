# def palid(name):
#     name=name.lower()
#     name=''.join(char for char in name if char.isalnum())
#     return name==name[::-1]
# name=input("Enter Any String to check is palidrom or not ::")
# if palid(name):
#     print("This is Palidroma String")
# else:
#     print("This is not Palidroma String")

def is_palindrome(name):
    return name == name[::-1]

nom=input("Enter any String to check palid or not...")
print(is_palindrome(nom))   # True
   # False
    

        