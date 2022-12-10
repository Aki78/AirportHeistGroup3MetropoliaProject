extends Sprite

onready var init_pos = position

onready var init_color = modulate

onready var speed = 200

func _physics_process(delta):
		position.y += speed*delta

func _on_WhiteColor_timeout():
	modulate = init_color
