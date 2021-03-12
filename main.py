from flask import Flask
app = Flask(__name__)

import Authentication
import About
import DataEntry

if __name__ == '__main__':
    app.run(debug=False)
