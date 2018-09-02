from bottle import route, run

@route('/')
@route('/hello/<name>')
def greet(name = 'Stranger'):
    return template('Hello {{name}}, how are you?', name = name)

run(host = 'localhost', port = 8080, debug = True);