from flask import Blueprint, render_template, request
from node import LinkedList

linkedlist_bp = Blueprint('linkedlist', __name__)
global_linked_list = LinkedList()

@linkedlist_bp.route('/linkedlist', methods=['GET', 'POST'])
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