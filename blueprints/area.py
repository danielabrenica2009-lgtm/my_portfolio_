from flask import Blueprint, render_template, request

area_bp = Blueprint('area', __name__)

@area_bp.route('/circle', methods=['GET', 'POST'])
def circle():
    result, radius = None, None
    if request.method == 'POST':
        try:
            radius = float(request.form.get('radius'))
            result = 3.14159 * (radius ** 2)
        except ValueError:
            result = None
    return render_template('circle.html', result=result, radius=radius)

@area_bp.route('/triangle', methods=['GET', 'POST'])
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

@area_bp.route('/touppercase', methods=['GET', 'POST'])
def touppercase():
    result, original_text = None, None
    if request.method == 'POST':
        original_text = request.form.get('inputString', '')
        result = original_text.upper()
    return render_template('touppercase.html', result=result, original_text=original_text)