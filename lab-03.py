#program1
for i in range (1,11):
     print(i)
     
#program2
n = int(input("Enter a number: "))
sum = 0
i = 1
while i <= n:
       sum +=i
       i +=1
       
print("Sum:", sum)
    
#program3
num = int(input("Enter a number: "))
for i in range (1,11):
    print(num,'x',i,'=',num*i)
    
#program4
n = int(input("Enter a number: "))
factorial = 1
for i in range (1,n+1):
    factorial *=i
    
print("Factorial:", factorial)

#program5
for i in ramge (1,51):
    if i%2 ==0:
        print(i)
        
        
#program6
n = int(input("Enter a number: "))
reverse = 0
while n>0:
    digit  = n%10
    reverse = digit*10+reverse
    n=n//10
print("Reverse:", reverse)

#program7
a=0
b=1

n = int(input("Enter a number: "))
for i in range (1, n+1):
    print (a,endl" ")
    a,b=b,a+b
    
#program8
n = int(input("Enter a number: "))
for i in range (1, n+1):
    for j in range (1,i+1):
        print("*", end=" ")
        
#program9
n = int(input("Enter a number: "))
for i in range (2,n)
    if n%i==0:
       print(n,"is not a prime number")
       break
else:
    print(n,"is a prime number")        
    
    
#program10
n = int(input("Enter a number: "))
sum = 0 
while n>0:
    digit = n%10
    sum +=digit
    n = n//10
print("Sum of digits:", sum)

#program11
count =0
ch = input("Enter a character: ")
vowels = "aeiouAEIOU"
for i in ch:
    if i in vowels:
        count +=1
print("Number of vowels:", count)

#program12
ch = input("Enter a string: ")
reverse = " "
for i in ch:
    reverse = i + reverse
print("Reverse string:", reverse)

#program13
a = {1,2,3,4,5}
for i in a:
    print(i)
    
#program14
n = int(input("Enter a number: "))
for i in range (1, 101):
    if n%3==0:
        print("is divisible by 3")
    else:
         print(n,"is not divisible by 3"):
              
#program15
n = int(input("Enter a number: "))
for i in range (1, n+1):
    if n%7==0:
        break
    else:
        print(n,"is not divisible by 7")
    