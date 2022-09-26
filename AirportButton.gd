extends TextureButton

var mouse_out
var mouse_over

func _ready():
	pass

func _on_TextureButton_mouse_entered():
	rect_scale = Vector2(0.035,0.035)
	pass

func _on_TextureButton_mouse_exited():
	rect_scale = Vector2(0.025,0.025)
	pass
