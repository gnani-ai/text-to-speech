import json
import requests
from configparser import ConfigParser
from log_config.logger import get_logger

logger = get_logger(__name__)

# Reading from config file
parser = ConfigParser()
parser.read('user.config')


def tts_service(request_headers, request_payload):
    """ Method to send text and get converted audio string in response
        Args:
            request_headers (json): request headers
            request_payload (json): request payload
        Raises:
            Exceptions
        Returns:
            response: Response from the server
    """
    try:
        response = requests.request("GET", api_url,verify=cert,
                                    headers=request_headers,
                                    data=json.dumps(request_payload))

        return response.json()

    except BaseException as exception:
        logger.exception('Exception in getting tts !' + str(exception))
        return {"audioContent": ""}


if __name__ == '__main__':
    """ Set all below parameters in the config file. """

    logger.info("Main Method ! - Start")
    api_url = parser.get('TTS_USER', 'TTS_API_URL')
    token = parser.get('TTS_USER', 'TOKEN')
    accesskey = parser.get('TTS_USER', 'ACCESSKEY')
    language = parser.get('TTS_USER', 'LANGUAGE')
    product = parser.get('TTS_USER', 'PRODUCT')

    text = parser.get('TTS_REQUEST_BODY', 'TEXT')
    lang_code = parser.get('TTS_REQUEST_BODY', 'LANGCODE')
    name = parser.get('TTS_REQUEST_BODY', 'NAME')
    ssml_gender = parser.get('TTS_REQUEST_BODY', 'SSMLGENDER')
    audio_encoding = parser.get('TTS_REQUEST_BODY', 'AUDIOENCODING')
    sample_rate = parser.get('TTS_REQUEST_BODY', 'SAMPLERATE')

    """SSL Configuration goes here.
    Paste the 'chain.pem' mailed to you in the root directory.
    """
    cert = "cert.pem"
    
    # construct request headers
    headers = {"token": token, "accesskey": accesskey, "lang": language,
               "product": product,"Content-Type": "application/json"}

    # construct response headers
    payload = {"input": {"text": text},
               "voice": {"languageCode": lang_code, "name": name,
                         "ssmlGender": ssml_gender},
               "audioConfig": {"audioEncoding": audio_encoding,"sampleRate":sample_rate}}

    response = tts_service(headers, payload)
    logger.info("Response from tts server : {}".format(response))
    logger.info("Main Method ! - End")
