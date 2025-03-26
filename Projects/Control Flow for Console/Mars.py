import sys  

# Define gravity constants for each planet
GRAVITY_CONSTANTS = {
    "Mercury": 0.376,
    "Venus": 0.889,
    "Mars": 0.378,
    "Jupiter": 2.36,
    "Saturn": 1.081,
    "Uranus": 0.815,
    "Neptune": 1.14
}

def calculate_weight_on_planet(earth_weight, planet):
    planet = planet.capitalize()  # Convert first letter to uppercase (handles user input case variations)
    
    if planet in GRAVITY_CONSTANTS:
        planetary_weight = round(earth_weight * GRAVITY_CONSTANTS[planet], 2)
        return f"🌍 Your weight on **{planet}** would be: **{planetary_weight} kg** 🪐"
    else:
        return "❌ Invalid planet name! Please enter a valid planet (Mercury, Venus, Mars, etc.)."

def main():
    print("\n🚀 **Welcome to the Planetary Weight Converter!** 🚀")
    print("Find out your weight on different planets! 🌍➡️🪐\n")
    
    try:
        earth_weight = float(input("🔹 Enter your weight on Earth (kg): "))
        
        planet = input("🔹 Enter the name of a planet: ").strip()

        result = calculate_weight_on_planet(earth_weight, planet)
        print("\n" + result + "\n")
    
    except ValueError:
        print("\n❌ Invalid input! Please enter a valid number for weight.\n")
        sys.exit()

if __name__ == "__main__":
    main()
