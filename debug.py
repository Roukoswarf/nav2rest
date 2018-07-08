#!/usr/bin/python
if __name__ == '__main__':
	import main
	from bottle import run, static_file, TEMPLATES
	from os import path

	run(server='cherrypy', app=main.app, host='::', port=5000, reloader=True, debug=True)
