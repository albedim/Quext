from flask import jsonify

from fastfix.model.entity.User import User
from fastfix.utils.Util import Util


#
# @author: albedim <dimaio.albe@gmail.com>
# Created on: 23/01/23
# Created at: 15:04
# Version: 1.0.0
# Description: This is the class for the research service
#


class ResearchService():

    def __init__(self, researchRepository):
        self.researchRepository = researchRepository

    def add(self, request):
        self.researchRepository.add(request.get('name'), request.get('userId'))
        return Util.createSuccessResponse(True, Util.RESEARCH_SUCCESSFULLY_ADDED)

    def get(self, userId):
        return Util.createList(self.researchRepository.get(userId))
