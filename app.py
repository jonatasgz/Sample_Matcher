# Sample Matcher
# Copyright (C) Jonatas Garcez 2024

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

from flask import Flask, render_template, request, session
import pandas as pd
from tools import get_secret

app = Flask(__name__)

app.secret_key = get_secret()

# File upload settings
app.config['MAX_CONTENT_LENGTH'] = 20 * 1024 * 1024

ALLOWED_EXTENSIONS = set(['xlsx'])

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['POST', 'GET'])
def home():
    msg = ''
    color = ''
    if request.method == 'POST':
        if session.get('samples'):
            test_sample = request.form['test_sample']
            for sample in session['samples']:
                if str(sample).lower() in str(test_sample).lower():
                    msg = 'Yes'
                    color = 'success'
                    return render_template('home.html', msg=msg, color=color)
            msg = 'No'
            color = 'danger'
            return render_template('home.html', msg=msg, color=color) 
        else:
            msg = 'Could not find samples list'
            color = 'warning'
            return render_template('home.html', msg=msg, color=color)
    return render_template('home.html', msg=msg, color=color)

@app.route('/upload', methods = ['POST'])        
def upload():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            db = pd.read_excel(file, header = None)
            session['samples'] = db.iloc[:,0].to_list()
            msg = 'File successfuly imported'
            return render_template('home.html', msg=msg)
        else: 
            msg = 'Could not read the file'
            return render_template('home.html', msg=msg)

if __name__ == '__main__':
    app.run(host='localhost', port=5020, debug=False)