# Flask Blog Application

A simple and elegant blog application built with Flask, featuring post management, draft functionality, and a responsive design.

## Features

### ✅ Implemented Features

- **Post Management**
  - Create new blog posts
  - Edit existing posts
  - View individual post details
  - List all published posts
  - Draft functionality (save posts as drafts)

- **User Interface**
  - Responsive design using Bootstrap 5
  - Modern and clean UI
  - Flash message system for user feedback
  - Character counting for title field
  - Word counting for content
  - Form validation

- **Navigation**
  - Easy navigation between posts, drafts, and create new post
  - Breadcrumb navigation
  - Tabbed interface for published posts and drafts

- **Static Assets**
  - Custom CSS styling
  - JavaScript enhancements (character count, form validation, etc.)
  - Bootstrap integration for responsive design

## Project Structure

```
project/
├── app.py                          # Application factory and Blueprint registration
├── routes/
│   └── post_routes.py             # Route definitions
├── controllers/
│   └── post_controller.py         # Business logic (controllers)
├── models/
│   ├── user.py                    # User model
│   └── post.py                    # Post model
├── templates/                     # Jinja2 HTML templates
│   ├── base.html                  # Base template
│   ├── posts.html                 # Posts list view
│   ├── post_detail.html           # Single post view
│   └── post_form.html             # Create/edit post form
├── static/                        # CSS, JS, images
│   ├── css/
│   │   └── style.css              # Custom styles
│   └── js/
│       └── script.js              # JavaScript functionality
├── requirements.txt               # Python dependencies
└── README.md                      # This file
```

## Installation and Setup

### Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

### Step-by-Step Installation

1. **Clone or download the project**
   ```cmd
   cd c:\Users\yadav\OneDrive\Desktop\Assignment
   ```

2. **Create a virtual environment (recommended)**
   ```cmd
   python -m venv venv
   venv\Scripts\activate
   ```

3. **Install dependencies**
   ```cmd
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```cmd
   python app.py
   ```

5. **Open your browser and navigate to**
   ```
   http://localhost:5000
   ```

## Usage

### Creating Posts

1. Click "New Post" in the navigation or on the posts page
2. Fill in the title and content
3. Check "Publish now" to publish immediately, or leave unchecked to save as draft
4. Click "Create Post"

### Managing Posts

- **View all published posts**: Go to `/posts`
- **View drafts**: Go to `/posts/drafts`
- **Edit a post**: Click "Edit" on any post card or detail page
- **View post details**: Click "View" on any post card

### Navigation

- **Home**: Welcome page with quick links
- **Posts**: View all published posts
- **Drafts**: View all draft posts
- **New Post**: Create a new blog post

## Features in Detail

### Draft Workflow

- Posts can be saved as drafts (unpublished)
- Drafts are accessible via the "Drafts" page
- You can publish a draft by editing it and checking "Publish now"
- Published posts and drafts are clearly distinguished with badges

### Form Handling & Validation

- **Client-side validation**: Required fields are validated before submission
- **Server-side validation**: Backend validation with error messages
- **Character counting**: Live character count for title field (max 200 characters)
- **Word counting**: Live word count for content area
- **Flash messages**: Success and error messages are displayed to users

### Responsive Design

- **Mobile-friendly**: Works on all device sizes
- **Bootstrap 5**: Modern and responsive UI components
- **Custom styling**: Enhanced with custom CSS for better appearance

### JavaScript Enhancements

- **Live character counting** for title field
- **Form validation** before submission
- **Auto-hiding flash messages** after 5 seconds
- **Unsaved changes warning** when leaving the page
- **Loading states** for form submissions

## Technical Details

### Models

- **Post Model**: Handles blog post data with title, body, publication status, and timestamps
- **User Model**: Basic user structure (for future authentication features)

### Controllers

- **Post Controller**: Business logic for CRUD operations on posts
- Separation of concerns between routes and business logic

### Templates

- **Base Template**: Common layout with navigation, footer, and flash message handling
- **Jinja2 Features**: Template inheritance, loops, conditionals, and filters

### Static Assets

- **CSS**: Custom styling with CSS variables and responsive design
- **JavaScript**: Enhanced user experience with dynamic features

## Development Notes

### In-Memory Storage

Currently uses in-memory storage for simplicity. In a production environment, you would:
- Use a proper database (SQLite, PostgreSQL, etc.)
- Implement user authentication
- Add database migrations
- Implement proper error handling and logging

### Security Considerations

For production deployment, consider:
- Using environment variables for sensitive configuration
- Implementing CSRF protection
- Adding user authentication and authorization
- Input sanitization and validation
- HTTPS configuration

## Future Enhancements

Possible improvements for this application:
- User authentication and authorization
- Categories and tags for posts
- Comments system
- Search functionality
- Pagination for large numbers of posts
- Image upload for posts
- Rich text editor
- SEO optimization
- API endpoints
- Admin dashboard

## Troubleshooting

### Common Issues

1. **Port already in use**: Change the port in `app.py` or kill the process using the port
2. **Module not found**: Make sure you've activated the virtual environment and installed requirements
3. **Template not found**: Ensure the templates directory structure is correct

### Debug Mode

The application runs in debug mode by default, which provides:
- Detailed error messages
- Automatic reloading on code changes
- Interactive debugger

## License

This project is created for educational purposes as part of a Flask web development assignment.

## Contact

For questions or issues, please refer to the course materials or contact your instructor.
