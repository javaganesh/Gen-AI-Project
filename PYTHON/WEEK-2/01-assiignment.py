# name=input("Enter your name: ")
# print(name[0])
# name= "Ganesh"
# vcount=0
# for i in range(len(name)):
#     if name[i] == 'a' or name[i] == 'e' or name[i] == 'i' or name[i] == 'o':
#         vcount+=1
#
# print(vcount)

#reverse string
#print("reverse string ",name[-1],name[-2],name[-3],name[-4],name[-5],name[-6])
# size =len(name)
# for i in range(0,size,-1):
#     print(name[i])


name = input("Enter your name: ")

print("Upper :", name.upper())
print("Lower :", name.lower())
print("Length:", len(name))
print("Reverse:", name[::-1])