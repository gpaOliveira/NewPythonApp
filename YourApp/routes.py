from YourApp import app
from flask import render_template

"""Routes to allow clients to do stuff"""

#References: https://blog.miguelgrinberg.com/post/designing-a-restful-api-with-python-and-flask


@app.route('/v1/alive', methods=['GET'])
def alive():
    return "Alive", 200


@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404
