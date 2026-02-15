from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    # Carica la Landing Page dalla cartella templates
    return render_template('index.html')

@app.route('/contact', methods=['POST'])
def contact():
    # Gestione della strategia relazionale (Alfano)
    return "Messaggio ricevuto! Grazie per esserti unito alla Carovana."

if __name__ == '__main__':
    app.run(debug=True)
