extends Node2D

onready var arrow = $ArrowAlpha
onready var n = 0

func _ready():
	pass

func close():
	var arror2 = arrow.duplicate()
	add_child(arror2)
	arror2.position.x += 100
	
func get_dist():
	return abs(arrow.position.y - $ArrowGoal.position.y)

func _input(e):
	n+=1
	if Input.is_action_pressed("ui_right") and get_dist() < 100:
		print(n,"win")
	elif Input.is_action_pressed("ui_right") and get_dist() > 100:
		print(n, "lose")
	if Input.is_action_pressed("ui_left") or Input.is_action_pressed("ui_up") or Input.is_action_pressed("ui_down") :
		print("Yiou lose")

func _physics_process(delta):
	arrow.position.y += 100*delta
