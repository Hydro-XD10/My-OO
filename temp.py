'''n= int(input("Enter the number of seconds "))

def seconds_to_minutes(n):
    minutes=n//60
    return(minutes)
print(seconds_to_minutes(n))

def seconds_to_hours(n):
    mit=0
    mit=n//60
    hours=n//60
    return(hours)
print(seconds_to_hours(n))
  

  '''
'''
#task 2

def fun (a,b,hyp):
      if hyp:
       
         c=(a**2+b**2)**0.5
         print(f"hypot is {c}")
      else:
        c=(abs(a**2-b**2))**0.5
        print(f" other side is {'c}")
    
fun(5,3,F'alse)
   '''


'''

def word_frequency(text):
    split_text= text.split()
    frequencies = {}
    for word in split_text:
        word= word.lower()
        if word in frequencies:
            frequencies[word]+=1
        else:
            frequencies[word]=1
    return (frequencies)
        
word_frequency("string is this is")
    







def count(text):
    words=[]
    text= text.split()
    for a in text :
           a=a.lower()
           #if a not in words:
           words.append(a) 
    #print(words)
    for i in words:

        count=words.count(i)
        
        last= (f"the word {i} appear {count} times")
        print(last)




count("hi my name is abdul I like football as well horseback riding thanks for reading i apreciattet")
'''

'''
  # define the two numbwers that you want to find the common numbers between them  
def cd(number1, number2):
   # another function to find divisor
    def divisors(The_Number):
#a list that of divisors       
        divisors = []
       # loob from one to n including n
        for i in range(1, The_Number + 1):
            # check if n/i remainder is 0 so it will be can be ddvided to this number so it will ad to the list
            if The_Number % i == 0:
                divisors.append(i)
        return divisors

# check what numbers can be dvided on number from 1 to the number 
    divisors_number1 = divisors(number1)
    divisors_number2 = divisors(number2)
    common_factor_list = []
    #check if the two numbers has common factors and add them to cds list
    for d in divisors_number1:
        if d in divisors_number2:
            common_factor_list.append(d)
    
    return common_factor_list 
'''
#quuest2
'''
def find_primes(n):
    if n <= 2:
        return []
    
    is_prime = [True] * n
    is_prime[0] = is_prime[1] = False 
    
    # Implement the Sieve of Eratosthenes
    for i in range(2, int(n ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n, i):
                is_prime[j] = False
                
    primes = []
    for i in range(n):
        if is_prime[i]:
            primes.append(i)
    
    return primes 

print(find_primes(1000000))
'''
'''
def count_words(n):
   Text=n
   text_split=Text.split()
   print(text_split.count("the"))
   for word in Text:
    if word in Text
   return (n)

count_words("this is a thing that the is useless")
    

'''

'''
#this is Matrix (:
M = [
[1, 2, 3,], 
[4, 5, 6,],
[7, 8, 9,]
]
#
def digonal_sum(input_list) :
    summ=0 #set sum to 0
    for i in range (len(input_list)):#loob from 0 to 2
        summ+= input_list[i][i]# identify the index [0][0] and add it to sum then [1][1]then [2][2] etc..
    
    return(summ)# the result is summ
'''


#Q3
'''
def common_elements(list1,list2):
    common_list=[]
    for numbers1 in list1:
        if numbers1 in list2:
            common_list.append(numbers1)
            L2.remove(numbers1)
    return(common_list)
        
L1=[1,2,3,4,5,6,7,8,9,9,0]
L2=[1,2,3,4,5,6,7,8,9,9,9,0,0]
        
print(common_elements(L1, L2))
'''

'''
#Q4
def is_palindrome(word): # the function find if a word is a palindrome or not
    if word == word[::-1]: #check if the word is the same word but reversed by using slice and the step is -1
        print(f"{word} is a palindrome") #print the word is palindrome if it is pass the condition
    else:
        print(f"{word} is not a plindrome") #print that the word is not plindrome if did not pass the condition
    return(word)

is_palindrome("radar")

'''


'''
#Q6
data = [{'name': 'Alice', 'age': 25}, {'name': 'Bob', 'age': 30}, {'name': 'Charlie', 'age': 25}]
def filter_by_value(Data,Key,Value):
    matches=[]
    for dicta in Data:
        #print(dicta)
        if dicta [Key] == Value:
            matches.append(dicta)
    return(matches)
    
print(filter_by_value(data, "age", 25))
'''

    
    
   
    
   
    
   
    
  

            




'''
#Q7
L1=["a","b","c","d","e","f","g","h","i","j","k","l","h","h","e","a","a","h"]

def remove_duplicates(input_string):
    L2=[]
    for char in input_string:
        if char not in L2:
            L2.append(char)     
    return(L2)

    
print(remove_duplicates(L1))
'''
'''
#Q8
def caculate_factroial(n):
    total=1
    for z in range(1,n+1):
         total= total*z
         #print(total)
    return(total)
print(caculate_factroial(5))
'''
'''
#Q9'

nested_list=[1,[2,[3,4],5],6]
flatten_list=[]
trash=[]
list_of_numbers=["1","2","3","4","5","6","7","8","9","0"]
string=str(nested_list)
for a in string:
    trash.append(a)
for i in trash:
    if i in list_of_numbers:
        flatten_list.append(i)
print(flatten_list)







    
    
   
    
    
flatten_list(nested_list)



'''
'''
#Q10

#def merge_dicts(dict1, dict2):



def merge_dicts(dict1, dict2):
    merged_dict = {}
    for key in dict1:
        merged_dict[key] = dict1[key]  
    for key in dict2:
        merged_dict[key] = dict2[key]
    return merged_dict
dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 4, 'd': 5}
result = merge_dicts(dict1, dict2)
print(result)
'''






'''

#Task 1


def menu():  # this is a menu function that convert from decimal to binary or binary to decmial
 d=input("Write 1 for Binary to Decimal or enter 2 for Decimal to Binary or 3 to exit ")
 
  
 if d == "1":
    
            Binary=input("Write the Binary number ")
            s_bin=str(Binary) # convert the number to string. This will allow me to loob into the characters
            the_number_of_characters=len(Binary) # find the number of characters
            decmial=0 
            for index in range(0,the_number_of_characters): # this loob going to loob in range t 0 to the number of character not including the_number_of_characters
                int_digits= int(s_bin[index]) # here we take each one because the index is changing and convert it back to intger so we can do the mathmatical operation
                decmial+= int_digits*2**index  #here we gonna find the total by add on it the digit to the power of index which is loob from 0 to the_number_of_characters
            print(decmial) # print total which is the dec number
 elif d=="2": 
     decimal=int(input("enter a decimal number "))
     binary=[]# embty list to begin with
     while decimal/2 !=0: # loob as lon as decimal/2 not equal 1
         remain=decimal%2     # finding remain by the modulus "%"
         if remain ==1: # if condition if the remain is 1
              binary.append("1")# if its 1 it gonna add "1" to the list
              remain=decimal #and set a new value for the decimal (we set it to the remain to contnue the mathmatical operation of converting binary to decmial)
         else: # if something else
             binary.append("0") # it will add "0" because nothing else except "0" is avialible
         decimal=decimal//2 # and it will set new value again to the decimal to contnue
     print(binary)

menu()

'''
'''
#Task2

def Triplets(list_of_numbers):
    

    L=[] #embty list for the input
    e=[] # embty list that will contain the triplets
    summ=0
    #[a,b,c]
    for a in range(len(L)-2):# loob at range from the number of digits at L except the last 2
        for b in range(a+1,len(L)-1): # loob at range from the number after a to the last number
            for c in range(b+1, len(L)):# loob from the number agter b to the last number
                summ= L[a]+L[b]+L[c] # 
                triple = [L[a],L[b],L[c]]
                triple.sort()
                if summ ==0 and triple not in e:
                
                 e.append(triple) 
#sett= set(e)  
                print(e)          
                return(e)

L=[1,2,3,4,-1,2,-1,1]
Triplets()
'''
'''
#task3

def numberofzerosinfactorial(n):
    
    total=1
    for z in range(1,n+1):
     total= total*z
    print(total)
    
    stotal=str(total)
    aim=stotal[::-1]
    
    counter=0 
    #print(aim)
    
    
    
    
    for digit in str(aim):
        if digit=="0":  
                counter+=1
        else:
            break
    print(counter)  
    return(counter)
numberofzerosinfactorial(19)
'''

'''

#week revision workwheet2 
#task1

Total=0
n=int(input("enter a number "))
L=[500,200,100,50,20,10,5,2,1]
g=n
output=[]
for m in L:
   while n>= m:
       n=n-m
       output.append(m)
print(output)



'''


#Task2
'''
def menu():
    d=int(input("Write 1 for the even Divisor for number or Write 2 for the odd divisor for number "))  
    
    if d ==2 :
        num=int(input("Enter the number "))
        List_of_div=[]
        for ff in range(1,num):
                if num % ff ==0 :
                    if ff%2 ==0:
                        List_of_div.append(ff)
        print(List_of_div)
        
    if d ==1 :
        num=int(input("Enter the number "))
        List_of_div=[]
        for ff in range(1,num):
                if num % ff ==0 :
                    #if ff%2 ==0:
                    if ff%2==1:
                        List_of_div.append(ff)
        print(List_of_div)

    return()

menu()
'''
#Task3
'''
def find_pairs(arr):
    result = []
    
    
    for i in range(len(arr) ):  
        for j in range(i + 1, len(arr)):  
            
            result.append((arr[i], arr[j]))
    for pair in result:
        print(pair[0], pair[1])

arr = [1, 2, 3,4]
find_pairs(arr)
'''
'''

def avialible():
    
    mechanics={"Bob":1 ,"Steve":3}
    value_to_find= "none"
    for key, value in mechanics.items():
        if value == value_to_find:
            x=print(f"The mechanic avialible is {key}")
        
        else:
            closest_appointment=0
            prev=0
            for val in mechanics.items():
                if val < prev :
                    val=closest_appointment
                else:
                    val=prev
            
            
            
            
            
            
            
            
            
    return(x) 


avialible()    

'''
'''
def the_proper(n):
    common_n=[]
    for num in range(1,n):
        #print(num)
        if n%num ==0:
            common_n.append(num)
    #print(common_n)
    return(common_n)
            



def sum_of_the_proper(proper_factors):
    sum_of_factors=0
    for num in proper_factors:
        sum_of_factors+=num
    #print(sum_of_factors)
    return(sum_of_factors)

final=[]
for i in range (1,10000):
    proper_factors=the_proper(i)
    d_a=sum_of_the_proper(proper_factors)
#print(the_proper(mm))
    d_b=sum_of_the_proper(the_proper(d_a))
    if i ==d_b and d_a !=d_b:
        pair=[i,d_a]
        pair.sort()
        if pair not in final:
            final.append(pair)
print(final)
'''
        




#mock test



'''
#Q1

def first_colum_sum(matrix):
    Total= matrix[0][0]+ matrix[1][0]+matrix[2][0]
    return Total


def any_matrix_first_sum(n):
    total=0 
    for row in n: # loob through the rows
        total+=row[0] # get the first element of each row
    return (total) # return total
'''

#q2
'''
n=1
while n<=10:
    if n%3==0 :
        print(n, end="\n")
    print("-")
    n+=1 
print(".")
'''

#q4
'''
def func(a,b=2,c=3):
    if b>=2:
        for i in range(b):
            print(a*c)
    return c



func("1")
'''





#Q1 work shhet 6  FC724




class off_road_wheels:
    def __init__ (self,tire_size):
        self.tire_size= tire_size
        

class Car:
    def __init__(self,make,model,year,color,tire):
        self.make = make
        self.model =model
        self.__year= year
        self.__color=color
        self.tire= tire  

    
    def honk(self):
        return (f"the car {self.model} is honking")


    def brake(self):
        return (f"the car {self.model} is braking")
        
    def accelerate(self):
        return (f"the car {self.make} {self.model} is accelrating")

class Bicycle:
    def __init__(self,model, weight, color):
        self.model=model
        self.weight=weight
        self.color=color
        
    def accelerate(self):
        return (f"the bike {self.model} {self.color} is accelrating")




def vehicle_move(vehicle):
    return vehicle.accelerate()


car1=Car("Porsche","911",1977,"White",22)
bike=Bicycle("AA", 7, "White")
print (vehicle_move(car1))


Cars=[("Porsche","911",1977,"White",22),]
print (Cars[0])













'''
tire= off_road_wheels(27)

#car1= Car("Porsche","911",1977,"White")
car2=Car("Aston Martin","Vantage",2024,"silver",tire)

print(car2.tire.tire_size)
'''









#Work sheet 2 week 6 FC724

'''
#q1

class employees:
    def __init__(self,jop,number,age,name):
        self.jop =jop
        self.number=number
        self.age= age
        self.name=name
        
        
        
    employeez=[]
        
    def add (jop,number,age,name):
            staff=[]
            staff.append(jop)
            staff.append(number)
            staff.append(age)
            staff.append(name)
            return staff
    staff=employeez
    employeez.append(employees("cashire",1123, 12, "John"))

  '''  


#q1 exam style
















'''


#work sheet FC724 for week 7
#q2 
from math import sqrt 

print(sqrt(49))

from math import pi

print(pi*7**2)


import random as rand
print(rand.randint(1, 10))

'''

