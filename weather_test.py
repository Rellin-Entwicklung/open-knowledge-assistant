from datetime import datetime
from dwdweather import DwdWeather

# Create client object.
dwd = DwdWeather(resolution="hourly")

# Find closest station to position.
closest = dwd.nearest_station(lon=13.2, lat=52.56)

# The hour you're interested in.
# The example is 2014-03-22 12:00 (UTC).
query_hour = datetime(2020, 3, 4, 1)

result = dwd.query(station_id=closest["station_id"], timestamp=query_hour)
print(result)