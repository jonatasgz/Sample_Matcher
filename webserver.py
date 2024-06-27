# I run this file using gunicorn through a systemd service

from app import app

if __name__ == '__app__':
    app.run()