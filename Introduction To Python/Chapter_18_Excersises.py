# Things to do, chapter 18
# https://learning.oreilly.com/library/view/introducing-python-2nd/9781492051374/ch18.html#idm45794967988776

from flask import Flask, render_template, request

# 18.1 If you haven’t installed flask yet, do so now. This will also install werkzeug, jinja2, and possibly other
# packages.
print("\n------ 18.1 ------")
print(f"Flask is installed: {Flask}")

# 18.2 Build a skeleton website, using Flask’s debug/reload development web server. Ensure that the server starts up
# for hostname localhost on default port 5000. If your computer is already using port 5000 for something else,
# use another port number.
print("\n------ 18.2 ------")

# I'm not sure what the author means by "skeleton website". I assume it's just the app itself, without any pages.
app = Flask(__name__, static_folder='.', static_url_path='', template_folder="Files")

# 18.3 Add a home() function to handle requests for the home page. Set it up to return the string It's alive!.
print("\n------ 18.3 ------")


@app.route('/')
def home():
    return "It's alive!!"


print("Created page")

# 18.4 Create a Jinja2 template file called home.html with the following contents:
# <html>
# <head>
# <title>It's alive!</title>
# <body>
# I'm of course referring to {{thing}}, which is {{height}} feet tall and {{color}}.
# </body>
# </html>
print("\n------ 18.4 ------")
print("Created template home.html in the Files folder")

# 18.5 Modify your server’s home() function to use the home.html template. Provide it with three GET parameters:
# thing, height, and color.
print("\n------ 18.5 ------")


# We'll make a distinct page for this one so the previous one doesn't break.
@app.route('/second/')
def home2():
    thing = request.args.get('thing')
    height = request.args.get('height')
    colour = request.args.get('colour')
    return render_template('home.html', thing=thing, height=height, colour=colour)


app.run(port=5320, debug=True)

# When you run this script, go here to see it in action:
# First site:
# http://127.0.0.1:5320

# Second site:
# http://127.0.0.1:5320/second/?thing=Kermit&height=61&colour=green
