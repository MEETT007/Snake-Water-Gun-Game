from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
import random

app = Flask(__name__)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///game_history.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database model
class GameResult(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_choice = db.Column(db.String(10), nullable=False)
    computer_choice = db.Column(db.String(10), nullable=False)
    result = db.Column(db.String(10), nullable=False)

# Initialize the database
with app.app_context():
    db.create_all()

# Route for the root URL
@app.route('/')
def index():
    return render_template('index.html')

# Route to play the game
@app.route('/play', methods=['POST'])
def play_game():
    data = request.json
    user_choice_str = data.get('choice')
    choices = {"s": 1, "w": 0, "g": -1}
    reversed_choices = {1: "Snake", 0: "Water", -1: "Gun"}

    if user_choice_str not in choices:
        return jsonify({"error": "Invalid choice"}), 400

    user_choice = choices[user_choice_str]
    computer_choice = random.choice([-1, 0, 1])

    # Determine result
    result = (
        "Draw" if computer_choice == user_choice else
        "Lose" if (computer_choice == 1 and user_choice == 0) or
                 (computer_choice == 0 and user_choice == -1) or
                 (computer_choice == -1 and user_choice == 1) else
        "Win"
    )

    # Save the result in the database
    game_result = GameResult(
        user_choice=reversed_choices[user_choice],
        computer_choice=reversed_choices[computer_choice],
        result=result
    )
    db.session.add(game_result)
    db.session.commit()

    return jsonify({
        "user_choice": reversed_choices[user_choice],
        "computer_choice": reversed_choices[computer_choice],
        "result": result
    })

# Route to fetch game history
@app.route('/history', methods=['GET'])
def get_history():
    results = GameResult.query.all()
    return jsonify([
        {
            "id": result.id,
            "user_choice": result.user_choice,
            "computer_choice": result.computer_choice,
            "result": result.result
        } for result in results
    ])

if __name__ == '__main__':
    app.run(debug=True)
