extends Button

onready var cash = 5000
var success_rate
var prize

func _ready():
	randomize()
	self_modulate.a = 0.0
	$Cash.text = str(cash)
	set_success_rate()

func set_cash(price):
	$Cash.text = str(price)

func hide_success_rate():
	$SuccessRate.hide()
	$Prize.hide()

func show_success_rate():
	$SuccessRate.show()
	$Prize.show()

	

func set_success_rate():
	var heist_sucess = true
	
	success_rate = int(rand_range(0,100))
	prize = 100*int(rand_range(1,10))
	$SuccessRate.text = str(success_rate) + "%"
	$Prize.text = "€" + str(prize)
	
	if success_rate > rand_range(0,100):
		heist_sucess = true
	else:
		heist_sucess = false
		
	return heist_sucess 
	
