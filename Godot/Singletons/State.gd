extends Node

const FILE_NAME = "user://score.json"

onready var env = {
	"score": []
}

func _ready():
	load_score()

func save_score(score):
	env.score = [score]
	var file = File.new()
	file.open(FILE_NAME, File.WRITE)
	file.store_string(to_json(env))
	file.close()


func load_score():
	var file = File.new()

	if file.file_exists(FILE_NAME):
		file.open(FILE_NAME, File.READ)
		var best_score=parse_json(file.get_as_text());
		print(best_score)
		return best_score.score[0]
	else:
		save_score(0)

