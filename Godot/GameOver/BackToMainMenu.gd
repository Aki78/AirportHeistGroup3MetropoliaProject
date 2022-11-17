extends Button


func _on_BackToMainMenu_pressed():
	Sound.stop_panic()
	Sound.stop_victory()
	get_tree().change_scene("res://Hud/MainMenu.tscn")




