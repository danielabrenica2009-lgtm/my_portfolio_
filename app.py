import math
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)

# Memory storage for Linked List
linked_list_data = []


# 1. Homepage
@app.route('/')
def index():
  return render_template('index.html')


# 2. Profile Page
@app.route('/profile')
def profile():
  user_data = {
      'name': 'Daniel Abrenica',
      'course': 'Bachelor of Science in Computer Engineering 2-1',
      'title': 'Student / Aspiring Developer',
      'bio': (
          'A passionate student exploring web development, data structures, and'
          ' algorithms.'
      ),
      'skills': ['Python', 'Flask', 'HTML/CSS', 'JavaScript', 'Data Structures'],
  }  # <--- Siguraduhing may closing brace '}' dito!
  return render_template('profile.html', user=user_data)


# 3. Contact Page
@app.route('/contact')
def contact():
  contact_info = {
      'email': 'danielabrenica2009@gmail.com',
      'phone': '+63 960 504 5065',
      'github': 'https://github.com/danielabrenica2009-lgtm',
      'linkedin': 'https://www.linkedin.com/in/daniel-abrenica-b2a23a438/',
      'location': 'Antipolo City, Rizal, Philippines',
  }
  return render_template('contact.html', contact=contact_info)


# 4. Programming Works Overview
@app.route('/works')
def works():
  return render_template('works.html')


# 4.1 String to Uppercase Converter
@app.route('/works/touppercase', methods=['GET', 'POST'])
def touppercase():
  result = None
  original_text = ''
  if request.method == 'POST':
    original_text = request.form.get('inputString', '')
    result = original_text.upper()
  return render_template(
      'touppercase.html', result=result, original_text=original_text
  )


# 4.2 Area of Circle Calculator
@app.route('/works/area/circle', methods=['GET', 'POST'])
def circle():
  result = None
  radius = None
  if request.method == 'POST':
    try:
      radius = float(request.form.get('radius', 0))
      result = math.pi * (radius**2)
    except (ValueError, TypeError):
      result = None
  return render_template('circle.html', result=result, radius=radius)


# 4.3 Area of Triangle Calculator
@app.route('/works/area/triangle', methods=['GET', 'POST'])
def triangle():
  result = None
  base = None
  height = None
  if request.method == 'POST':
    try:
      base = float(request.form.get('base', 0))
      height = float(request.form.get('height', 0))
      result = 0.5 * base * height
    except (ValueError, TypeError):
      result = None
  return render_template(
      'triangle.html', result=result, base=base, height=height
  )


# 4.4 Linked List Implementation UI
@app.route('/works/linkedlist', methods=['GET', 'POST'])
def linkedlist():
  global linked_list_data
  if request.method == 'POST':
    action = request.form.get('action')
    value = request.form.get('value', '').strip()

    if action == 'add_head' and value:
      linked_list_data.insert(0, value)
    elif action == 'add_tail' and value:
      linked_list_data.append(value)
    elif action == 'pop_head' and linked_list_data:
      linked_list_data.pop(0)
    elif action == 'clear':
      linked_list_data = []

    return redirect(url_for('linkedlist'))

  return render_template('linkedlist.html', items=linked_list_data)


if __name__ == '__main__':
  app.run(debug=True)