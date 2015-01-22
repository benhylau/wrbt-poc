import webapp2
import re

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        userAgent = self.request.headers.get('User-Agent')
        if userAgent is not None and re.search(r'\bandroid\b', userAgent, re.I):
            self.redirect('market://details?id=com.groundupworks.flyingphotobooth')
        else:
            self.redirect('http://hyperboria.net')
application = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)
