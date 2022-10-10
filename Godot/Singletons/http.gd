extends Node
onready var http_request_init = HTTPRequest.new()
onready var http_request_check = HTTPRequest.new()
onready var current_airport = 1
onready var closest_list = [1,2,3]

onready var game_state = {}

func _ready():
	add_child(http_request_init)
	add_child(http_request_check)
	http_request_init.connect("request_completed", self, "_on_request_completed")
	http_request_init.request("http://127.0.0.1:5000/get_init")
	var user_name = to_json({"name": "Godette"})
	yield(http_request_init, "request_completed")
	var error = http_request_init.request("http://127.0.0.1:5000/send_user_name", [], true, HTTPClient.METHOD_POST, to_json(game_state))
	print("AAAAA")
	yield(http_request_init, "request_completed")
	http_request_check.request("http://127.0.0.1:5000/check_init")
	print("BBBBB")
func _on_request_completed(result, response_code, headers, body):
	var json = JSON.parse(body.get_string_from_utf8()).result
	json["player"][0] = "AK37"
	game_state = json
	print("game state is", json)



func send_move(i):
	pass
