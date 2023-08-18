from air_sdk import AirApi
import api_vars
air = AirApi(username=api_vars.user, password=api_vars.api_token)
print(air.simulations.list())