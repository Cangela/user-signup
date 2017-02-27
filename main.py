import webapp2
import cgi
import re

form = """
<!DOCTYPE html>
    <html>
        <head>
        <style>
            .error {color: red;
            }
        </style>
        </head>
        <body>
            <h1>Signup</h1>
            <form  method="post">
            <table>
                <tr>
                    <td><label for="username">Username</label></td>
                <td>
                    <input  type="text" name = "username" value = "%(username)s">
                    <label class="error">%(error_username)s</label>
                </td>
                </tr>

                <tr>
                    <td><label for="password">Password</label></td>
                <td>
                    <input type="password" name = "password" value="">
                    <label class="error">%(error_password)s</label>
                </td>
                </tr>

                <tr>
                    <td><label for="verify password">Verify Password</label></td>
                <td>
                    <input type="password" name = "verify" value="">
                    <label class="error">%(error_verify)s</label>

                </td>
                </tr>
                <tr>
                    <td><label for="email">Email (optional)</label></td>
                <td>
                    <input name = "email" type="text" value="%(email)s">
                    <label style="color:red">%(error_email)s</label>
                </td>
                </tr>
                </table>
                    <input type="submit">
        </form>
    </body>
    </html>
"""

def escape_html(s):
    return cgi.escape(s, quote=True)


USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
def valid_username(username):
    return USER_RE.match(username)

PASS_RE = re.compile(r"^.{3,20}$")
def valid_password(password):
    return password and PASS_RE.match(password)

Email_RE = re.compile(r'^[\S]+@[\S]+.[\S]+$')
def valid_email(email):
        return not email or Email_RE.match(email)

class Signup(webapp2.RequestHandler):
    def Write_Form(self, username ="", error_username="", error_password = "",  error_verify = "", email = "", error_email = ""):
        self.response.out.write(form % {'username': escape_html(username),
                                        'error_username': error_username,
                                        'error_password': error_password,
                                        'error_verify': error_verify,
                                        'email': escape_html(email),
                                        'error_email': error_email})

    def get(self):

        self.Write_Form()

    def post(self):

        have_error = False

        username = self.request.get('username')
        password = self.request.get('password')
        verify = self.request.get('verify')
        email = self.request.get('email')

        error_username = ""
        error_password = ""
        error_verify = ""
        error_email = ""

        if not valid_username(username):

            error_username = "That's not a valid username!"
            have_error = True

        if not valid_password(password):

            error_password = "That's not a valid password!"
            have_error = True

        if password != verify:

            error_verify = "Your passwords didn't match!"
            have_error = True

        if not valid_email(email):

            error_email = "That's not a vaild email!"
            have_error = True

        if have_error:

            self.Write_Form(username, error_username, error_password, error_verify, email, error_email)

        else:
            self.redirect('/Welcome?username='+ username)

class Welcome(webapp2.RequestHandler):
    """If no errors, goes to Welcome Page"""
    def get(self):
        username = self.request.get("username")
        if valid_username(username):
            self.response.out.write("<h1>Welcome, " + username + "!</h1>")



app = webapp2.WSGIApplication([
    ('/', Signup),
    ('/Welcome', Welcome)
], debug=True)
