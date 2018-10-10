from flask import *
app = Flask(__name__)

recipes_data = json.load(open("static/jsonfiles/recipes.json"))
food_data = json.load(open("static/jsonfiles/food.json"))

"""
 MAIN PAGES
"""
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

"""
 REAL FOOD - FRUIT
"""
@app.route('/fruit/')
@app.route('/realfood/fruit/')
def fruit():
    return render_template('realfood/fruit_layout.html')

@app.route('/spring/')
@app.route('/summer/')
@app.route('/fruit/spring/')
@app.route('/fruit/summer/')
@app.route('/realfood/spring/')
@app.route('/realfood/summer/')
@app.route('/realfood/fruit/spring-and-summer/')
def spring():
    return render_template('realfood/spring_fruits.html')

@app.route('/fall/')
@app.route('/winter/')
@app.route('/realfood/fall/')
@app.route('/realfood/winter/')
@app.route('/realfood/fall-and-winter/')
@app.route('/realfood/fruit/fall/')
@app.route('/realfood/fruit/winter/')
@app.route('/realfood/fruit/fall-and-winter/')
def winter():
    return render_template('realfood/winter_fruits.html')

@app.route('/tropical/')
@app.route('/fruit/tropical/')
@app.route('/realfood/fruit/tropical/')
def tropical():
    return render_template('realfood/tropical_fruits.html')

@app.route('/<fruit>/')
@app.route('/realfood/<fruit>/')
@app.route('/realfood/fruit/<fruit>/')
@app.route('/realfood/fruit/winter/<fruit>/')
@app.route('/realfood/fruit/fall/<fruit>/')
@app.route('/realfood/fruit/summer/<fruit>/')
@app.route('/realfood/fruit/spring/<fruit>/')
@app.route('/realfood/fruit/spring-and-summer/<fruit>/')
@app.route('/realfood/fruit/fall-and-winter/<fruit>/')
@app.route('/realfood/fruit/tropical/<fruit>/')
def s_fruits(fruit):
    return render_template('realfood/all_fruits.html', fruit=fruit)

"""
 REAL FOOD - VEGETABLES
"""
@app.route('/vegetables/')
@app.route('/realfood/vegetables/')
def vegs():
    return render_template('realfood/vegetables.html')

@app.route('/vegetables/<veg>/')
@app.route('/realfood/vegetables/<veg>/')
def vegs2(veg):
    return render_template('realfood/all_vegetables.html', veg=veg)

"""
 REAL FOOD - FISH & MEAT
"""
@app.route('/fish/')
@app.route('/meat/')
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

"""
 REAL FOOD - OTHERS
"""
@app.route('/realfood/others/')
def other():
    return render_template('realfood/other.html')

@app.route('/realfood/others/<other>/')
def all_others(other):
    return render_template('realfood/all_others.html', other=other)


"""
 MEAL PLAN - RECIPES
"""
@app.route('/recipes/')
@app.route('/mealplan/recipes/')
def r():
    # PRINT ALL RECIPE NAMES
    names = []
    for r in recipes_data['recipes']:
        names.append(r['name'])
    return render_template('mealplan/recipes.html', recipes=names)

@app.route('/recipes/<search>/')
@app.route('/mealplan/recipes/<search>/')
def r_search(search):
    # PRINT ONE RECIPE
    ingredients = []
    for r in recipes_data['recipes']:
        if r['name'].lower() == search:
            name = r['name']
            how_to_cook = r['preparation']
            ingredients = r['ingredients']
        else:
            # 404 ERROR
            name = "Sorry, we don't have that recipe, yet"
            how_to_cook = ":("
            ingredients = []
    return render_template('mealplan/recipe.html', name=name , preparation=how_to_cook, ingredients=ingredients)

@app.route('/groceries/<option>/')
def groceryopt(option):
    option.lower()
    if option == 'diet' or option == 'sport' or option == 'events':
        return render_template('groceries/grocery_shop.html', option=option)
    else:
        return render_template('404error.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
