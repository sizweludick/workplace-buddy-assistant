from flask import Flask, request, render_template
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

# --- SARS Connector ---
def fetch_sars_tax_info():
    url = "https://www.sars.gov.za/tax-rates/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    return soup.get_text()[:500]

# --- Labour Law Connector ---
def fetch_labour_info():
    url = "https://www.labour.gov.za/DocumentCenter"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    return soup.get_text()[:500]

# --- Salary Calculator ---
def calculate_salary(hours, rate, period="hourly"):
    if period == "hourly":
        return hours * rate
    elif period == "daily":
        return hours * rate
    elif period == "weekly":
        return hours * rate * 5
    elif period == "monthly":
        return hours * rate * 22
    elif period == "annual":
        return hours * rate * 260
    else:
        raise ValueError("Invalid period")

# --- Messaging Service ---
class NoticeBoard:
    def __init__(self):
        self.messages = []

    def post_message(self, manager, message):
        self.messages.append({"manager": manager, "message": message})

    def view_messages(self):
        return self.messages

board = NoticeBoard()

# --- Routes ---
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/tax")
def tax_info():
    return fetch_sars_tax_info()

@app.route("/labour")
def labour_info():
    return fetch_labour_info()

@app.route("/salary", methods=["POST"])
def salary():
    hours = int(request.form.get("hours", 0))
    rate = int(request.form.get("rate", 0))
    period = request.form.get("period", "hourly")
    return f"You earn R{calculate_salary(hours, rate, period)} for {period} work."

@app.route("/messages", methods=["POST"])
def post_message():
    manager = request.form.get("manager")
    message = request.form.get("message")
    board.post_message(manager, message)
    return "Message posted successfully! <a href='/messages'>View Messages</a>"

@app.route("/messages", methods=["GET"])
def view_messages():
    return "<br>".join([f"{m['manager']}: {m['message']}" for m in board.view_messages()])

if __name__ == "__main__":
    app.run(debug=True)
