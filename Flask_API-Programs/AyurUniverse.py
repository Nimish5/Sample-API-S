# Create a web page or make a request where you can GET/ retrieve items in a web page and POST/ create an item in the server or on the go.

from flask import Flask, jsonify, request

app = Flask(__name__)

Wellness_centers = [
    {
        "name": "Ananda In The Himalayas",
        "center_id": 40,
        "center_info": [
            {
                "vendor": "Aveg",
                "place": "Himalayas",
                "price": 5000
            }
        ] 
    }
]

# GET - /Wellness_centers (GET - Wellness_centers list)
@app.route("/Wellness_centers")
def wellness_centers():
    return jsonify({"Wellness Centers": Wellness_centers})        # return {"Wellness Centers": Wellness_centers}
# We can also return a dictionary object, without importing jsonify(no need to import jsonify 
# to return/ display a dictionary object)


# GET - /Wellness_centers/Wellness_center (GET - Wellness_center dictionary)
@app.route('/Wellness_center/<string:name>')
def wellness_center(name):
    for wellness_center in Wellness_centers:
        if wellness_center["name"] == name:
            return wellness_center
    return f"The name {name} does not matches the name in the Wellness_centers dictionary!"


@app.route("/Wellness_center/<int:id>")
def wellness_c(id):
    for w_c in Wellness_centers:
        if w_c["center_id"] == id:
            return w_c
    return f"The id {id} dose not matches the id in the Wellness_centers dictionary!"


@app.route('/Wellness_center/<string:name>/center_info')
def Center_details(name):
    for w_c in Wellness_centers:
        if w_c["name"] == name:
            return jsonify({"Center Information": w_c["center_info"]})
    return "Center Information not Found!"


# POST - /Wellness_center   (POST - To create a new wellness center in the list of centers)
@app.route("/Wellness_center", methods = ["POST"])
def create_new_center():
    request_data = request.get_json()
    new_center = {
        "name": request_data["name"], 
        "center_id": request_data["center_id"],
        "center_info": []
    }
    Wellness_centers.append(new_center)
    return new_center


@app.route('/Wellness_center/<string:name>/center_info', methods = ["POST"])
def update_center_info(name):
    input_data = request.get_json()
    for w_c in Wellness_centers:
        if w_c["name"] == name:
            info = {
                "vendor": input_data["vendor"],
                "place": input_data["place"],
                "price": input_data["price"]
            }
            w_c["center_info"].append(info)
            return jsonify(info)
    return f"The name {name} does not found in the Wellness_centers dictionaries!"


if __name__ == "__main__":
    app.run(debug=True)

