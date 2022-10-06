extends HScrollBar



func _ready():
	value = AudioServer.get_bus_volume_db(AudioServer.get_bus_index("Master"))
	

func _on_HScrollBar_value_changed(value):
	print(value)
	if value == -30:
		AudioServer.set_bus_volume_db(AudioServer.get_bus_index("Master"), -100)
	else:
		AudioServer.set_bus_volume_db(AudioServer.get_bus_index("Master"), value)
