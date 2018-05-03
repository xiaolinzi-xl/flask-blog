# -*- coding:utf-8 _*-
""" 
   @author: xiaolinzi
   @file: __init__.py.py 
   @time: 2018/05/01
"""
from flask import Blueprint

main = Blueprint('main',__name__)

from . import views,errors
