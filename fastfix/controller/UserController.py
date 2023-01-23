from flask import Blueprint, request
from flask_cors import cross_origin

from fastfix.controller.PasswordMagicLinkController import passwordMagicLinkService
from fastfix.model.repository.UserRepository import UserRepository
from fastfix.service.UserService import UserService
from fastfix.utils.Util import Util

user: Blueprint = Blueprint('UserController', __name__, url_prefix=Util.getURL('user'))

userRepository: UserRepository = UserRepository()
userService: UserService = UserService(userRepository, passwordMagicLinkService)


@user.route("/signin", methods=['POST'])
@cross_origin()
def signin():
    return userService.signin(request.json)


@user.route("/signup", methods=['POST'])
@cross_origin()
def signup():
    return userService.signup(request.json)


@user.route("/change-password", methods=['PUT'])
@cross_origin()
def changePassword():
    return userService.changePassword(request.json)




