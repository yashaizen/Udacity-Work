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

form="""
	<form method="post">
	<label>Month
		<input type="text">
	</label>
	<label>Date
		<input type="text">
	</label>
	<label>Year
		<input type="text">
	</label>
	<br>
	<input type="submit">
	</form>
	"""

months=["january","february","march","april","may","june","july","august","september","october","november" ,"december"]
 
abbv = dict((m[:3], m) for m in months )
def valid_month(month):
    if month:
        sm = month[:3].lower()
        return abbv.get(sm)

def valid_day(day):
    if day and day.isdigit():
        day = int(day)
        if day > 0 and day <= 31:
            return day
    

def valid_year(year):
    if year and year.isdigit():
        year = int(year)
        if year > 1990 and year < 2020:
            return year







class MainHandler(webapp2.RequestHandler):

    def get(self):
    	#self.response.headers['Content-Type'] = 'text/html'
        self.response.out.write(form)


    def post(self):
    	user_month = valid_month(self.request.get('month'))
    	user_day = valid_day(self.request.get('day'))
    	user_year = valid_year(self.request.get('year'))

    	if not (user_month and user_day and user_year):	
    	    self.response.out.write(form)

    	else :
		    self.response.out.write("Thanks")
	


app = webapp2.WSGIApplication([('/', MainHandler)
], debug=True)
