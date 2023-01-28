import spacy
from googletrans import Translator
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation
from collections import Counter
from heapq import nlargest

import pandas as pd
import easyocr
import cv2
from quext.utils.Util import Util

#
# @author: albedim <dimaio.albe@gmail.com>
# Created on: 27/01/23
# Created at: 23:14
# Version: 1.0.0
# Description: This is the class for the summary service
#


class SummaryService():

    def __init__(self):
        pass

    def get(cls, request):
        imageName = Util.decodeImage(request.get('encodedImage'))
        text = cls.getText(imageName)
        Util.deleteFile(imageName)
        return Util.createSuccessResponse(True, cls.summary(request.get('language'), text))


    def getText(cls, image):
        img = cv2.imread('quext/files/' + image)
        reader = easyocr.Reader(['en'])
        result = reader.readtext(img, paragraph=False)
        df = pd.DataFrame(result)
        doc = ''
        for sentence in df[1]:
            doc += str(sentence) + ' '
        return doc


    def summary(cls, language, text):
        nlp = spacy.load('en_core_web_sm')
        translator = Translator()
        text = translator.translate(text, dest='en').text
        doc = nlp(text)
        keyword = []
        stopwords = list(STOP_WORDS)
        pos_tag = ['PROPN', 'ADJ', 'NOUN', 'VERB']
        for token in doc:
            if token.text in stopwords or token.text in punctuation:
                continue
            if token.pos_ in pos_tag:
                keyword.append(token.text)

        freq_word = Counter(keyword)
        sent_strength = {}
        for sent in doc.sents:
            for word in sent:
                if word.text in freq_word.keys():
                    if sent in sent_strength.keys():
                        sent_strength[sent] += freq_word[word.text]
                    else:
                        sent_strength[sent] = freq_word[word.text]

        summarized_sentences = nlargest(cls.getStrength(text), sent_strength, key=sent_strength.get)
        newText = ''
        for sentence in summarized_sentences:
            newText += str(sentence)

        return translator.translate(newText, dest=language).text


    def getStrength(self, text):
        if len(text) <= 1500:
            return 2
        if 1500 < len(text) <= 2740:
            return 4
        if len(text) > 2740:
            return 6
