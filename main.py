from bottle import get, post, request
from init import app, nav
from config import authmethod
if authmethod == 'BASIC':
	from zeep.exceptions import TransportError

@get('/<function>')
def navapi(function):
	if authmethod == 'BASIC':
		try: 
			# call nav
			response = getattr(nav.service, function)(**dict(request.query))
			response = list(filter(None.__ne__, response))
			return{'status': 200, 'data': response}
		except TransportError as error:
			return{'status': error.status_code, 'data': error.content}
	
	elif authmethod == 'NTLM':
		# call nav
		status, data = getattr(nav.service, function)(**dict(request.query))
		if status == 200 and data:
			# remove garbage data, present in both mity and broda
			data = filter(None, data)
		elif data:
			data = '{}'.format(data)
		else:
			data = []
		
		return{'status': status, 'data':data}
