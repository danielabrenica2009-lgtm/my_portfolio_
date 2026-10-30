from flask import Blueprint, render_template, request
from node import Stack

stack_bp = Blueprint('stack', __name__)
global_stack = Stack()

@stack_bp.route('/stack', methods=['GET', 'POST'])
def stack():
    message = ""
    if request.method == 'POST':
        action = request.form.get('action')
        value = request.form.get('value')

        if action == 'push' and value:
            global_stack.push(value)
            message = f"Successfully pushed '{value}' to the stack."
        elif action == 'pop':
            popped = global_stack.pop()
            message = f"Successfully popped '{popped}' from the stack." if popped is not None else "Stack is empty!"
        elif action == 'peek':
            top_val = global_stack.peek()
            message = f"Top of stack (Peek): '{top_val}'" if top_val is not None else "Stack is empty!"

    return render_template('stack.html', items=global_stack.get_all(), message=message)