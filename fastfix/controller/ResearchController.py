from flask import Blueprint, request
from flask_cors import cross_origin

from fastfix.controller.PasswordMagicLinkController import passwordMagicLinkService
from fastfix.model.repository.ResearchRepository import ResearchRepository
from fastfix.model.repository.UserRepository import UserRepository
from fastfix.service.ResearchService import ResearchService
from fastfix.service.UserService import UserService
from fastfix.utils.Util import Util

research: Blueprint = Blueprint('ResearchController', __name__, url_prefix=Util.getURL('research'))

researchRepository: ResearchRepository = ResearchRepository()
researchService: ResearchService = ResearchService(researchRepository)


@research.route("/add", methods=['POST'])
@cross_origin()
def add():
    return researchService.add(request.json)


@research.route("/get/<userId>", methods=['GET'])
@cross_origin()
def get(userId):
    return researchService.get(userId)




