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
import webapp2
import jinja2
import logging
import os

jinja_environment = jinja2.Environment(
  loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))#this little bit sets jinja's relative directory to match the directory name(dirname) of the current __file__, in this case, helloworld.py


class MainHandler(webapp2.RequestHandler):
    def get(self):
        hello_template = jinja_environment.get_template('templates/hello.html')
        self.response.out.write(hello_template.render())


        #put inside handler
        # sentence = 'Hello, world!'
        # self.response.write(self.TalkLikeAJedi(sentence))

        #put in handler
    #     n = 31
    #     if self.IsPrime(n):
    #       self.response.write('%d is prime' % n)
    #     else:
    #       self.response.write('%d is not prime' % n)
    #
    # def TalkLikeAJedi(self, sentence):
    #     """Converts a sentence to Jedi-speak. Adapted from Python 3 for Absolute Beginners: http://www.google.com/books?id=sQGFIX_0xCUC&pg=PA242"""
    #     # Strip whitespace and punctuation
    #     sentence = sentence.strip().rstrip('.!')
    #     # Lowercase the first letter of the sentence
    #     sentence = sentence[0].lower() + sentence[1:]
    #     # Piratify the text
    #     sentence = 'Patience, ' + sentence + ', my young padawan.'
    #
    #     return sentence
    #
    # def IsPrime(self, n):
    #     """A simple (but inefficient) check to see whether a number is prime."""
    #     for possible_factor in range(2, n):
    #         logging.info(possible_factor)
    #         if n % possible_factor == 0:
    #             logging.info('Found a factor: %d', possible_factor)
    #             return False
    #     return True





# /count
class CountHandler(webapp2.RequestHandler):
    def get(self):
        for x in range(1,101):
            self.response.write(str(x) + "<br>")

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/count', CountHandler)
], debug=True)
