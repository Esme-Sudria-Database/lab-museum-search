# pylint: disable=invalid-name
from flask import Flask, request
from flask import render_template
import elasticsearch


app = Flask(__name__)


@app.route("/")
def index():
    query = request.args.get('q', default='', type=str)

    if query != '':
        museums = query_museum(query) # call elasticsearch to perform a research
    else:
        museums = []

    return render_template('search.html',
                           query=query,
                           museums=museums)


def query_museum(keywords):
    pass

@app.cli.command("import-data")
def import_data():
    print("you have to implement the data loading inside elasticsearch")
