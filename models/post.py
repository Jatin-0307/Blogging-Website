from datetime import datetime

class Post:
    """Post model for blog posts"""
    
    # In-memory storage for demonstration (in real app, use a database)
    _posts = []
    _next_id = 1
    
    def __init__(self, title, body, is_published=False):
        self.id = Post._next_id
        Post._next_id += 1
        self.title = title
        self.body = body
        self.is_published = is_published
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
    
    def save(self):
        """Save the post (add to list if new, update timestamp if existing)"""
        self.updated_at = datetime.now()
        
        # Check if post already exists in the list
        existing_post = None
        for i, post in enumerate(Post._posts):
            if post.id == self.id:
                existing_post = i
                break
        
        if existing_post is not None:
            # Update existing post
            Post._posts[existing_post] = self
        else:
            # Add new post
            Post._posts.append(self)
    
    @classmethod
    def get_all_posts(cls, published=None):
        """Get all posts, optionally filtered by published status"""
        if published is None:
            return cls._posts.copy()
        
        return [post for post in cls._posts if post.is_published == published]
    
    @classmethod
    def get_by_id(cls, post_id):
        """Get a post by its ID"""
        for post in cls._posts:
            if post.id == post_id:
                return post
        return None
    
    def __repr__(self):
        return f"<Post(id={self.id}, title='{self.title}', published={self.is_published})>"
