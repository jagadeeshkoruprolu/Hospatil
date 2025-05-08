from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

symptom_conditions = {
    "hi": "Hello! How can I assist you today?",
    "hello": "Hi there! What symptoms are you experiencing?",
    "hey": "Hey! I'm here to help you with health-related queries.",
    "fever": "You may have a common viral infection. Stay hydrated and rest.",
    "headache": "It might be a migraine or tension headache. Try resting in a quiet, dark room.",
    "cough": "This could be a sign of cold or allergy. If persistent, consult a doctor.",
    "stomach pain": "Could be indigestion or gastritis. Drink warm water and avoid spicy food.",
    "cold": "It may be seasonal flu or common cold. Take rest and drink warm fluids.",
    "sore throat": "It may be due to infection. Gargle with warm salt water.",
    "back pain": "Might be due to muscle strain. Apply hot compress and rest.",
    "diarrhea": "Could be food poisoning. Stay hydrated and eat bland food.",
    "vomiting": "Avoid solid food for a while and sip oral rehydration solutions.",
    "skin rash": "May be an allergy. Consider antihistamines and consult a dermatologist.",
    "fatigue": "You may be overworked. Ensure proper sleep and nutrition.",
    "dizziness": "Could be due to low BP or dehydration. Sit down and drink water."
}

medicine_recommendations = {
    "fever": ["Paracetamol", "Crocin", "Dolo 650"],
    "headache": ["Aspirin", "Ibuprofen", "Disprin"],
    "cough": ["Benadryl", "Dextromethorphan", "Honey syrup"],
    "stomach pain": ["Omeprazole", "Pantoprazole", "Gelusil"],
    "cold": ["Cetrizine", "Sinarest"],
    "sore throat": ["Strepsils", "Vicks lozenges"],
    "back pain": ["Moov", "Volini", "Ibuprofen"],
    "diarrhea": ["ORS", "Loperamide"],
    "vomiting": ["Domperidone", "Emeset"],
    "skin rash": ["Cetirizine", "Calamine lotion"],
    "fatigue": ["Multivitamins", "Rest"],
    "dizziness": ["ORS", "Fludrocortisone"]
}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    user_input = request.args.get("msg").lower()

    response = symptom_conditions.get(user_input, "Sorry, I don't have information on that. Please consult a doctor.")

    if user_input in medicine_recommendations:
        medicines = medicine_recommendations[user_input]
    else:
        medicines = []

    return jsonify({"response": response, "medicines": medicines})

if __name__ == "__main__":
    app.run(debug=True)


#
# pip install flask
# python app.py
#
# 
# 
# 
# 
# 0