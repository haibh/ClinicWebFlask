#!flask/bin/python
# Run a test server.
import os

from app import app
app.secret_key = os.urandom(12)
app.run(debug=True)