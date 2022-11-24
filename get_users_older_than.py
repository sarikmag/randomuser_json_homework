from from_json import read_json
def get_users_older_than(data:dict, age:int)->list:
    """Gets all users older than a certain age from the data
    Args:
        data (dict): The data from the JSON file
        age (int): The age to filter users by
    Returns:
        list: A list of users
    """
    users=data['users']
    l=[]
    for i in users:
        if i['age']>age:
            l+=[i['name']['first']]
    return l
print(get_users_older_than(read_json('users.json'),24))