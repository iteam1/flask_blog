from flask import Blueprint, render_template

errors = Blueprint('errors',__name__)

# thread error handler as a round
@errors.app_errorhandler(404)
def error_404(error):
    return render_template('errors/404.html'),404

# thread error handler as a round
@errors.app_errorhandler(403)
def error_403(error):
    return render_template('errors/403.html'),403

# thread error handler as a round
@errors.app_errorhandler(405)
def error_405(error):
    return render_template('errors/405.html'),405

# thread error handler as a round
@errors.app_errorhandler(500)
def error_500(error):
    return render_template('errors/500.html'),500