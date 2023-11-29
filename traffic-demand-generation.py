import traci
import random
import time
import csv

# Define the simulation parameters
sumo_binary = "sumo"  # Path to the SUMO binary
sumo_config_file = r"C:\Users\NAGATEJA\Sumo\2023-10-20-13-38-47/osm.sumocfg"  # Replace with your SUMO configuration file
sim_duration = 3600  # Simulation duration in seconds
output_file = "traffic_demand.csv"  # Output file to store traffic demand

# Open the CSV file for writing
with open(output_file, "w", newline="") as csvfile:
    fieldnames = ["VehicleID", "VehicleType", "DepartureTime", "RouteID", "OtherDetails"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    # Connect to the SUMO simulation
    traci.start([sumo_binary, "-c", sumo_config_file])

    # Main simulation loop
    simulation_time = 0

    while simulation_time < sim_duration:
        # Generate random vehicle type
        vehicle_type = random.choice(["car", "bus", "truck", "bike"])  # Add more vehicle types as needed

        # Generate a random route for the vehicle
        route_id = f"route_{vehicle_type}_{simulation_time}"
        traci.route.add(route_id, ["150785556#0", "150785556#0-AddedOffRampEdge"])  # Replace "random_edge" with your edge ID

        # Add a vehicle of the selected type to the simulation
        vehicle_id = f"{vehicle_type}_{simulation_time}"
        traci.vehicle.add(vehicle_id, route_id, departPos="random", departSpeed="random")

        # Simulate additional details for each vehicle
        other_details = f"Additional info for {vehicle_id}"

        # Write vehicle information to the CSV file
        writer.writerow({
            "VehicleID": vehicle_id,
            "VehicleType": vehicle_type,
            "DepartureTime": simulation_time,
            "RouteID": route_id,
            "OtherDetails": other_details
        })

        # Increment the simulation time by a random time step
        time_step = random.uniform(2, 10)  # Adjust the time step range as needed
        simulation_time += time_step
        traci.simulationStep()

    # Finish the simulation
    traci.close()
