from flask import render_template, send_from_directory
from app import app
from app.orktrack import orktrack

app.register_blueprint(orktrack)



@app.route('/audio/<path:filename>')
def get_orkaudio(filename):
    return send_from_directory('/var/log/orkaudio/audio', filename)





