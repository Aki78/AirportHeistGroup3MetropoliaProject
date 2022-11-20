extends Button


func _on_BackToMainMenu_pressed():
	Sound.stop_panic()
	Sound.stop_victory()
	Sound.stop_game_over_music()
	Sound.play_deep()
	get_tree().change_scene("res://Hud/MainMenu.tscn")
#	$Timer.start()

	







func _on_Timer_timeout():
	get_tree().change_scene("res://Hud/MainMenu.tscn")

