import os
import logging
from flask import Flask, render_template, redirect, url_for

# Set up logging
logging.basicConfig(level=logging.DEBUG)

# Create Flask app
app = Flask(__name__)
app.secret_key = os.environ.get("SESSION_SECRET", "default-secret-key")

# Routes
@app.route('/')
def index():
    return render_template('index.html', active='home')

@app.route('/education')
def education():
    return render_template('education.html', active='education')

@app.route('/skills')
def skills():
    return render_template('skills.html', active='skills')

@app.route('/responsibilities')
def responsibilities():
    return render_template('responsibilities.html', active='responsibilities')

@app.route('/achievements')
def achievements():
    return render_template('achievements.html', active='achievements')

@app.route('/contact')
def contact():
    return render_template('contact.html', active='contact')

# Route for downloading resume
@app.route('/download_resume')
def download_resume():
    return redirect(url_for('static', filename='files/resume.pdf'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
