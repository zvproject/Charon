from flask import render_template, url_for
from app import app, APP_SOURCE
from app.functions import get_list_of_footer_social_links
import os

footer_list = get_list_of_footer_social_links(os.path.join(APP_SOURCE, "footer_links.txt"))


@app.route('/')
@app.route('/index')
def index():
	navigation = ['Projects', 'Portfolio', 'About', 'Contact/Join']
	return render_template("main_menu.html", title="Home", links=footer_list, menu=navigation)

@app.route('/projects')
def projects():

	return render_template("projects.html", title="Projects", links=footer_list)

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.shtml'), 404

@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html'), 500

