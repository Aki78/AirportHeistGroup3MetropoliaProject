extends VBoxContainer



# Called when the node enters the scene tree for the first time.
func _ready():
	CameraScript.animate_list(self)




func _on_StartButton_pressed():
	var anima = CameraScript.my_ease_out(self)
	yield(anima, "animation_completed")
	get_tree().change_scene("res://MainGame/GameScreen.tscn")
