import csv

casualties = {}

#counts deaths and injuries in 2019 in US
with open("GunViolence2019.csv", "r") as csvfile:
    reader = csv.DictReader(csvfile)
    for item in reader:
        for key in item.keys():
            if key in casualties and key not in ["Incident ID", "Incident Date", "State", "City Or County", "Address", "Operations"]:
                casualties[key] += int(item[key])
            elif key not in ["Incident ID", "Incident Date", "State", "City Or County", "Address", "Operations"]:
                casualties[key] = int(item[key])
    print(casualties)

#sorts states by deaths + injuries