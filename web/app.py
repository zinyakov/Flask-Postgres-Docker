from flask import render_template
from index import app, db
from models import Release


@app.route('/', methods=['GET'])
def index():
    releases = Release.query.order_by(Release.date_posted.desc()).all()
    return render_template('index.html', releases=releases)

@app.route('/about', methods=['GET'])
def about():
    return render_template('about.html')

@app.route('/release/<string:release_id>', methods=['GET'])
def show_release(release_id):
    release = Release.query.filter(Release.id == release_id).first()
    return render_template('release.html', release=release)


if __name__ == '__main__':
    app.run()
