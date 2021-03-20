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

#sorts states by deaths + injuries



#Prints outputs to file for online reading
with open("results.txt", "w") as results:
    results.write("Casualties from Mass Shootings in 2019 in the US: \n")
    d = "Deaths: " + str(casualties["# Killed"])
    i = "Injuries: " + str(casualties["# Injured"])
    t = "Total Casualties: " + str(casualties["# Killed"] + casualties["# Injured"])
    print(d)
    print(i)
    print(t)
    results.write(d + "\n")
    results.write(i + "\n")
    results.write(t + "\n")