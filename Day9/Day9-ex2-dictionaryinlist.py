travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]


def add_new_country(country, visit, cities):
 
  new_country = {}

  new_country["country"] = country
  new_country["visits"] = visit
  new_country["cities"] = cities
  travel_log.append(new_country) #since it is inside list you can use append method




add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)
