extends VBoxContainer
#
func _ready():
	for _i in get_children():
		_i.modulate.a = 0

func appear():
	for _i in get_children():
		_i.modulate.a = 1
		
func dissapear():
	for _i in get_children():
		_i.modulate.a = 0

func add_info(name, coordinate, distance, price, co2):
	$AirportName.text = name
	$Price.text = str(price)
	$Distance.text = str(distance)
	$CO2.text = str(co2)

