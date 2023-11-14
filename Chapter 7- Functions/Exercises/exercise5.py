#Write a function called describe_city() that accepts the name of a city and its country. The function should print a simple sentence, 

#such as Reykjavik is in Iceland. Give the parameter for the country a default value.

#Call your function for three different cities, at least one of which is not in the default country.

#function of describe_city()

def describe_city(city, country='pakistan'):
    """Describe a city."""
    msg = city.title() + " is in " + country.title() + "."
    print(msg)

describe_city('Karachi')
describe_city('Liverpool', 'England')
describe_city('Lahore')