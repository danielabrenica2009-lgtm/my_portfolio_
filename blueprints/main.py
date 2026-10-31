from flask import Blueprint, render_template, request, redirect, url_for, current_app
from flask_mail import Message

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    return render_template('index.html')

@main_bp.route('/profile')
def profile():
    user_data = {
        "name": "Daniel Abrenica",
        "course": "Bachelor of Science in Computer Engineering",
        "title": "Aspiring Software Developer and Web Developer",
        "bio": "I am passionate student wherein I love about web development and data structures.",
        "skills": ["Python", "Flask", "HTML/CSS", "JavaScript", "SQL"]
    }
    return render_template('profile.html', user=user_data)

@main_bp.route('/works')
def works():
    return render_template('works.html')

@main_bp.route('/contact', methods=['GET', 'POST'])
def contact():
    contact_info = {
        "email": "danielabrenica2009@gmail.com",
        "phone": "+63 960 504 5065",
        "location": "Antipolo City Rizal, Philippines",
        "github": "https://github.com/danielabrenica2009-lgtm",
        "linkedin": "https://www.linkedin.com/in/daniel-abrenica-b2a23a438/"
    }

    if request.method == 'POST':
        sender_name = request.form.get('name')
        sender_email = request.form.get('email')
        subject = request.form.get('subject')
        message_body = request.form.get('message')

        try:
            # Uses an extensions from current_app
            mail = current_app.extensions['mail']
            msg = Message(
                subject=f"Portfolio Message: {subject}",
                sender=current_app.config['MAIL_USERNAME'],
                recipients=['danielabrenica2009@gmail.com'],
                reply_to=sender_email
            )
            msg.body = f"New message from MyPortfolio Website:\n\nName: {sender_name}\nEmail: {sender_email}\nSubject: {subject}\n\nMessage:\n{message_body}"
            mail.send(msg)
        except Exception as e:
            print(f"Error: {e}")

        return redirect(url_for('main.contact'))

    return render_template('contact.html', contact=contact_info)