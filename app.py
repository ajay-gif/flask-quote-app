from flask import Flask, render_template, request
import random
import os

app = Flask(__name__)

# List of quote dictionaries
QUOTES = [
    {
        "text": "The only way to do great work is to love what you do.",
        "author": "Steve Jobs",
        "category": "Inspirational"
    },
    {
        "text": "I am so clever that sometimes I don't understand a single word of what I am saying.",
        "author": "Oscar Wilde",
        "category": "Funny"
    },
    {
        "text": "Life is what happens when you're busy making other plans.",
        "author": "John Lennon",
        "category": "Inspirational"
    },
    {
        "text": "Behind every great person is a substantial amount of coffee.",
        "author": "Anonymous",
        "category": "Funny"
    },
    {
        "text": "It always seems impossible until it's done.",
        "author": "Nelson Mandela",
        "category": "Inspirational"
    },
    {
        "text": "My wallet is like an onion, opening it makes me cry.",
        "author": "Anonymous",
        "category": "Funny"
    },
    {
        "text": "The future belongs to those who believe in the beauty of their dreams.",
        "author": "Eleanor Roosevelt",
        "category": "Inspirational"
    },
    {
        "text": "I'm not arguing, I'm just explaining why I'm right.",
        "author": "Anonymous",
        "category": "Funny"
    }
]

@app.route('/')
def home():
    selected_category = request.args.get('category', 'all')
    
    # Filter quotes if a category is selected
    if selected_category in ['Inspirational', 'Funny']:
        filtered_quotes = [q for q in QUOTES if q['category'] == selected_category]
    else:
        filtered_quotes = QUOTES

    # Select a random quote
    random_quote = random.choice(filtered_quotes)

    return render_template(
        'index.html',
        quote=random_quote,
        current_category=selected_category
    )

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)