# -*- coding: utf-8 -*-
# Diccionario
from flask import Flask, request, render_template, jsonify
import requests
import logging

# "/home"
# "/word/<word>"

app = Flask(__name__)

@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/Receta/<ingrediente>")
def Receta(q):
    params = get_params_for_ingrediente(q)
    return render_template("Receta.html", **params)

@app.route("/api/Receta/<ingrediente>")
def api_Recetas(q):
    params = get_params_for_ingrediente(q)
    return render_template("Receta.html", **params)

def get_params_for_ingrediente(q):
    #"Accept-Encoding: gzip",
    #"Content-Encoding": gzip,
    headers = {
    "app_id" : "1d52e538",
    "app_key":"628ee144ba2f725bd69b2c4544a3f251",
        }

        response = requests.get("https://test-es.edamam.com/search" + "ingrediente", headers=headers)

        #get.encrypted-area HTTP/1.1
        #Host: "https://test-es.edamam.com/search"
        #Accept-Encoding: gzip, deflate

        #HTTP/1.1 200 OK,
        #Date: mon, 26 June 2016 22:38:34 GMT,
        #Server: Apache/1.3.3.7 (Unix)  (Red-Hat/Linux),
        #Last-Modified: Wed, 08 Jan 2003 23:11:55 GMT,
        #Accept-Ranges: bytes,
        #Content-Length: 438,
        #Connection: close,
        #Content-Type: text/html; charset=UTF-8,
        #Content-Encoding: gzip,deflate,
if response.status_code == 200:
            response_dict = response.json()
            results = response_dict["results"][0]
            lexicalEntries = results["lexicalEntries"]
            ingredientes = []
            for le in lexicalEntries:
                entries = le["entries"]
                for entry in entries:
                    senses = entry["senses"]
                    for sense in senses:
                        defs = sense["ingredientes"]
                        for ingredientes in defs:
                            ingredientes.append(ingredientes)
        #definitions = [le["entries"]["senses"][0] for le in lexicalEntries]

else:
        ingredientes = []
        print("ERROR!!")
    #params = {
    #    "ingrediente": ingrediente,
    #    "definitions": definitions
    #}
    #return params

if __name__ == "__main__":
    app.run(debug=True)
