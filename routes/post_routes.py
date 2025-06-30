from flask import Blueprint, render_template, request, redirect, url_for, flash
from controllers.post_controller import (
    list_posts, get_post, create_post, update_post, list_drafts
)

post_bp = Blueprint('posts', __name__, url_prefix='/posts')

@post_bp.route('/', methods=['GET'])
def show_posts():
    """
    Retrieve published posts via list_posts(published=True)
    and render 'posts.html' with the posts list.
    """
    posts = list_posts(published=True)
    return render_template('posts.html', posts=posts, page_title="Published Posts")

@post_bp.route('/<int:post_id>', methods=['GET'])
def post_detail(post_id):
    """
    Fetch a single post by ID using get_post(post_id)
    and render 'post_detail.html' with the post.
    """
    post = get_post(post_id)
    return render_template('post_detail.html', post=post)

@post_bp.route('/new', methods=['GET', 'POST'])
def new_post():
    """
    On GET, render 'post_form.html'.
    On POST, collect form data from request.form and call create_post(form).
    """
    if request.method == 'POST':
        return create_post(request.form)
    return render_template('post_form.html', post=None, page_title="Create New Post")

@post_bp.route('/<int:post_id>/edit', methods=['GET', 'POST'])
def edit_post(post_id):
    """
    On GET, fetch post and render 'post_form.html' with post data.
    On POST, collect form data and call update_post(post_id, form).
    """
    if request.method == 'POST':
        return update_post(post_id, request.form)
    
    post = get_post(post_id)
    return render_template('post_form.html', post=post, page_title="Edit Post")

@post_bp.route('/drafts', methods=['GET'])
def drafts():
    """
    Retrieve unpublished posts via list_drafts()
    and render 'posts.html' with the drafts list.
    """
    drafts = list_drafts()
    return render_template('posts.html', posts=drafts, page_title="Draft Posts")
