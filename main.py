# pip install ibm_watson wget

from ibm_watson import SpeechToTextV1 # Libreria de Voz a Texto
import json # Libreria para manejar JSON
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator # Libreria para identificacion

from pandas.io.json import json_normalize # Modulo de la libreria pandas para manejar datos en JSON

url_s2t = "https://stream.watsonplatform.net/speech-to-text/api" # URL conexion API

iam_apikey_s2t = "kXg5FLdYOG7iCTr9Zk1z_030MN4lH5njPBJdaex2B0IS" # APIKEY

authenticator = IAMAuthenticator(iam_apikey_s2t) # Nuevo ojeto con la clave
s2t = SpeechToTextV1(authenticator=authenticator) # Nuevo objeto de SpeechToText incluyendo la autenticacion
s2t.set_service_url(url_s2t) # Iniciamos el servicio y no conectamos a la URL
print(s2t) # Mostramos si recibe respuesta

filename='audio.ogg' # Nombre del archivo

with open(filename, mode="rb")  as wav: # abrimos el archivo en lectura binaria como wav
    response = s2t.recognize(audio=wav, content_type='audio/ogg') # esperamos la respuesta del servicio con su metodo reconocer


print(response.result) # Mostramos la respuesta

jnor=json_normalize(response.result['results'],"alternatives") # Hacemos mas legible la respuesta y la guardamos en jnor

print(jnor) # Mostramos la respuesta mas legible en JSON

print(response) 

recognized_text=response.result['results'][0]["alternatives"][0]["transcript"]
type(recognized_text)


from ibm_watson import LanguageTranslatorV3

url_lt='https://gateway.watsonplatform.net/language-translator/api'

apikey_lt='1CTb7nGfTV3HJbsc-0D79st08ezuTCgYM1qRVJMkZcPz'

version_lt='2018-05-01'

authenticator = IAMAuthenticator(apikey_lt)
language_translator = LanguageTranslatorV3(version=version_lt,authenticator=authenticator)
language_translator.set_service_url(url_lt)
print(language_translator)

#from pandas.io.json import json_normalize

json_normalize(language_translator.list_identifiable_languages().get_result(), "languages")

translation_response = language_translator.translate(\
    text=recognized_text, model_id='en-es')
print(translation_response)

translation=translation_response.get_result()
print(translation)

spanish_translation =translation['translations'][0]['translation']
print(spanish_translation)

translation_new = language_translator.translate(text=spanish_translation ,model_id='es-en').get_result()

translation_eng=translation_new['translations'][0]['translation']
print(translation_eng)

French_translation=language_translator.translate(text=translation_eng , model_id='en-fr').get_result()

frances=French_translation['translations'][0]['translation']
print(frances)