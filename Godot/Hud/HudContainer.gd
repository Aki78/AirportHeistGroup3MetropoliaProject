extends VBoxContainer



# Called when the node enters the scene tree for the first time.
func _ready():
	CameraScript.animate_list(self)
	Sound.play_hud()

func _on_StartButton_pressed():
	Sound.play_click()
	var anima = CameraScript.my_ease_out(self)
	yield(anima, "animation_completed")
	get_tree().change_scene("res://MainGame/GameScreen.tscn")


func _on_HudContainer_tree_exiting():
	Sound.stop_hud()



func _on_SettingsButton_pressed():
	var anima = CameraScript.my_ease_out(self)
	yield(anima, "animation_completed")
	get_tree().change_scene("res://Settings/Settings.tscn")


func _on_HudContainer_tree_exited():
	pass
