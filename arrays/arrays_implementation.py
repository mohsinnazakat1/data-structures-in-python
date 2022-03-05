# Some tasks realted to Array and their big O
# ---------------------------------------------

# Accesing any index in array is a task of O(1)
# Printing all elements of array is a task of O(n)
# Inserting elements at a certain index is a task of O(n)
# Deleting elements from a certain index is a task of O(n)

# Some information about arrays 
# --------------------------------

# Array in python (that are acutally lists) are dynamic 
# In dynamic arrays we have grey memory areas that can be used when the size of data exceeds 
# Assignment of those grey memory areas follows the patter of geomatric progression *2 
# In python list can store multiple datatypes 

#Exercise code related to lists 

myList = [
	{
		'January':2200,
		'February': 2350,
        'March' : 2600,
        'April': 2130,
        'May': 2190
	}
]

#printing expensis of all the monthss
print(myList[0]['January'])
print(myList[0]['February'])
print(myList[0]['March'])
print(myList[0]['April'])
print(myList[0]['May'])

#1. In Feb, how many dollars you spent extra compare to January?
print("1. In Feb, how many dollars you spent extra compare to January?\n{value}".format(value = myList[0]['February'] -myList[0]['January'] ))

#2. Find out your total expense in first quarter (first three months) of the year.
print("2. Find out your total expense in first quarter (first three months) of the year.\n{value}".format(value = myList[0]['February'] +myList[0]['January']+myList[0]['January'] ))


#3. Find out if you spent exactly 2000 dollars in any month
print("3. Find out if you spent exactly 2000 dollars in any month\n")
for key in myList[0]:
    if myList[0][key] == 2000:
        print (key)

#4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
print("4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list\n")
myList[0]['June'] = 1980
print(myList[0])

#5. You returned an item that you bought in a month of April and got a refund of 200$. Make a correction to your monthly expense list based on this
print("5. You returned an item that you bought in a month of April and got a refund of 200$. Make a correction to your monthly expense list based on this\n")
myList[0]['April'] -= 200
print(myList[0])



