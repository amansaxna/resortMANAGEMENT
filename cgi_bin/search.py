import json
#get rough_value = location 	;	if location in loc[] <--cities.json <--states.json
# display value_location+ state_id
#print(y["age";])
def location_value(a):
	print("hotels_id in " + a + ":")
	with open('hotels.json') as data_file1:    
		data1 = json.load(data_file1)
		hotels = data1['hotels']

		for i in hotels:
			x = i['state_id']

			if x == a:
				print("hotel_id = "+x)
a= "Delhi"
location_value(a)
