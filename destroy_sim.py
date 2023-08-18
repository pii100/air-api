from air_sdk import AirApi
import api_vars
air = AirApi(username='<user>', password='<api_token>')
simulation = air.simulations.get('<simulation_uuid>')
simulation.delete()