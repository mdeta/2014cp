#@+leo-ver=5-thin
#@+node:lee.20141212200847.12: * @file application.py
#@@language python
#@@tabwidth -4

#@+<<decorations>>
#@+node:lee.20141212201841.2: ** <<decorations>>
import cherrypy
import os
from symbol import *
import random
#@-<<decorations>>

#@+others
#@+node:lee.20141215164031.40: ** folder setting
_curdir = os.path.join(os.getcwd(), os.path.dirname(__file__))

if 'OPENSHIFT_REPO_DIR' in os.environ.keys():
    # 表示程式在雲端執行
    data_dir = os.environ['OPENSHIFT_DATA_DIR']
    tmp_dir = data_dir + 'tmp'
else:
    # 表示程式在近端執行
    data_dir = _curdir + "/local_data/"

tmp_dir = data_dir + 'tmp'

if not os.path.exists(data_dir):
    os.makedirs(data_dir)

if not os.path.exists(tmp_dir):
    os.makedirs(tmp_dir)
#@+node:lee.20141212201841.9: ** template
template = """
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>FinalProject</title>
    <style type="text/css">
        body{
            font-family: "Ubuntu","Helvetica Neue",Arial,sans-serif;
        }
        .center{
            text-align: center;
        }
        #headline{
            display: block;
        }
        #headline .logo{
            margin-left: 2em;
            float: left;
            color:#42253B;
        }
        .supertitle{
            font-weight: 300;
        }

        #headline .meta{
            float: right;
            margin-right: 3em;
        }
        #headline .meta li{
            list-style: none;
            color:#4C2C69;
        }
        .clearboth{
            clear:both;
        }

        nav{
            border-top: 3px dashed #7E7F9A;
            border-bottom: 3px dashed #7E7F9A;
            margin-bottom: 1em;
        }
        nav ul{
            padding: 0;
            margin: 5px auto;
            list-style: none;
            font-size: 0;
        }
        nav ul li{
            font-size: 20px;
            background-color: #EB9486;
            color: white;
            display: inline-block;
            width: 20%;
            height: 3em;
            line-height: 3em;
            text-align: center;
            text-transform: uppercase;
            -webkit-box-sizing: border-box;
            -moz-box-sizing: border-box;
            box-sizing: border-box;
            outline: 2px solid white;
            overflow: hidden;
        }

        nav ul li:hover{
            background: #F3DE8A;
        }


        nav a{
            text-decoration: none;
            color:inherit;
            display: block;
        }
        #content{

        }

    </style>
</head>
<body>
    <div id="headline">
        <div class="logo"><h1 class="supertitle">Computer Programming</h1></div>
        <div class="meta">
            <ul>
                <li class="name">Bill</li>
            </ul>
        </div>
        <div class="clearboth"></div>
    </div>
    <nav>
        <ul>
            <li><a href="/">Home</a></li>
            <li>link2</li>
            <li>link3</li>
            <li>link3</li>
            <li>link3</li>
        </ul>
    </nav>
    <div id="content">
        %s
    </div>
</body>
</html>
"""
#@+node:lee.20141212201841.4: ** class Final


class Final(object):
    #@+others
    #@+node:lee.20141212201841.13: *3* _cp_config
    _cp_config = {

        'tools.encode.encoding': 'utf-8',
        'tools.sessions.on': True,
        'tools.sessions.storage_type': 'file',
        'tools.sessions.locking': 'early',
        'tools.sessions.storage_path': tmp_dir,

        'tools.sessions.timeout': 60,
    }
    #@+node:lee.20141212201841.5: *3* def index

    @cherrypy.expose
    def index(self):
        return self.use_template("""<h1>hello world</h1>""")
    #@+node:lee.20141212201841.6: *3* def asciiImage

    def asciiImage(self, inp):
        if inp == '':
            return ''
        row = 9

        content = ""

        for r in range(row):
            for c in inp:
                out_symbol = symbolDict.get(c, symbolDict[""])(r)
                content += out_symbol
            content += "<br />"
        return content
    #@+node:lee.20141212201841.11: *3* def asciiForm

    @cherrypy.expose
    def asciiForm(self):
        # form, action to asciiOutput
        content = """
            <h1>say something</h1>
            <form method="get" action="/asciiOutput">
                <input type="text" name="text" />
                <button type="submit">Say it now!</button>
            </form>
        """
        return self.use_template(content)
    #@+node:lee.20141212201841.8: *3* def asciiOutput

    @cherrypy.expose
    def asciiOutput(self, text):
        # output asciiImage
        return self.use_template(self.asciiImage(text))
    #@+node:lee.20141212201841.10: *3* def use_template

    def use_template(self, content):
        start = """
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>FinalProject</title>
        <style type="text/css">
            body{
                font-family: "Ubuntu","Helvetica Neue",Arial,sans-serif;
            }
            .center{
                text-align: center;
            }
            #headline{
                display: block;
            }
            #headline .logo{
                margin-left: 2em;
                float: left;
                color:#42253B;
            }
            #headline .author{
                font-size:2em;
            }
            .supertitle{
                font-weight: 300;
            }

            #headline .meta{
                float: right;
                margin-right: 3em;
            }
            #headline .meta li{
                list-style: none;
                color:#4C2C69;
            }
            .clearboth{
                clear:both;
            }

            nav{
                border-top: 3px dashed #7E7F9A;
                border-bottom: 3px dashed #7E7F9A;
                margin-bottom: 1em;
            }
            nav ul{
                padding: 0;
                margin: 5px auto;
                list-style: none;
                font-size: 0;
            }
            nav ul li{
                font-size: 20px;
                background-color: #EB9486;
                color: white;
                display: inline-block;
                width: 20%;
                height: 3em;
                line-height: 3em;
                text-align: center;
                text-transform: uppercase;
                -webkit-box-sizing: border-box;
                -moz-box-sizing: border-box;
                box-sizing: border-box;
                outline: 2px solid white;
                overflow: hidden;
            }

            nav ul li:hover{
                background: #F3DE8A;
            }


            nav a{
                text-decoration: none;
                color:inherit;
                display: block;
            }
            #content{

            }

        </style>
    </head>
    <body>
        <div id="headline">
            <div class="logo"><h1 class="supertitle">Computer Programming</h1></div>
            <div class="meta">
                <ul>
                    <li class="author">Author</li>
                </ul>
            </div>
            <div class="clearboth"></div>
        </div>
        <nav>
            <ul>
                <li><a href="/">Home</a></li>
        """
        Links = ""
        for L in self.link():
            Links += '<li><a href="/%s">%s</a></li>' % (L, L)
        rest_start = """
            </ul>
        </nav>
        <div id="content">
        """

        end = """
         </div>
        </body>
        </html>
        """
        return start + Links + rest_start + content + end
    #@+node:lee.20141212201841.12: *3* def guessForm

    @cherrypy.expose
    def guessForm(self, guessNumber=None):
        # get count from session
        count = cherrypy.session.get("count", None)
        # if is None, it mean it does not exist
        if not count:
            # create one
            count = cherrypy.session["count"] = 0

        # get answer from session
        answer = cherrypy.session.get("answer", None)
        # if is None, it mean it does not exist
        if not answer:
            # create one
            answer = cherrypy.session["answer"] = random.randint(1, 100)

        form = """
        <form>
        <input type="text" name="guessNumber">
        <input type="submit" value="guessNow!">
        </form>
        """

        message = {
            "welcome": "guess a number from 1 to 99",
            "error": "must input a number, your input is %s" % str(guessNumber),
            "successful": "correct! your input is %s answer is %d total count %d" % (str(guessNumber), answer, count),
            "smaller": "smaller than %s and total count %d" % (str(guessNumber), count),
            "bigger": "bigger than %s and total count %d" % (str(guessNumber), count),
        }

        if guessNumber is None:
            return self.use_template("<h1>" + message["welcome"] + "</h1>" + form)
        else:
            # convert guessNumber to int
            try:
                guessNumber = int(guessNumber)
            except:
                # if fail
                # throw error
                return self.use_template("<h1>" + message["error"] + "</h1>" + form)

            # convert ok, make count plus one, everytime
            cherrypy.session["count"] += 1

            if guessNumber == answer:
                # clear session count and answer
                del cherrypy.session["count"]
                del cherrypy.session["answer"]
                # throw successful
                return self.use_template("<h1>" + message["successful"] + '</h1><a href="/guessForm">play again</a>')
            elif guessNumber > answer:
                # throw small than guessNumber
                return self.use_template("<h1>" + message["smaller"] + "</h1>" + form)
            else:
                # throw bigger than guessNumber
                return self.use_template("<h1>" + message["bigger"] + "</h1>" + form)
    #@+node:lee.20141212201841.14: *3* def link

    def link(self):
        aviable_link = ["asciiForm", "guessForm"]
        return aviable_link
    #@-others
#@+node:lee.20141212201841.3: ** run env
if 'OPENSHIFT_REPO_DIR' in os.environ.keys():
    # 在 openshift
    application = cherrypy.Application(Final())
else:
    # 在其他環境下執行
    cherrypy.quickstart(Final())
#@-others
#@-leo
