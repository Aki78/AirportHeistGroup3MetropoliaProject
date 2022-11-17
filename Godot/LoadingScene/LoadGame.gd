extends Sprite


func _ready():
	Sound.stop_hud()



func _on_Timer_timeout():
	get_tree().change_scene("res://MainGame/GameScreen.tscn")
