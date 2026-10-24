from flask import Flask, render_template, request, redirect, url_for
from flask_mail import Mail, Message
from node import Stack, LinkedList, Queue, Deque, infix_to_postfix

app = Flask(__name__)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'danielabrenica2009@gmail.com'
app.config['MAIL_PASSWORD'] = 'zdfcwbxyulnugzre'

mail = Mail(app)

global_stack = Stack()
global_linked_list = LinkedList()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/profile')
def profile():
    user_data = {
        "name": "Daniel Abrenica",
        "course": "Bachelor of Science in Computer Engineering",
        "title": "Aspiring Software Developer and Web Developer",
        "bio": "I am passionate student wherein I love about web development and data structures.",
        "skills": ["Python", "Flask", "HTML/CSS", "JavaScript", "SQL"]
    }
    return render_template('profile.html', user=user_data)

@app.route('/works')
def works():
    return render_template('works.html')

@app.route('/contact', methods=['GET', 'POST'])
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
            msg = Message(
                subject=f"Portfolio Message: {subject}",
                sender=app.config['MAIL_USERNAME'],
                recipients=['danielabrenica2009@gmail.com'],
                reply_to=sender_email
            )
            msg.body = f"New message from MyPortfolio Website:\n\nName: {sender_name}\nEmail: {sender_email}\nSubject: {subject}\n\nMessage:\n{message_body}"
            mail.send(msg)
        except Exception as e:
            print(f"Error: {e}")

        return redirect(url_for('contact'))

    return render_template('contact.html', contact=contact_info)

@app.route('/circle', methods=['GET', 'POST'])
def circle():
    result, radius = None, None
    if request.method == 'POST':
        try:
            radius = float(request.form.get('radius'))
            result = 3.14159 * (radius ** 2)
        except ValueError:
            result = None
    return render_template('circle.html', result=result, radius=radius)

@app.route('/triangle', methods=['GET', 'POST'])
def triangle():
    result, base, height = None, None, None
    if request.method == 'POST':
        try:
            base = float(request.form.get('base'))
            height = float(request.form.get('height'))
            result = 0.5 * base * height
        except ValueError:
            result = None
    return render_template('triangle.html', result=result, base=base, height=height)

@app.route('/touppercase', methods=['GET', 'POST'])
def touppercase():
    result, original_text = None, None
    if request.method == 'POST':
        original_text = request.form.get('inputString', '')
        result = original_text.upper()
    return render_template('touppercase.html', result=result, original_text=original_text)

@app.route('/infixtopostfix', methods=['GET', 'POST'])
def infixtopostfix():
    result, steps, infix_expr = None, [], ""
    if request.method == 'POST':
        infix_expr = request.form.get('infixExpression', '')
        if infix_expr:
            result, steps = infix_to_postfix(infix_expr)
    return render_template('infixtopostfix.html', result=result, steps=steps, infix_expr=infix_expr)

@app.route('/stack', methods=['GET', 'POST'])
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

@app.route('/linkedlist', methods=['GET', 'POST'])
def linkedlist():
    message = ""
    if request.method == 'POST':
        action = request.form.get('action')
        value = request.form.get('value')
        index_str = request.form.get('index')

        if action == 'append' and value:
            global_linked_list.append(value)
            message = f"Successfully appended '{value}' to the linked list."
        elif action == 'prepend' and value:
            global_linked_list.prepend(value)
            message = f"Successfully prepended '{value}' to the linked list."
        elif action == 'insert':
            try:
                idx = int(index_str) if index_str else 0
                if value:
                    success = global_linked_list.insert_at_index(idx, value)
                    message = f"Successfully inserted '{value}' at index {idx}." if success else f"Invalid index {idx}."
                else:
                    message = "Please provide a value to insert."
            except ValueError:
                message = "Invalid index format."
        elif action == 'search' and value:
            idx = global_linked_list.search(value)
            message = f"Value '{value}' found at index {idx}." if idx != -1 else f"Value '{value}' not found in list."
        elif action == 'delete' and value:
            deleted = global_linked_list.delete_value(value)
            message = f"Successfully deleted '{value}'." if deleted else f"Value '{value}' not found in list."
        elif action == 'pop_head':
            popped = global_linked_list.pop_head()
            message = f"Successfully popped head '{popped}'." if popped is not None else "Linked list is empty!"
        elif action == 'pop_tail':
            popped = global_linked_list.pop_tail()
            message = f"Successfully popped tail '{popped}'." if popped is not None else "Linked list is empty!"
        elif action == 'clear':
            global_linked_list.clear()
            message = "Linked list cleared."

    return render_template('linkedlist.html', items=global_linked_list.get_all(), message=message)

# Global instances for Queue and De-queue
global_queue = Queue()
global_deque = Deque()

@app.route('/queue', methods=['GET', 'POST'])
def queue_view():
    message = ""
    if request.method == 'POST':
        action = request.form.get('action')
        value = request.form.get('value')

        if action == 'enqueue' and value:
            global_queue.enqueue(value)
            message = f"Successfully enqueued '{value}'."
        elif action == 'dequeue':
            popped = global_queue.dequeue()
            message = f"Successfully dequeued '{popped}'." if popped is not None else "Queue is empty!"
        elif action == 'peek':
            top_val = global_queue.peek()
            message = f"Front of queue: '{top_val}'" if top_val is not None else "Queue is empty!"

    return render_template('queue.html', items=global_queue.get_all(), message=message)

@app.route('/dequeue', methods=['GET', 'POST'])
def dequeue_view():
    message = ""
    if request.method == 'POST':
        action = request.form.get('action')
        value = request.form.get('value')

        if action == 'add_front' and value:
            global_deque.add_front(value)
            message = f"Successfully added '{value}' to Front."
        elif action == 'add_rear' and value:
            global_deque.add_rear(value)
            message = f"Successfully added '{value}' to Rear."
        elif action == 'remove_front':
            popped = global_deque.remove_front()
            message = f"Successfully removed '{popped}' from Front." if popped is not None else "Deque is empty!"
        elif action == 'remove_rear':
            popped = global_deque.remove_rear()
            message = f"Successfully removed '{popped}' from Rear." if popped is not None else "Deque is empty!"

    return render_template('dequeue.html', items=global_deque.get_all(), message=message)

# Main Sorting Menu / Dashboard
@app.route('/sorting')
def sorting_dashboard():
    return render_template('sorting_menu.html')

# Individual Sorting Pages
@app.route('/sorting/bubble')
def bubble_sort():
    return render_template('bubblesorting.html')

@app.route('/sorting/selection')
def selection_sort():
    return render_template('selectionsorting.html')

@app.route('/sorting/insertion')
def insertion_sort():
    return render_template('insertionsorting.html')

@app.route('/sorting/merge')
def merge_sort():
    return render_template('mergesorting.html')

@app.route('/sorting/quick')
def quick_sort():
    return render_template('quicksorting.html')


if __name__ == '__main__':
    app.run(debug=True)