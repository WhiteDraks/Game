#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 15:07:26 2020

@author: dincersalihkurnaz
"""

from flask import Flask,render_template,request

"""app adında flask fonksüyonu oluşturuyoruz"""
app = Flask(__name__)


"""anasayfayı oluşturuyoruz(elif in webpage i yazısı çıkacak) """
@app.route("/")
def index():
    """ message = "Bu bir mesajdır."""
    

    return render_template("index.html")

@app.route("/toplam" ,methods = ["GET","POST"])
def toplam():
    if request.method == "POST":
        number1 = request.form.get("number1")
        number2 = request.form.get("number2")
        return render_template("number.html",total = int(number1) + int(number2))
    else:
        return render_template("number.html")
if __name__ == "__main__":
    app.run(debug = True)
