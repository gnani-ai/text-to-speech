# Welcome to GNANI API Text-To-Speech Service

This document describes the Gnani’s TTS API that is used to get the TTS audio data.

## Prequisites for setting up the API

* Token and accesskey and certificate received from gnani to your registered email id.This is mandatory to access the api.

## How to setup the API

In your client tts code, you are required to pass headers along with the request paylod. 
The headers must contain token, accesskey, language that you want to use and product as key value pairs. 
Update the user.config file with all these parameters.

#### For Example:
 **In TTS_USER section:**
 ```
    token           : eyJhbGcIIUz.iOiJIUzI1NiIs-5cC.N2N2OWxBRUsxT
    access_key      : 7f550a9f4c44173a37664d938f1
    language        : hi-IN
    product         : tts
    tts-api-url     : https://asr.gnani.ai/synthesize
```
**In TTS_REQUEST_BODY section:**

 ```
    text            : आज मैं आपकी कैसे मदद कर सकता हूँ
    langcode        : hi-IN 
    name            : gnani
    ssmlgender      : FEMALE
    audioencoding   : pcm16 
```

* After updating the user.config file you can run the particular client and get the response data. 

## How API works:

### Request Headers :
```
        {
             "token": string <token to authenticate user>, 
             "accesskey": string <accesskey to authenticate user>, 
             "lang": string <language to select decodeing model inorder to convert input text to audio string>,
             "product": string <Gnani product to be used>,
        }

```
### Request Body :
```
        {
              "input": { 
                        "text": string <input text to tts server>
              },
              "voice": {
                         "languageCode": string <lang_code of input string>,
                          "name": string <name of user>,
                         "ssmlGender":string <ssml_gender of user>
              },
               "audioConfig": {
                          "audioEncoding": string <audio_encoding of the response string>
               }
        }
```

### Sample Response Format

```
    {
        "audioContent": <converted audio string here>
    }
```

### Note 
- Your request will not be authenticated if you fail to add any of these headers to your request.
- You are required to add certficate (cert.pem) that was sent to the registered email id as part of your code.

## Sample Code
Here are the list of sample codes.

REST Codes
- [NodeJs](https://github.com/gnani-ai/text-to-speech/tree/main/rest-codes/Nodejs-Client)
- [Python](https://github.com/gnani-ai/text-to-speech/tree/main/rest-codes/Python-Client)

### Support or Contact

#### Disclaimer
The Speech APIs are completely proprietary and are the sole property of Gnani.ai. We reserve the right to remove users access at any point of time. Note that the free access to the APIs are purely for testing or experimental purposes, and will be available to the users for a limited amount of time, after which they will have to purchase the commercial version. Gnani.ai will immediately remove access if the user is found to be using the APIs for commercial purposes. If you wish to obtain unlimited access, you can make an enquiry on the website or write to us at operations@gnani.ai. Also if you are having trouble please raise an issue or mail to us at operations@gnani.ai
