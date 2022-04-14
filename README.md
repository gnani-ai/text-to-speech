# Welcome to GNANI API Text-To-Speech Service

This document describes the Gnani’s TTS API that is used to get the TTS audio data.

## Supported Languages

### Single Speaker Text to Speech

| Language | Language Code | Gender | Sample Text                                                             | Sample Audio |
|----------|---------------|--------|-------------------------------------------------------------------------|--------------|
| English  | En-IN         | Female | "Hello. How are you doing?"                                             |             |
|          | En-IN         | Male   | "I'm fine. Thank you for asking."                                       |              |
| Hindi    | Hi-IN         | Female | "मैं ज्ञानी की ओर से बात कर रहा हूँ"                                          |              |
|          | Hi-IN-al      | Female | "नमस्ते मेरा नाम गीता है. क्या यह आपसे बात करने का सही समय है"                  | ![Sample](samples/al.wav)              |
|          | Hi-IN         | Male   | "मैं ज्ञानी की ओर से बात कर रहा हूँ"                                          |              |
| Kannada  | Kn-IN         | Female | "ನಾನು ಕರ್ನಾಟಕದ ಧ್ವನಿಯನ್ನು ಪ್ರತಿನಿಧಿಸುತ್ತಿದ್ದೇನೆ"                              |              |
|          | Kn-IN         | Male   | "ಹಲವು ಸಂಘ ಸಂಸ್ಥೆಗಳು ಖಂಡನಾ ಹೇಳಿಕೆ ನೀಡಿ ಐಎಎಸ್ ಅಧಿಕಾರಿಗೆ ನೈತಿಕ ಬಲ ನೀಡಿದ್ದಾರೆ" |              |
| Tamil    | Ta-IN         | Female | "அதனால் காதுக்குள் குச்சி பட்ஸ் விட்டு சுத்தம் செய்யக் கூடாது"                     |              |
|          | Ta-IN         | Male   | "ஒரு கலைஞன் போல் அவர் அந்த ஷாட்டை ஆடுவார்"                                    |              |
| Telugu   | Te-IN         | Female | " కానీ రామ్ చరణ్ కి హీరో నితిన్ కెరీర్ ప్రస్తుతం అంతగా బాగోలేదు"                            |              |
|          | Te-IN         | Male   | "ఆ వ్యక్తి ఎవరో గుర్తించి అతడితో టచ్ లోకి వెళ్లాడు"                                    |              |
| Marathi  | Mr-IN         | Female | "पण मी जे आजपर्यंत करत आलो तेच मला करायचं आहे"                                |              |



### Multispeaker Text to Speech

| Langauge | Language Code          | Gender | Name Tag       |
|----------|------------------------|--------|----------------|
| English  | multispeaker-english   | Female | Ella           |
|          |                        |        | Ruth           |
|          |                        |        | Casedey        |
|          |                        |        | April          |
|          |                        |        | Jenny          |
|          |                        |        | May            |
|          |                        |        | Amber          |
|          |                        |        | Judy           |
|          |                        |        | Sandy          |
|          |                        |        | Scarlette      |
| English  | multispeaker-english   | Male   | John           |
|          |                        |        | Aron           |
|          |                        |        | Philip         |
|          |                        |        | Tom            |
|          |                        |        | Rudy           |
|          |                        |        | Brian          |
|          |                        |        | Alex           |
|          |                        |        | Stan           |
|          |                        |        | Brock          |
|          |                        |        | Mike           |
| Hindi    | multispeaker-hindi     | Male   | Shaique        |
|          |                        |        | Jeevan         |
|          |                        |        | Arvind         |
|          |                        |        | Achuth         |
|          |                        |        | Abinay         |
|          |                        |        | Pradeep        |
|          |                        |        | Prasant        |
|          |                        |        | Mahesh         |
|          |                        |        | Naresh         |
|          |                        |        | Sreenath       |
| Hindi    | multispeaker-hindi     | Female | Sandhya        |
|          |                        |        | Bindu          |
|          |                        |        | Chitra         |
|          |                        |        | Supriya        |
|          |                        |        | Priya          |
|          |                        |        | Shanvi         |
|          |                        |        | Uma            |
|          |                        |        | Saniha         |
|          |                        |        | Vani           |
|          |                        |        | Siri           |
| Kannada  | Multispeaker-kannada   | Female | Gowramma       |
|          |                        |        | Gowri          |
|          |                        |        | padma          |
|          |                        |        | bharathi       |
|          |                        |        | manjula        |
|          |                        |        | suchithra      |
|          |                        |        | sowmya         |
|          |                        |        | shambavi       |
|          |                        |        | vidya          |
|          |                        |        | rashmika       |
| Kannada  | Multispeaker-kannada   | Male   | Prajwal        |
|          |                        |        | Prathik        |
|          |                        |        | arjun          |
|          |                        |        | bhoregowda     |
|          |                        |        | Krishna        |
|          |                        |        | yograj         |
|          |                        |        | bharath        |
|          |                        |        | manoj          |
|          |                        |        | harshavardhan  |
|          |                        |        | kushal         |
| Tamil    | Multispeaker-tamil     | Female | shashi         |
|          |                        |        | amudhavali     |
|          |                        |        | divyabharathi  |
|          |                        |        | nethravathi    |
|          |                        |        | pallavi        |
|          |                        |        | kavya          |
|          |                        |        | komalvali      |
|          |                        |        | sneha          |
|          |                        |        | sumathi        |
|          |                        |        | indhuleka      |
| Tamil    | Multispeaker-tamil     | Male   | Niranjan       |
|          |                        |        | gopal          |
|          |                        |        | munigovander   |
|          |                        |        | vijay          |
|          |                        |        | ajith          |
|          |                        |        | lokesh         |
|          |                        |        | ram            |
|          |                        |        | senthil        |
|          |                        |        | srinivas       |
|          |                        |        | arun           |
| Telugu   | Multispeaker-telugu    | Female | roja           |
|          |                        |        | anushka        |
|          |                        |        | anusha         |
|          |                        |        | gayathri       |
|          |                        |        | namrutha       |
|          |                        |        | chaithra       |
|          |                        |        | bindhu         |
|          |                        |        | lakshmi        |
|          |                        |        | monika         |
|          |                        |        | lalitha        |
| Telugu   | Multispeaker-telugu    | Female | ravi teja      |
|          |                        |        | harish         |
|          |                        |        | akileshwar     |
|          |                        |        | jagan          |
|          |                        |        | santhosh       |
|          |                        |        | hemath         |
|          |                        |        | sudhir         |
|          |                        |        | anirudh        |
|          |                        |        | nelson         |
|          |                        |        | bheem          |
| Marati   | Multispeaker-marathi   | Female | Akshayaa       |
|          |                        |        | Bhagyashi      |
|          |                        |        | Bhandishtha    |
|          |                        |        | Bhavanika      |
|          |                        |        | Bhavanjali     |
|          |                        |        | Bhaveeka       |
|          |                        |        | Bhavyani       |
|          |                        |        | Dharaa         |
|          |                        |        | Dharika        |
|          |                        |        | Dharmi         |
| Marati   | Multispeaker-marathi   | Male   | Adhrgu         |
|          |                        |        | Alagumuthu     |
|          |                        |        | Dhaval         |
|          |                        |        | Ilesh          |
|          |                        |        | Mirajkar       |
|          |                        |        | Namniya        |
|          |                        |        | Nandedkar      |
|          |                        |        | Narvel         |
|          |                        |        | Navjat         |
|          |                        |        | Nidhra         |
| Marati   | Multispeaker-malayalam | Female | Jini           |
|          |                        |        | Pujya          |
|          |                        |        | Reman          |
|          |                        |        | Reneeka        |
|          |                        |        | Shreeya        |
|          |                        |        | Shrejal        |
|          |                        |        | Shrena         |
|          |                        |        | Teja           |
|          |                        |        | Udaya          |
|          |                        |        | Uditi          |
| Marati   | Multispeaker-malayalam | Male   | Upendra        |
|          |                        |        | Ushapati       |
|          |                        |        | Utpal          |
|          |                        |        | Uttam          |
|          |                        |        | Vachan         |
|          |                        |        | Vachaspati     |
|          |                        |        | Vadish         |
|          |                        |        | Vagindra       |
|          |                        |        | Vagish         |
|          |                        |        | Vaidyanaath    |
| Gujarati | Multispeaker-gujarati  | Female | Reya           |
|          |                        |        | Ruhi           |
|          |                        |        | Sahana         |
|          |                        |        | Samiha         |
|          |                        |        | Samit          |
|          |                        |        | Shivangi       |
|          |                        |        | Suhana         |
|          |                        |        | Swasti         |
|          |                        |        | Tanmayi        |
|          |                        |        | Tishya         |
| Gujarati | Multispeaker-gujarati  | Male   | Aabharan       |
|          |                        |        | Aabhas         |
|          |                        |        | Aabhavannan    |
|          |                        |        | Aabheer        |
|          |                        |        | Aacharappan    |
|          |                        |        | Aacharya       |
|          |                        |        | Aachman        |
|          |                        |        | Aachuthan      |
|          |                        |        | Aadalarasan    |
|          |                        |        | Aadalarasu     |
| Nepali   | Multispeaker-Nepali    | Female | Alisha         |
|          |                        |        | Heena          |
|          |                        |        | Poudel nishita |
|          |                        |        | Shirisha       |
|          |                        |        | Shubhu         |
|          |                        |        | Soneeya        |
|          |                        |        | Baijanthi      |
|          |                        |        | Balapuspika    |
|          |                        |        | Bhavaroopa     |
|          |                        |        | Bhavisana      |
| Nepali   | Multispeaker-Nepali    | Male   | Indradu        |
|          |                        |        | Indragop       |
|          |                        |        | Iraianbu       |
|          |                        |        | Jaysha         |
|          |                        |        | Juddha         |
|          |                        |        | Sanani         |
|          |                        |        | Saudis         |
|          |                        |        | Sejun          |
|          |                        |        | Shalva         |
|          |                        |        | Shraey         |
| punjabi  | Multispeaker-punjabi   | Female | Hafa           |
|          |                        |        | Hafeeza        |
|          |                        |        | Haffafa        |
|          |                        |        | Hananiah       |
|          |                        |        | Harlee         |
|          |                        |        | Harleen        |
|          |                        |        | Harshida       |
|          |                        |        | Hartleigh      |
|          |                        |        | Harva          |
|          |                        |        | Harveen        |
| punjabi  | Multispeaker-punjabi   | Male   | Guneet         |
|          |                        |        | Gurjas         |
|          |                        |        | Gurkeerat      |
|          |                        |        | Gurleen        |
|          |                        |        | Gurman         |
|          |                        |        | Gurmeet        |
|          |                        |        | Gurnoor        |
|          |                        |        | Gursharan      |
|          |                        |        | Keerat         |
|          |                        |        | Kirpal         |
| bengali  | Multispeaker-bengali   | Female | Gaurita        |
|          |                        |        | Gehna          |
|          |                        |        | Golapi         |
|          |                        |        | Grahati        |
|          |                        |        | Haimanti       |
|          |                        |        | Indrani        |
|          |                        |        | Jemisha        |
|          |                        |        | Jhanvi         |
|          |                        |        | Jhumpa         |
|          |                        |        | Jiniya         |
| bengali  | Multispeaker-bengali   | Male   | Minati         |
|          |                        |        | Mithin         |
|          |                        |        | Modan          |
|          |                        |        | Modanatha      |
|          |                        |        | Monohar        |
|          |                        |        | Monojit        |
|          |                        |        | Mounish        |
|          |                        |        | Naba           |
|          |                        |        | Nabakumar      |
|          |                        |        | Nabhas         |

For more information about Gnani API's Please visit www.gnani.ai or reach out to hello@gnani.ai

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
    samplerate      : 8000
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
                          "audioEncoding": string <audio_encoding of the response string>,
                          "sampleRate" : integet <samplerate of the response audio >" 
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
- [NodeJs](https://github.com/gnani-ai/text-to-speech/tree/master/rest-codes/Nodejs-Client)
- [Python](https://github.com/gnani-ai/text-to-speech/tree/master/rest-codes/Python-Client)

### Support or Contact

#### Disclaimer
The Speech APIs are completely proprietary and are the sole property of Gnani.ai. We reserve the right to remove users access at any point of time. Note that the free access to the APIs are purely for testing or experimental purposes, and will be available to the users for a limited amount of time, after which they will have to purchase the commercial version. Gnani.ai will immediately remove access if the user is found to be using the APIs for commercial purposes. If you wish to obtain unlimited access, you can make an enquiry on the website or write to us at hello@gnani.ai. Also if you are having trouble please raise an issue or mail to us at hello@gnani.ai
