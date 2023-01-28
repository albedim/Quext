from flask import Blueprint, request
from flask_cors import cross_origin

from quext.controller.PasswordMagicLinkController import passwordMagicLinkService
from quext.model.repository.UserRepository import UserRepository
from quext.service.SummaryService import SummaryService
from quext.service.UserService import UserService
from quext.utils.Util import Util

summary: Blueprint = Blueprint('SummaryController', __name__, url_prefix=Util.getURL('summary'))

summaryService: SummaryService = SummaryService()


@summary.route("/get", methods=['POST'])
@cross_origin()
def get():
    return summaryService.get(request.json)




