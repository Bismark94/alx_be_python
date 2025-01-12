# temp_conversion_tool.py

# 1. Define global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5.0 / 9.0
CELSIUS_TO_FAHRENHEIT_FACTOR = 9.0 / 5.0

def convert_to_celsius(fahrenheit):
    """
    Converts a Fahrenheit temperature to Celsius,
    using the FAHRENHEIT_TO_CELSIUS_FACTOR global variable.
    """
    # (Fahrenheit - 32) * (5/9)
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

def convert_to_fahrenheit(celsius):
    """
    Converts a Celsius temperature to Fahrenheit,
    using the CELSIUS_TO_FAHRENHEIT_FACTOR global variable.
    """
    # (Celsius * (9/5)) + 32
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return fahrenheit

def main():
    try:
        # Prompt the user for a temperature
        user_temp_input = input("Enter the temperature to convert: ")
        # Validate user input is numeric
        if not user_temp_input.replace('.', '', 1).isdigit() and not (user_temp_input.startswith('-') and user_temp_input[1:].replace('.', '', 1).isdigit()):
            raise ValueError("Invalid temperature. Please enter a numeric value.")
        
        temperature = float(user_temp_input)

        # Prompt the user for the unit (C or F)
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

        # Decide which function to call based on the unit
        if unit == 'C':
            converted_temp = convert_to_fahrenheit(temperature)
            print(f"{temperature}°C is {converted_temp}°F")
        elif unit == 'F':
            converted_temp = convert_to_celsius(temperature)
            print(f"{temperature}°F is {converted_temp}°C")
        else:
            print("Invalid unit. Please enter either 'C' for Celsius or 'F' for Fahrenheit.")

    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
