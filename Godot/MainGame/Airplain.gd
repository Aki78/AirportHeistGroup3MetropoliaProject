extends Button

onready var cash = 5000

func _ready():
	self_modulate.a = 0.0
	$Cash.text = str(cash)

func set_cash(price):
	$Cash.text = str(price)
