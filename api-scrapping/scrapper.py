import requests
import json

# URL and query parameters for the API requests.
url = "https://crmapi.upgrad.com/consumer/v2/profile/list"
query_params = {
    "page" : 0,
    "size" : 10
}

# Empty list to hold and store the scrapped data
scrapped_data = []

# Initial request to the API
response = requests.get(url, params=query_params)

# Continous requests with next page untill pages run out on the API.
while len(response.json()) > 0:
    
    scrapped_data.extend(response.json())
    
    query_params["page"] += 1
    
    response = requests.get(url, params=query_params)
print("Extracted mentor data values : " + str(len(scrapped_data)))

# Attributes to be filtered out of each mentor data valued to the default value in case the attribute is NA in scrapped data.
keys_to_extract = {
    "profilePictureURL": None, 
    "firstName": "", 
    "lastName": "", 
    "email": "", 
    "countryCode":"", 
    "phoneNumber":"", 
    "linkedInUrl":"", 
    "salutation":""
}

# Filter out the attributes from the scrapped data.
for mentor in scrapped_data[:]:
    
    new_mentor_data = {}

    for key, default_val in keys_to_extract.items():
        new_mentor_data[key] = mentor.get(key, default_val)
    
    scrapped_data.remove(mentor)
    
    scrapped_data.append(new_mentor_data)
print("Final no. of values produced: " + str(len(scrapped_data)))

# Storing data to a JSON file.
data_store_file  = "../assets/data.json"

with open(data_store_file, "w") as data_file:
    json.dump(scrapped_data, data_file)

print("Data store at : " + data_store_file)
