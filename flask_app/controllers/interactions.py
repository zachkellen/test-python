from flask_app import app
from flask import render_template, redirect, session, request, flash
from flask_app.models.interaction import Interaction
import json

@app.route('/')          
def hello_world():
    return render_template('index.html')

@app.route('/Interactions/', methods=['POST'])
def create_int():
    print(request.form['firstName'])
    if(Interaction.interaction_validator(request.form)):
        import requests
        r = requests.post('https://flowerbay2-developer-edition.na163.force.com/services/apexrest/Interactions/', json={
            'firstName' : request.form['firstName'],
            'lastName' : request.form['lastName'],
            'phoneNumber' : request.form['phoneNumber'],
            'email' : request.form['email'],
            'address' : request.form['address'],
            'city' : request.form['city'],
            'state' : request.form['state'],
            'zipCode' : request.form['zipCode'],
            'productInterest' : request.form['productInterest'],
            'source' : 'Web Form'
        })
        return redirect('/thankyou')
    return redirect('/')

@app.route('/thankyou')
def thanks():
    return render_template('thankyou.html')