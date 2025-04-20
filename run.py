from app import create_app  # Import the create_app function from the app package
from app.utils.db import db
app = create_app()  # Create the app instance

if __name__ == '__main__':
    app.run(debug=True)