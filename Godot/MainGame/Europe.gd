extends Sprite

export var AirportScene : PackedScene
onready var first_airport = $Airports/AirportNode5
onready var airports = $Airports
onready var state = {"current_airport":first_airport, "neighbors":[], "cash":5000, "interpol_airport":$Airports/AirportNode14}

var min_dist = 700

func _ready():
	Sound.play_spy()
	Sound.stop_click()
	print(state["current_airport"].rect_position)
	print(get_closest_airport())
	$Airplain.position = state["current_airport"].rect_position
	connect_airports()
	update_state(state["current_airport"])

func _on_Button_pressed():
	var anima = CameraScript.my_ease_out(self)
	yield(anima, "animation_completed")

func connect_airports():
	for _i in $Airports.get_children():
		print("connecting: ", _i.name)
		_i.connect("pressed",self,"on_airport_pressed", [_i])

func get_closest_airport():
	var current_airport = state["current_airport"]
	var airports = $Airports
	state["neighbors"] = []
	for _i in airports.get_children():
		var dist = get_dist(_i, current_airport)
		if dist < min_dist:
			state["neighbors"].append(_i)
	print(state)

func get_dist(a,b):
	return (a.rect_position-b.rect_position).length()
func get_pos_dist(a,b):
	return (a.position-b.position).length()

func start_tween(airport1, airport2):
	var tween = get_node("Tween")
	tween.interpolate_property($Airplain, "position",
			airport1.rect_position, airport2.rect_position, 1,
			Tween.TRANS_LINEAR, Tween.EASE_IN_OUT)
	tween.start()
	yield(tween,"tween_all_completed")

func erase_far():
	for _i in airports.get_children():
		_i.modulate.a = 0.3
		_i.set_disabled(true)
	for _i in state["neighbors"]:
		_i.modulate.a = 1
		_i.set_disabled(false)
	state["current_airport"].set_disabled(true)
	state["current_airport"].modulate.a=0;

func update_state(my_airport):
	state["current_airport"] = my_airport
	move_interpol()
	$Interpol.position = state["interpol_airport"].rect_position + Vector2(55,35)
	get_closest_airport()
	erase_far()

	$Airplain.position = state["current_airport"].rect_position + Vector2(50,50)

func _on_Europe_tree_exiting():
	Sound.stop_spy()
	
func move_interpol():
	var old_interpol_airport = state["interpol_airport"]
	var rand_num = randi()%len(airports.get_children())
	state["interpol_airport"] = airports.get_children()[rand_num] 
	var tween = get_node("Tween")
	tween.interpolate_property($Interpol, "position",
			old_interpol_airport.rect_position, state["interpol_airport"].rect_position, 1,
			Tween.TRANS_LINEAR, Tween.EASE_IN_OUT)
	tween.start()
	yield(tween,"tween_all_completed")
	if get_pos_dist($Airplain, $Interpol) < 1:
		print("Game over")
	

func on_airport_pressed(new_airport):
	print("yes")
	var old_airport = state["current_airport"]
	update_state(new_airport)
	start_tween(old_airport, new_airport)
	
	
