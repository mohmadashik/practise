
# def token_required(func):
#     @wraps(func)
#     def validate_token(*args,**kwargs):
#         token = args[0]
#         if token == 'valid':
#             func(*args,**kwarrgs):
#         else:
#             return 'Un Authorized'
#     return validate_token

# @app.route('/home')
# @token_required
# def home():
#     return 'home page'

import os 

def hash_func(data):
    return len(data)

path  ='test'
all_files = os.listdir(path)
duplicates  = {}
for file in all_files:
    with open(file) as f:
        data = f.read()
        hash_key = hash_func(data)
        if hash_key in duplicates:
            duplicates[hash_key] +=1
        else:

            duplicates[hash_key] =1

for file_data,repitions in duplicates.items():
    if repitions >1:
        print ('duplicate')



