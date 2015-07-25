#!/usr/bin/env python
# encoding: utf-8
# vim: set et sw=4 ts=4 sts=4 fenc=utf-8
# Author: YuanLin

from __future__ import absolute_import
from flask_script import Manager, Server, Shell

from crawl.app import create_app

manager = Manager(create_app)
manager.add_option('-c', '--config', dest='config', required=False)
# manager.add_command('shell', Shell(make_context=make_shell_context))
manager.add_command('runserver', Server(
    use_debugger=True,
    use_reloader=True,
    host='0.0.0.0')
    )


if __name__ == '__main__':
    manager.run()
