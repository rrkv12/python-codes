def only_upp(list2):
    upper=[]
    for i in list2:
        if i.isupper():
            upper.append(i)
    return upper
def cap_all(list2): #Returns the capital letters from a list
    cap=[]
    for i in list2:
        cap.append(i.capitalize())
    return cap
def delete_pop(list2):
    x=list2.pop(1) #if you know the index of the element you want you can use pop.
    #It removes the item from the list and store it in the variable you given.
    #pop modifies the list and returns the element that was removed. If you don’t provide an
    #index, it deletes and returns the last element.
    print(list2)
    return x
def delete_del(list2):
    del list2[1] #If you don’t need the removed value, you can use the del operator:
    return list2
def only_small(list2): #Returns the small letters from a list
    small=[]
    for i in list2:
        if i.isupper()==False:
            small.append(i)
    return small
def pages(s,t): #Returns all the odd page numbers from a range of page numbers
    op=[]
    for i in range(s,t):
        if i%2 != 0:
            op.append(i)
    return op
def acronyms(): #Create Acronyms
    user_input=str(input("Enter a phrase: ")) # Enter a phrase
    a="" # Initialize an empty string
    text = user_input.split() #Spliting the given string and converting it into a list
    for i in text: #Initialize the loop to get the initial letter of each string
        a=a+str(i[0]).upper() #Capitalize them
    return a

def sort_sent(lis):
    delimeter=' '
    e=delimeter.join(lis)
    return e
#List Exercises
#Excercise 1
def nested_sum(t):
    total=0
    for nested in t:
        total+= sum(nested)
    return total
#Excercise 2

def cumsum(x):
    c=[]
    total=0
    for i in x:
        total += i
        c.append(total)
    return c

#Excercise 3

def middle(y):
    return y[1:-1]

#Excercise 4

def chop(p):
    del p[0]
    del p[-1]
    return p #If function returns nothing, don't use 'return'
#Excercise 5
def is_sorted(b):
    return b == sorted(b)

#Excercise 6
def is_anagram(word1,word2):
    return sorted(word1) == sorted(word2)

#Excercise 7

def has_duplicates(word1):
    t=list(word1)
    t.sort()
    for i in range(len(t)-1):
        if t[i] == t[i+1]:
            return True
    return False
    




    
            

    
