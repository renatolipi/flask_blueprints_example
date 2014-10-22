from flask import Flask
from my_application.views import my_application_bp

app = Flask(__name__)
app.register_blueprint(my_application_bp)


if __name__ == '__main__': 
    app.run(debug=True)
