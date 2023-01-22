import requests
from flask import jsonify

from fastanswers.utils.Util import Util


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

    def get(self, request: str):
        response = requests.get('https://api.stackexchange.com/2.3/search/advanced?order=asc&pagesize=80&sort=creation'
                                '&q=' + request.replace(" ", "%20") +
                                '&site=stackoverflow&filter=!-MBrU_IzpJ5H-AG6Bbzy.X-BYQe(2v-.J').json()['items']
        answers = self.getAnswers(response)
        return self.balance(answers)

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

    # get the answers which are tagged
    @classmethod
    def filterByTrust(cls, answers):
        finalResponse = []
        for answer in answers:
            if answer['is_accepted']:
                finalResponse.append(answer)
        return finalResponse

    # balances the results
    def balance(self, answers):
        trustedAnswers = self.filterByTrust(answers)
        if len(trustedAnswers) > 0:
            return self.cut(trustedAnswers)

    @classmethod
    def cut(cls, array: list):
        if len(array) >= 3:
            return jsonify([
                array[len(array) - 3],
                array[len(array) - 2],
                array[len(array) - 1]
            ])
        else:
            return jsonify(array)


