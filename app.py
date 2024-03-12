# Importations nécessaires
from flask import Flask, request, jsonify
from flask_mail import Mail, Message
from flask_cors import CORS

# Configuration de l'application Flask
app = Flask(__name__)
CORS(app, resources={r"/send_email": {"origins": "http://localhost:3000"}}, methods=["POST"])

# Configuration de Flask-Mail
app.config['SECRET_KEY'] = "tsfyguaistyatuis589566875623568956"
app.config['MAIL_SERVER'] = "smtp.googlemail.com"
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = "nourgarali12345@gmail.com"
app.config['MAIL_PASSWORD'] = "tmok wtxn cbia xobx"

mail = Mail(app)

# Route pour envoyer l'e-mail
@app.route("/send_email", methods=["POST"])
def send_email():
    try:
        # Récupérer les données depuis le corps de la requête
        email = request.json.get('email')
        subject = request.json.get('subject')
        message = request.json.get('message')

        # Configuration du message directement dans le code
        msg_title = subject
        sender = "noreply@app.com"
        msg = Message(msg_title, sender=sender, recipients=[email])
        msg.body = message

        # Envoi de l'e-mail
        mail.send(msg)

        # Retourner une réponse JSON avec les détails de l'e-mail
        return jsonify({
            "message": "Email envoyé avec succès",
            "sujet": subject,
            "corps_message": message
        })
    except Exception as e:
        print("Erreur:", str(e))
        return jsonify({"error": f"L'e-mail n'a pas pu être envoyé : {str(e)}"}), 500

# Point d'entrée de l'application Flask
if __name__ == "__main__":
    app.run(debug=True)
