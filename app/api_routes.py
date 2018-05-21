import json
from flask import Flask
from flask import render_template, url_for, redirect, request, abort, send_from_directory
from app import app, ser
from app.models import WebColor


@app.route('/api/v1/color_by_id', methods=['POST'])
def set_colorid():
    if not request.json:
       abort(400)
    id = int(request.json.get('id'))
    my_color = WebColor.query.get(id)
    if ser:
        out = '{} {} {}'.format(
            int(my_color.color[1:3], 16),
            int(my_color.color[3:5], 16),
            int(my_color.color[3:7], 16)
        )
        ser.write(bytes(out, encoding='utf-8'))
    return json.dumps({'color': my_color.color, 'name': my_color.name})


@app.route('/api/v1/set_color', methods=['POST'])
def set_color():
    if not request.json:
        abort(400)
    red = request.json.get('red')
    green = request.json.get('green')
    blue = request.json.get('blue')

    if ser:
        out = '{} {} {}'.format(red, green, blue)
        ser.write(bytes(out, encoding='utf-8'))
    return json.dumps({'color': "#%s%s%s" % (('%X' % red).zfill(2), ('%X' % green).zfill(2), ('%X' % blue).zfill(2))}), 200
