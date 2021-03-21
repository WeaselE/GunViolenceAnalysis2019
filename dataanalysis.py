import csv

casualties = {}
state_killed = {}
state_injured = {}
state_combined = {}
#counts deaths and injuries in 2019 in US
with open("GunViolence2019.csv", "r") as csvfile:
    reader = csv.DictReader(csvfile)
    for item in reader:
        #Finds state with most Killed, Injured, and both.
        if item["State"] in state_killed.keys():
            state_killed[item["State"]] += int(item["# Killed"])
        else:
            state_killed[item["State"]] = int(item["# Killed"])
        if item["State"] in state_injured.keys():
            state_injured[item["State"]] += int(item["# Injured"])
        else:
            state_injured[item["State"]] = int(item["# Injured"])
        if item["State"] in state_combined.keys():
            state_combined[item["State"]] += (int(item["# Killed"]) + int(item["# Injured"]))
        else:
            state_combined[item["State"]] = (int(item["# Killed"]) + int(item["# Injured"]))
        for key in item.keys():
            #Finds # injured and Killed, makes casualties results
            if key in casualties and key in ["# Killed", "# Injured"]:
                casualties[key] += int(item[key])
            elif key in ["# Killed", "# Injured"]:
                casualties[key] = int(item[key])
# print("DEATHS: ",state_killed)
# print("\n\n\n\n\nINJURIES: ",state_injured)
# print("\n\n\n\n\nCOMBINED: ",state_combined)
#Finds state with most deaths, injuries, and combined
max_k = ["", 0]
max_i = ["", 0]
max_c = ["", 0]
for i in state_killed:
    if max_k[1] < state_killed[i]:
        max_k = [i, state_killed[i]]
for i in state_injured:
    if max_i[1] < state_injured[i]:
        max_i = [i, state_injured[i]]
for i in state_combined:
    if max_c[1] < state_combined[i]:
        max_c = [i, state_combined[i]]

#Prints outputs to file for online reading
with open("results.txt", "w") as results:
    results.write("Casualties from Mass Shootings in 2019 in the US: \n")
    d = "Deaths: " + str(casualties["# Killed"])
    i = "Injuries: " + str(casualties["# Injured"])
    t = "Total Casualties: " + str(casualties["# Killed"] + casualties["# Injured"])
    print()
    print(d)
    print(i)
    print(t)
    results.write(d + "\n")
    results.write(i + "\n")
    results.write(t + "\n")

    results.write("\nStates with most Deaths, Injuries, and combined from Mass Shootings in 2019: \n")

    state_k = "State with most Deaths: " + str(max_k[0]) + " = " + str(max_k[1])
    state_i = "State with most Injuries: " + str(max_i[0]) + " = " + str(max_i[1])
    state_c = "State with most Combined Deaths and Injuries: " + str(max_c[0]) + " = " + str(max_c[1])
    print()
    print(state_k)
    print(state_i)
    print(state_c)
    results.write(state_k + "\n")
    results.write(state_i + "\n")
    results.write(state_c + "\n")
    print()
    # results.write("\nStates sorted by deaths: \n")
    # mx = ["", 0]
    # while True:
    #     if len(state_killed.keys()) <= 0:
    #         break
    #     for i in state_killed:
    #         if mx[1] < state_killed[i]:
    #             mx[0] = i
    #             mx[1] = state_killed[i]
    #     mx_r = str(mx[0]) + " = " + str(mx[1])
    #     print(mx_r)
    #     state_killed.pop(mx[0])
    #     mx[1] = 0
    
    #Gives source of Data analytics
    results.write("\n\n\nSource: https://www.gunviolencearchive.org/reports/mass-shooting?year=2019")