from wsgiref.simple_server import make_server
from wsgi import application

httpd = make_server('', 8011, application)
print 'Serving HTTP on port 8011...'
httpd.serve_forever