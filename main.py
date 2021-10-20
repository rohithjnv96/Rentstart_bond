import flask
import csv
from flask import Flask

app = Flask(__name__)

@app.route("/apply",methods=["POST"])
def apply():
    in_json = flask.request.json
    # print(in_json)

    list_of_docs=[]
    if(in_json["centerlink_number"] == ""):
        list_of_docs.append("centerlink number")
    if(in_json["current_assets_proof_submitted"] == "no"):
        list_of_docs.append("current_assets_proof")
    if (in_json["citizenship_proof_submitted"]  == "no" ):
        list_of_docs.append("please submit citizenship_proof")
    if (in_json["medicare_card_copy_submitted"]  == "no" ):
        list_of_docs.append("medicare_card_copy")
    if (in_json["income_proof_submitted"]  == "no" ):
        list_of_docs.append("income_proof")
    if(list_of_docs != []):
        print("ERROR: Please submit documents ->" + str(list_of_docs))
        return("Please submit documents -> " + str(list_of_docs))

    with open('list_applicants.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if(row != []):
                if (row[0] == in_json["centerlink_number"]):
                    print("application with same centerlink id found in DB: you can check the status of application")
                    return "application with same centerlink id found in DB: you can check the status of application"
    file.close()

    for key in in_json:
        print(key + ": " + in_json[key])

    fields = []
    for key in in_json:
        fields.append(in_json[key])
    print(fields)
    with open('list_applicants.csv', 'a') as fd:
        writer = csv.writer(fd)
        writer.writerow(fields)
    fd.close()

    fields = []
    fields.append(in_json["centerlink_number"])
    fields.append("Processing")
    with open('application_status.csv', 'a') as fd:
        writer = csv.writer(fd)
        writer.writerow(fields)
    fd.close()

    print("applied successfully")
    return "applied successfully"

@app.route("/status")
def status():
    app_status = ""
    in_json = flask.request.json
    with open('application_status.csv', 'r') as file:
        reader = csv.reader(file)
        for each in reader:
            if (each != []):
                if (each[0] == in_json["centerlink_number"]):
                    app_status = each[1]
                    break
    file.close()
    
    if(app_status != ""):
        print("Status: " + str(app_status))
        return "Status: " + app_status
    else:
        print("application with centerlink number: " + str(in_json["centerlink_number"]) + " not found")
        return "application with centerlink number: " + in_json["centerlink_number"] + " not found"

if __name__ == "__main__":
    app.run()