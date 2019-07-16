def city_country(city, country):
    return(city.title() + ", " + country.title())


place = city_country(country='India', city='Mumbai')
print(place)

place = city_country('Brooklyn', 'America')
print(place)

place = city_country('Richmond', 'America')
print(place)