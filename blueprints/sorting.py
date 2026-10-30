from flask import Blueprint, render_template

sorting_bp = Blueprint('sorting', __name__)

@sorting_bp.route('/sorting')
def sorting_dashboard():
    return render_template('sorting_menu.html')

@sorting_bp.route('/sorting/bubble')
def bubble_sort():
    return render_template('bubblesorting.html')  # Tugma sa bubblesorting.html

@sorting_bp.route('/sorting/selection')
def selection_sort():
    return render_template('selectionsorting.html') # Tugma sa selectionsorting.html

@sorting_bp.route('/sorting/insertion')
def insertion_sort():
    return render_template('insertionsorting.html') # Tugma sa insertionsorting.html

@sorting_bp.route('/sorting/merge')
def merge_sort():
    return render_template('mergesorting.html')     # Tugma sa mergesorting.html

@sorting_bp.route('/sorting/quick')
def quick_sort():
    return render_template('quicksorting.html')     # Tugma sa quicksorting.html