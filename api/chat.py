from flask import Flask, request, jsonify

app = Flask(__name__)

def chatbot_response(message):
    responses = {
        "hello": "Hi there! How can I help you?",
        "how are you": "I'm just a bot, but I'm doing great!",
        "bye": "Goodbye! Have a nice day!"
    }
    return responses.get(message.lower(), "Sorry, I don't understand that.")

@app.route("/api/chat", methods=["GET"])
def chat():
    user_message = request.args.get("message")
    if not user_message:
        return jsonify({"error": "Please provide a message parameter."}), 400
    response = chatbot_response(user_message)
    return jsonify({"response": response})

def handler(event, context):
    return app(event, context)
