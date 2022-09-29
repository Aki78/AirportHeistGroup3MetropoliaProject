extends Node2D

func _ready():
	CameraScript.my_ease_in(self)


func _on_Button_pressed():
	var anima = CameraScript.my_ease_out(self)
	yield(anima, "animation_completed")
