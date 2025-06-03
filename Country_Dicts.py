country = {
    'USA': {
        'name': 'united states of america',
        'continent': 'north america',
        },
    'India': {
        'name': 'india',
        'continent': "asia",
        },
    }

for country, country_info in country.items():
    print(f"\nCountry: {country}")
    country = f"{country_info['name']}"
    continent = country_info['continent']
    
    print(f"\tCountry: {country.title()}")
    print(f"\tContinent: {continent.title()}")
