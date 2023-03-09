# Write a Program which input a list of n number and search for an element from this given list. 

L1=[]
n=int(input("How many values to enter:"))  
for i in range(n):  
    numb=int(input("Enter elements:")) 
L1.append(numb)  
ele=int(input("Enter an element to search for:") )
print("Given List:",L1)  
found=False  
for x in L1: 
    if x==ele:  
        pos=L1.index(ele)+1  
print("The element is found on:",pos,"position in the list")  
found=True  
if found==False:  
    print("The element is not found") 
