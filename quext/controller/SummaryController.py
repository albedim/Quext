from flask import Blueprint, request
from flask_cors import cross_origin

from quext.service.SummaryService import getSummary
from quext.utils.Util import Util

summary: Blueprint = Blueprint('SummaryController', __name__, url_prefix=Util.getURL('summary'))


@summary.route("/get", methods=['POST'])
@cross_origin()
def getSummaryReq():
    return getSummary(request.json)




