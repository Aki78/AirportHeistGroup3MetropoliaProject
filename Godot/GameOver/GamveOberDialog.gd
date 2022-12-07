extends RichTextLabel

onready var counter = -20	
	
func _process(delta):
	counter += 0.2
	self.set_bbcode("Smuggler: [fade start=" + str(counter) + " length=10]" + "Your team members were caught. You must go back to Vantaa airport to regroup." + "[/fade]")
