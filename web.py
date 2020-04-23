#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 15:44:10 2020

@author: dincersalihkurnaz
"""
"""
kütüphaneyi yüklüyoruz"""

from flask import Flask,render_template

"""app adında flask fonksüyonu oluşturuyoruz"""
app = Flask(__name__)


"""anasayfayı oluşturuyoruz(elif in webpage i yazısı çıkacak) """
@app.route("/")
def index():
    return render_template("index.html",number = 10)

"""search dekoratörü oluşturuyoruz"""
@app.route("/search")
def search():
    return "Search page"

"""delete dekoratörü oluşturuyoruz"""

@app.route("/delete/item")
def delete():
    return "Delete item"
"""id adı verip alma"""
@app.route("/delete/<string:id>")
def deleteId(id):
    return "Id: " + id



    
if __name__ == "__main__":
    app.run(debug = True)


