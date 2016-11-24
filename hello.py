def app(env, start_response):
  body = [p for p in env['QUERY_STRING'].split('&')]
  body = '\n'.join(body)
  status = '200 OK'
  response_headers = [('Content-Type', 'text/plain'),
                      ('Content-Length', str(len(body)))]
  start_response(status, response_headers)
  return [ body ]