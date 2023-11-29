import os
import traci
import sumolib
import duarouter

sumo_bin = r"C:\Program Files (x86)\Eclipse\Sumo\bin\sumo.exe"
duarouter_bin = r"C:\Program Files (x86)\Eclipse\Sumo\bin\duarouter.exe"
sumo_config = "osm.sumocfg"

def run_simulation():
    # Start the SUMO simulation and duarouter separately
    traci.start([sumo_bin, "-c", sumo_config, "--start", "--quit-on-end"], label="sumo")
    duarouter.start([duarouter_bin, "-c", sumo_config], label="duarouter")

    # Perform route generation using duarouter
    print("Generating routes...")
    duarouter.run()

    # Load the generated routes into the SUMO simulation
    traci.load(["--route-files", "duarouter.routes.xml"])

    # Main simulation loop
    for step in range(1000):
        traci.simulationStep()

    # Close the connections
    traci.close()
    duarouter.close()

if __name__ == "_main_":
    run_simulation()
    
duarouter -n C:\Users\NAGATEJA\Sumo\2023-10-20-13-38-47\osm.net.xml -r C:\Users\NAGATEJA\Sumo\2023-10-20-13-38-47\combined_trips.rou.xml --output-file output_data.xml

