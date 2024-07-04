# Global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def convert_to_celsius(fahrenheit):
    """Converts temperature from Fahrenheit to Celsius."""
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

def convert_to_fahrenheit(celsius):
    """Converts temperature from Celsius to Fahrenheit."""
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return fahrenheit

def temp_conversion_tool():
    """Interactive temperature conversion tool."""
    while True:
        try:
            temperature = float(input("Enter the temperature to convert: "))
            unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

            if unit == 'F':
                converted_temp = convert_to_celsius(temperature)
                print(f"{temperature:.1f}°F is {converted_temp:.2f}°C")
            elif unit == 'C':
                converted_temp = convert_to_fahrenheit(temperature)
                print(f"{temperature:.1f}°C is {converted_temp:.2f}°F")
            else:
                print("Invalid unit. Please enter 'C' or 'F'.")
                continue

        except ValueError:
            print("Invalid temperature. Please enter a numeric value.")
            continue

        another_conversion = input("Do you want to convert another temperature? (yes/no): ").strip().lower()
        if another_conversion != 'yes':
            print("Exiting temperature conversion tool.")
            break

if __name__ == "__main__":
    temp_conversion_tool()
