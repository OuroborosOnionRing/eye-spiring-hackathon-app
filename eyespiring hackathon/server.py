from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/help')
def help():
    return render_template('next.html')

@app.route('/selfhelp')
def selfhelp():
    return render_template("selfhelp.html")

@app.route('/prohelp')
def prohelp():
    return render_template("prohelp.html")
#############################################################selfhelp
@app.route('/sports')
def sports():
    return render_template("sports.html")

@app.route('/causal')
def casual():
    return render_template("casual.html")

@app.route('/comfort')
def comfort():
    return render_template("comfort.html")

@app.route('/work')
def work():
    return render_template("work.html")
##################################################################
@app.route('/checkout')
def checkout():
    return render_template("checkout.html")

@app.route('/thanks')
def thanks():
    return render_template('thanks.html')

@app.route('/chat')
def chat():
    return render_template('chat.html')

@app.route('/maps')
def maps():
    return render_template('maps.html')


app.run(debug=True, port=5000)