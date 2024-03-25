house_type=input("What house type?: ")

if house_type == "Single":    
    season=input("What is the season?: ")
    if season == "Fall":
        print("Single\n Fall,Spring: $50.00")
    if season == "Spring":
        print("Single\n Fall,Spring: $50.00")
    if season == "Winter":
        print("Single\n Winter $250.00")
    if season == "Summer":
        air=input("Does it have central air?: ")
        if air == "Yes":
            print("Single\n Summer: $200.00")
        else:            
            print("Single\n Summer: $50.00")
            

if house_type == "Duplex":    
    season=input("What is the season?: ")
    if season == "Fall":
        print("Duplex\n Fall,Spring: $40.00")
    if season == "Spring":
        print("Duplex\n Fall,Spring: $40.00")
    if season == "Winter":
        print("Duplex\n Winter $200.00")
    if season == "Summer":
        air=input("Does it have central air?: ")
        if air == "Yes":
            print("Duplex\n Summer: $150.00")
        else:            
            print("Duplex\n Summer: $40.00")

            
if house_type == "Row":    
    season=input("What is the season?: ")
    if season == "Fall":
        print("Row\n Fall,Spring: $35.00")
    if season == "Spring":
        print("Row\n Fall,Spring: $35.00")
    if season == "Winter":
        print("Row\n Winter $175.00")
    if season == "Summer":
        air=input("Does it have central air?: ")
        if air == "Yes":
            print("Row\n Summer: $125.00")
        else:            
            print("Row\n Summer: $25.00")


