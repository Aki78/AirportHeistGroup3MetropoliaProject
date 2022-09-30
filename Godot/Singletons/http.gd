extends Node
onready var http_request = HTTPRequest.new()

func _ready():
	add_child(http_request)
	http_request.connect("request_completed", self, "_on_request_completed")
	http_request.request("http://127.0.0.1:5000/airport/00AA")

#func _on_Button_pressed():
#	$HTTPRequest.request("http://127.0.0.1:5000/airport/00AA")

func _on_request_completed(result, response_code, headers, body):
	var json = JSON.parse(body.get_string_from_utf8())
	print(json.result["airport_name"])
