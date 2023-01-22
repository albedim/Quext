from fastanswers.model.entity.User import User
from fastanswers.utils.Util import Util

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

    def create(self, userId):
        self.passwordMagicLinkRepository.create(userId)
        return Util.createSuccessResponse(True, Util.LINK_SUCCESSFULLY_CREATED)