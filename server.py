from flask import Flask

app = Flask(__name__)
booking = [
    {"id":1, "whn":"2026-11-25","who":"Andrew"},
    {"id":2, "whn":"2026-11-27","who":"Andrew"},
]

@app.route("/", methods=["GET"])
def index():
    return "<h1>Welcome to the Booking API</h1>"

@app.route("/api/booking", methods=["GET"])
def list_booking():
    return {"booking": booking}

if __name__ == "__main__":
    app.run(debug=True)