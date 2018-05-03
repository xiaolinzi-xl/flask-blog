# -*- coding:utf-8 _*-
""" 
   @author: xiaolinzi
   @file: views.py 
   @time: 2018/05/01
"""
from flask import render_template
from . import main


@main.route('/')
def index():
    return render_template('index.html')