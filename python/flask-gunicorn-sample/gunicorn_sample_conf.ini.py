"""gunicorn WSGI server configuration."""
workers = 2
threads = 1
bind = '0.0.0.0:8000'
daemon = False