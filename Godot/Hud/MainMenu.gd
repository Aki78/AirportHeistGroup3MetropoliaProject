extends ColorRect

func _ready():
	color.b = 0.3
	color.g = 0.3
#	modulate.b = 155
#	color.r = 255


func _on_Timer_timeout():

	color.r = rand_range(0.5,0.8)

