extends Node

var ws = []
var bs = []

var random_width = 2.0

func _ready():
	randomize()

func zeros_mat(nX, nY):
	var mat = []
	for x in nX:
		mat.append([])
		for _y in nY:
			mat[x].append(0)
	return mat

func ones_mat(nY, nX):
	var mat = []
	for x in nX:
		mat.append([])
		for _y in nY:
			mat[x].append(1)
	return mat


func rand_mat(nY, nX):
	var mat = []
	for x in nX:
		mat.append([])
		for _y in nY:
			mat[x].append(rand_range(-random_width,random_width))
	return mat

func one_mat(nY, nX):
	var mat = []
	for x in nX:
		mat.append([])
		for _y in nY:
			mat[x].append(1)
	return mat

func zeros_vec(nX):
	var vec = []
	for _x in nX:
		vec.append(0)
	return vec

func ones_vec(nX):
	var vec = []
	for _x in nX:
		vec.append(1)
	return vec

func rand_vec(nX):
	var vec = []
	for _x in nX:
		vec.append(rand_range(-random_width,random_width))
	return vec

func add_biases(vec, biases):
	var b_vec = []
	for i in biases.size():
		b_vec.append(vec[i] + biases[i])
	return b_vec

func init_weights(in_size, out_size, n_node, n_layer):
	ws.append(rand_mat(in_size, n_node))
	if n_layer > 1:
		for i in n_layer - 1:
			ws.append(rand_mat(n_node,n_node))
	ws.append(rand_mat(n_node, out_size))

func init_biases(out_size, n_node, n_layer):
	bs.append(rand_vec(n_node))
	if n_layer > 1:
		for i in n_layer - 1: # Do not include the last layer
			bs.append(rand_vec(n_node))
	bs.append(rand_vec(out_size))


func init_weights_ones(in_size, out_size, n_node, n_layer):
	ws.append(one_mat(in_size, n_node))
	if n_layer > 1:
		for i in n_layer:
			ws.append(one_mat(n_node,n_node))
	ws.append(one_mat(n_node, out_size))

func init_biases_ones(out_size,n_node, n_layer):
	bs.append(ones_vec(n_node))
	if n_layer > 1:
		for i in n_layer - 1:
			bs.append(ones_vec(n_node))
	bs.append(ones_vec(out_size))

func multiply_vec(vec, mat):
	var new_vec = zeros_vec(mat.size())
	for i in new_vec.size():
		for j in mat[0].size(): # !!![0]?
			new_vec[i] = new_vec[i] + vec[j] * mat[i][j]
	return new_vec

func act_tanh(vec):
	var act_vec = []
	for i in vec.size():
		act_vec.append(tanh(vec[i]))
	return act_vec

func act_relu(vec):
	var act_vec = []
	for i in vec.size():
		act_vec.append(relu(vec[i]))
	return act_vec

func feed_forward_lin(input):
	var new_vec = act_relu(add_biases(multiply_vec(input, ws[0]), bs[0]))
	if ws.size() > 1:
		for i in ws.size()-2:
			new_vec = act_relu(add_biases(multiply_vec(new_vec, ws[i+1]), bs[i+1]))
	# output layer linear		
	new_vec = multiply_vec(new_vec, ws[-1])
	return new_vec


func feed_forward_lin_softmax(input):
	var new_vec = act_relu(add_biases(multiply_vec(input, ws[0]), bs[0]))
	if ws.size() > 1:
		for i in ws.size()-2:
			new_vec = act_relu(add_biases(multiply_vec(new_vec, ws[i+1]), bs[i+1]))
	# output layer linear	no biases
	new_vec = multiply_vec(new_vec, ws[-1])
	#print("lin: ", new_vec)
	new_vec = softmax(new_vec)
	return new_vec


func feed_forward_relu_softmax(input):
	var new_vec = act_relu(add_biases(multiply_vec(input, ws[0]), bs[0]))
	if ws.size() > 1:
		for i in ws.size()-2:
			new_vec = act_relu(add_biases(multiply_vec(new_vec, ws[i+1]), bs[i+1]))
	# output layer linear		
	new_vec = act_relu(add_biases(multiply_vec(new_vec, ws[-1]), bs[-1]))
	new_vec = softmax(new_vec)
	return new_vec

# nn with an extra softmax layer
func feed_forward_tanh_softmax(input):
	var new_vec = act_tanh(add_biases(multiply_vec(input, ws[0]), bs[0]))
	if ws.size() > 1:
		for i in ws.size()-2:
			new_vec = act_tanh(add_biases(multiply_vec(new_vec, ws[i+1]), bs[i+1]))
	# output layer softmax, ignoring the last layer of ws[-1] dangling		
	new_vec = act_tanh(add_biases(multiply_vec(new_vec, ws[-1]), bs[-1]))
	#print("tanh: ", new_vec)
	new_vec = softmax(new_vec)
	#print(new_vec)
	return new_vec

func softmax(vec):
	var e_x = vec.duplicate(true)
	var my_max = vec.max()
	for i in vec.size():
		e_x[i] = exp(vec[i] - my_max)
	var my_sum = sum(e_x)
	for i in vec.size():
		e_x[i] = e_x[i]/my_sum

	return e_x 

func sum(vec):
	var sum = 0
	for i in vec.size():
		sum += vec[i]
	return sum

func cdf(vec):
	var total = sum(vec)
	var result = []
	var cumsum = 0
	for w in vec.size():
		cumsum += vec[w]
		result.append(cumsum / total)
	return result

func choice2_idx(prop_vec):
	var cdf_vals = cdf(prop_vec)
	var x = rand_range(0, 1)
	if x < cdf_vals[0]:
		return 0
	else:
		return 1

func relu(x):
	if x > 0:
		return x
	return 0
