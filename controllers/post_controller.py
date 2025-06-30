from models.post import Post
from flask import flash, redirect, url_for, abort

def list_posts(published):
    """
    Query Post model filtered by is_published status.
    Return a list of posts.
    """
    return Post.get_all_posts(published=published)

def get_post(post_id):
    """
    Retrieve a post by its ID or abort with 404 if not found.
    """
    post = Post.get_by_id(post_id)
    if not post:
        abort(404)
    return post

def create_post(form):
    """
    Extract title, body, and is_published from form.
    Validate fields, flash errors, save new Post, flash success, redirect.
    """
    title = form.get('title', '').strip()
    body = form.get('body', '').strip()
    is_published = bool(form.get('is_published'))
    
    # Validation
    if not title:
        flash('Title is required!', 'error')
        return redirect(url_for('posts.new_post'))
    
    if not body:
        flash('Body is required!', 'error')
        return redirect(url_for('posts.new_post'))
    
    # Create new post
    try:
        post = Post(title=title, body=body, is_published=is_published)
        post.save()
        flash('Post created successfully!', 'success')
        if is_published:
            return redirect(url_for('posts.show_posts'))
        else:
            return redirect(url_for('posts.drafts'))
    except Exception as e:
        flash(f'Error creating post: {str(e)}', 'error')
        return redirect(url_for('posts.new_post'))

def update_post(post_id, form):
    """
    Fetch existing post, update attributes from form,
    validate, save changes, flash messages, and redirect.
    """
    post = get_post(post_id)
    
    title = form.get('title', '').strip()
    body = form.get('body', '').strip()
    is_published = bool(form.get('is_published'))
    
    # Validation
    if not title:
        flash('Title is required!', 'error')
        return redirect(url_for('posts.edit_post', post_id=post_id))
    
    if not body:
        flash('Body is required!', 'error')
        return redirect(url_for('posts.edit_post', post_id=post_id))
    
    # Update post
    try:
        post.title = title
        post.body = body
        post.is_published = is_published
        post.save()
        flash('Post updated successfully!', 'success')
        if is_published:
            return redirect(url_for('posts.show_posts'))
        else:
            return redirect(url_for('posts.drafts'))
    except Exception as e:
        flash(f'Error updating post: {str(e)}', 'error')
        return redirect(url_for('posts.edit_post', post_id=post_id))

def list_drafts():
    """
    Reuse list_posts to fetch unpublished posts.
    """
    return list_posts(published=False)
