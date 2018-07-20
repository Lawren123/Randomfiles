#
# and ask for filters to filter

from filter import *

filename = "reef.jpg"
filename2 = "reef_filter.jpg"

original = load_img(filename)

newImg = lawren3(original)

save_img(newImg,filename2)
show_img(newImg)
