from flask import Blueprint, request
from flask_cors import cross_origin

from quext.service.SummaryService import getSummaryByImage, getSummaryByText
from quext.utils.Util import Util

summary: Blueprint = Blueprint('SummaryController', __name__, url_prefix=Util.getURL('summary'))


@summary.route("/image/get", methods=['POST'])
@cross_origin()
def getSummaryByImageReq():
    return getSummaryByImage(request.json)


@summary.route("/text/get", methods=['POST'])
@cross_origin()
def getSummaryByTextReq():
    return getSummaryByText(request.json)




