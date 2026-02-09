#**args

def save_user(**user):
    print(user)
#    print(user[name]) #NameError: name 'name' is not defined
    print(user["name"])
    print(user['age'])
    print(user["weight"])

#    for i in save_user: #TypeError: 'function' object is not iterable
    print(  )
    for i in user:
        print(i)

save_user(name = 'May', age = 30, weight = 78.53)