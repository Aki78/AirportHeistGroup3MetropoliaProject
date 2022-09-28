extends TextureButton

var mouse_out
var mouse_over

onready var bubbleAnimation = $AnimationPlayer

func _ready():
	pass

func _on_TextureButton_mouse_entered():
	bubbleAnimation.play("oscilate")
#	rect_scale = Vector2(0.035,0.035)
#	rect_scale = Vector2(bubbleAnimation.osc, bubbleAnimation)

func _on_TextureButton_mouse_exited():
	bubbleAnimation.stop(true)
	rect_scale = Vector2(0.025,0.025)

