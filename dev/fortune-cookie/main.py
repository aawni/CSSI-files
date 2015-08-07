#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2, random, jinja2, os
from google.appengine.ext import ndb

jinja_environment = jinja2.Environment(
  loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

class CookieHandler(webapp2.RequestHandler):
    def get(self):

        fortunes=[]
        fortunes.append('You will be run over by an ice cream truck.')
        fortunes.append('You will later regret the most recent decision you have made.')
        fortunes.append('You will get food poisoning.')
        fortunes.append('You will become filthy rich.')
        fortunes.append('You will find true love in a port-a-potty.')
        fortunes.append('You will inherit a horse who will become your best friend and eventually save your life.')
        fortunes.append('You will have 20 children and not be able to remember their names.')
        fortunes.append('You will move to Fiji.')
        fortunes.append('You will learn Portuguese.')
        fortunes.append('You will be reincarnated as a cockroach.')
        selected_fortune= fortunes[random.randint(0,9)]

        template_vars={"fortune": selected_fortune}
        template = jinja_environment.get_template('templates/cookie.html')
        self.response.out.write(template.render(template_vars))

class EightBallAnswer(ndb.Model):
    answer=ndb.StringProperty(required=True)
    question=ndb.StringProperty(required=True)

class EightBallHandler(webapp2.RequestHandler):
    def get(self):
        #type can be pos neg or neutral
        template_vars = {"question": self.request.get('question'), "type": self.request.get('type')}
        filtered_search= EightBallAnswer.query().filter(EightBallAnswer.question==template_vars["question"]).fetch()
        if filtered_search:
            template_vars["response"]=filtered_search[0].answer
        else:

            responses = []
            responses.append('It is certain')
            responses.append('It is decidedly so')
            responses.append('Without a doubt')
            responses.append('Yes definitely')
            responses.append('You may rely on it')
            responses.append('As I see it, yes')
            responses.append('Most likely')
            responses.append('Outlook good')
            responses.append('Yes')
            responses.append('Signs point to yes')
            responses.append('Reply hazy try again')
            responses.append('Ask again later')
            responses.append('Better not tell you now')
            responses.append('Cannot predict now')
            responses.append('Concentrate and ask again')
            responses.append('Do not count on it')
            responses.append('My reply is no')
            responses.append('My sources say no')
            responses.append('Outlook not so good')
            responses.append('Very doubtful')

            if (template_vars["type"]=="pos"):
                template_vars["response"]=responses[random.randint(0,11)]
            elif (template_vars["type"]=="neg"):
                template_vars["response"]=responses[random.randint(15,19)]
            elif (template_vars["type"]=="neutral"):
                template_vars["response"]=responses[random.randint(11,15)]
            else:
                template_vars["response"]=responses[random.randint(0,19)]

            answer_to_store = EightBallAnswer(question=template_vars["question"], answer= template_vars["response"])
            answer_to_store.put()

        template = jinja_environment.get_template('templates/eightball.html')
        self.response.out.write(template.render(template_vars))

class WhirlyBirdHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('templates/whirlybird.html')
        self.response.out.write(template.render())

    def post(self):
        # colors can be red, green, blue, yellow (lengths 3, 4, 5, 6)
        # numbers can be 1, 2, 3, 4
        #range of final_sum is (4,10), there sould be 7 options

        template_vars = {"color": self.request.get('color'), "number": self.request.get('number')}

        final_sum = len(template_vars["color"]) + int(template_vars["number"])
        fortunes=[]
        fortunes.append('You will later regret the most recent decision you have made.')
        fortunes.append('You will get food poisoning.')
        fortunes.append('You will become filthy rich.')
        fortunes.append('You will find true love in a port-a-potty.')
        fortunes.append('You will inherit a horse who will become your best friend and eventually save your life.')
        fortunes.append('You will have 20 children and not be able to remember their names.')
        fortunes.append('You will be reincarnated as a cockroach.')

        template_vars["fortune"]= fortunes[final_sum-4]

        template = jinja_environment.get_template('templates/whirlybird_result.html')
        self.response.out.write(template.render(template_vars))





app = webapp2.WSGIApplication([
    ('/', CookieHandler),
    ('/8ball', EightBallHandler),
    ('/whirlybird', WhirlyBirdHandler)
], debug=True)
