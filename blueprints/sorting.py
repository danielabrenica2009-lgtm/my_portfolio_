from flask import Blueprint, render_template

sorting_bp = Blueprint('sorting', __name__)

@sorting_bp.route('/sorting')
def sorting_dashboard():
    return render_template('sorting_menu.html')

@sorting_bp.route('/sorting/bubble')
def bubble_sort():
    return render_template('bubblesorting.html')  # Connects with bubblesorting.html

@sorting_bp.route('/sorting/selection')
def selection_sort():
    return render_template('selectionsorting.html') # Connects with selectionsorting.html

@sorting_bp.route('/sorting/insertion')
def insertion_sort():
    return render_template('insertionsorting.html') # Connects with insertionsorting.html

@sorting_bp.route('/sorting/merge')
def merge_sort():
    return render_template('mergesorting.html')     # Connects with mergesorting.html

@sorting_bp.route('/sorting/quick')
def quick_sort():
    return render_template('quicksorting.html')     # Connects with quicksorting.html