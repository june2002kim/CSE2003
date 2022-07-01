#Palindrome
def Palindrome(x):
    if len(x)<=1:
        return True
    if x[0]!=x[len(x)-1]:
        return False
    return Palindrome(x[1:-1])

x=input("Input: ")
if Palindrome(x):
    print("Palindrome!")
else:
    print("Not palindrome.")
