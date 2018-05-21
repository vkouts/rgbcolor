from flask_script import Manager
from app import app, db
from app.models import WebColor

manager = Manager(app)
RED = {'name': 'Pure Red', 'color': '#FF0000'}
GREEN = {'name': 'Pure Green', 'color': '#00FF00'}
BLUE = {'name': 'Pure Blue', 'color': '#0000FF'}


@manager.command
def show_urls():
    import urllib
    output = []
    for rule in app.url_map.iter_rules():

        options = {}
        for arg in rule.arguments:
            options[arg] = "[{0}]".format(arg)

        methods = ','.join(rule.methods)
        url = url_for(rule.endpoint, **options)
        line = urllib.unquote("{:50s} {:20s} {}".format(rule.endpoint, methods, url))
        output.append(line)

    for line in sorted(output):
        print(line)


@manager.command
def parse_x11():
    import re
    with open('x11colors.txt', 'r') as fil:
        for line in fil:
            searchstr = re.match('(.*)\s+(#.*?)\s+.*', line)
            if searchstr:
                color_name = searchstr.group(1)
                color_val = searchstr.group(2)
                print(color_name, color_val)
                c = WebColor(name=color_name, color=color_val)
                db.session.add(c)
                db.session.commit()

@manager.command
def random_webcolor():
    import random
    from time import sleep
    from app import ser

    max_count = WebColor.query.count() + 1
    sleep(3)

    while True:
        if random.choice([1,2,3]) == 1:
            my_color = random.choice([RED, GREEN, BLUE])

            out = '{} {} {}'.format(
                int(my_color['color'][1:3], 16),
                int(my_color['color'][3:5], 16),
                int(my_color['color'][3:7], 16)
            )
            ser.write(bytes(out, encoding='utf-8'))
            print("color = {color}({code})".format(color=my_color['name'], code=my_color['color']))
        else:
            indx = random.randrange(1, max_count)
            my_color = WebColor.query.get(indx)

            out = '{} {} {}'.format(
                int(my_color.color[1:3], 16),
                int(my_color.color[3:5], 16),
                int(my_color.color[3:7], 16)
            )

            ser.write(bytes(out, encoding='utf-8'))
            print("color = {color}({code})".format(color=my_color.name, code=my_color.color))
            #sleep(TIMEPERIOD)
        sleep(random.randrange(2,10))

@manager.command
def random_color():
    import random
    from time import sleep
    from app import ser

    def random_color():
        return random.choice([0, 254]) if random.choice([True, False]) \
        else random.randrange(0,254)

    sleep(3)

    while True:
        if random.choice([1,2,3]) == 1:
            my_color = random.choice([RED, GREEN, BLUE])

            out = '{} {} {}'.format(
                int(my_color['color'][1:3], 16),
                int(my_color['color'][3:5], 16),
                int(my_color['color'][3:7], 16)
            )
            ser.write(bytes(out, encoding='utf-8'))
            print("color = {color}({code})".format(color=my_color['name'], code=my_color['color']))
        else:
            red = random_color()
            green = random_color()
            blue = random_color()

            out = '{} {} {}'.format(red, green, blue)
            ser.write(bytes(out, encoding='utf-8'))
            print("color = random(#%X%X%X)" % (red, green, blue))
        sleep(random.randrange(2,10))


if __name__ == "__main__":
    manager.run()
