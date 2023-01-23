from flask import Blueprint, request
from flask_cors import cross_origin
from fastfix.model.repository.UserRepository import UserRepository
from fastfix.service.StackOverFlowService import StackOverFlowService
from fastfix.service.UserService import UserService
from fastfix.utils.Util import Util

stackOverFlow: Blueprint = Blueprint('StackOverFlowController', __name__, url_prefix=Util.getURL('stackoverflow'))

stackOverFlowService: StackOverFlowService = StackOverFlowService()


@stackOverFlow.route("/get", methods=['GET'])
@cross_origin()
def get():
    return stackOverFlowService.get(request.args.get('query'), request.args.get('language'))



