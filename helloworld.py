def application(environ, start_response):
    status = '200 OK'
    output = b'Hello World, Now I am testing automation with CI/CD Pipeline!'
    response_headers = [('Content-type', 'text/plain'),
    ('Content-Length', str(len(output)))]
    start_response(status, response_headers)
    return [output]
