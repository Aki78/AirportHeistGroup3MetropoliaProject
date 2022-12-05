extends Sprite

func _ready():
	pass 
	
func init(airport):
	position = airport.rect_position

func get_dist(a,b):
	return (a.rect_position-b.rect_position).length()

func move_interpol(state, airports):
	var old_interpol_airport = state["interpol_airport"]
	var rand_num = randi()%len(airports)
	while 1:
		old_interpol_airport = state["interpol_airport"]
		rand_num = randi()%len(airports)


		if (get_dist(old_interpol_airport, airports[rand_num] )) < 700:
			break
	state["interpol_airport"] = airports[rand_num] 
	var tween = get_node("Tween")
	tween.interpolate_property(self, "position",
			old_interpol_airport.rect_position, state["interpol_airport"].rect_position, 1,
			Tween.TRANS_LINEAR, Tween.EASE_IN_OUT)
	tween.start()
	yield(tween,"tween_all_completed")
