# -*- coding:utf-8 _*-
""" 
   @author: xiaolinzi
   @file: __init__.py.py 
   @time: 2018/05/03
"""

from flask import Blueprint

auth = Blueprint('auth',__name__)

from . import views