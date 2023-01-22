from flask import Blueprint, request
from flask_cors import cross_origin
from fastanswers.model.repository.UserRepository import UserRepository
from fastanswers.service.StackOverFlowService import StackOverFlowService
from fastanswers.service.UserService import UserService
from fastanswers.utils.Util import Util

stackOverFlow: Blueprint = Blueprint('StackOverFlowController', __name__, url_prefix=Util.getURL('stackoverflow'))

stackOverFlowService: StackOverFlowService = StackOverFlowService()


@stackOverFlow.route("/get", methods=['GET'])
@cross_origin()
def get():
    return stackOverFlowService.get(request.args.get('query'))



