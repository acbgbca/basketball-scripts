# Not used, added as a reference

import adal
import requests
import json
import csv

tenant = "x"
client_id = "y"
client_secret = "z"

authority = "https://login.microsoftonline.com/" + tenant
RESOURCE = "https://graph.microsoft.com"

context = adal.AuthenticationContext(authority)

# Use this for Client Credentials
token = context.acquire_token_with_client_credentials(
   RESOURCE,
   client_id,
   client_secret
   )

graph_api_endpoint = 'https://graph.microsoft.com/v1.0{0}'

# Create contact folder
# create_url = graph_api_endpoint.format('/users/xyz/contactFolders')
# headers = { 
# 'User-Agent' : 'python_tutorial/1.0',
# 'Authorization' : 'Bearer {0}'.format(token["accessToken"]),
# 'Accept' : 'application/json',
# 'Content-Type' : 'application/json'
# }

# response = requests.post(url = create_url, headers = headers, json = {"displayName": "testFolder"}).json()
# print (json.dumps(response, indent=2))

# request_url = graph_api_endpoint.format('/users/xyz/contactFolders')
# headers = { 
# 'User-Agent' : 'python_tutorial/1.0',
# 'Authorization' : 'Bearer {0}'.format(token["accessToken"]),
# 'Accept' : 'application/json',
# 'Content-Type' : 'application/json'
# }

# response = requests.get(url = request_url, headers = headers).json()
# print (json.dumps(response, indent=2))


teams = {}

with open('participants_2024012293609.csv') as csvfile:
    csvreader = csv.DictReader(csvfile)
    for row in csvreader:
        if not row['Age Group'] or not row['Gender'] or not row['Team']:
            continue
        if row['Gender'] not in teams.keys():
            teams[row['Gender']] = {}
        
        if row['Team'] not in teams[row['Gender']].keys():
            teams[row['Gender']][row['Team']] = []
        
        teams[row['Gender']][row['Team']].append(row)

for gender in teams:
    # Create gender folder
    create_url = graph_api_endpoint.format('/users/xyz/contactFolders')
    headers = { 
        'User-Agent' : 'python_tutorial/1.0',
        'Authorization' : 'Bearer {0}'.format(token["accessToken"]),
        'Accept' : 'application/json',
        'Content-Type' : 'application/json'
    }

    response = requests.post(url = create_url, headers = headers, json = {"displayName": gender}).json()
    print (json.dumps(response, indent=2))
    genderFolderId = response['id']
    for team in teams[gender]:
        # Create team folder
        response = requests.post(url = create_url, headers = headers, json = {"displayName": team, "parentFolderId": genderFolderId}).json()
        print (json.dumps(response, indent=2))
        teamFolderId = response['id']
        for row in teams[gender][team]:
            # Add contact to team folder
            createContactUrl = graph_api_endpoint.format('/users/xyz/contactFolders/' + teamFolderId + '/contacts')
            parentName = row['Parent/Guardian1 First Name'] + " " + row['Parent/Guardian1 Last Name']
            request = {
                "givenName": row['First Name'],
                "surname": row['Last Name'],
                "emailAddresses": [
                    {
                        "address": row['Account Holder Email'],
                        "name": row['First Name'] + " " + row['Last Name']
                    }
                ]}
            response = requests.post(url = createContactUrl, headers = headers, json = request).json()
            print (json.dumps(response, indent=2))
        break
    break