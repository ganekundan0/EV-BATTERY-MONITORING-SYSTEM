
print("===================================")
print("     EV BATTERY MONITORING SYSTEM")
print("===================================")

# Enter battery information

voltage = float(input("Enter Battery Voltage (V): "))
current = float(input("Enter Battery Current (A): "))
temperature = float(input("Enter Temperature (C): "))
battery_level = float(input("Enter Battery Level (%): "))

# Calculate power

power = voltage * current

# Display battery report

print("\n========== BATTERY REPORT ==========")

print("Voltage:", voltage, "V")
print("Current:", current, "A")
print("Temperature:", temperature, "C")
print("Battery Level:", battery_level, "%")
print("Power:", power, "W")

# Display sample status

if temperature > 45:
    print("Status: Temperature Alert")
else:
    print("Status: Normal")

print("===================================")
