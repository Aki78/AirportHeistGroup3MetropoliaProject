extends Node
onready var http_request = HTTPRequest.new()
onready var current_airport = 1
onready var airport_info = [{"Name":"something0", "Coordinate":[100, 100], "Distance":100,"Price":2000, "CO2": 150},
{"Name":"something1", "Coordinate":[200, 200], "Distance":100,"Price":2000, "CO2": 150},{"Name":"something2", "Coordinate":[300, 300], "Distance":100,"Price":2000, "CO2": 150},{"Name":"something3", "Coordinate":[400, 400], "Distance":100,"Price":2000, "CO2": 150},{"Name":"something4", "Coordinate":[500, 500], "Distance":100,"Price":2000, "CO2": 150}]
onready var closest_list = [1,2,3]

#func _ready():
#	add_child(http_request)
#	http_request.connect("request_completed", self, "_on_request_completed")
##	http_request.request("http://127.0.0.1:5000/airport/00AA")
#	var body = to_json({"name": "Godette"})
#	var error = http_request.request("http://127.0.0.1:5000/send", [], true, HTTPClient.METHOD_POST, body)
#
##func _on_Button_pressed():
##	$HTTPRequest.request("http://127.0.0.1:5000/airport/00AA")
#
#func _on_request_completed(result, response_code, headers, body):
#	var json = JSON.parse(body.get_string_from_utf8())
#	print(json.result["airport_name"])


func send_move(i):
	pass
