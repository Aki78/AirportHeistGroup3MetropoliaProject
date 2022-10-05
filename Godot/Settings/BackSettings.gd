extends Button

func _on_BackSettings_pressed():
	print("Go back to menu")
	get_tree().change_scene("res://Hud/MainMenu.tscn")


func _on_BackSettings_tree_exited():
	Sound.stop_pink()
