from flask import *
app = Flask(__name__)

@app.route('/')
def root():
    return render_template('index.html')

@app.route('/realfood/')
def realfood():
    return render_template('realfood.html')

@app.route('/mealplan/')
def mealplan():
    return render_template('mealplan.html')

@app.route('/groceries/')
def groceries():
    return render_template('groceries.html')

@app.route('/contact/')
def contact():
    return render_template('contact.html')

@app.route('/realfood/fruit/')
def fruit():
    return render_template('fruit_layout.html')

@app.route('/realfood/fruit/spring-and-summer/')
def spring():
    return render_template('spring_fruits.html')

@app.route('/realfood/fruit/spring-and-summer/<fruit>/')
def s_fruits(fruit):
    return render_template('summer.html', fruit=fruit)

@app.route('/realfood/fruit/fall-and-winter/')
def winter():
    return render_template('winter_fruits.html')

@app.route('/realfood/fruit/fall-and-winter/<fruit>/')
def w_fruits(fruit):
    return render_template('winter.html', fruit=fruit)

@app.route('/realfood/fruit/tropical/')
def tropical():
    return render_template('tropical_fruits.html')

@app.route('/realfood/fruit/tropical/<fruit>/')
def t_fruits(fruit):
    return render_template('tropical.html', fruit=fruit)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
