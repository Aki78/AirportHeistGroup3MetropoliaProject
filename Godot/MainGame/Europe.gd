extends Sprite

export var AirportScene : PackedScene

onready var airports = []


func _ready():
	Sound.play_spy()
	Sound.stop_click()
	
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

func start_tween(my_vec1, my_vec2):
	$Airplain.modulate.a = 1
	var tween = get_node("Tween")
	tween.interpolate_property($Airplain, "position",
			my_vec1, my_vec2, 1,
			Tween.TRANS_LINEAR, Tween.EASE_IN_OUT)
	tween.start()
	yield(tween,"tween_all_completed")
	$Airplain.modulate.a = 0


func _on_AnimateMe_pressed():
	start_tween(Vector2(0,0), Vector2(1000,1000))


func _on_Europe_tree_exiting():
	Sound.stop_spy()
