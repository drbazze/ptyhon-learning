# Import the necessary modules
import requests

# Define a function to convert currencies
def currency_converter(amount, from_currency, to_currency):
    # Set the API endpoint for currency conversion
    api_endpoint = f"https://open.er-api.com/v6/latest/USD/{from_currency}"
    
    
    # Send a GET request to the API endpoint
    response = requests.get(api_endpoint)
    
    # Get the JSON data from the response
    data = response.json()
    
    # Extract the exchange rate for the target currency
    exchange_rate = data["rates"][to_currency]
    
    # Calculate the converted amount
    converted_amount = amount * exchange_rate
    
    # Return the converted amount
    return converted_amount

#Run this part when the file is executed as a script
if __name__ == "__main__":
    # Prompt the user to enter the amount, source currency, and target currency
    try:
        amount = float(input("Enter the amount: "))
        from_currency = input("Enter the source currency code: ").upper()
        to_currency = input("Enter the target currency code: ").upper()

        # Convert the currency and print the result
        result = currency_converter(amount, from_currency, to_currency)
        print(f"{amount} {from_currency} is equal to {result} {to_currency}")
    except Exception as error:
        print("An error occurred:", type(error).__name__)