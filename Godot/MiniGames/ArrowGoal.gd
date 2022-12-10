extends Sprite

onready var init_color = modulate

func _on_WhiteColor_timeout():
	modulate = init_color
