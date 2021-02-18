def ratio(pic):
	prop = pic.base_width // pic.base_height
	ratio_w = pic.base_width / pic.width
	ratio_h = pic.base_height / pic.height
	width = (pic.width // ratio_h) 
	height = (pic.height // ratio_w)
	return width, height