extends Button

onready var cash = 5000
var success_rate

func _ready():
	randomize()
	self_modulate.a = 0.0
	$Cash.text = str(cash)
	set_success_rate()

func set_cash(price):
	$Cash.text = str(price)

func hide_success_rate():
	$SuccessRate.hide()

func show_success_rate():
	$SuccessRate.show()

func set_success_rate():
	var heist_sucess = true
	
	success_rate = rand_range(0,100)
	$SuccessRate.text = str(int(success_rate)) + "%"
	
	if success_rate > rand_range(0,100):
		heist_sucess = true
	else:
		heist_sucess = false
		
	return heist_sucess 
	
