import constants
import inspect
import requests
import json

class datatemps:
    def __init__(self, logger, dataUser={}):
        a = 1
        self.logger = logger
        self.dataUser = dataUser

    def update(self) -> None:
        chat_id = self.dataUser.get(constants.DATA_CHAT_ID)
        self.logger.info(constants.START + ":" + inspect.stack()
                         [1][3], extra=self.dataUser.get(constants.EXTRA_PARAMS))

        payload = 'chat_id=12345&data=%7B%7D'

        response = requests.request(
            "POST", constants.URL_BACKEND + constants.CONTENT_DATA_TEMP, headers=constants.DEFAULT_HEADER, data=payload
        )
        
        _response = json.loads(response.text)
        code_response = response.status_code

        self.logger.info(constants.RESPONSE_API_CORE.replace(
                    "{msg}", response.text), extra=self.dataUser.get(constants.EXTRA_PARAMS))

        self.logger.info(constants.END, extra=self.dataUser.get(constants.EXTRA_PARAMS))
        
    async def get(self,chat_id) -> None:
        chat_id = self.dataUser.get(constants.DATA_CHAT_ID)
        self.logger.info(constants.START + ":" + inspect.stack()
                         [1][3], extra=self.dataUser.get(constants.EXTRA_PARAMS))

        payload = 'chat_id=' + str(chat_id)

        response = requests.request(
            "GET", constants.URL_BACKEND + constants.CONTENT_DATA_TEMP, headers=constants.DEFAULT_HEADER, data=payload
        )
        
        _response = json.loads(response.text)
        code_response = response.status_code

        self.logger.info(constants.RESPONSE_API_CORE.replace(
                    "{msg}", response.text), extra=self.dataUser.get(constants.EXTRA_PARAMS))

        self.logger.info(constants.END, extra=self.dataUser.get(constants.EXTRA_PARAMS))
        
        return _response