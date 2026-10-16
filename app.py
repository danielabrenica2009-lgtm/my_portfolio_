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
  }
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
  message = None

  if request.method == 'POST':
    action = request.form.get('action')
    value = request.form.get('value', '').strip()
    index_str = request.form.get('index', '').strip()

    if action == 'add_tail' and value:
      linked_list_data.append(value)
      message = f"Appended '{value}' to the end."
    elif action == 'add_head' and value:
      linked_list_data.insert(0, value)
      message = f"Prepended '{value}' to the start."
    elif action == 'insert_index' and value:
      try:
        idx = int(index_str)
        if 0 <= idx <= len(linked_list_data):
          linked_list_data.insert(idx, value)
          message = f"Inserted '{value}' at index {idx}."
        else:
          message = 'Error: Index out of range.'
      except ValueError:
        message = 'Error: Please enter a valid integer for index.'
    elif action == 'search' and value:
      if value in linked_list_data:
        idx = linked_list_data.index(value)
        message = f"Value '{value}' found at index {idx}."
      else:
        message = f"Value '{value}' not found in the list."
    elif action == 'delete_val' and value:
      if value in linked_list_data:
        linked_list_data.remove(value)
        message = f"Deleted value '{value}' from the list."
      else:
        message = f"No index or value found for '{value}'."
    elif action == 'pop_head' and linked_list_data:
      popped = linked_list_data.pop(0)
      message = f"Popped '{popped}' from the head."
    elif action == 'pop_tail' and linked_list_data:
      popped = linked_list_data.pop()
      message = f"Popped '{popped}' from the tail."
    elif action == 'clear':
      linked_list_data = []
      message = 'Linked list cleared.'

    return render_template(
        'linkedlist.html', items=linked_list_data, message=message
    )

  return render_template('linkedlist.html', items=linked_list_data, message=None)


# 4.5 Infix to Postfix Expression Converter (Strict Validation)
@app.route('/works/infixtopostfix', methods=['GET', 'POST'])
def infixtopostfix():
  postfix_result = None
  infix_expr = ''
  steps = []

  if request.method == 'POST':
    infix_expr = request.form.get('infixExpression', '').strip()
    if infix_expr:
      precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
      allowed_chars = set(precedence.keys()).union({'(', ')'})

      # 1. I-check kung may lumabas na invalid character (hindi letra/numero, hindi operator, hindi parenthesis, hindi space)
      invalid_chars = [char for char in infix_expr if not (char.isalnum() or char in allowed_chars or char.isspace())]

      # 2. I-check din kung may kasamang operator
      has_operator = any(op in infix_expr for op in precedence.keys())

      if invalid_chars:
        steps.append(f"Error: Invalid character(s) detected: {', '.join(set(invalid_chars))}. Only letters, numbers, operators (+, -, *, /, ^), and brackets are allowed.")
        postfix_result = "Error: Invalid Expression (Contains Invalid Symbols)"
      elif not has_operator:
        steps.append("Error: Invalid expression. An infix expression must contain at least one valid operator (+, -, *, /, ^).")
        postfix_result = "Error: Invalid Expression (Missing Operators)"
      else:
        ops_stack = []
        output_list = []

        tokens = list(infix_expr.replace(' ', ''))
        steps.append(
            f"Initialized empty stacks. Scanning tokens: {' '.join(tokens)}"
        )

        for token in tokens:
          if token.isalnum():
            output_list.append(token)
            steps.append(
                f"Operand '{token}' found ➔ Added directly to output:"
                f" {''.join(output_list)}"
            )
          elif token == '(':
            ops_stack.append(token)
            steps.append(
                f"Opening bracket '(' found ➔ Pushed to ops stack:"
                f" {list(ops_stack)}"
            )
          elif token == ')':
            steps.append(
                "Closing bracket ')' found ➔ Popping from ops stack to output"
                " until '(' is met."
            )
            while ops_stack and ops_stack[-1] != '(':
              popped = ops_stack.pop()
              output_list.append(popped)
            if ops_stack and ops_stack[-1] == '(':
              ops_stack.pop()
            steps.append(f"Current Output: {''.join(output_list)}")
          elif token in precedence:
            while (
                ops_stack
                and ops_stack[-1] != '('
                and ops_stack[-1] in precedence
                and precedence[ops_stack[-1]] >= precedence[token]
            ):
              popped = ops_stack.pop()
              output_list.append(popped)
              steps.append(
                  f"Operator precedence rule: Popped '{popped}' to output."
              )
            ops_stack.append(token)
            steps.append(
                f"Operator '{token}' pushed to ops stack. Current Ops Stack:"
                f" {list(ops_stack)}"
            )

        while ops_stack:
          popped = ops_stack.pop()
          output_list.append(popped)
          steps.append(
              f"End of expression ➔ Popped remaining '{popped}' to output."
          )

        postfix_result = ''.join(output_list)
        steps.append(f'Final Postfix Expression: {postfix_result}')

  return render_template(
      'infixtopostfix.html',
      result=postfix_result,
      infix_expr=infix_expr,
      steps=steps,
  )


if __name__ == '__main__':
  app.run(debug=True)