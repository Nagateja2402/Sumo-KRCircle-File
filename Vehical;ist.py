import traci

# Define the path to the SUMO binary and your SUMO configuration file
sumo_binary = "sumo"  # Path to the SUMO binary
sumo_config_file = r"C:\Users\NAGATEJA\Sumo\2023-10-20-13-38-47/osm.sumocfg"  # Replace with your SUMO configuration file

# Connect to the SUMO simulation
traci.start([sumo_binary, "-c", sumo_config_file])

# Get a list of all vehicles in the simulation
vehicle_ids = traci.vehicle.getIDList()

# Print the list of vehicle IDs
print("List of vehicles in the SUMO simulation:")
for vehicle_id in vehicle_ids:
    print(vehicle_id)

# Finish the simulation
traci.close()
