from flask import Flask, render_template
from scraper import Scraper

app = Flask(__name__)
@app.route("/")
def index():
    vamp_list = Scraper()
    data = vamp_list.fetcher()
    data = vamp_list.processer()
    return render_template('index.html',data=data)

app.run(debug=True)
            
    
