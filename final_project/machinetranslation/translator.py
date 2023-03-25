"""
This module provides functions for translating text between English and French
"""
import os
from ibm_watson import LanguageTranslatorV3
from ibm_watson import ApiException
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

dirname = os.path.dirname(os.path.abspath(__file__))

dotenv_path = os.path.join(dirname,'env','.env')

load_dotenv(dotenv_path)

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(version='2018-05-01',authenticator=authenticator)

language_translator.set_service_url(url)

def english_to_french(englishText):
    """
    Translate English text to French.

    Args:
        englishText (String): Text in English

    Returns:
        String: French translation of English text
    """
    french_text = None 
    if bool(englishText):
        try:
            translation = language_translator.translate(text=englishText
            ,model_id='en-fr').get_result()
            french_text = translation['translations'][0]['translation']
        except ApiException as ex:
            print("Error calling API"+str(ex.code) + ": " + ex.message)
    else:
        raise ValueError('text must be provided')
    return french_text

def french_to_english(frenchText):
    """
    Translate French text to English.

    Args:
        frenchText (String): Text in French

    Returns:
        String: English translation of French text
    """
    english_text = None
    if bool(frenchText):
        try:
            translation = language_translator.translate(text=frenchText
            ,model_id='fr-en').get_result()
            english_text = translation['translations'][0]['translation']
        except ApiException as ex:
            print("Error calling API"+str(ex.code) + ": " + ex.message)
    else:
        raise ValueError('text must be provided')
    return english_text


if __name__ == "__main__":
    V_TEXT = "I would like to translate this text some issue with the sentence formation"
    print(english_to_french(V_TEXT))
    print(french_to_english(english_to_french(V_TEXT)))
    