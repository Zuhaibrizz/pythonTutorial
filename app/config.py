class Config:
    SECRET_KEY = 'your_secret_key'
    SQLALCHEMY_DATABASE_URI = 'mysql://username:password@localhost/mydatabase'  # Update this with your actual MySQL credentials
    SQLALCHEMY_TRACK_MODIFICATIONS = False
