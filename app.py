import random
from flask import Flask, render_template, request

app = Flask(__name__)

# Sample options for categories
OPTIONS = {
    'meals': ['Pasta', 'Salad', 'Burger', 'Sushi', 'Pizza'],
    'outfits': ['Jeans + T-shirt', 'Dress', 'Suit', 'Shorts + Top', 'Sweater + Pants'],
    'tasks': ['Check emails', 'Gym workout', 'Read book', 'Call friend', 'Grocery shopping']
}

@app.route('/', methods=['GET', 'POST'])
def index():
    choice = None
    if request.method == 'POST':
        category = request.form['category']
        choice = random.choice(OPTIONS.get(category, []))
    return render_template('index.html', choice=choice, options=OPTIONS)

if __name__ == '__main__':
    app.run(debug=True)
