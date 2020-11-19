var request = require('request')
var config = require('./config/config');
var fs = require('fs')
/**
 * Method to send text and get converted audio string in response
 *
 * @param {object} options to the tts server request
 * @returns
 */

function tts_service(options){
    request(options, function (error, response) {
      if (error) throw new Error(error);
      console.log(response.body);
    });
}

/**
 * Main Method
 *
 * Setting the all parameters required for rest request
 * Requesting tts_service to convert given text to audio-string
 *
 * @returns
 */
function main(){
    try{
        var api_url = config.TTS_API_URL
        var token = config.TOKEN
        var accesskey = config.ACCESSKEY
        var language = config.LANGUAGE
        var product = config.PRODUCT
        var text = config.TEXT
        var lang_code = config.LANGCODE
        var name = config.NAME
        var ssml_gender = config.SSMLGENDER
        var audio_encoding = config.AUDIOENCODING
           var options = {
        'method': 'GET',
        'url': api_url,
        'headers': {
            'token': token,
            'accesskey': accesskey,
            'lang': language,
            'product': product,
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            "input":{
                "text":text
                },
            "voice":{
                "languageCode":lang_code,
                "name":name,
                "ssmlGender":ssml_gender
                },
            "audioConfig":{
                "audioEncoding":audio_encoding
                    }
            }),
        cert: fs.readFileSync(config.CERT_FILE_PATH),
        rejectUnauthorized: false

        };
        tts_service(options)
    }catch (error) {
        console.log(error.message);
    }
}

//main method called here
main()