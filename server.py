from flask import Flask
app = Flask(__name__)


@app.route("/", methods=["GET"])
def root():
    return "Welcome TO ITIL exam......."

@app.route("/modules", methods=["GET"])
def root1():
    return "FCN, Security Concepts, COSA, NDC, PKI, CF, CA, ITIL&DevOps"
@app.route("/me", methods=["GET"])
def root2():
    return "230344223042 SamadhanD 7007007007"

app.run(host="0.0.0.0", port=4000, debug=True)
