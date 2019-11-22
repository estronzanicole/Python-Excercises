priority_index = {
  (1, 'premier'): [1, 34, 12],
  (1, 'mvp'): [84, 22, 24],
  (2, 'standard'): [93, 81, 3],
}

print(list(priority_index.keys()))

# first package is 1 and then because it's a tuple you can put 1 more
# combining all 3 data structions (tulple as a key)
# allows you to add meta data
# have multiple items

# to print convert to list
# call the priority index
# call keys//////////////////////////////////////////////////////
users = ["kristnine", 'Tiffany', 'Jordan', 'Leann']  #list of users-database query

print(users)

users.remove('Jordan') #remove function takes an arguement- the value we are removing

print(users)

popped_user = users.pop()  #pop returns the last item  of the list so you can use it!
                           #and stores in the variable
print(popped_user)
print(users)

del users[0]
print(users)

#working with list that you know the value -remove is perfect to use-searches entire collect_incoming_data(
#pop is if you want the very last element in the list 
#del or delete only use if you know the list and you are deleting
