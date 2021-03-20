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



#Prints outputs to file for online reading
with open("results.txt", "w") as results:
    results.write("Deaths and injuries in 2019 in the US: \n")
    for key in casualties.keys():
        header = key.replace("#", "")
        header = header.strip()
        num = str(casualties[key])
        print(num)
        output = num + " " + header + "\n"
        results.write(output)