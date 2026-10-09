from flask import Flask, render_template, request, jsonify
from datetime import datetime

app = Flask(__name__)


# -----------------------------------
# Chatbot response function
# -----------------------------------

def chatbot_response(message):

    message = message.lower().strip()

    # Greetings
    if message in ["hi", "hello", "hey", "hii"]:
        return "Hello! 👋 How can I help you?"

    # Name
    elif "your name" in message or "who are you" in message:
        return "I am PyBot, a Python-based chatbot 🤖."

    # Python
    elif "python" in message:
        return (
            "Python is a high-level, interpreted programming language "
            "known for its simple syntax and wide range of applications."
        )

    # Programming
    elif "programming" in message:
        return (
            "Programming is the process of writing instructions "
            "that a computer can execute."
        )

    # Flask
    elif "flask" in message:
        return (
            "Flask is a lightweight Python web framework used "
            "to create web applications and APIs."
        )

    # API
    elif "api" in message:
        return (
            "API stands for Application Programming Interface. "
            "It allows different software applications to communicate "
            "with each other."
        )

    # Time
    elif "time" in message:
        current_time = datetime.now().strftime("%I:%M %p")
        return f"The current time is {current_time}."

    # Date
    elif "date" in message:
        current_date = datetime.now().strftime("%d-%m-%Y")
        return f"Today's date is {current_date}."

    # How are you
    elif "how are you" in message:
        return "I am doing great! 😊 Thanks for asking."

    # Help
    elif "help" in message:
        return (
            "You can ask me about Python, programming, Flask, "
            "API, date, time, or simply say hello."
        )

    # Thank you
    elif "thank" in message:
        return "You're welcome! 😊"

    # Bye
    elif message in ["bye", "goodbye", "see you"]:
        return "Goodbye! 👋 Have a nice day!"

    # Default response
    else:
        return (
            "Sorry, I don't understand that yet. "
            "Try asking me about Python, Flask, API, programming, "
            "date or time."
        )


# -----------------------------------
# Home page
# -----------------------------------

@app.route("/")
def home():
    return render_template("index.html")


# -----------------------------------
# Chatbot API
# -----------------------------------

@app.route("/api/chat", methods=["POST"])
def chat():

    data = request.get_json()

    user_message = data.get("message", "").strip()

    if not user_message:
        return jsonify({
            "error": "Please enter a message."
        }), 400

    bot_message = chatbot_response(user_message)

    return jsonify({
        "user_message": user_message,
        "bot_message": bot_message,
        "status": "success"
    })


# -----------------------------------
# Run application
# -----------------------------------

if __name__ == "__main__":
    app.run(debug=True)