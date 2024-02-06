from api.air_quality import AirQualityApi
import json


api_keyword = "Delhi"
aqi = AirQualityApi(api_keyword)

aqi_response = aqi.get_response()
aqi.response_dump(aqi_response)
aqi.get_available_stations(aqi_response)