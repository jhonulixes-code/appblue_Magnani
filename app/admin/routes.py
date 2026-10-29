from flask import render_template
from app.admin import admin

@admin.route('/panel')
def panel():
    return render_template('panel.html')