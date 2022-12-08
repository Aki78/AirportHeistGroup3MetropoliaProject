extends RichTextLabel


onready var counter = -20	


func _process(delta):
	counter += 1
	self.set_bbcode("Smuggler: [fade start=" + str(counter) + " length=10]" 
	+ "Interpol is onto you, get to Portugal ASAP." 
	+ "[/fade]")



func _on_SpeakingTime_timeout():
	self.visible = false
