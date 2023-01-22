from fastanswers.model.entity.User import User
from fastanswers.utils.Util import Util

#
# @author: albedim <dimaio.albe@gmail.com>
# Created on: 22/01/23
# Created at: 02:35
# Version: 1.0.0
# Description: This is the class for the user service
#


class UserService():

    def __init__(self, userRepository):
        self.userRepository = userRepository

    def signin(self, request: dict):
        user: User = self.userRepository.signin(
            request.get('email'),
            Util.hash(request.get('password'))
        )
        if user is not None:
            return Util.createSuccessResponse(True, user.userId)
        else:
            return Util.createWrongResponse(False, Util.USER_NOT_FOUND, 404)

    def exists(self, email) -> bool:
        return self.userRepository.exists(email) > 0

    def signup(self, request: dict):
        if not self.exists(request.get('email')):
            self.userRepository.signup(
                request.get('name'),
                request.get('email'),
                Util.hash(request.get('password'))
            )
            return Util.createSuccessResponse(True, Util.USER_SUCCESSFULLY_ADDED)
        else:
            return Util.createWrongResponse(False, Util.USER_ALREADY_EXISTS, 403)