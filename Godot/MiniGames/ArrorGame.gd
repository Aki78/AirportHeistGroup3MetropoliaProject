extends Node2D

onready var arrow = $ArrowAlpha
onready var n = 0

export var direction = "left"

signal lost()
signal success()

func _ready():

	if direction == "left":
		rotate_children(180)
	elif direction == "down":
		rotate_children(90)
	elif direction == "up":
		rotate_children(-90)

func init(speed):
	randomize()
	$ArrowAlpha.position.y = rand_range(-1300,100)
	$ArrowAlpha.show()
	$ArrowAlpha.speed = speed
func rotate_children(deg):
	for _i in get_children():
		if _i.name[0] == "A":
			_i.rotation_degrees = deg
	
func get_dist():
	return abs(arrow.position.y - $ArrowGoal.position.y)

func _input(e):
	n+=1
	var invar = "ui_" + direction
	if Input.is_action_pressed(invar) and get_dist() < 1000:
		print(n,"win")
		$WhiteColor.start()
		$ArrowAlpha.position.y = 0
		$ArrowGoal.modulate = Color(255,255,255)
		$ArrowAlpha.hide()
		emit_signal("success")
		
		
func _physics_process(delta):
	if $ArrowAlpha.position.y > 1500 and $ArrowAlpha.is_visible():
#		print("lost")
		emit_signal("lost")





