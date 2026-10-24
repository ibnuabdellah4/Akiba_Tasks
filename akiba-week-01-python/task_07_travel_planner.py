destination = input("Where is your destination?:  ")
distance = float(input("Approxiamte distance:  "))
speed = float(input("Average speed:  "))
time = distance / speed

print(f'''
    Destination: {destination}
    Distance: {distance} km
    Average Speed: {speed} km/h

    Estimated Travel Time: {time} hours
''')
