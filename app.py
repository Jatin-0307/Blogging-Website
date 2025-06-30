from flask import Flask, render_template
from routes.post_routes import post_bp
from models.post import Post

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'  # Change this in production

# Custom template filter for line breaks
@app.template_filter('nl2br')
def nl2br_filter(text):
    """Convert newlines to HTML line breaks"""
    if text:
        return text.replace('\n', '<br>')
    return text

# Register blueprints
app.register_blueprint(post_bp)

@app.route('/')
def home():
    """Home page that redirects to posts"""
    return render_template('base.html')

def create_sample_data():
    """Create some sample posts for demonstration"""
    if not Post._posts:  # Only create if no posts exist
        # Published post
        post1 = Post(
            title="Welcome to Flask Blog",
            body="This is your first blog post! Flask Blog is a simple yet powerful blogging platform built with Flask.\n\nYou can create, edit, and manage your blog posts with ease. Posts can be saved as drafts or published immediately.\n\nFeatures include:\n- Rich text content\n- Draft functionality\n- Responsive design\n- Easy post management",
            is_published=True
        )
        post1.save()
        
        # Draft post
        post2 = Post(
            title="Getting Started with Flask",
            body="Flask is a lightweight WSGI web application framework in Python. It's designed to make getting started quick and easy, with the ability to scale up to complex applications.\n\nThis post is currently a draft. You can find it in the Drafts section and publish it when you're ready.",
            is_published=False
        )
        post2.save()
        
        # Another published post
        post3 = Post(
            title="Building Web Applications",
            body="Web development has evolved significantly over the years. Modern frameworks like Flask provide developers with powerful tools to build robust applications.\n\nKey concepts in web development:\n- MVC Architecture\n- Template Engines\n- Database Integration\n- User Authentication\n- Responsive Design\n\nFlask makes all of these concepts accessible and easy to implement.",
            is_published=True
        )
        post3.save()

if __name__ == '__main__':
    create_sample_data()
    app.run(debug=True)
