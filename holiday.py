# Get user input
city_flight = input("Where will you be flying to? ")
num_nights = int(input("How many nights will you stay at the hotel? "))
rental_days = int(input("How many days will you need a car rental? "))

def hotel_cost(num_nights):
    # Assume a price per night
    price_per_night = 100
    return num_nights * price_per_night

def plane_cost(city_flight):
    # Flight costs based on city
    if city_flight == "Bucharest":
        return 300
    elif city_flight == "Sofia":
        return 250
    elif city_flight == "Budapest":
        return 200
    else:
        return 150  # Default cost for other cities

def car_rental(rental_days):
    # Daily rental cost
    daily_cost = 40
    return rental_days * daily_cost

def holiday_cost(num_nights, city_flight, rental_days):
    return hotel_cost(num_nights) + plane_cost(city_flight) + car_rental(rental_days)

# Calculate total cost
total_cost = holiday_cost(num_nights, city_flight, rental_days)

# Print holiday details 
# Note: \n is a special character that starts a new line
print("\nHoliday Details:")
print(f"City: {city_flight}")
print(f"Total Hotel Cost: ${hotel_cost(num_nights)}")
print(f"Total Flight Cost: ${plane_cost(city_flight)}")
print(f"Total Car Rental Cost: ${car_rental(rental_days)}")
print(f"Total Holiday Cost: ${total_cost}")
