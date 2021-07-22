# Section 3: Your First Rest API (Last 5 Videos of Section 3)

from flask import Flask, jsonify, request

app = Flask(__name__)

families = [ 
    {
    "name": "Nimish Pathak",
    "members": [
        {   
            "name": "Mummy", 
            "salary": 40   
        }
    ] 
} ]

# GET - GET request is used to retreive the data from the backend/ server(Used to send data back only)
# POST - POST request is used to receive/ save the data to the server/ backend.

# GET - /families
@app.route('/families')
def get_families():
    return jsonify({"families": families})


# GET - /family/<string:name>
@app.route("/family/<string:name>")
def get_family(name):             # get the items in the dictionary, "families"
    for family in families:
        if family["name"] == name:
            return jsonify(family)
    return "The given name, dosen't matches the name in the family dictionary, 'Family does not found'"


# GET - /family/<string:name/members>
@app.route("/family/<string:name>/members")
def get_family_members(name):
    for family in families:
        if family["name"] == name:
            return jsonify({'members': family["members"]})
    return jsonify({"message": "Members not found!"})


# POST - /family          data = {name: value}
@app.route('/family', methods = ['Post'])
def create_family():
    input_data = request.get_json()
    new_family = {
        "name": input_data["name"],
        "members": []
    }
    families.append(new_family)
    return jsonify(new_family)


# POST - /family/<string:name>/members
@app.route("/family/<string:name>/members", methods = ["POST"])
def create_family_members(name):
    request_data = request.get_json()
    for family in families:
        if family["name"] == name:
            new_member = {
                "name": request_data["name"],
                "salary": request_data["salary"]
            }
            family["members"].append(new_member)
            return jsonify(new_member)
    return "Name not found, The given name dosen't matches the name in the family dictionary"

if __name__ == "__main__":
    app.run(debug=True)
