from quext.model.entity.User import User
from quext.utils.Util import Util

#
# @author: albedim <dimaio.albe@gmail.com>
# Created on: 22/01/23
# Created at: 02:35
# Version: 1.0.0
# Description: This is the class for the user service
#


class UserService():

    def __init__(self, userRepository, passwordMagicLinkService):
        self.passwordMagicLinkService = passwordMagicLinkService
        self.userRepository = userRepository

    def signin(self, request: dict):
        try:
            user: User = self.userRepository.signin(
                request.get('email'),
                Util.hash(request.get('password'))
            )
            if user is not None:
                return Util.createSuccessResponse(True, user.userId)
            else:
                return Util.createWrongResponse(False, Util.USER_NOT_FOUND, 404)
        except AttributeError:
            return Util.createWrongResponse(False, Util.INVALID_REQUEST, 405)

    def exists(self, email) -> bool:
        return self.userRepository.exists(email) > 0

    def changePassword(self, request):
        try:
            self.userRepository.changePassword(
                request.get('userId'),
                Util.hash(request.get('password'))
            )
            self.passwordMagicLinkService.delete(request.get('userId'))
            return Util.createSuccessResponse(True, Util.USER_PASSWORD_SUCCESSFULLY_CHANGED)
        except AttributeError:
            return Util.createWrongResponse(False, Util.INVALID_REQUEST, 405)

    def signup(self, request: dict):
        try:
            if not self.exists(request.get('email')):
                self.userRepository.signup(
                    request.get('name'),
                    request.get('email'),
                    Util.hash(request.get('password'))
                )
                return Util.createSuccessResponse(True, Util.USER_SUCCESSFULLY_ADDED)
            else:
                return Util.createWrongResponse(False, Util.USER_ALREADY_EXISTS, 403)
        except AttributeError:
            return Util.createWrongResponse(False, Util.INVALID_REQUEST, 405)