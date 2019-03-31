from datetime import date

# import Flask ::: for implementig flask server
from flask import Flask, render_template,request


# create a new web-app whixh is a Flask application while __name__	represents that his is  
#the file that will reresent the web-app		
app = Flask(__name__,static_url_path='/static')

#import .jason files => hotels.json
import json
with open('hotels.json') as data_file1:    
		data1 = json.load(data_file1)
		hotels = data1['hotels']

#GLOBAL-variables => check_in, check_out.


#/ represent the default page llocalhost/
@app.route("/")
#Declarator funtion
def index():
	today = date.today() 
	return render_template("frontpage.html",day=today)


@app.route("/search",methods=["post"])
def search():
	#from form get location search for hotels in hotels.json
	location = request.form.get("location")	
	check_in = request.form.get("check_in")
	check_out = request.form.get("check_out")
	return render_template("search.html", country=location, hotels = hotels)

@app.route("/rooms",methods=["post"])
def rooms():
	#from form get location search for hotels in hotels.json
	hotel_name = request.form.get("id")
	return render_template("room.html", hotel_name=hotel_name, hotels = hotels)

@app.route("/booking",methods=["post"])
def booking():
	room_id = request.form.get("id")
	hotel_id = request.form.get("hotel_id")
	return render_template("booking.html", room_id= room_id, hotel_id=hotel_id ,hotels = hotels)
