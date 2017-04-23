# coding=UTF-8

from flask import Flask, request, render_template, abort
from geventwebsocket.handler import WebSocketHandler
from gevent.pywsgi import WSGIServer
from datetime import datetime

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/echo/')
def message():
    if request.environ.get('wsgi.websocket'):
        ws = request.environ['wsgi.websocket']
        while True:
            if ws.closed is False:
                message = ws.receive()
                ws.send("[" + str(message) + "]" + "[" + \
                        str(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))+"]")
            else:
                abort(404)
    return "Connected!"


if __name__ == '__main__':
    http_server = WSGIServer(('', 5000), app, handler_class=WebSocketHandler)
    print("Listenning on port 5000...")
    http_server.serve_forever()
    

