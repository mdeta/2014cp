#@+leo-ver=5-thin
#@+node:lee.20141215164031.94: * @file a40323101.py
#@@language python
#@@tabwidth -4
#@+<<decorations>>
#@+node:lee.20141215164031.95: ** <<decorations>>
import cherrypy
import random
from symbol import *
from jinja2 import Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader('templates'))
#@-<<decorations>>

#@+others
#@+node:lee.20141215164031.96: ** class Application
class Application(object):
    #@+others
    #@+node:lee.20141215164031.97: *3* def get_nav
    def get_nav(self):
        """
        取得 nav link
        """
        #(URL 路徑, anchor name)
        anchors = [('index', 'home'), ('guessForm', '猜數字'), ('multipliedTable', '乘法表'), ('asciiForm', '使用圖案印出字'), ('https://github.com/mdeta/2014cp', 'github repository'), ('/', 'back to list')]
        return anchors
    #@+node:lee.20141215164031.98: *3* def index
    @cherrypy.expose
    def index(self):
        """
        個人首頁
        """
        tmpl = env.get_template('personal_page.html')
        extra_content = {
            'title':'personal page',
            'photo_url':'http://placekitten.com/g/350/300',
            'name':'Lee',
            'ID':'123456789',
            'class':'nfu',
            'anchors':self.get_nav(),
            'self_evaluations':[('Porject7', 80), ('Porject8', 90), ('Porject9', 100)]
        }
        return tmpl.render(extra_content)

    #@+node:lee.20141215164031.99: *3* def guessForm
    @cherrypy.expose
    def guessForm(self, guessNumber=None):
        
        # get template
        tmpl = env.get_template('form.html')
        
        form = """
        <form action="" method="get">
          <label for="guessNumber">Guess Number(1~99)</label>
          <input name="guessNumber" type="text">
          <input type="submit" value="Send" class="button button-primary">
        </form>
        """
        
        # set common content
        extra_content = {'title':'guessform', 'form':form, 'anchors':self.get_nav()}
        
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



        message = {
            "welcome": "guess a number from 1 to 99",
            "error": "must input a number, your input is %s" % str(guessNumber),
            "successful": "correct! your input is %s answer is %d total count %d" % (str(guessNumber), answer, count),
            "smaller": "smaller than %s and total count %d" % (str(guessNumber), count),
            "bigger": "bigger than %s and total count %d" % (str(guessNumber), count),
        }

        if guessNumber is None:
            extra_content['output'] = message['welcome']
            return tmpl.render(extra_content)
        else:
            # convert guessNumber to int
            try:
                guessNumber = int(guessNumber)
            except:
                # if fail
                # throw error
                extra_content['output'] = message['error']
                return tmpl.render(extra_content)

            # convert ok, make count plus one, everytime
            cherrypy.session["count"] += 1

            if guessNumber == answer:
                # clear session count and answer
                del cherrypy.session["count"]
                del cherrypy.session["answer"]
                # throw successful
                extra_content['form'] = ''
                extra_content['output'] = message["successful"]+'<a href="guessForm">play again</a>'
            elif guessNumber > answer:
                # throw small than guessNumber
                extra_content['output'] = message["smaller"]
            else:
                # throw bigger than guessNumber
                extra_content['output'] = message["bigger"]
            return tmpl.render(extra_content)
    #@+node:lee.20141215164031.100: *3* def multipliedTable
    @cherrypy.expose
    def multipliedTable(self, first=None, second=None):
        tmpl = env.get_template('form.html')

        message = {
            'error': 'you must input correct type data.',
            'welcome': 'Welcome to multiplied table page.',
        }
        form = """
        <form action="" method="post">
          <label for="first">first number(an integer)</label>
          <input name="first" type="text">
          <label for="first">second number(an integer)</label>
          <input name="second" type="text">
          <input type="submit" value="Send" class="button button-primary">
        </form>
        """

        extra_content = {
            'title': 'multipliedTable', 'form': form, 'anchors': self.get_nav()}

        if first is None and second is None:
            extra_content['output'] = message.get('welcome')
            return tmpl.render(extra_content)

        try:
            first = int(first)
            second = int(second)
        except:
            #raise error
            extra_content['output'] = message.get('error')
            return tmpl.render(extra_content)
        output = ''
        for f in range(1, first + 1):
            for s in range(1, second + 1):
                output += str(f) + '*' + str(s) + '=' + str(f * s) + '<br/>'
        extra_content['output'] = '<p>' + output + '</p>'
        return tmpl.render(extra_content)
    #@+node:lee.20141215164031.101: *3* def asciiForm
    @cherrypy.expose
    def asciiForm(self, text=None):
        tmpl = env.get_template('form.html')
        
        messages = {
            'welcome':'welcome to ascii form',
        }
        form = """
        <form method="get" action="">
            <label for="text">Say....</label>
            <input type="text" name="text" />
            <input type="submit" value="Send" class="button button-primary">
        </form>
        """
        extra_content = {
            'title': 'asciiForm', 'form': form, 'anchors': self.get_nav()}
        
        if text is None:
            extra_content['output'] = messages.get('welcome')
        else:
            extra_content['output'] = self.asciiImage(text)
        return tmpl.render(extra_content)
    #@+node:lee.20141215164031.102: *3* def asciiImage
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
    #@-others
#@-others
#@-leo
