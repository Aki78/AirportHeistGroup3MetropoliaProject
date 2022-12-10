extends Sprite

onready var init_pos = position

onready var init_color = modulate

func _physics_process(delta):
		position.y += 100*delta

func _on_WhiteColor_timeout():
	modulate = init_color
