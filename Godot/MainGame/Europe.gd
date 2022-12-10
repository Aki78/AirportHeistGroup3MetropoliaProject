extends Sprite

export var AirportScene : PackedScene
onready var first_airport = $Airports/AirportNode5
onready var airports = $Airports
onready var destination = $Airports/AirportNode10
onready var state = {"current_airport":first_airport, "neighbors":[], "cash":5000, "interpol_airport":$Airports/AirportNode14}
onready var paris_airport = $Airports/AirportNode14
onready var camera = $Camera2D

var min_dist = 700
var arrow_speed = 500

onready var is_close = false
onready var first_interpol = $Interpols/Interpol
onready var Interpol = preload("res://MainGame/Interpol.tscn")
onready var mouse_down = false

var mouse_position_before

func _ready():
	Sound.play_panic()
	$Player.rect_position = state["current_airport"].rect_position
	connect_airports()
	update_state(state["current_airport"])
	first_interpol.position = $Airports/AirportNode14.rect_position
	first_interpol.get_node("InterpolArea").connect("area_entered",self,"_on_InterpolArea_area_entered")
	first_interpol.init(paris_airport, airports.get_children())
	camera.current = true
	stop_minigame()
#	Sound.play_smuggler_voice()
	
func connect_minigame():
	$MiniGame.connect("heist_success", self, "_on_heist_success")
	for _i in $MiniGame.get_children():
		_i.connect("lost", self, "_on_caught")
func disconnect_minigame():
	for _i in $MiniGame.get_children():
		_i.disconnect("lost", self, "_on_caught")
		
func start_minigame(speed):
	$MiniGame.show()
	$MiniGame.init(speed)


	connect_minigame()


func stop_minigame():
	$MiniGame.hide()
	disconnect_minigame()

	

func init_interpol():
	var new_interpol = Interpol.instance()
	new_interpol.init(paris_airport, airports.get_children())
	$Interpols.add_child(new_interpol)
	new_interpol.get_node("InterpolArea").connect("area_entered",self,"_on_InterpolArea_area_entered")

func _on_Button_pressed():
	var anima = CameraScript.my_ease_out(self)
	yield(anima, "animation_completed")

func connect_airports():
	for _i in $Airports.get_children():
		_i.connect("pressed",self,"on_airport_pressed", [_i])

func get_closest_airport():
	var current_airport = state["current_airport"]
	var airports = $Airports
	state["neighbors"] = []
	for _i in airports.get_children():
		var dist = get_dist(_i, current_airport)
		if dist < min_dist:
			state["neighbors"].append(_i)

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

func on_airport_pressed(new_airport):
	var old_airport = state["current_airport"]
	update_state(new_airport)
	update_ui()
	start_tween(old_airport, new_airport)
	if state["cash"] < 0:
		$GameOverTimer.start()

func _on_GameOverTimer_timeout():
	var anima = CameraScript.my_ease_out(self)
	yield(anima, "animation_completed")
	get_tree().change_scene("res://GameOver/GameOverScene.tscn")

func minus_cash(new_airport):
	state["cash"] -= new_airport.price

func plus_cash(amount, player):
	state["cash"] += amount
	print(amount," ", player.cash, "" ,state["cash"])
	player.set_cash(state["cash"])

func update_ui():
	$Player.set_cash(state["cash"])

func _on_WonTimer_timeout():
	var anima = CameraScript.my_ease_out(self)
	yield(anima, "animation_completed")
	get_tree().change_scene("res://Won/WonScene.tscn")

func _on_Player_pressed():
	start_minigame(arrow_speed)

func _on_InterpolArea_area_entered(area):
	print("AREA", area)
	if ($Player/PlayerArea == area):
		Sound.stop_spy()
		$InterpolTimer.stop()
		$GameOverTimer.start()

func _input(e):
	if Input.is_action_pressed("zoomin") and camera.zoom.x > 0.5:
		camera.zoom *= 0.9
	if Input.is_action_pressed("zoomout") and camera.zoom.x < 2:
		camera.zoom *= 1.1
	if Input.is_action_pressed("mouse_left"):
		mouse_down = true
	else:
		mouse_down = false

func _process(delta):
	var mouse_position_now = get_global_mouse_position()
	if mouse_down:
		camera.offset += 50*delta*(-mouse_position_now + mouse_position_before)
	mouse_position_before = mouse_position_now

func _on_caught():
	print("lost signal")
	stop_minigame()
	init_interpol()
	
func _on_heist_success():
	print("SUCCESSSSSS")
	arrow_speed *= 1.1
	stop_minigame()
	plus_cash(500, $Player)
