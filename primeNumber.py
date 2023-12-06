
# a=[1,2,4,3]

# key=2
# for index,x in enumerate(a):
#     if x==key:
#         print(index)
# prime number 
n=int(input("Enter the value of N"))

count=0

for x in range(1,n+1):
  
   if n % x==0:
      count+=1

print(count)
if count==2:
   print("Prime number")
else:
   print("not prime Number")
    