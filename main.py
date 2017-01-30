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
import cgi
import re


form= """
<h1>Signup</h1>


<form  ="post">
    <table>
         <tr>
            <td><label for="username">Username</label></td>
            <td>
            <input  type="text" name = "username" ><br>
            </td>
        </tr>
        <tr>
            <td><label for="password">Password</label></td>
            <td>
            <input type="password" name = "password"><br>
            </td>
        </tr>
        <tr>
            <td><label for="verify password">Verify Password</label></td>
            <td>
            <input type="password" name = "verify"><br>
            </td>
        </tr>
        <tr>
            <td><label for="email">Email (otional)</label></td>
            <td>
            <input name = "email"><br>
            </td>
        </tr>
    </table>
    <input type="submit">

</form>
"""

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write(form)
        username = self.request.get('username')
        password = self.request.get('password')
        verify = self.request.get('verify')

    def post(self):
        self.response.write(form)
        if len('username') <3:
            self.response.write("No!")
        else:
            self.response.write("hello + username")
#class WelcomePage(object):


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
