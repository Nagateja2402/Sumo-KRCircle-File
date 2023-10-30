import os
import subprocess
import sys
import traci
import traci.constants as tc

# Path to SUMO binaries
sumo_binary = "sumo"

# Path to network and route files
net_file = r"C:\Users\NAGATEJA\Sumo\2023-10-20-13-38-47/osm.net.xml"
route_file = r"C:\Users\NAGATEJA\Sumo\2023-10-20-13-38-47/output_dynamic_routes.rou.xml"

# Start SUMO as a subprocess
sumo_cmd = [sumo_binary, "-c", r"C:\Users\NAGATEJA\Sumo\2023-10-20-13-38-47/osm.sumocfg"]
sumo_proc = subprocess.Popen(sumo_cmd, stdout=sys.stdout, stderr=sys.stderr)

# Connect to SUMO simulation
traci.start(["sumo", "-c", r"C:\Users\NAGATEJA\Sumo\2023-10-20-13-38-47/osm.sumocfg"])

try:
    # DUArouter initialization
    traci.simulationStep()
    # traci.setRoutingMode(tc.RoutingMode.DUAROUTER)
    # traci.setAdaptationInterval(tc.DUAROUTER_ADAPTATION_INTERVAL, 300)  # Adaptation interval in seconds

    # Add a vehicle to the simulation
    traci.route.add("route0", ["150785556#0", "150785556#0-AddedOffRampEdge"])  # Define a route for the vehicle
    traci.vehicle.add("vehicle1", "route0", departPos="random", departSpeed="random")

    # Simulation loop
    while traci.simulation.getMinExpectedNumber() > 0:
        traci.simulationStep()

    # End simulation
    traci.close()
except Exception as e:
    print("Error: ", str(e))
finally:
    # Close SUMO and end the subprocess
    traci.close()
    sumo_proc.terminate()
    sumo_proc.wait()