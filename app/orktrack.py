from flask import Blueprint, render_template, abort, request, jsonify
from app.publisher import publisher





orktrack = Blueprint('Orktrack', __name__, template_folder='templates', url_prefix='/orktrack')

@orktrack.route('/')
def index():
    return "pyOrkTrack is running. Use /command to communicate"


@orktrack.route('/command', methods=['GET', 'POST'])
def command():



    if request.args.get('type') == "init":
        print("Orkaudio Connection Initialized. Orkaudio is now connected")
        return ("class=simpleresponse success=true comment=PyOrekaConnectSuccess")

    elif request.args.get('type') == "tape":
        call_data = request.args.to_dict()
        publisher.publish(call_data)

        print("Received Tape message")
        return ("class=taperesponse success=true comment=ReceivedTape deletetape=false")

    else:

        print("Unknown post from orkaudio:", request)
        return ("class=response success=false comment=UnknownResponseType")
