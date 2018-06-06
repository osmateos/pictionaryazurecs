"""
This script runs the drawingCognitive application using a development server.
"""

from os import environ
from drawingCognitive import app

if __name__ == '__main__':
    HOST = environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(environ.get('SERVER_PORT', '8080'))
    except ValueError:
        PORT = 80
    app.run(host='0.0.0.0', port=PORT, debug=True)
