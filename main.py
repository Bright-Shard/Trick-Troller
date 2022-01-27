from flask import Flask, render_template, request
from base64 import b64decode, b64encode

def decode(encoding, txt):
	if encoding == 'b64' or encoding == '64' or encoding == 'base64':
		print(b64decode(bytes(txt, 'utf-8')))
		return str(b64decode(bytes(txt, 'utf-8')))


app = Flask('Trick Troller')


@app.route('/redirect')
@app.route('/goto')
def redirect():
	url = request.args.get('url')
	encoding = request.args.get('enc')
	if url != None:
		if encoding == None:
			return render_template('redirect.html', url=url)
		else:
			return render_template('redirect.html', url=decode(encoding, url))


@app.route('/')
def home():
	return render_template('home.html')


@app.route('/rick')
@app.route('/rick<wildcard>')
@app.route('/rick/<wildcard>')
@app.route('/rick/<wildcard>/<subwildcard>')
def rick_roll(wildcard=None, subwildcard=None):
	return render_template('rickroll.html')


@app.route('/library')
@app.route('/library<wildcard>')
@app.route('/library/<wildcard>')
@app.route('/library/<wildcard>/<subwildcard>')
def babel_rickroll(wildcard=None, subwildcard=None):
	return render_template('library-of-babel-rickroll.html')


@app.route('/api/<func>')
def b64(func=None):
	txt = request.args.get('txt')
	if txt != None and func != None:
		if func == '64':
			return b64encode(bytes(txt, 'utf-8'))
		elif func == 'd64':
			return b64decode(bytes(txt, 'utf-8'))
	else:
		return 'That didn\'t work :/'


app.run('0.0.0.0', 80)
