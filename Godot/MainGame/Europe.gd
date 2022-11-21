extends Sprite

export var AirportScene : PackedScene
onready var first_airport = $Airports/AirportNode5
onready var airports = $Airports
onready var destination = $Airports/AirportNode10
onready var state = {"current_airport":first_airport, "neighbors":[], "cash":5000, "interpol_airport":$Airports/AirportNode14}

var min_dist = 700
onready var is_close = false
var dialog

func _ready():
	Sound.play_spy()
	#Sound.play_panic()
	print(state["current_airport"].rect_position)
	print(get_closest_airport())
	$Player.rect_position = state["current_airport"].rect_position
	connect_airports()
	update_state(state["current_airport"])
	dialog = Dialogic.start('timeline-choose')

	dialog.connect('dialogic_signal',self, 'dialogic_listener')
	$Interpol.position = $Airports/AirportNode14.rect_position



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
	return (a.rect_position-b.position).length()

func start_tween(airport1, airport2):
	var tween = get_node("Tween")
	tween.interpolate_property($Player, "rect_position",
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
	minus_cash(my_airport)
	state["current_airport"] = my_airport
	get_closest_airport()
	erase_far()
	if state["current_airport"] == destination:
		$WonTimer.start()
		Sound.stop_panic()
		Sound.stop_spy()
		Sound.play_victory()
		if State.load_score() < state.cash:
			State.save_score(state.cash)

	$Player.rect_position = state["current_airport"].rect_position + Vector2(0,0)

func _on_Europe_tree_exiting():
	Sound.stop_spy()
	
func move_interpol():
	var old_interpol_airport = state["interpol_airport"]
	var rand_num = randi()%len(airports.get_children())
	while 1:
		old_interpol_airport = state["interpol_airport"]
		rand_num = randi()%len(airports.get_children())


		if (get_dist(old_interpol_airport, airports.get_children()[rand_num] )) < 700:
			break
	state["interpol_airport"] = airports.get_children()[rand_num] 
	var tween = get_node("Tween")
	tween.interpolate_property($Interpol, "position",
			old_interpol_airport.rect_position, state["interpol_airport"].rect_position, 1,
			Tween.TRANS_LINEAR, Tween.EASE_IN_OUT)
	tween.start()
	yield(tween,"tween_all_completed")
#	if get_pos_dist($Player, $Interpol) < 1:
#		print("Game over")
#		Sound.stop_spy()
#		$GameOverTimer.start()
	

func on_airport_pressed(new_airport):
	print("yes")
	var old_airport = state["current_airport"]
	update_state(new_airport)
	update_ui()
	start_tween(old_airport, new_airport)
	if state["cash"] < 0:
		$GameOverTimer.start()
	if get_dist(state["current_airport"], state["interpol_airport"]) < 700 and not is_close:
		Sound.stop_spy()
		Sound.play_panic()
		is_close = true
	if is_close and get_dist(state["current_airport"], state["interpol_airport"]) > 700 :
		Sound.stop_panic()
		Sound.play_spy()
		is_close = false

func _on_GameOverTimer_timeout():
	print("GAAAAMMMEEE OOOVVVEEEERRRR")
	var anima = CameraScript.my_ease_out(self)
	yield(anima, "animation_completed")
	get_tree().change_scene("res://GameOver/GameOverScene.tscn")


func minus_cash(new_airport):
	print("price is: ", new_airport.price)
	state["cash"] -= new_airport.price

func update_ui():
	$Player.set_cash(state["cash"])

func _on_WonTimer_timeout():
	
	print("Won")
	var anima = CameraScript.my_ease_out(self)
	yield(anima, "animation_completed")
	get_tree().change_scene("res://Won/WonScene.tscn")
func dialogic_listener(a):
	match a:
		"yes":
			print("YES!")
			Sound.play_deep()


func _on_Player_pressed():
#	dialog.queue_free()
	dialog = Dialogic.start("timeline-choose")
	add_child(dialog)

func _on_InterpolArea_area_entered(area):
	print("ENTERED")
	print("Game over")
	Sound.stop_spy()
	$InterpolTimer.stop()
	$GameOverTimer.start()


func _on_InterpolMove_timeout():
	move_interpol()
#	$Interpol.position = state["interpol_airport"].rect_position # + Vector2(55,35)
