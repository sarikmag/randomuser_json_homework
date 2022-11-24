from from_json import read_json
def get_male_users_from_country(data:dict, country:str)->list:
    """
    Get male users from a country from the data
    Args:
        data (dict): The data from the JSON file
        country (str): The country to get users from
    Returns:

        list: A list of users
    """ 
    users=data['users']
    l=[]
    i=0
    for i in users:
        if i['country']==country and i['gender']=='male':
            l+=[i['name']['first']]
    return l
print(get_male_users_from_country((read_json('users.json')),'Norway'))   