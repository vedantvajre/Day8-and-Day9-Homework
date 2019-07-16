def describe_city(city, country='America'):
    msg = (city.title() + " is in " + country.title() + ".")
    print(msg)


describe_city('Richmond')
describe_city('Brooklyn')
describe_city('Mumbai', 'India')
