from flask import Flask, request

app = Flask(__name__)
booking = [
    {"id":1, "whn":"2026-11-25","who":"Andrew"},
    {"id":2, "whn":"2026-11-27","who":"Andrew"},
]

@app.route("/", methods=["GET"])
def index():
    return """
    <script src=/static/m.js defer></script>
    <script src=/static/booking.js defer></script>
    <link rel="stylesheet" href=/static/booking.css>
    <h1>Welcome to the Booking API</h1>"""

@app.route("/api/booking", methods=["POST"])
def make_booking():
    data = request.get_json()
    new_id = len(booking) + 1
    data["id"] = new_id
    booking.append(data)
    return {"booking": booking}

@app.route("/api/booking", methods=["GET"])
def list_booking():
    return {"booking": booking}

if __name__ == "__main__":
    app.run(debug=True)