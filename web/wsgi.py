from app import create_app, db
from app.auth.models import User

app = create_app()

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User}
    # u = User(email='susan@example.com', username='susan')

if __name__ == "__main__":
    app.run()