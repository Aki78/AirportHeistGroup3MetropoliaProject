extends Button


func _on_BackToMainMenu_pressed():
	get_tree().change_scene("res://Hud/MainMenu.tscn")
	Sound.stop_panic()
