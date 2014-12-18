#@+leo-ver=5-thin
#@+node:lee.20141215164031.46: * @file application.py
#@@language python
#@@tabwidth -4

#@+<<decorations>>
#@+node:lee.20141215164031.47: ** <<decorations>>
import cherrypy
import os
from symbol import *
import random
from jinja2 import Environment, FileSystemLoader


#@-<<decorations>>

#@+others
#@+node:lee.20141215164031.48: ** folder setting
_curdir = os.path.join(os.getcwd(), os.path.dirname(__file__))

if 'OPENSHIFT_REPO_DIR' in os.environ.keys():
    # 表示程式在雲端執行
    data_dir = os.environ['OPENSHIFT_DATA_DIR']
    tmp_dir = data_dir + 'tmp'
    templates_dir = os.environ['OPENSHIFT_REPO_DIR'] + 'templates'
    static_dir = os.environ['OPENSHIFT_REPO_DIR'] + 'static'
else:
    # 表示程式在近端執行
    data_dir = _curdir + "local_data/"
    templates_dir = _curdir + "templates"
    tmp_dir = data_dir + 'tmp'
    static_dir = _curdir + "static"

env = Environment(loader=FileSystemLoader(templates_dir))

if not os.path.exists(data_dir):
    os.makedirs(data_dir)

if not os.path.exists(tmp_dir):
    os.makedirs(tmp_dir)
#@+node:lee.20141215164031.50: ** class Final


class Final(object):
    #@+others
    #@+node:lee.20141215164031.51: *3* _cp_config
    _cp_config = {

        'tools.encode.encoding': 'utf-8',
        'tools.sessions.on': True,
        'tools.sessions.storage_type': 'file',
        'tools.sessions.locking': 'early',
        'tools.sessions.storage_path': tmp_dir,
        'tools.sessions.timeout': 60,
    }
    #@+node:lee.20141215164031.52: *3* def index

    @cherrypy.expose
    def index(self):
        tmpl = env.get_template('index.html')
        std_list = ["403231{0:02d}".format(s) for s in range(1, 58)]
        return tmpl.render(title='index', students=std_list)
    #@-others
#@+node:lee.20141215164031.86: ** def error_page_404


def error_page_404(status, message, traceback, version):
    tmpl = env.get_template('404.html')
    return tmpl.render(title='404')

cherrypy.config.update({'error_page.404': error_page_404})
#@+node:lee.20141215164031.60: ** run env
#from std import a40323100

root = Final()

import std
import imp

for i in range(1, 58):
    try:
        mod = imp.load_source(
            "a403231%02d" % i, _curdir + "std/a403231%02d.py" % i)
        setattr(root, "403231%02d" % i, mod.Application())
    except:
        pass

application_conf = {
    '/static': {
        'tools.staticdir.on': True,
        'tools.staticdir.dir': static_dir
    },
    # 設定靜態 templates 檔案目錄對應
    '/templates': {
        'tools.staticdir.on': True,
        'tools.staticdir.dir': templates_dir,
        'tools.staticdir.index': 'index.htm'
    },
}

if 'OPENSHIFT_REPO_DIR' in os.environ.keys():
    # 在 openshift
    application = cherrypy.Application(root, config=application_conf)
else:
    # 在其他環境下執行
    cherrypy.quickstart(root, config=application_conf)
#@-others
#@-leo
