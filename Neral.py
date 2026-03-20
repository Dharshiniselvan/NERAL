#INTRODUCTION
print("Welcome to Neral!A beginner-friendly crop recommendation tool.Enter mode of farming, water level,soil type,and manure to get a crop suggestion.")

#LOADING COMBINATIONS
def crop(mode,water,soil="none",manure="none"):

    # CLOSED
    if mode=="closed":
        return "Mushroom"

    # ROOFTOP
    elif mode=="rooftop":
        if manure=="organic":
            return "Leafy Greens"
        else:
            return "Vegetables"

    # HILL
    elif mode=="hill":
        if water=="medium" and soil=="loamy":
            return "Tea"
        elif water=="low" and soil=="sandy":
            return "Spices"
        else:
            return "No suitable crop recommendation,try different combination"

    # BARREN
    elif mode=="barren":
        if water=="low":
            return "Millets"
        else:
            return "No suitable crop recommendation,try different combination"

    # OPEN
    elif mode=="open":

        if water=="high" and soil=="clay":
            return "Rice"

        elif water=="high" and soil=="loamy":
            return "Sugarcane"

        elif water=="medium" and soil=="loamy":
            if manure=="organic":
                return "Vegetables"
            else:
                return "Wheat"

        elif water=="low" and (soil=="sandy" or soil=="none"):
            if manure=="organic":
                return "Groundnut"
            else:
                return "Millets"

        else:
            return "No suitable crop recommendation,try different combination"

    # DEFAULT
    else:
        return "Invalid mode"

#GETTING INPUT FROM THE USER
while True:
    print("\n--- Neral Crop Recommendation System ---")

    # MODE (Mandatory)
    while True:
        print("\nSelect Mode of Farming (Mandatory):")
        print("1. Rooftop")
        print("2. Open")
        print("3. Closed")
        print("4. Hill")
        print("5. Barren")

        mode=input("Enter your choice (1-5): ")

        if mode=="1":
            mode="rooftop"
            break
        elif mode=="2":
            mode="open"
            break
        elif mode=="3":
            mode="closed"
            break
        elif mode=="4":
            mode="hill"
            break
        elif mode=="5":
            mode="barren"
            break
        else:
            print("Invalid input! You must select a valid option.")

    # WATER (Mandatory)
    while True:
        print("\nSelect Water Level (Mandatory):")
        print("1. Low")
        print("2. Medium")
        print("3. High")

        water=input("Enter your choice (1-3): ")

        if water=="1":
            water="low"
            break
        elif water=="2":
            water="medium"
            break
        elif water=="3":
            water="high"
            break
        else:
            print("Invalid input! You must select a valid option.")

    # SOIL
    while True:
        print("\nSelect Soil Type:")
        print("1. Clay")
        print("2. Sandy")
        print("3. Loamy")
        print("4. Ignore")

        soil=input("Enter your choice (1-4): ")

        if soil=="1":
            soil="clay"
            break
        elif soil=="2":
            soil="sandy"
            break
        elif soil=="3":
            soil="loamy"
            break
        elif soil=="4":
            soil="none"
            break
        else:
            print("Invalid input! Try again.")

    # MANURE
    while True:
        print("\nSelect Manure Type:")
        print("1. Organic")
        print("2. Chemical")
        print("3. Ignore")

        manure=input("Enter your choice (1-3): ")

        if manure=="1":
            manure="organic"
            break
        elif manure=="2":
            manure="chemical"
            break
        elif manure=="3":
            manure="none"
            break
        else:
            print("Invalid input!Try again.")

    # INPUT SUMMARY
    print("\n--- INPUT SUMMARY ---")
    print("Mode:",mode)
    print("Water:",water)
    print("Soil:",soil)
    print("Manure:",manure)

    #FUNCTION CALLING
    result=crop(mode,water,soil,manure)
    print("\nRecommended Crop:",result)

    #TO CONTINUE WITH RECOMMENDATION OR EXIT
    inp=input("\nDo you want to try another input? (yes/no): ")

    if inp.strip().lower()=="no":
        print("Hope you had a satisfied Crop Recommendation,Thank You...")
        break