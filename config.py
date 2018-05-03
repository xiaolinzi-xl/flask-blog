# -*- coding:utf-8 _*-
""" 
   @author: xiaolinzi
   @file: config.py 
   @time: 2018/05/01
"""
import os
from develop_info import develop_envs

class Config:
    SECRET_KEY = develop_envs.get('SECRET_KEY') or 'hard to guess string'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = develop_envs.get('SQLALCHEMY_DATABASE_URI')

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True


class ProductionConfig(Config):
    DEBUG = False


config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}

