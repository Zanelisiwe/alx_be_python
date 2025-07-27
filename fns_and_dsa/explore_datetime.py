# explore_datetime.py

from datetime import datetime, timedelta

def display_current_datetime():
    # Save the current date and time in a variable
    current_date = datetime.now()
    
    # Format the current date and time
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    
    # Print the formatted date and time
    print("Current date and time:", formatted_date)

def calculate_future_date():
    # Prompt the user to enter number of days
    try:
        days_to_add = int(input("Enter the number of days to add to the current date: "))
        
        # Get the current date and calculate the future date
        current_date = datetime.now()
        future_date = current_date + timedelta(days=days_to_add)
        
        # Format and print the future date
        formatted_future_date = future_date.strftime("%Y-%m-%d")
        print("Future date:", formatted_future_date)
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

# Run the functions
display_current_datetime()
calculate_future_date()
