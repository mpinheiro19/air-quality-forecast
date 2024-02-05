from dotenv import load_dotenv
import os, logging, requests

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s]: %(message)s",
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler("loginfo.log")
    ]
)

load_dotenv()

class AirQualityApi():


    def __init__(self, city):
        self.api_token = os.getenv("API_TOKEN")
        self.city = city
        logging.info(f"Conector de API válido para a cidade {self.city}")
        logging.info(f"Buscando conexão para o token com final {self.api_token[-5:]}")

    def get_available_stations(self):

        response=requests.get(f"https://api.waqi.info/search/?keyword={self.city}&token={self.api_token}")
        logging.info(f"Api retornando status: {response.status_code} \n\n {response.text}")
        return response.text


api=AirQualityApi(city='São Paulo')
api.get_available_stations()