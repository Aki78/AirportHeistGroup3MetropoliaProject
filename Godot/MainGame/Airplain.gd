extends Button

onready var cash = 5000
var success_rate

func _ready():
	randomize()
	self_modulate.a = 0.0
	$Cash.text = str(cash)
#	set_success_rate()

func set_cash(price):
	$Cash.text = str(price)

func expand():
	$Wave.expand_player()

#func hide_success_rate():
#	$SuccessRate.hide()
#	$Prize.hide()

#func show_success_rate():
#	$SuccessRate.show()
#	$Prize.show()

