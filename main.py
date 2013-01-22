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
import os
import jinja2

from google.appengine.ext import db

jinja_environment = jinja2.Environment(autoescape = True,
                                        loader = jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__), 'Templates')))

class Recipie(db.Model):
    #The title of the recipie and the style of the beer
    title = db.StringProperty(required = True)
    style = db.StringProperty(required = True)
    #Lists the type of malts used, with the amount of each in (Unit?!)
    #in the corresponding list position (Consider checking to see if both lists are of equal length)
    malttype = db.ListProperty(str, required = True)
    maltamt = db.ListProperty(float, required = True)
    #Lists the type of hops used, with the amount of each in (Unit?!)
    #in the corresponding list position (Consider checking to see if both lists are of equal length)
    #hopboiltime is an integer that specifies at which point in the boil the hops should be added
    hoptype = db.ListProperty(str, required = True)
    hopamnt = db.ListProperty(float, required = True)
    hopboiltime = db.ListProperty(int, required = True)
    #Lists the type of extra fermentable ingredients used, with the amount of each in (Unit?!)
    #in the corresponding list position (Consider checking to see if both lists are of equal length)
    xtrafermentables = db.ListProperty(str)
    amtxtrafermentables = db.ListProperty(float)
    #Lists the type of extra boil ingredients used, with the amount of each in (Unit?!)
    #in the corresponding list position (Consider checking to see if both lists are of equal length)
    xtraboil = db.ListProperty(str)
    amtxtraboil = db.ListProperty(float)
    xtraboiltime = db.ListProperty(int)

    yeast = db.StringProperty(required = True)

    #This will be the function which generates a recipie based on certain inputs and parameters
    def render(self):
        pass

class MainHandler(webapp2.RequestHandler):
    def get(self):
    	template = jinja_environment.get_template('main.html')
        self.response.write(template.render())

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
