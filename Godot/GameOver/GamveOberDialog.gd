extends RichTextLabel

onready var counter = -20	
	
func _process(delta):
	counter += 1
	self.set_bbcode("[fade start=" + str(counter) + " length=10]" + "Your team members were caught. You must go back to Vantaa airport to regroup." + "[/fade]")