extends Sprite

export var AirportScene : PackedScene
onready var first_airport = $Airports/AirportNode5
onready var airports = $Airports
onready var state = {"current_airport":first_airport, "neighbors":[]}

var min_dist = 700

func _ready():
	Sound.play_spy()
	Sound.stop_click()
	print(state["current_airport"].rect_position)
	print(get_closest_airport())
	$Airplain.position = state["current_airport"].rect_position
	connect_airports()
	update_state()

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

func start_tween(my_vec1, my_vec2):
	$Airplain.modulate.a = 1
	var tween = get_node("Tween")
	tween.interpolate_property($Airplain, "position",
			my_vec1, my_vec2, 1,
			Tween.TRANS_LINEAR, Tween.EASE_IN_OUT)
	tween.start()
	yield(tween,"tween_all_completed")
	$Airplain.modulate.a = 0

func erase_far():
	for _i in airports.get_children():
		_i.modulate.a = 0.3
		_i.set_disabled(true)
	for _i in state["neighbors"]:
		_i.modulate.a = 1
		_i.set_disabled(false)

func update_state():
	get_closest_airport()
	erase_far()

	$Airplain.position = state["current_airport"].rect_position
	
func _on_AnimateMe_pressed():
	start_tween(Vector2(0,0), Vector2(1000,1000))

func _on_Europe_tree_exiting():
	Sound.stop_spy()
	
func on_airport_pressed(airport):
	print("yes")
	state["current_airport"] = airport
	update_state()
