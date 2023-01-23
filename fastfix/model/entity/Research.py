import datetime
import math

from app import sql

#
# @author: albedim <dimaio.albe@gmail.com>
# Created on: 23/01/23
# Created at: 15:04
# Version: 1.0.0
# Description: This is the class for the research entity
#


class Research(sql.Model):
    id: int = sql.Column(sql.Integer, primary_key=True)
    name: str = sql.Column(sql.String(100), nullable=False)
    date: str = sql.Column(sql.String(24), nullable=True)
    userId: str = sql.Column(sql.Integer, nullable=False)

    def __init__(self, name, userId):
        self.name = name
        self.date = str(math.trunc(float(datetime.datetime.timestamp(datetime.datetime.now()))))
        self.userId = userId

    def toJson(self):
        return {
            'id': self.id,
            'name': self.name,
            'date': int(self.date),
            'userId': self.userId
        }
