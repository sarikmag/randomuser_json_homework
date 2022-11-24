from from_json import read_json
def get_users_from_country(data:dict, country:str)->list:
    """Gets all users from a country from the data
    Args:
        data (dict): The data from the JSON file
        country (str): The country to get users from
    Returns:
        list: A list of users
    """
    users=data['users']
    l=[]
    for i in users:
        if i['country']==country:
            l+=[i['name']['first']]
    return l
print(get_users_from_country(read_json('users.json'),'Norway'))