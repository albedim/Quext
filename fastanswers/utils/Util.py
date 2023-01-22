import datetime
from flask import jsonify
from resources.rest_service import config

#
# @author: albedim <dimaio.albe@gmail.com>
# Created on: 22/01/23
# Created at: 02:35
# Version: 1.0.0
# Description: This is the class for the utils
#


class Util():

    USER_NOT_FOUND = 'This user was not found'
    USER_SUCCESSFULLY_ADDED = 'This user was successfully added'
    USER_ALREADY_EXISTS = 'This user already exists'

    @classmethod
    def createList(cls, elements):
        response = []
        for element in elements:
            response.append(element.toJson())
        return jsonify(response)

    @classmethod
    def createSuccessResponse(cls, success, param):
        return jsonify({
            "date": str(datetime.datetime.now()),
            "success": success,
            "param": param,
            "code": 200,
        })

    @classmethod
    def createWrongResponse(cls, success, error, code):
        return jsonify({
            "date": str(datetime.datetime.now()),
            "success": success,
            "error": error,
            "code": code,
        })

    @classmethod
    def getURL(cls, controllerName):
        return '/api/v_' + config['version'].replace('.', '_') + '/' + controllerName

    @classmethod
    def hash(cls, password: str):
        chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
        hashedPassword = ""
        encryptedChars = "C0yZEIipDF23djS5muGMfnV6HtcW4q9BJLXlPakrghNeK1AsU8xRwQbzYO7Tov"
        for i in range(len(password)):
            for j in range(len(chars)):
                if password[i] == chars[j]:
                    hashedPassword += encryptedChars[j]
                    break
        return hashedPassword

    @classmethod
    def unHash(cls, password: str):
        chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
        unhashedPassword = ""
        encryptedChars = "C0yZEIipDF23djS5muGMfnV6HtcW4q9BJLXlPakrghNeK1AsU8xRwQbzYO7Tov"
        for i in range(len(password)):
            for j in range(len(encryptedChars)):
                if password[i] == encryptedChars[j]:
                    unhashedPassword += chars[j]
                    break
        return unhashedPassword
