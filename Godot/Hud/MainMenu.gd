extends ColorRect

func _ready():
	color.b = 0.2
	color.g = 0.2
#	modulate.b = 155
#	color.r = 255


func _on_Timer_timeout():
	print(randi()%255)
	color.r = rand_range(0.5,0.8)
	print(color.r)