from fastfix.model.entity.User import User
from fastfix.utils.Util import Util

#
# @author: albedim <dimaio.albe@gmail.com>
# Created on: 22/01/23
# Created at: 02:35
# Version: 1.0.0
# Description: This is the class for the user service
#


class PasswordMagicLinkService():

    def __init__(self, passwordMagicLinkRepository):
        self.passwordMagicLinkRepository = passwordMagicLinkRepository

    def create(self, request):
        self.passwordMagicLinkRepository.create(request['userId'])
        return Util.createSuccessResponse(True, Util.LINK_SUCCESSFULLY_CREATED)

    def get(self, request):
        passwordMagicLink = self.passwordMagicLinkRepository.get(request['link'])
        if passwordMagicLink is not None:
            return Util.createSuccessResponse(True, passwordMagicLink.userId)
        else:
            return Util.createWrongResponse(False, Util.USER_NOT_FOUND, 404)

    def delete(self, userId):
        self.passwordMagicLinkRepository.delete(userId)
        return Util.createSuccessResponse(True, None)