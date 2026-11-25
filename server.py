from flask import Flask, request
maxBookingsPerPerson= 2;

app = Flask(__name__)
booking = [
    {"id":1, "whn":"2026-11-25","who":"andrew"},
    {"id":2, "whn":"2026-11-27","who":"andrew"},
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
    if len([b for b in booking if b['who']==data['who']]) < maxBookingsPerPerson:
        new_id = len(booking) + 1
        data["id"] = new_id
        booking.append(data)
    else:
        return {"error": "Booking limit reached for this person."}, 400
    return {"booking": booking}

@app.route("/api/booking/<id>", methods=["DELETE"])
def rm_booking(id):
    global booking
    booking = [b for b in booking if str(b["id"]) != id]
    return {"booking": booking}

@app.route("/api/booking", methods=["GET"])
def list_booking():
    return {"booking": booking}

if __name__ == "__main__":
    app.run(debug=True)