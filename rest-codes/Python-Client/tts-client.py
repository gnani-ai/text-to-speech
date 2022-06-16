import json
import httpx
import numpy as np
from scipy.io.wavfile import write

from configparser import ConfigParser
from log_config.logger import get_logger

logger = get_logger(__name__)

# Reading from config file
parser = ConfigParser()
parser.read('user.config')

LANGUAGE_MAPPING = {'en-IN': "english_female",
                    'kn-IN': "kannada_female",
                    'hi-IN': "hindi_female",
                    'ta-IN': "tamil_female",
                    'mr-IN': "marathi_female"}


def tts_service(request_headers, request_payload, lang_code, sample_rate):
    """ Method to send text and get converted audio string in response
        Args:
            request_headers (json): request headers
            request_payload (json): request payload
            lang_code (str) : string
        Raises:
            Exceptions
        Returns:
            response: Response from the server
    """
    try:
        output_audio_file_name = "tts_output.wav"
        api_url = "https://asr.gnani.ai/predictions/" + str(LANGUAGE_MAPPING[lang_code])
        response = httpx.post(api_url, data=request_payload, headers=request_headers)
        response_json = response.json()
        audio = response_json["audio_raw"]
        audio = np.asarray(audio, dtype=np.int16)
        write(output_audio_file_name, int(sample_rate), audio)
        logger.info(f"!!!! Successfully generated audio file = {output_audio_file_name} with the given samplerate !!!!!")
    except Exception as exception:
        logger.exception('Exception in getting audio from TTS response - !' + str(exception))
        logger.info(f"Actual Response from tts server - {response.text}")


if __name__ == '__main__':
    """ Set all below parameters in the config file. """

    logger.info("Main Method ! - Start")
    token = parser.get('TTS_USER', 'TOKEN')
    accesskey = parser.get('TTS_USER', 'ACCESSKEY')
    language = parser.get('TTS_USER', 'LANGUAGE')
    product = parser.get('TTS_USER', 'PRODUCT')
    lang_code = parser.get('TTS_USER', 'LANGUAGE')

    text = parser.get('TTS_REQUEST_BODY', 'TEXT')
    sample_rate = parser.get('TTS_REQUEST_BODY', 'SAMPLERATE')
    alpha = parser.get('TTS_REQUEST_BODY', 'ALPHA')
    pitch = parser.get('TTS_REQUEST_BODY', 'PITCH')
    pauses = parser.get('TTS_REQUEST_BODY', 'PAUSES')

    """SSL Configuration goes here.
    Paste the 'chain.pem' mailed to you in the root directory.
    """
    cert = "cert.pem"

    # construct request headers
    headers = {"token": token, "accesskey": accesskey,
               "product": product, "Content-Type": "application/x-www-form-urlencoded"}

    # construct response headers
    payload = {"input": text,
               "alpha": alpha,
               "pitch": pitch,
               "pauses": pauses,
               "sampleRate": sample_rate}

    tts_service(headers, payload, lang_code, sample_rate)
    logger.info("Main Method ! - End")

