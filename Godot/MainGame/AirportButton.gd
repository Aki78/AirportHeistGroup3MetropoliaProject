extends TextureButton

var mouse_out
var mouse_over

onready var bubbleAnimation = $AnimationPlayer

func _ready():
	rect_scale = Vector2(0.05,0.05)
	modulate.g =255
func _on_TextureButton_mouse_entered():
#	bubbleAnimation.play("oscilate")
	rect_scale = Vector2(0.1,0.1)
#	rect_scale = Vector2(bubbleAnimation.osc, bubbleAnimation)

func _on_TextureButton_mouse_exited():
#	bubbleAnimation.stop(true)
	rect_scale = Vector2(0.05,0.05)

