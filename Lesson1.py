'''
Use of function print
'''
# print('H')
# print('E')
# print('L')
# print('L')
print('O')
# l = ['H','E','L','L','O']
# word = ""
# for i in range(len(l)) :
#     print(l[i],"\n")
#
# for i in range(len(l)):
#     word = word +l[i]
# print(word)

firstName = input('My First Name is:')
lastName = input('My Last Name is :')
name = firstName + " " + lastName
homeAddress = input('Home Adress :')
phoneNumber = input('Cell Number :')
print('So, my visit card is : \n' + name)
print()

print("Address : " + homeAddress, end=" ")
print("Cell : " +phoneNumber)
