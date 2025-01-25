cities = {
    "Nariobi": {
        "country": "Kenya",
        "population": "2000000",
        "fun fact": "Only city with a National park",
    },
    "Paris": {
        "country": "France",
        "population": "6000000",
        "fun fact": "Famous for the Eifel Tower",
    },
    "Kampala": {
        "country": "Uganda",
        "population": "20000000",
        "fun fact": "Capital of Uganda",
    },
}

for city, details in cities.items():
    print(
        f"City - {city} : \ncountry - {details["country"]}\nPopulation - {details["population"]}\nFun fact - {details["fun fact"]}\n"
    )
