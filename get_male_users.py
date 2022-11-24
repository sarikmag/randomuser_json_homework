from from_json import read_json
def get_male_users(data:dict)->list:
    """Gets all male users from the data
    Args:
        data (dict): The data from the JSON file
    Returns:
        list: A list of users
    """
    users=data['users']
    l=[]
    for i in users:
        if i['gender']=='male':
            l+=[i['name']['first']]
    return l
print(get_male_users(read_json('users.json')))
