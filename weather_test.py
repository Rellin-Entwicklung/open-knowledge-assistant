from datetime import datetime
from dwdweather import DwdWeather

# Create client object.
dwd = DwdWeather(resolution="hourly")

# Find closest station to position.
closest = dwd.nearest_station(lon=7.0, lat=51.0)

# The hour you're interested in.
# The example is 2014-03-22 12:00 (UTC).
query_hour = datetime(2014, 3, 22, 12)

result = dwd.query(station_id=closest["station_id"], timestamp=query_hour)
print(result)
