"""This function handles the transfer process for the user."""

from BankingClasses.checking import CheckingAccount
from BankingClasses.savings import SavingsAccount




def main():
    max_attempts = 3
    attempts = 0

    while attempts < max_attempts:
        email = input("Enter your email: ")
        password = input("Enter your password: ")
        
        if validate_login(email, password):  # Assuming you have a function to validate login
            print("Login successful!")
            break
        else:
            attempts += 1
            print("Invalid credentials. Please try again.")

    if attempts == max_attempts:
        print("Maximum number of attempts reached. Exiting program.")

def validate_login(email, password):
    # Replace this with your actual validation logic
    return email == "user@example.com" and password == "password123"

if __name__ == "__main__":
    main()












def main():
    """
    This function is the entry point of the banking system.
    It prompts the user to enter their email and password for authentication.
    If the email and password are valid, the default balances are shown.
    It then presents a menu of options to the user,
    allowing them to make deposits, withdrawals, or transfers between accounts.
    """
    email = input("Enter your email: ")
    print("Your password should be at least 8 characters long,\n"
          "contain at least one uppercase and lowercase letter,\n"
          "one number, and one of the following special characters:!@#$%^&*.")
    password = input("Enter your password: ")

    # Initialize the attempts variable to 1.
    attempts = 1
    # Use a while loop to validate the email and password.
    while attempts < 3:


        ##class Validation:
            ##@staticmethod
                
        # Your validation logic here
    

           ## @staticmethod
                    
        # Your validation logic here
               
        # Validate the email and password using the Validation class.
           
            # If the email or password is invalid, print a message
            # and increment the attempts variable.
            if attempts >= 3:
                print("Maximum number of attempts reached. Exiting program.")
                exit()  # Or any other way you want to exit the program

    # If the maximum number of attempts is reached, print a message
    # and exit the program.

print("Maximum number of attempts reached. Exiting program.")
def add(a, b):
    return a + b  # This returns the sum of a and b

result = add(5, 3)  # Calls the function and stores the returned value in result
print(result) 
    # Set up accounts with default balances.
checking_account = CheckingAccount(4321.00)
savings_account = SavingsAccount(6543.21)

    # Print a message for the user inform them of their checking
    # and savings balances.
print("\nHere are your account balances:")
    # Use the get_balance method to retrieve the
    # current balance of each account.
print(f"Checking: ${checking_account.get_balance():,.2f}")
print(f"Savings: ${savings_account.get_balance():,.2f}")

    # Write a while loop to present options for the user.
    # Have the loop run until the user chooses to quit (q).
while True:
        print("\nWhat would you like to do?")
        print("Make a deposit? Enter 1")
        print("Make a withdrawal? Enter 2")
        print("Make a transfer? Enter 3")
        print("Check account balances? Enter 4")
        print("Quit? Enter q\n")
       

print("Output:")
def output():
    print(output)
def test_main_banking_flow(self):
    # Redirect standard output to capture prints
    captured_output = io.StringIO()
    sys.stdout = captured_output

    your_function_call()  # Call the function that produces output

    # Reset standard output to default
    sys.stdout = sys.__stdout__

    output = captured_output.getvalue()  # Get the printed output
    print("Captured Output:")
    print(output)
    # Continue with your assertions...
print("Expected Value:")
def expected_value():
    print(expected_value)

        # Create a list of valid choices.
                
            # Use if/elif conditional statements to check the user's choice.
            # If the choice is in the list of valid choices,
            # call the appropriate function.
            # Pass in the checking_account and savings_account objects.
    def choice():
        if choice == '1':
                handle_deposit(checking_account, savings_account)

                handle_withdrawal(checking_account, savings_account)

                handle_transfer(checking_account, savings_account)

                balances(checking_account, savings_account)

    
        # If the user enters an invalid choice, print a message.
    
print("Invalid choice. Please enter 1, 2, 3, 4, or q.\n")


if __name__ == "__main__":
    main()

