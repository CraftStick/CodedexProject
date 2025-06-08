import imageio.v3 as iio

filenames = ['image2.png', 'image1.png' ] # List of image filenames
images = []
for filename in filenames:
    images.append(iio.imread(filename))  # Read each image and append to the list

    iio.imwrite('team.gif', images, duration= 500, loop=0)  # Create a GIF from the list of images