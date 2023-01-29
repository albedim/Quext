from cv2 import cv2
from googletrans import Translator

from quext.utils.Util import Util
from nltk.corpus import stopwords
from nltk.cluster.util import cosine_distance

import pandas as pd
import easyocr
import numpy as np
import networkx as nx
import nltk

from quext.utils.exceptions.IncorrectApiKeyException import IncorrectApiKeyException

nltk.download('stopwords')


#
# @author: albedim <dimaio.albe@gmail.com>
# Created on: 27/01/23
# Created at: 23:14
# Version: 1.0.0
# Description: This is the class for the summary service
#


def getSummary(request):
    try:
        Util.checkApiKey(request['API_KEY'])  # if not, raise exception
        imageName = Util.decodeImage(request['encodedImage'])
        text = getText(imageName)
        Util.deleteFile(imageName)
        return Util.createSuccessResponse(True, generate_summary(text, 4, request['language']))
    except KeyError:
        return Util.createWrongResponse(False, Util.INVALID_REQUEST, 405)
    except IncorrectApiKeyException:
        return Util.createWrongResponse(False, Util.INCORRECT_API_KEY, 403)


def getText(image):
    translator = Translator()
    img = cv2.imread('quext/files/' + image)
    reader = easyocr.Reader(['en'])
    result = reader.readtext(img, paragraph=False)
    df = pd.DataFrame(result)
    doc = ''
    for sentence in df[1]:
        doc += str(sentence) + ' '
    return translator.translate(doc, dest='en').text


def readArticle(text):
    article = text.split(". ")
    sentences = []

    for sentence in article:
        sentences.append(sentence.replace("[^a-zA-Z]", " ").split(" "))
    sentences.pop()

    return sentences


def sentenceSimilarity(sent1, sent2, stopwords=None):
    if stopwords is None:
        stopwords = []

    sent1 = [w.lower() for w in sent1]
    sent2 = [w.lower() for w in sent2]

    allWords = list(set(sent1 + sent2))

    vector1 = [0] * len(allWords)
    vector2 = [0] * len(allWords)

    # build the vector for the first sentence
    for w in sent1:
        if w in stopwords:
            continue
        vector1[allWords.index(w)] += 1

    # build the vector for the second sentence
    for w in sent2:
        if w in stopwords:
            continue
        vector2[allWords.index(w)] += 1

    return 1 - cosine_distance(vector1, vector2)


def buildSimilarityMatrix(sentences, stop_words):
    # Create an empty similarity matrix
    similarityMatrix = np.zeros((len(sentences), len(sentences)))

    for idx1 in range(len(sentences)):
        for idx2 in range(len(sentences)):
            if idx1 == idx2:  # ignore if both are same sentences
                continue
            similarityMatrix[idx1][idx2] = sentenceSimilarity(sentences[idx1], sentences[idx2], stop_words)

    return similarityMatrix


def generateSummary(text, top_n, language):
    stopWords = stopwords.words('english')
    summarizeText = []

    # Step 1 - Read text anc split it
    sentences = readArticle(text)

    # Step 2 - Generate Similary Martix across sentences
    sentenceSimilarityMartix = buildSimilarityMatrix(sentences, stopWords)

    # Step 3 - Rank sentences in similarity martix
    sentence_similarity_graph = nx.from_numpy_array(sentenceSimilarityMartix)
    scores = nx.pagerank(sentence_similarity_graph)

    # Step 4 - Sort the rank and pick top sentences
    ranked_sentence = sorted(((scores[i], s) for i, s in enumerate(sentences)), reverse=True)

    for i in range(top_n):
        summarizeText.append(" ".join(ranked_sentence[i][1]))

    # Step 5 - Offcourse, output the summarize text
    translator = Translator()
    return translator.translate(". ".join(summarizeText), dest=language).text
