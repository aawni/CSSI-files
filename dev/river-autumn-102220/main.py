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
import os
import webapp2
import jinja2
from google.appengine.ext import ndb


JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class Song(ndb.Model):
    name = ndb.StringProperty(required=True)

class Artist(ndb.Model):
    name = ndb.StringProperty(required=True)
    song_keys = ndb.KeyProperty(Song, repeated=True)

class MainHandler(webapp2.RequestHandler):
    def get(self):
        # Get all of the student data from the datastore
        query = Artist.query()
        artist_data = query.fetch()
        # Pass the data to the template
        template_values = {
            'artists' : artist_data
        }
        template = JINJA_ENVIRONMENT.get_template('index.html')
        self.response.write(template.render(template_values))

    def post(self):
        # Get the artist and song title from the form
        artist = self.request.get('artist')
        song = self.request.get('song_title')

        if artist and song:

            query = Artist.query()
            artist_data = query.fetch()
            in_artist_data=False
            counter=0
            index_of_artist=0
            for artist1 in artist_data:
                if artist1.name==artist:
                    in_artist_data=True
                    index_of_artist=counter
                counter+=1

            if in_artist_data:
                song_to_add = Song(name=song)
                song_to_add.put()
                artist_to_add=artist_data[index_of_artist]
                artist_to_add.song_keys.append(song_to_add.key)
                artist_to_add.put()
            else:
                artist_to_add = Artist(name=artist)
                artist_to_add.put()
                song_to_add = Song(name=song)
                song_to_add.put()
                artist_to_add.song_keys.append(song_to_add.key)
                artist_to_add.put()
        # Redirect to the main handler that will render the template
            self.redirect('/')

        else:
            self.redirect('/')


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
