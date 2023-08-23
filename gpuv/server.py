from flask import Flask, send_from_directory, jsonify
from flask_cors import CORS
import gpuv

app = Flask(__name__)
CORS(app)


#   Path for main Svelte page
@app.route("/")
def base():
    return send_from_directory("frontend/dist", "index.html")


# Path for all static assets (compiled CSS/JS, etc.)
@app.route("/<path:path>")
def home(path):
    return send_from_directory("frontend/dist", path)


@app.route("/nvml")
def nvml_endpoint():
    nv = gpuv.Nvml()
    return jsonify(nv.get())


if __name__ == "__main__":
    app.run(debug=False)
