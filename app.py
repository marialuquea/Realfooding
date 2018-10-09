from flask import *
app = Flask(__name__)

@app.route('/')
def root():
    return render_template('index.html')

@app.route('/realfood/')
def realfood():
    return render_template('realfood.html')

@app.route('/ultraprocessed/')
def ultra():
    return render_template('ultra.html')

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
    return render_template('realfood/fruit_layout.html')

@app.route('/realfood/fruit/spring-and-summer/')
def spring():
    return render_template('realfood/spring_fruits.html')

@app.route('/realfood/fruit/winter/<fruit>/')
@app.route('/realfood/fruit/fall/<fruit>/')
@app.route('/realfood/fruit/summer/<fruit>/')
@app.route('/realfood/fruit/spring/<fruit>/')
@app.route('/realfood/fruit/spring-and-summer/<fruit>/')
@app.route('/realfood/fruit/fall-and-winter/<fruit>/')
@app.route('/realfood/fruit/tropical/<fruit>/')
def s_fruits(fruit):
    return render_template('realfood/all_fruits.html', fruit=fruit)

@app.route('/realfood/fruit/fall-and-winter/')
def winter():
    return render_template('realfood/winter_fruits.html')

@app.route('/realfood/fruit/tropical/')
def tropical():
    return render_template('realfood/tropical_fruits.html')


@app.route('/realfood/vegetables/')
def vegs():
    return render_template('realfood/vegetables.html')

@app.route('/realfood/vegetables/<veg>/')
def vegs2(veg):
    return render_template('realfood/all_vegetables.html', veg=veg)

@app.route('/realfood/fish/')
@app.route('/realfood/meat/')
@app.route('/realfood/fish-meat/')
def fm():
    return render_template('realfood/fish-meat.html')

@app.route('/realfood/fish/<type>/')
@app.route('/realfood/meat/<type>/')
@app.route('/realfood/fish-meat/<type>/')
def fm2(type):
    return render_template('realfood/all-fish-meat.html', type=type)

@app.route('/realfood/others/')
def other():
    return render_template('realfood/other.html')

@app.route('/realfood/others/<other>/')
def all_others(other):
    return render_template('realfood/all_others.html', other=other)


data = json.load(open("static/jsonfiles/recipes.json"))
@app.route('/mealplan/recipes/')
def r():
    # PRINT ALL RECIPE NAMES
    names = []
    for r in data['recipes']:
        names.append(r['name'])
    return render_template('mealplan/recipes.html', recipes=names)

@app.route('/mealplan/recipes/<search>')
def r_search(search):
    # PRINT ONE RECIPE
    ingredients = []
    for r in data['recipes']:
        if r['name'].lower() == search:
            name = r['name']
            how_to_cook = r['preparation']
            for i in r['ingredients']:
                ingredients.append(i)
    return render_template('mealplan/recipe.html', name=name , preparation=how_to_cook, ingredients=ingredients)




if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
