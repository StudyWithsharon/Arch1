#implemented a dictionary within a function, a dictionary is like a list but different, in a dictionary there are keys that represent values
def holiday(month, day): 
    holidays = {
        "Nieuwjaarsdag":(1, 1),
        "Drie Koningen":(1, 6),
        "Valentijnsdag":(2, 14),
        "Carnaval":(2, 19),
        "Goede Vrijdag":(4, 7),
        "1e Paasdag":(4, 9),
        "2e Paasdag":(4, 10),
        "Koningsdag":(4, 27),
        "Dag van de arbeid":(5, 1),
        "Dodenherdenking":(5, 4),
        "Bevrijdingsdag":(5, 5),
        "Moederdag":(5, 14),
        "Hemelvaartsdag":(5, 18),
        "1e Pinksterdag":(5, 28),
        "2e Pinksterdag":(5, 29),
        "Vaderdag":(6, 18),
        "Prinsjesdag":(9, 19),
        "Dierendag":(10, 4),
        "Sint Maarten":(11, 11),
        "Sinterklaas":(12, 5),
        "1e Kerstdag":(12, 25),
        "2e Kerstdag":(12, 26),
        "Ouderjaarsdag":(12, 31),
    }

  #we use a comprehension list to iterate over the dictionary it checks months and days for a match, list comprehension is basicly creating a new list from another and it can be used with dictionaries as well   
  matching_holidays = [event for event, date in holidays.items() if (month, day) == date]

    if matching_holidays:
        for holiday in matching_holidays:
            print(f"{holiday}")
    else:
        print("No holiday found on given input")

try:
    input_user = input("Please enter a date in the following format (Month: 12, Day: 5): ")
    month = int(input_user.split(",")[0].split(":")[1].strip()) #using strip to remove whitespaces and trailingspaces
    day = int(input_user.split(",")[1].split(":")[1].strip()) 
    holiday(month, day)
except ValueError:
    print("Invalid input format. Please enter the date in the format Month: x, Day: y.")
