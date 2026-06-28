n=int(input("Enter a number of elements : "))
numbers=[]

for i in range(n):
  num=float(input(f"Enter the number {i+1} : "))
  numbers.append(num)

avg=sum(numbers)/n
print("Average = ", avg) 
