from dotenv import load_dotenv
import os, logging, requests, json

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

    def get_response(self) -> json:
        response = requests.get(f"https://api.waqi.info/search/?keyword={self.city}&token={self.api_token}")
        logging.info(f"Api retornando {response.status_code}: {response.json()['status']}")
        return response.json()

    def response_dump(self, api_response: json, filename='aqi_dump') -> None:
        with open(f"./artifacts/{filename}.json",'w',encoding='utf8') as fp:
            json.dump(
                api_response,
                fp,
                indent=4,
                ensure_ascii=False
            )
        logging.info(f"Arquivo salvo em './artifacts/{filename}.json'")
        return

    def get_available_stations(self, api_response) -> list:
        try:
            assert len(api_response['data']) > 0

            stations_list=[
                api_response['data'][station_value]['station']['url']
                for station_value 
                in range(len(api_response['data']))
            ]

            logging.info(f"Foram encontradas {len(api_response['data'])} estações para a cidade selecionada!")
            
            return stations_list

        except AssertionError as e:
            logging.warn(f"Não foi possível encontrar estações para o keyword informado: {e}")
            pass