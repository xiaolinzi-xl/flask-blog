# -*- coding:utf-8 _*-
""" 
   @author: xiaolinzi
   @file: manage.py 
   @time: 2018/05/01
"""
from flask_migrate import Migrate,MigrateCommand
from flask_script import Manager,Shell
from app import create_app, db
from app.models import User, Role

app = create_app('default')
migrate = Migrate(app, db)
manager = Manager(app)


def make_shell_context():
    return dict(app=app,db=db, User=User, Role=Role)

manager.add_command('db',MigrateCommand)
manager.add_command('shell',Shell(make_context=make_shell_context))

if __name__ == '__main__':
    manager.run()