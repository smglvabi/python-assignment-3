
name = input("Enter driver name: ")
destination = (input("Enter destination:"))
distance = float(input("Enter distance (km): "))
consumption = float(input("Enter fuel consumption (L/100km): "))
fuel_price = float(input("Enter fuel price (KZT/L): "))


litres_needed = distance * consumption / 100
fuel_cost = litres_needed * fuel_price
cost_per_km = fuel_cost / distance
if distance < 100:
    category = "Short trip"
elif distance >= 100 and distance <= 500:
    category = "Medium trip"
else:
    category = "Long trip"
    


print("=" * 30)

print("Driver :", name)
print("Destination :",destination)
print("Distance :", distance, "km")
print("Consumption :", consumption, "L/100km")
print("Fuel cost :", fuel_cost, "KZT")
print("Cost per km :", cost_per_km, "KZT")
print("Category:", category)

#B2
for km in range(100,int(distance)+1, 100):
    cost = (fuel_cost*km)/distance
    print(km, "km:", cost, "KZT")

#B3

print("Destination uppercase : ", destination.upper())
print("Destination lowercase : ", destination.lower())
print("Length : ", len(destination))
print("Letter 'a' count : ", destination.lower().count('a') )


print("=" * 30)
