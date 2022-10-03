extends Sprite

export var AirportScene : PackedScene

onready var airports = []


func _ready():
	randomize()
	CameraScript.my_ease_in(self)
	for i in range(5):
		var airport = AirportScene.instance()
		airport.rect_position.x =Http.airport_info[i]["Coordinate"][0] # rand_range(-100,100)*i
		airport.rect_position.y =Http.airport_info[i]["Coordinate"][1] #rand_range(-100,100)*i
		var name = Http.airport_info[i]["Name"]
		var distance = Http.airport_info[i]["Distance"]
		var price = Http.airport_info[i]["Price"]
		var co2 = Http.airport_info[i]["CO2"]
		airports.append(airport)
		airport.add_info(name, 0 ,distance, price, co2)
		if i in Http.closest_list:
			airport.modulate.b = 255
		else:
			airport.modulate.r = 255
			airport.modulate.a = 0.3
		airport.init(i)
		add_child(airport)

func _on_Button_pressed():
	var anima = CameraScript.my_ease_out(self)
	yield(anima, "animation_completed")
