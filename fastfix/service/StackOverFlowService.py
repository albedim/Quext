import datetime

import requests
from fastfix.service.TranslatingService import TranslatingService
import translators.server as ts
from flask import jsonify
from googletrans import Translator

from fastfix.utils.Util import Util


#
# @author: albedim <dimaio.albe@gmail.com>
# Created on: 22/01/23
# Created at: 02:35
# Version: 1.0.0
# Description: This is the class for the stackOverFlow service
#

class StackOverFlowService():

    def __init__(self):
        pass

    def get(self, request: str, language: str):
        newRequest = TranslatingService.translate(request.replace("%20", " "), 'en')
        response = requests.get('https://api.stackexchange.com/2.3/search/advanced?pagesize=80' +
                                '&order=desc&sort=activity&title='+newRequest.replace(" ", "%20") +
                                '&site=stackoverflow&filter=!-MBrU_IzpJ5H-AG6Bbzy.X-BYQe(2v-.J').json()['items']
        answers = self.getAnswers(response)
        return self.balance(answers, language)

    # get the answers from json response
    @classmethod
    def getAnswers(cls, response):
        finalResponse = []
        for question in response:
            if "answers" in question:
                answers = question['answers']
                for answer in answers:
                    finalResponse.append(answer)
        return finalResponse

    # get the answers which are accepted
    @classmethod
    def filterByTrust(cls, answers, language):
        finalResponse = []
        for answer in answers:
            if answer['is_accepted']:
                finalResponse.append({
                    'timestamp': int(datetime.datetime.timestamp(datetime.datetime.now())),
                    'title': TranslatingService.translate(answer['title'], language),
                    'answer': TranslatingService.join(answer['body'], language)
                })
        return finalResponse

    # balances the results
    def balance(self, answers, language):
        trustedAnswers = self.filterByTrust(answers, language)
        if len(trustedAnswers) > 0:
            return jsonify(trustedAnswers)
        return Util.createWrongResponse(False, Util.RESULTS_NOT_FOUND, 404)


