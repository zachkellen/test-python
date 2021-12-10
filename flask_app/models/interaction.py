from flask import flash, request
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


class Interaction():
    def __init__(self,data):
        self.firstName = data['firstName']
        self.lastname = data['lastname']
        self.phoneNumber = data['phoneNumber']
        self.email = data['email']
        self.address = data['address']
        self.city = data['city']
        self.state = data['state']
        self.zipCode = data['zipCode']
        self.productInterest = data['productInterest']
        self.source = data['source']

    @staticmethod
    def interaction_validator(data):
        is_valid = True
        if len(data['firstName']) < 2 or len(data['firstName']) > 50 :
            flash('First name is required and must be between 2 and 50 characters.')
            is_valid = False
        if len(data['lastName']) < 2 or len(data['lastName']) > 50 :
            flash('Last name is required and must be between 2 and 50 characters.')
            is_valid = False
        if len(data['phoneNumber']) < 1 :
            flash('Phone number is required.')
            is_valid = False
        if len(data['phoneNumber']) > 11 :
            flash('Please do not use any symbols with your phone number.')
            is_valid = False
        if not EMAIL_REGEX.match(data['email']): 
            flash("Invalid email address.")
            is_valid = False
        if len(data['email']) < 2 or len(data['email']) > 50 :
            flash('Email is required and must be between 2 and 50 characters.')
            is_valid = False
        if len(data['address']) < 2 or len(data['address']) > 255 :
            flash('Street address is required and must be between 2 and 255 characters.')
            is_valid = False
        if len(data['city']) < 2 or len(data['city']) > 50 :
            flash('City is required and must be between 2 and 50 characters.')
            is_valid = False
        if len(data['state']) != 2 :
            flash('State is required. Please use two letter abbreviation code for state (eg "ND", "MN")')
            is_valid = False
        if len(data['zipCode']) < 2 or len(data['zipCode']) > 50 :
            flash('Zip Code is required and must be between 2 and 50 characters.')
            is_valid = False
        if data['productInterest'] == '0' :
            flash('Please select a Product of Interest.')
            is_valid = False

        
        return is_valid