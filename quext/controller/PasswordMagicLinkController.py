from flask import Blueprint, request
from flask_cors import cross_origin

from quext.model.repository.PasswordMagicLinkRepository import PasswordMagicLinkRepository
from quext.service.PasswordMagicLinkService import PasswordMagicLinkService
from quext.utils.Util import Util

passwordMagicLink: Blueprint = Blueprint('PasswordMagicLink', __name__, url_prefix=Util.getURL('password-magic-link'))

passwordMagicLinkRepository: PasswordMagicLinkRepository = PasswordMagicLinkRepository()
passwordMagicLinkService: PasswordMagicLinkService = PasswordMagicLinkService(passwordMagicLinkRepository)


@passwordMagicLink.route("/create", methods=['POST'])
@cross_origin()
def signin():
    return passwordMagicLinkService.create(request.json)


@passwordMagicLink.route("/get", methods=['POST'])
@cross_origin()
def get():
    return passwordMagicLinkService.get(request.json)




