import random
from flask import Flask, render_template, request

app = Flask(__name__)

# Sample options for categories

OPTIONS = {
    'home': ['Relax on couch 🛋️', 'Watch Netflix 📺', 'Play with kitty 🐱', 'Nap time 😴'],
    'outfits': ['Casual jeans 👖', 'Party dress ✨', 'Sporty look 🏃‍♀️', 'Cozy sweater 🧥'],
    'outings': ['Coffee shop ☕', 'Park walk 🌳', 'Movie night 🎬', 'Shopping spree 🛍️'],
    'meals': ['Pizza party 🍕', 'Healthy salad 🥗', 'Pasta love 🍝', 'Ice cream dessert 🍦']
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
