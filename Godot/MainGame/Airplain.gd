extends Sprite

onready var cash = 5000

func _ready():
	modulate.r = 0.5
	scale.x= 1
	scale.y = 1
	$Cash.text = str(cash)

func set_cash(price):
	$Cash.text = str(price)
