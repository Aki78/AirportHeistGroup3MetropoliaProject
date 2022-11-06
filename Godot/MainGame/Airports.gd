extends Node2D



func _ready():
	for _i in get_children():
		randomize()
		_i.set_price(round(rand_range(100,1000)))

