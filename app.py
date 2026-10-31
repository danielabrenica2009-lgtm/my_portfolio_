from flask import Flask
from flask_mail import Mail

# Imports of all Blueprints from the 'blueprints' folder
from blueprints.main import main_bp
from blueprints.area import area_bp
from blueprints.stack import stack_bp
from blueprints.linkedlist import linkedlist_bp
from blueprints.queue_dequeue import queue_dequeue_bp
from blueprints.infix_to_postfix_route import infix_bp
from blueprints.sorting import sorting_bp

app = Flask(__name__)

# Mail Configuration
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'danielabrenica2009@gmail.com'
app.config['MAIL_PASSWORD'] = 'zdfcwbxyulnugzre'

mail = Mail(app)

# Registration of all Blueprints
app.register_blueprint(main_bp)
app.register_blueprint(area_bp)
app.register_blueprint(stack_bp)
app.register_blueprint(linkedlist_bp)
app.register_blueprint(queue_dequeue_bp)
app.register_blueprint(infix_bp)
app.register_blueprint(sorting_bp)

if __name__ == '__main__':
    app.run(debug=True)