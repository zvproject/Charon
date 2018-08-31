from flask import render_template, url_for
from app import app, APP_SOURCE
from app.functions import get_list_of_footer_social_links, get_projects
import os

footer_list = get_list_of_footer_social_links(os.path.join(APP_SOURCE, "footer_links.txt"))


@app.route('/')
@app.route('/index')
def index():
	navigation = ['Projects', 'Portfolio', 'About', 'Contact/Join']
	return render_template("main_menu.html", title="Home", links=footer_list, menu=navigation)

@app.route('/projects')
def projects():
	get_projects(APP_SOURCE)
	return render_template("projects.html", title="Projects", links=footer_list)

@app.route('/portfolio')
def portfolio():
	navigation = ['Art','Web Design','Animation','Coding']
	return render_template("main_menu.html", title="Portfolio", links=footer_list, menu=navigation)

@app.route('/art')
def art():
	return render_template("art.html", title="Art", links=footer_list)

@app.route('/web')
def web():
	return render_template("web.html", title="Web Design", links=footer_list)

@app.route('/animation')
def animation():
	return render_template("animation.html", title="Animation", links=footer_list)

@app.route('/coding')
def coding():
	return render_template("coding.html", title="Coding", links=footer_list)


@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.shtml'), 404

@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html'), 500

