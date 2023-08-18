from air_sdk import AirApi
import api_vars
air = AirApi(username=api_vars.user, password=api_vars.api_token)
dot_file_path = 'topology.dot'
topology = air.topologies.create(dot=dot_file_path)
sim_title = 'API Simulation'
simulation = air.simulations.create(topology=topology, title=sim_title)
simulation.start()
print(f'Simulation "{simulation.title}" ID "{simulation.id}" created')