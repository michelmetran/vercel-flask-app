import os
from flask import Flask
import numpy as np

app = Flask(__name__)


@app.route('/')
def home():
    return 'Home Page Route'


@app.route('/about')
def about():
    return 'About Page Route'


@app.route('/portfolio')
def portfolio():
    a = np.random.choice([1, 2, 3, 4, 5, 6])
    return f'Portfolio {a} Page Route'


@app.route('/contact')
def contact():
    return 'Contact Page Route'


@app.route('/api')
def api():
    with open(
            os.path.join('..', 'data', 'data/data.json'),
            mode='r'
    ) as my_file:
        text = my_file.read()
        return text


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    print(os.getcwd())
    app.run(host='0.0.0.0', port=port)

