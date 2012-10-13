g = gimp.pdb
images = gimp.image_list() 
my_image = images[0]
layers = my_image.layers
w = g.gimp_image_width(my_image)
h = g.gimp_image_height(my_image)
print "Image Resolution: w=%d,h=%d"%(w,h)

new_layer = g.gimp_layer_new( my_image, w, h, RGBA_IMAGE, "LeopardLayer", 100, NORMAL_MODE)
my_image.add_layer( new_layer )

g.gimp_context_set_pattern("Leopard")
g.gimp_edit_fill(new_layer, PATTERN_FILL)
g.gimp_layer_set_opacity(new_layer, 20)
g.gimp_layer_set_mode(new_layer, SCREEN_MODE)