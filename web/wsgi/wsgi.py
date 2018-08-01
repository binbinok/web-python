def application(environ, start_response):
    start_response('200 OK', ['Content-type', 'text/html'])
    return '<h1>hello, web!</h1>'
