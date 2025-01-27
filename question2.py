# Set the hard-coded PIN, make sure to make it a string since the input function returns string values!
correct_pin = "1993"

# Create a variable to define the maximum number of attempts as 3
attempts = 3

# Set up a for each style loop with two parameters
# START value is 1 and STOP value is the maximum attempts plus 1 (because the STOP value isn't included in the output)
# This range specifies how many times the loop can run, i.e. 3
for attempt in range(1, attempts + 1):

    # Use the input function to prompt user to supply a PIN
    supplied_pin = input("Please enter your PIN: ")

    # Set conditional tests
    # First condition - if the PIN is correct, then print "Access granted". Use an f-string to interpolate the attempt variable
    if supplied_pin == correct_pin:
        print(f"Access granted. You have entered the correct PIN in {attempt} attempt(s).")
        # Important: Add a break statement to exit the loop at this point because the condition has been met (right PIN has been supplied)
        break

    # Set additional condition, i.e. for as long as the user's attempts are less than 3, and the supplied PIN is not correct, they will receive this message
    # Specify the number of attempts the user has made by interpolating attempts - attempt, each time the user puts in the wrong PIN, the number of attempts left decreases by 1
    elif attempt < attempts:
        print(f"Wrong, you have {attempts - attempt} attempt(s) left.")

    # Last condition, if the user enters the wrong PIN 3 times then print Access denied.
    else:
        print("Access denied. You have entered the incorrect PIN too many times.")

# Errors: Didn't make correct_pin a string, didn't add 1 to the STOP value (first tried to use 3 without defining max_attempts)