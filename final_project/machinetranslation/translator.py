"""This module translates from english to french and viceversa"""

import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(f'{apikey}')
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(f'{url}')

def englishToFrench(englishText):
    """This function translates from english to french"""
    translation = language_translator.translate(
    text=f'{englishText}',
    model_id='en-fr').get_result()
    frenchText = translation["translations"][0]["translation"]
    return frenchText

def frenchToEnglish(frenchText):
    """This function translates from french to english"""
    translation = language_translator.translate(
    text=f'{frenchText}',
    model_id='fr-en').get_result()
    englishText = translation["translations"][0]["translation"]
    return englishText

