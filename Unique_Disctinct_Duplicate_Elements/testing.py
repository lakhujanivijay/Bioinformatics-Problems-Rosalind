import PIL
from PIL import Image
import fnmatch, os 
count=0
final_images, file_list=[], []

for file in os.listdir('.'):
    if fnmatch.fnmatch(file, '*.png'):
        file_list.append(file)

file_list=sorted(file_list)

for j in range(0,len(file_list)-1):
    if file_list[j][:-4] == file_list[j+1][:-11]:
        count+=1
        final_images.append(file_list[j])
        final_images.append(file_list[j+1])
        images = map(Image.open,final_images)
        widths, heights = zip(*(i.size for i in images))
	total_width = widths[0]
	max_height = max(heights)
	new_im=Image.new('RGB', (total_width, max_height),(255, 255, 255))
        x_offset = 0
        y_offset = 0
        for im in images:
            new_im.paste(im, (x_offset,y_offset))
            x_offset += im.size[1]-40
            y_offset += 100

        result= file_list[j][:-4] + '_final.png'
        new_im.save(result)
        final_images=[]
        result=''
        print 'running for ' + str(count)
