import json
from urllib import response
from flask import Flask, render_template
from flask import request

import requests

app = Flask(__name__)

BACKEND_URL = "http://127.0.0.1:5000/data_types"


@app.get("/")
def get_index():
    response = requests.get(BACKEND_URL)
    scan_data = response.json()
    return render_template("main.html", data_types=scan_data)


@app.get("/data_types_table")
def datatypes():
    return render_template('datatypes.html')


@app.get("/about")
def about():
    me = {
        "first_name": "Sebastian",
        "last_name": "Lopez-Wells",
        "hobbies": "Baseball, literature, Programming",
        "bio": "My name is Sebastian Lopez Wells and I am a student in ITT and SDGKU's online courses."
    }
    return render_template('about.html', about_dict=me)


@app.get("/integers")
def get_ints_page():
    url = "%s/%s" % (BACKEND_URL, "integers")
    response = requests.get(url)
    int_data = response.json()
    return render_template("data_type.html", data_type=int_data[0])


@app.get("/floats")
def get_floats_page():
    url = "%s/%s" % (BACKEND_URL, "floats")
    response = requests.get(url)
    float_data = response.json()
    return render_template("data_type.html", data_type=float_data[0])


@app.get("/bools")
def get_bools_page():
    url = "%s/%s" % (BACKEND_URL, "booleans")
    response = requests.get(url)
    bool_data = response.json()
    return render_template("data_type.html", data_type=bool_data[0])


@app.get("/strings")
def get_strings_page():
    url = "%s/%s" % (BACKEND_URL, "strings")
    response = requests.get(url)
    string_data = response.json()
    return render_template("data_type.html", data_type=string_data[0])


@app.get("/lists")
def get_lists_page():
    url = "%s/%s" % (BACKEND_URL, "lists")
    response = requests.get(url)
    list_data = response.json()
    return render_template("data_type.html", data_type=list_data[0])


@app.get("/dictionaries")
def get_dictionaries_page():
    url = "%s/%s" % (BACKEND_URL, "dictionaries")
    response = requests.get(url)
    dictionary_data = response.json()
    return render_template("data_type.html", data_type=dictionary_data[0])


@app.get("/tuples")
def get_tuples_page():
    url = "%s/%s" % (BACKEND_URL, "tuples")
    response = requests.get(url)
    tuples_data = response.json()
    return render_template("data_type.html", data_type=tuples_data[0])


@app.get("/create/data_types")
def get_data_type_form():
    return render_template("new.html")


@app.post("/create/data_types")
def create_data_type():
    form_data = request.form
    new_dt = {
        "name": form_data.get("name"),
        "summary": form_data.get("summary"),
        "description": form_data.get("description")
    }
    response = requests.post(BACKEND_URL, json=new_dt)

    if response.status_code == 204:
        return render_template("new_success.html")
    else:
        return render_template("failed.html")
