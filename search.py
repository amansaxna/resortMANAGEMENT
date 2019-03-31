import json
#get rough_value = location 	;	if location in loc[] <--cities.json <--states.json
# display value_location+ state_id
#find min and max;;
print("hotels_id in the database ")
with open('hotels.json') as data_file1:    
	data1 = json.load(data_file1)

	hotels = data1['hotels']

	for i in hotels:
	
		if i['name'] == 'taj 1':


			for j in i['room']:

				a = j['room_no']







				print(a)
			print("end of rooms")
