# UPDATE DICTIONARIES AND LISTS

x = [ [5,2,3], [10,8,9] ] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

# 1
x[1][0] = 15
# print(x)

# 2
students[0]["last_name"] = "Bryant"
# print(students[0])

# 3
sports_directory['soccer'][0] = "Andres"
# print(sports_directory['soccer'])

# 4
z[0]['y'] = 30
# print(z)

# ITERATE LISTS OF DICTIONARIES

def iterateDictionary(some_list):
    for index in range(len(some_list)):
        # print(index)
        for key in some_list[index]:
            # print(key)
            print(key + " - " + some_list[index][key])

def itemsIterate(some_list):
    for index in range(len(some_list)):
        for key,value in some_list[index].items():
            print(key + " - " + value)

students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

iterateDictionary(students) 

itemsIterate(students)


# should output: (it's okay if each key-value pair ends up on 2 separate lines;
# bonus to get them to appear exactly as below!)
# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel

# GET VALUS FROM A LIST OF DICTIONARIES

def iterateDictionary2(key_name, some_list):
    for index in range(len(some_list)):
        print(some_list[index][key_name])

iterateDictionary2('first_name', students)

iterateDictionary2('last_name', students)

# Iterate through a dict with list values

def printInfo(some_dict):
    for keys in some_dict:
        print(len(some_dict[keys]) , keys.upper())
        for items in some_dict[keys]:
            print(items)
        print("")

dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
printInfo(dojo)

# output:
# 7 LOCATIONS
# San Jose
# Seattle
# Dallas
# Chicago
# Tulsa
# DC
# Burbank
    
# 8 INSTRUCTORS
# Michael
# Amy
# Eduardo
# Josh
# Graham
# Patrick
# Minh
# Devon
