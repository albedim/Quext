from flask import Blueprint, request
from flask_cors import cross_origin

from quext.service.PasswordMagicLinkService import createLink, getUserId
from quext.utils.Util import Util
from resources.config import config

passwordMagicLink: Blueprint = Blueprint('PasswordMagicLink', __name__, url_prefix=Util.getURL('password-magic-link'))


@passwordMagicLink.route("/create", methods=['POST'])
@cross_origin()
def createLinkReq():
    return createLink(request.json)


@passwordMagicLink.route("/get", methods=['POST'])
@cross_origin()
def getUserIdReq():
    return getUserId(request.json)




