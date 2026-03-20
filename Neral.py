#INTRODUCTION
print("Welcome to Neral! A beginner-friendly crop recommendation tool. Enter mode of farming, water level, soil type, and manure to get a crop suggestion.")


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

        mode = input("Enter your choice (1-5): ")

        if mode == "1":
            mode = "rooftop"
            break
        elif mode == "2":
            mode = "open"
            break
        elif mode == "3":
            mode = "closed"
            break
        elif mode == "4":
            mode = "hill"
            break
        elif mode == "5":
            mode = "barren"
            break
        else:
            print("Invalid input! You must select a valid option.")

    # WATER (Mandatory)
    while True:
        print("\nSelect Water Level (Mandatory):")
        print("1. Low")
        print("2. Medium")
        print("3. High")

        water = input("Enter your choice (1-3): ")

        if water == "1":
            water = "low"
            break
        elif water == "2":
            water = "medium"
            break
        elif water == "3":
            water = "high"
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

        soil = input("Enter your choice (1-4): ")

        if soil == "1":
            soil = "clay"
            break
        elif soil == "2":
            soil = "sandy"
            break
        elif soil == "3":
            soil = "loamy"
            break
        elif soil == "4":
            soil = "none"
            break
        else:
            print("Invalid input! Try again.")

    # MANURE
    while True:
        print("\nSelect Manure Type:")
        print("1. Organic")
        print("2. Chemical")
        print("3. Ignore")

        manure = input("Enter your choice (1-3): ")

        if manure == "1":
            manure = "organic"
            break
        elif manure == "2":
            manure = "chemical"
            break
        elif manure == "3":
            manure = "none"
            break
        else:
            print("Invalid input! Try again.")

    # INPUT SUMMARY
    print("\n--- INPUT SUMMARY ---")
    print("Mode:", mode)
    print("Water:", water)
    print("Soil:", soil)
    print("Manure:", manure)

    #FUNCTION CALLING

    #TO CONTINUE WITH RECOMMENDATION OR EXIT
    int = input("\nDo you want to try another input? (yes/no): ")

    if int.lower() == "no":
        print("Exiting system...")
        break
