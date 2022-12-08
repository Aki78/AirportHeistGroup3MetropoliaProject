extends ColorRect

func _ready():
	color.b = 0.3
	color.g = 0.3

func _on_Timer_timeout():
	color.r = rand_range(0.5,0.8)

func _on_HudBackGround_tree_exiting():
	Sound.stop_hud()
