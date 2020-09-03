from flask import Flask
import json
from simple_salesforce import Salesforce

sf = Salesforce(
    username="jrenzel66@protonmail.com",
    password="Hishem1993!",
    security_token="lbvUE196ou7lzwOm8TO6qsDB",
)

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello, World!"


@app.route("/sf")
def hello_sf():
    qu = sf.query(
        "SELECT Id FROM Account WHERE Atlas_Primary_Email__c = 'jrenzel66@protonmail.com'"
    )
    print(qu)
    return "We got em"

if __name__ == "__main__":
    app.run()