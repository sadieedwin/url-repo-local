from flask import Flask, render_template, redirect, url_for, request, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///links.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'your_secret_key'  # Needed for flashing messages!

db = SQLAlchemy(app)

from models import Link

@app.route('/')
def home():
    search_query = request.args.get('search')
    tag_filter = request.args.get('tag')
    page = request.args.get('page', 1, type=int) 

    query = Link.query

    if search_query:
        query = query.filter(
            (Link.title.ilike(f'%{search_query}%')) |
            (Link.description.ilike(f'%{search_query}%')) |
            (Link.tags.ilike(f'%{search_query}%'))
        )

    if tag_filter:
        query = query.filter(Link.tags.ilike(f'%{tag_filter}%'))

    links = query.order_by(Link.created_at.desc()).paginate(page=page, per_page=10)  # Paginate here

    all_tags = get_all_tags()

    return render_template('home.html', links=links, search_query=search_query, tag_filter=tag_filter, all_tags=all_tags)


# Helper: Get unique list of tags
def get_all_tags():
    tags = []
    all_links = Link.query.all()
    for link in all_links:
        if link.tags:
            tags.extend([t.strip() for t in link.tags.split(',')])
    return sorted(set(tags))  # Remove duplicates and sort


# Add Link
@app.route('/add', methods=['GET', 'POST'])
def add_link():
    if request.method == 'POST':
        title = request.form['title']
        url_link = request.form['url']
        description = request.form['description']
        tags = request.form['tags']

        if not title or not url_link:
            flash('Title and URL are required!', 'danger')
            return redirect(url_for('add_link'))

        new_link = Link(title=title, url=url_link, description=description, tags=tags)
        db.session.add(new_link)
        db.session.commit()
        flash('Link added successfully!', 'success')
        return redirect(url_for('home'))

    return render_template('add_link.html')

# Edit Link
@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_link(id):
    link = Link.query.get_or_404(id)

    if request.method == 'POST':
        link.title = request.form['title']
        link.url = request.form['url']
        link.description = request.form['description']
        link.tags = request.form['tags']

        db.session.commit()
        flash('Link updated successfully!', 'success')
        return redirect(url_for('home'))

    return render_template('edit_link.html', link=link)

# Delete Link
@app.route('/delete/<int:id>', methods=['POST'])
def delete_link(id):
    link = Link.query.get_or_404(id)
    db.session.delete(link)
    db.session.commit()
    flash('Link deleted successfully!', 'success')
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=False)
