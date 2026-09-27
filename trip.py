def trip_expenditure(travel_cost, food_cost, accommodation_cost, other_cost=0):
    """
    Function to calculate total trip expenditure.
    Arguments:
        travel_cost (float): Cost of travel (tickets, fuel, etc.)
        food_cost (float): Cost of food during the trip
        accommodation_cost (float): Cost of stay (hotel, etc.)
        other_cost (float): Any additional expenses (default = 0)
    Returns:
        float: Total expenditure
    """
    total = travel_cost + food_cost + accommodation_cost + other_cost
    return total

# Example usage
travel = float(input("Enter travel cost: "))
food = float(input("Enter food cost: "))
stay = float(input("Enter accommodation cost: "))
other = float(input("Enter other expenses (if any): "))

print("Total Trip Expenditure = ₹", trip_expenditure(travel, food, stay, other))
