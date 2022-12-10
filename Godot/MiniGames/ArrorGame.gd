extends Node2D

onready var arrow = $ArrowAlpha
onready var n = 0

export var direction = "left"

func _ready():
	if direction == "left":
		rotate_children(180)
	elif direction == "down":
		rotate_children(90)
	elif direction == "up":
		rotate_children(-90)
		

func rotate_children(deg):
	for _i in get_children():
		if _i.name[0] == "A":
			_i.rotation_degrees = deg

func close():
	var arror2 = arrow.duplicate()
	add_child(arror2)
	arror2.position.x += 100
	
func get_dist():
	return abs(arrow.position.y - $ArrowGoal.position.y)

func _input(e):
	n+=1
	var invar = "ui_" + direction
	if Input.is_action_pressed(invar) and get_dist() < 10:
		print(n,"win")
		$WhiteColor.start()
		$ArrowAlpha.position.y -= 1000
		$ArrowGoal.modulate = Color(255,255,255)





