# Calculate the distance  between two points ?



latitude1 = int(input("Enter the distance for x :"))
longitude1 = int(input("Enter the distance for x1 :"))
latitude2 = int(input("Enter the distance for y :"))
longitude2 = int(input("Enter the distance for y1 :"))

power = pow(longitude1-latitude1,2)+pow(longitude2-latitude2,2)

distance = int(power) ** 0.5

print(distance,"kilometers is the distance between the two points")