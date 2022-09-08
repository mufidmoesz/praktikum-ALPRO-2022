countries = {
    "indonesia": "Jakarta",
    "malaysia": "Kuala Lumpur",
    "thailand": "Bangkok",
    "singapore": "Singapore",
    "myanmar": "Naypyidaw",
    "brunei": "Bandar Seri Begawan",
    "laos": "Vientiane",
    "kamboja": "Phnom Penh",
    "timor leste": "Dili",
    "vietnam": "Hanoi",
    "filipina": "Manila",
}

while True:
    try:
        country = input("Sebutkan Negara : ") 
        print(f"Ibukota {country} adalah {countries[country.lower()]} ya teman teman")

        if country == 'stop':
            break
    except KeyError:
        print(f"{country} gak ada dalam dictionary nih")
        break
