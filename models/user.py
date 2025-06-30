from datetime import datetime

class User:
    """User model for blog users"""
    
    # In-memory storage for demonstration
    _users = []
    _next_id = 1
    
    def __init__(self, username, email, password):
        self.id = User._next_id
        User._next_id += 1
        self.username = username
        self.email = email
        self.password = password  # In real app, hash this!
        self.created_at = datetime.now()
    
    def save(self):
        """Save the user"""
        # Check if user already exists
        existing_user = None
        for i, user in enumerate(User._users):
            if user.id == self.id:
                existing_user = i
                break
        
        if existing_user is not None:
            User._users[existing_user] = self
        else:
            User._users.append(self)
    
    @classmethod
    def get_by_username(cls, username):
        """Get a user by username"""
        for user in cls._users:
            if user.username == username:
                return user
        return None
    
    @classmethod
    def get_by_id(cls, user_id):
        """Get a user by ID"""
        for user in cls._users:
            if user.id == user_id:
                return user
        return None
    
    def __repr__(self):
        return f"<User(id={self.id}, username='{self.username}')>"
