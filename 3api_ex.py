# list of free open sources no auth apis @ this url:
# https://mixedanalytics.com/blog/list-actually-free-open-no-auth-needed-apis/
# import dependencies
'''
pip install RandomUser
pip install requests
pip install requests
'''
import randomuser
import requests
import json
# import pandas as pd

# Load and use RandomUser API using RandomUser() Python library
def get_random_user():
    user = randomuser.RandomUser()
    return user.get_user()

# Example usage
random_user = get_random_user()
print("Random User:")
print(f"Name: {random_user['name']['first']} {random_user['name']['last']}")
print(f"Email: {random_user['email']}")
print(f"Country: {random_user['location']['country']}")
print()

#Use case (Run in  python)
''' some GET methods that we can use for the first api:
    
    <Get Methods>

get_cell()
get_city()
get_dob()
get_email()
get_first_name()
get_full_name()
get_gender()
get_id()
get_id_number()
get_id_type()
get_info()
get_last_name()
get_login_md5()
get_login_salt()
get_login_sha1()
get_login_sha256()
get_nat()
get_password()
get_phone()
get_picture()
get_postcode()
get_registered()
get_state()
get_street()
get_username()
get_zipcode()
'''
r = RandomUser()
some_list = r.generate_users(10)
name = r.get_full_name()
#For loop to generate users:
for user in some_list:
    print (user.get_full_name()," ",user.get_email())

for user in some_list:
    print(user.get_picture()) 


# a pandas dataframe with name,gender city,etc :
def get_users():
    users =[]
     
    for user in RandomUser.generate_users(10):
        users.append({"Name":user.get_full_name(),"Gender":user.get_gender(),"City":user.get_city(),"State":user.get_state(),"Email":user.get_email(), "DOB":user.get_dob(),"Picture":user.get_picture()})
      
    return pd.DataFrame(users)     

get_users() # generates a table with info
df1 = pd.DataFrame(get_users())   # data stored in the df1



# Load and use Fruityvice API using requests Python library
def get_random_fruit():
    fruityvice_api_url = "https://api.apis.guru/v2/specs/fruityvice.apis.guru/1.0.0/swagger.json"
    response = requests.get(fruityvice_api_url)
    api_spec = response.json()
    endpoints = api_spec['paths']
    random_fruit_endpoint = random.choice(list(endpoints.keys()))
    random_fruit_api_url = f"https://api.apis.guru{random_fruit_endpoint}"
    response = requests.get(random_fruit_api_url)
    random_fruit = response.json()
    return random_fruit

# Example usage
random_fruit = get_random_fruit()
print("Random Fruit:")
print(f"Name: {random_fruit['name']}")
print(f"Family: {random_fruit['family']}")
print(f"Genus: {random_fruit['genus']}")
print()

# use case 1: (Run in  python)
data = requests.get("https://fruityvice.com/api/fruit/all")
results = json.loads(data.text)
pd.DataFrame(results)
df2 = pd.json_normalize(results)
df2
#1,1
cherry = df2.loc[df2["name"] == 'Cherry'] #he family and genus of a cherry.
(cherry.iloc[0]['family']) , (cherry.iloc[0]['genus'])
#1,2
banana = df2.loc[df2["name"] == "Banana"]
print('Calories in a Banana: ',banana.iloc[0]['nutritions.calories'])



# Load and use Open-Joke-API using requests Python library
def get_random_joke():
    open_joke_api_url = "https://v2.jokeapi.dev/joke/Any"
    response = requests.get(open_joke_api_url)
    joke_data = response.json()
    if 'joke' in joke_data:
        return joke_data['joke']
    elif 'setup' in joke_data and 'delivery' in joke_data:
        return f"{joke_data['setup']} {joke_data['delivery']}"
    else:
        return "Failed to fetch joke."

# Example usage
random_joke = get_random_joke()
print("Random Joke:")
print(random_joke)

# Usecase 
data2 = requests.get("https://official-joke-api.appspot.com/jokes/ten") # loading data limited to 10 jokes
results2 = json.loads(data2.text) #retrieve the results

df3 = pd.DataFrame(results2) #Convert json data into pandas data frame. Drop the type and id columns.
df3.drop(columns=["type","id"],inplace=True)
df3