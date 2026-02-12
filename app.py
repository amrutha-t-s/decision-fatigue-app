import random
from flask import Flask, render_template, request, session
from datetime import datetime
import json

app = Flask(__name__)
app.secret_key = 'kitty-secret-meow-123'

# Default + Custom options (persistent)
def get_options():
    default_options = {
        'home': ['Relax on couch 🛋️', 'Watch Netflix 📺', 'Play with kitty 🐱', 'Nap time 😴'],
        'outfits': ['Casual jeans 👖', 'Party dress ✨', 'Sporty look 🏃‍♀️', 'Cozy sweater 🧥'],
        'outings': ['Coffee shop ☕', 'Park walk 🌳', 'Movie night 🎬', 'Shopping spree 🛍️'],
        'meals': ['Pizza party 🍕', 'Healthy salad 🥗', 'Pasta love 🍝', 'Ice cream dessert 🍦']
    }
    
    # Load custom options from session
    custom = session.get('custom_options', {})
    for category, options in custom.items():
        if category not in default_options:
            default_options[category] = []
        default_options[category].extend(options)
    
    return default_options

# Decision history
def get_history():
    return session.get('history', [])

@app.route('/', methods=['GET', 'POST'])
def index():
    options = get_options()
    choice = None
    history = get_history()
    
    if request.method == 'POST':
        category = request.form.get('category')
        custom_option = request.form.get('custom_option')
        
        if custom_option and custom_option.strip():
            # Add custom option
            custom_options = session.get('custom_options', {})
            if 'custom' not in custom_options:
                custom_options['custom'] = []
            custom_options['custom'].append(custom_option.strip())
            session['custom_options'] = custom_options
            category = 'custom'
            choice = custom_option.strip()
        elif category == 'surprise':
            # Surprise me! (random category + choice)
            category = random.choice(list(options.keys()))
            choice = random.choice(options[category])
        elif category in options:
            choice = random.choice(options[category])
        
        if choice:
            # Save to history
            history.append({
                'choice': choice,
                'category': category,
                'time': datetime.now().strftime("%H:%M")
            })
            session['history'] = history[-10:]  # Keep last 10
    
    return render_template('index.html', 
                         choice=choice, 
                         options=options, 
                         history=history[-5:],
                         has_history=len(history) > 0)

if __name__ == '__main__':
    app.run(debug=True)
