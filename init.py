from bottle import default_app, response
from config import *

if authmethod == 'NTLM':
	from suds.transport.https import WindowsHttpAuthenticated
	from suds.client import Client
	import ssl
	
	# disable ssl verification for funky certs
	if hasattr(ssl, '_create_unverified_context'):
		ssl._create_default_https_context = ssl._create_unverified_context
	
	ntlm = WindowsHttpAuthenticated(username=username, password=password)
	nav = Client(wsdl, transport=ntlm, faults = False)

elif authmethod == 'BASIC':
	from requests import Session
	from requests.auth import HTTPBasicAuth
	from zeep import Client
	from zeep.transports import Transport
	
	session = Session()
	#session.verify = False
	session.auth = HTTPBasicAuth(username, password)
	nav = Client(wsdl, transport=Transport(session=session))

app = default_app()

@app.hook('after_request')
def enable_cors():
	response.headers['Access-Control-Allow-Origin'] = '*'
	response.headers['Access-Control-Allow-Methods'] = 'PUT, GET, POST, DELETE, OPTIONS'
	response.headers['Access-Control-Allow-Headers'] = 'Origin, Accept, Content-Type, X-Requested-With, X-CSRF-Token'
