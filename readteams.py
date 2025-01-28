import csv

teams = {}

with open('participants_2025012802507.csv') as csvfile:
    csvreader = csv.DictReader(csvfile)
    for row in csvreader:
        if not row['Age Group'] or not row['Gender'] or not row['Team'] or not row['Status'] == 'Active':
            continue
        if row['Gender'] not in teams.keys():
            teams[row['Gender']] = {}
        
        if row['Team'] not in teams[row['Gender']].keys():
            teams[row['Gender']][row['Team']] = []
        
        teams[row['Gender']][row['Team']].append(row)

rowCount = 0

for gender in teams:
    for team in teams[gender]:
        print()
        print(gender + " " + team)
        for row in teams[gender][team]:
            parentName = row['Parent/Guardian1 First Name'] + " " + row['Parent/Guardian1 Last Name']
            print(row['First Name'] + " " + row['Last Name'] + " " + row['Account Holder Email'] + " " + parentName)
            rowCount+=1

print()
print("Rows:")
print(rowCount)