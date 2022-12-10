extends Sprite

var current_airport
var airports

func _ready():
	$InterpolTimer.start()
	
func init(init_airport, init_airports):
	position = init_airport.rect_position
	current_airport = init_airport
	airports = init_airports
	$Wave.expand_player()

func get_dist(a,b):
	return (a.rect_position-b.rect_position).length()

func move_interpol():
	var old_interpol_airport = current_airport
	var rand_num = randi()%len(airports)
	while 1:
		old_interpol_airport = current_airport
		rand_num = randi()%len(airports)
		if (get_dist(old_interpol_airport, airports[rand_num] )) < 700:
			break
	current_airport = airports[rand_num] 
	var tween = get_node("Tween")
	tween.interpolate_property(self, "position",
			old_interpol_airport.rect_position, current_airport.rect_position, 1,
			Tween.TRANS_LINEAR, Tween.EASE_IN_OUT)
	tween.start()
	yield(tween,"tween_all_completed")


func _on_InterpolTimer_timeout():
	move_interpol()
