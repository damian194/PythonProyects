def main():
    mass_kg = int(input("give me the mass in kilograms: "))
    c = 300000000  # light speed in m/s
    energy_joules = mass_kg * c**2
    print(f"the equivalent energy is: {energy_joules} Joules")
main()