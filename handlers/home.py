import render
import webapp2

from google.appengine.ext import ndb


class WhatPeopleEat(ndb.Model):
  person = ndb.StringProperty(required=True)
  food = ndb.StringProperty(required=True)
  amount = ndb.IntegerProperty(required=True)


class Handler(webapp2.RequestHandler):

  def get(self):
    names = ['sycs-100', 'sycs-135', 'sycs-181', 'SYCS-189', 'ECON-103']
    template_values = {'names': names}
    render.Template('home.html', template_values, self.response)

  def post(self):
    food = self.request.get('food')
    amount = self.request.get('amount')
    name = self.request.get('name')
    WhatPeopleEat(person=name, food=food, amount=int(amount)).put()
    text = 'Awesome people eat ' + food
    render.text(text, self.response)