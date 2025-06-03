Country_0 = {'Name': 'USA', 'Continent': 'North America'}
Country_1 = {'Name': 'India', 'Continent': 'Asia'}
Country_2 = {'Name': 'France', 'Continent': 'Europe'}

# This is a list that hase the same three dictionaries
Countries = [Country_0, Country_1, Country_2]

# This is printing all three dictionaries in the list
for Country in Countries:
    print(Country)
    
print("----------------------------------------------------")

print(Countries[1]["Name"])

