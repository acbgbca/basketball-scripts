import csv

players = {}
coaches = {}
teamManagers = {}

with open('participants_2025012802507.csv') as csvfile:
    csvreader = csv.DictReader(csvfile)
    for row in csvreader:
        if not row['Status'] == 'Active' or not row['Team']:
            continue

        contact = {}
        if row['Parent/Guardian1 First Name']:
            contact['firstname'] = row['Parent/Guardian1 First Name'].strip()
        else:
            contact['firstname'] = row['First Name'].strip()
        
        if row['Parent/Guardian1 Last Name']:
            contact['lastname'] = row['Parent/Guardian1 Last Name'].strip()
        else:
            contact['lastname'] = row['Last Name'].strip()
        contact['email'] = row['Account Holder Email']
        contact['phone'] = row['Account Holder Mobile']

        if row['Role'] == 'Player':
            players[row['Account Holder Email']] = contact
        elif row['Role'] == 'Coach':
            coaches[row['Account Holder Email']] = contact
        elif row['Role'] == 'Team Manager':
            teamManagers[row['Account Holder Email']] = contact
        else:
            print('Unknown role ' + row['Role'])
            exit(1)
        
        # childname = row['First Name'] + " " + row['Last Name']

        # if row['Team'] not in contact['teams']:
        #     contact['teams'].append(row['Team'])
        
        # if (childname not in contact['children']):
        #     contact['children'].append(childname)

fieldnames = ['firstname', 'lastname', 'email', 'phone']

with open('players.csv', 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(players.values())

with open('coaches.csv', 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(coaches.values())

with open('teamManagers.csv', 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(teamManagers.values())

# coachesFile = csv.DictWriter(open('coaches.csv'), fieldnames=['firstname', 'lastname', 'email', 'phone'])
# coachesFile.writeheader()
# coachesFile.writerows(coaches)

# tmFile = csv.DictWriter(open('teamManagers.csv'), fieldnames=['firstname', 'lastname', 'email', 'phone'])
# tmFile.writeheader()
# tmFile.writerows(teamManagers)

# rowCount = 0
# # print()
# # print('Players')
# for contact in players.values():
#     # print(contact['firstname'] + " " + contact['lastname'] + " " + contact['email'])
#     rowCount+=1
# print()
# print("Players:")
# print(rowCount)

# rowCount = 0
# print()
# print('Coaches')
# for contact in coaches.values():
#     print(contact['firstname'] + " " + contact['lastname'] + " " + contact['email'])
#     rowCount+=1
# print()
# print("Coaches:")
# print(rowCount)

# rowCount = 0
# print()
# print('Team Managers')
# for contact in teamManagers.values():
#     print(contact['firstname'] + " " + contact['lastname'] + " " + contact['email'])
#     rowCount+=1
# print()
# print("TMs:")
# print(rowCount)