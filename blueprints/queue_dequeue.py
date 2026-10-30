from flask import Blueprint, render_template, request
from node import Queue, Deque

queue_dequeue_bp = Blueprint('queue_dequeue', __name__)
global_queue = Queue()
global_deque = Deque()

@queue_dequeue_bp.route('/queue', methods=['GET', 'POST'])
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

@queue_dequeue_bp.route('/dequeue', methods=['GET', 'POST'])
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