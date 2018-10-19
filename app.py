from flask import *
import os
import json
import codecs

app = Flask(__name__)
app.secret_key = os.urandom(12)

recipes_data = json.load(open("jsonfiles/recipes.json"))
doubts = json.load(open("jsonfiles/doubts.json"))
fooddata = json.load(open("jsonfiles/food.json"))

"""
 MAIN PAGES
"""
@app.route('/')
def root():
    if not session.get('logged_in'):
        print('---------------YOU ARE NOT LOGGED IN--------------')
        login = False
    else:
        print('---------------YOU ARE LOGGED IN--------------')
        login = True
    return render_template('index.html', login=login)

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

def generateID(fileName):
    file = json.load(open("jsonfiles/" + fileName))
    max = 0
    for x in file:
        tempX = int(x)
        if tempX > max:
            max = tempX
    max += 1
    return str(max)

def findFood(search):
    for x in fooddata['stuff']:
        if x['name'].lower() == search.lower():
            name = x["name"]
            image = x["image"]
            description = x["description"]
            type = x['type']
            break
        else:
            # 404 error
            name = "Sorry, not found"
            image = "/static/img/error.png"
            description = "This is the person to blame."
            type = ""
    return (name, image, description, type)

@app.route('/contact/', methods=['POST', 'GET'])
def contact():
    if not session.get('logged_in'):
        login = False
        if request.method == 'POST':
            name=request.form['name']
            doubt=request.form['doubt']
            email=request.form['email']
            print (name, " ", email, " ", doubt)
            if name and doubt and email:
                # Save the doubt in json file
                newID = generateID('doubts.json')
                customer = {newID: {"name" : name, "email" : email, "doubt" : doubt}}
                doubts.update(customer)
                print(doubts)
                with open('jsonfiles/doubts.json', 'w') as outfile:
                    json.dump(doubts, outfile)
                flash('Thanks for your doubt ' + name + ' we will answer ASAP!')
            else:
                flash('Please fill all parts.')
    else:
        login = True
    return render_template('contact.html', doubt=doubts, login=login)

@app.route('/login', methods=['POST', 'GET'])
def do_admin_login():
    if request.method == 'GET':
        return render_template('login.html')
    if request.method == 'POST':
        if request.form['password'] == '1234' and request.form['username'] == 'maria':
            session['logged_in'] = True
            print('---------------LOGIN SUCCESSFUL-----------------')
            return redirect('/', code=302)
        else:
            print('---------------WRONG PASSWORD--------------')
            message = 'Wrong password'
            return render_template('login.html', message=message)


@app.route("/logout")
def logout():
    session['logged_in'] = False
    print('---------------You logged out--------------')
    return redirect('/', code=302)

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
    name, image, description, type = findFood(fruit)
    return render_template('realfood/foodies.html', name=name, image=image, description=description, type=type)

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
    name, image, description, type = findFood(veg)
    return render_template('realfood/foodies.html', name=name, image=image, description=description, type=type)

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

@app.route('/realfood/fish/<hello>/')
@app.route('/realfood/meat/<hello>/')
@app.route('/realfood/fish-meat/<hello>/')
def fm2(hello):
    name, image, description, type = findFood(hello)
    return render_template('realfood/foodies.html', name=name, image=image, description=description, type=type)

"""
 REAL FOOD - OTHERS
"""
@app.route('/realfood/others/')
def other():
    return render_template('realfood/other.html')

@app.route('/realfood/others/<other>/')
def all_others(other):
    name, image, description, type = findFood(other)
    return render_template('realfood/foodies.html', name=name, image=image, description=description, type=type)


"""
 MEAL PLAN - RECIPES
"""
@app.route('/recipes/')
@app.route('/mealplan/recipes/')
def r():
    if not session.get('logged_in'):
        login = False
    else:
        login = True
    # PRINT ALL RECIPE NAMES
    names = []
    for r in recipes_data['recipes']:
        names.append(r['name'])
    return render_template('mealplan/recipes.html', recipes=names, login=login)

@app.route('/recipes/<search>/')
@app.route('/mealplan/recipes/<search>/')
def r_search(search):
    # PRINT ONE RECIPE
    ingredients = [{}]
    for r in recipes_data['recipes']:
        if r['name'].lower() == search.lower():
            print(search)
            print(r['name'])
            name = r['name']
            how_to_cook = r['preparation']
            ingredients = r['ingredients']
            break
        else:
            # 404 ERROR
            name = "Sorry, we don't have that recipe, yet"
            how_to_cook = ":("
            ingredients = []
    return render_template('mealplan/recipe.html', name=name , preparation=how_to_cook, ingredients=ingredients)

@app.route('/mealplan/<option>/')
def mealplanopt(option):
    option.lower()
    if option == 'breakfast' or option == 'lunch' or option == 'dinner' or option == 'snacks':
        return render_template('mealplan/plans.html', option=option)
    else:
        return render_template('404error.html')


@app.route('/groceries/<option>/')
def groceryopt(option):
    option.lower()
    if option == 'diet' or option == 'sport' or option == 'events':
        return render_template('groceries/grocery_shop.html', option=option)
    else:
        return render_template('404error.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404error.html'), 404


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
