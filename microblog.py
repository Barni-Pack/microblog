from app import app, db
from app.models import User, Post


@app.shell_context_processor
def make_shell_context():
    # Add this code to venv/activate.ps1 if using powershell
    # $env:FLASK_APP = 'microblog.py'
    return {'db': db, 'User': User, 'Post': Post}