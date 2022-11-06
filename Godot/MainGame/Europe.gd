extends Sprite

export var AirportScene : PackedScene

onready var first_airport = $Airports/AirportNode5

onready var airports = $Airports

onready var state = {"current_airport":first_airport, "neighbors":[]}

func _ready():
	Sound.play_spy()
	Sound.stop_click()
	print(state["current_airport"].rect_position)
	print(get_closest_airport())

func _on_Button_pressed():
	var anima = CameraScript.my_ease_out(self)
	yield(anima, "animation_completed")


func get_closest_airport():
	var current_airport = state["current_airport"]
	var airports = $Airports
	state["neighbors"] = []
	for _i in airports.get_children():
		var dist = get_dist(_i, current_airport)
		if dist < 1000:
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
	pass
	

func _physics_process(delta):
	erase_far()
	

func _on_AnimateMe_pressed():
	start_tween(Vector2(0,0), Vector2(1000,1000))

func _on_Europe_tree_exiting():
	Sound.stop_spy()
