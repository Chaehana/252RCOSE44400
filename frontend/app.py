from flask import Flask, render_template, request, redirect
import requests

app = Flask(__name__)

# URL of the backend container inside Docker network
BACKEND_URL = "http://backend:5001"


@app.route("/", methods=["GET"])
def index():
    """
    TODO:
    - Send a GET request to BACKEND_URL + "/api/message"
    - Extract the message from the JSON responses
    - Render index.html and pass the message as "current_message"
    """
    try:
        response = requests.get(f"{BACKEND_URL}/api/message")
        data = response.json()
        message = data.get("message", "(no message yet)") #if no message is stored
    except Exception:
        message = "(backend unavailable)"
    pattern = r"(.*) \(updated at (,*)\)"
    match = re.match(pattern, message)
    if match:
        new_message = match.group(1).strip()
        timestamp = match.group(2).strip()
    else:
        new_message = message
        timestamp = None

    return render_template("index.html", current_message=new_message, updated_time = timestamp)


@app.route("/update", methods=["POST"])
def update():
    """
    TODO:
    - Get the value from the form field named "new_message"
    - Send a POST request to BACKEND_URL + "/api/message"
      with JSON body { "message": new_message }
    - Redirect back to "/"
    """
    new_message = request.form.get("new_message", "").strip()

    requests.post(
        f"{BACKEND_URL}/api/message",
        json={"message": new_message}
    )
    return redirect("/")


# v2 TODO:
# - Change page title (in HTML)
# - Parse timestamp from backend message
# - Show "Last updated at: <timestamp>" in the template


if __name__ == "__main__":
    # Do not change the host or port
    app.run(host="0.0.0.0", port=5000)
