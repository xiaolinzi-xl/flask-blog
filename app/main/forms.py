# -*- coding:utf-8 _*-
""" 
   @author: xiaolinzi
   @file: forms.py 
   @time: 2018/05/01
"""
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired

class NameForm(FlaskForm):
    name = StringField('What is your name?',validators=[DataRequired()])
    submit = SubmitField('Submit')