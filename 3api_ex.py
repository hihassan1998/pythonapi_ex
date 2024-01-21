# import dependencies
'''pip install RandomUser
pip install requests
'''
import randomuser
import requests

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
