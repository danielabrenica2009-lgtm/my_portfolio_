from flask import Blueprint, render_template, request
from node import infix_to_postfix

infix_bp = Blueprint('infix', __name__)

@infix_bp.route('/infixtopostfix', methods=['GET', 'POST'])
def infixtopostfix():
    result, steps, infix_expr = None, [], ""
    if request.method == 'POST':
        infix_expr = request.form.get('infixExpression', '')
        if infix_expr:
            result, steps = infix_to_postfix(infix_expr)
    return render_template('infixtopostfix.html', result=result, steps=steps, infix_expr=infix_expr)