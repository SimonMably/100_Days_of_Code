import numpy as np
from numpy.random import default_rng

import matplotlib.pyplot as plt
from scipy import misc  # contains an image of a racoon!
from PIL import Image  # for reading image files

# 1-Dimensional Arrays (Vectors)

my_array = np.array([1.1, 9.2, 8.1, 4.7])
print(my_array)

print(my_array.shape)

# Accessing an element within the array. Similar to how a List is accessed, by accessing the index
print(my_array[2])

# Displays the dimensions of an array with the ndim attribute
print(my_array.ndim)

# 2-Dimensional Arrays (Matrices)

# This array contains 2 rows and 4 columns. NumPy refers to the dimensions as
# axes (plural for axis), so first axis has a length of 2 and the second axis
# has a length of 4.
array_2d = np.array([[1, 2, 3, 9],
                     [5, 6, 7, 8]])
print(f"A 2-dimensional array: \n{array_2d}")

# We can access a particular row or column with the sqaure bracket notation with
# these these as well by specifying the index of the row and column to get the
# specific value
print(f"array_2d has {array_2d.ndim} dimensions")

# Accessing a 2-dimensional arrays shape
print(f"Its shape is {array_2d.shape}")

# Displaying the number of rows and columns of 2-dimensional array
print(f"It has {array_2d.shape[0]} rows and {array_2d.shape[1]} columns")

# Accessing the 3rd value in the 2nd row
print(f"The 3rd value in the 2nd row: {array_2d[1, 2]}")

#  To access an entire row and all its values, we can use the : operator
print(f"Accessing all the values in the first row: {array_2d[0, :]}")

# We can access a particular row or column with the sqaure bracket notation with
# these these as well by specifying the index of the row and column to get the
# specific value
print(f"array_2d has {array_2d.ndim} dimensions")

# Accessing a 2-dimensional arrays shape
print(f"Its shape is {array_2d.shape}")

# Displaying the number of rows and columns of 2-dimensional array
print(f"It has {array_2d.shape[0]} rows and {array_2d.shape[1]} columns")

# Accessing the 3rd value in the 2nd row
print(f"The 3rd value in the 2nd row: {array_2d[1, 2]}")

#  To access an entire row and all its values, we can use the : operator
print(f"Accessing all the values in the first row: {array_2d[0, :]}")

# N-Dimensional Arrays (Tensors)

mystery_array = np.array(
    [[[0, 1, 2, 3],  # 0, 0
      [4, 5, 6, 7]],  # 0, 1

     [[7, 86, 6, 98],  # 1, 0
      [5, 1, 0, 4]],  # 1, 1

     [[5, 36, 32, 48],  # 2, 0
      [97, 0, 27, 18]]]
    )  # 2, 1

#    0   1   2   3
# Note all the square brackets!

print(f"There are {mystery_array.ndim} dimensions.")
print(f"The shape is {mystery_array.shape}")

# Accesses the value of 18, located at the lower right corner of mystery_array
# via its index.
print(mystery_array[2, 1, 3])

# Retrieving the values from the 3rd axis - the dimension at index position 2,
# the vector at index position 1 (the secod line), : = the whole line.
print(mystery_array[2, 1, :])

# Retrieves the first elements from each dimension.
# The colons access the 1st 2 dimensions, while the 0 is the index position of all
# 3 dimensions.
print(mystery_array[:, :, 0])


# Using .arange() to create a vector withe values ranging from 10 - 29
a = np.arange(10, 30)
print(a)

# Using the slicing (:) operator to;
# 1. create an array that contains the last 3 values of a
# 2. create a subset with only the 4th, 5th and 6th values
# 3. Create a subset of a containing all the values except for the first 12
# 4. Create a subset that only contains the even numbers
b = a[-3:]
print(f"1. {b}")

c = a[3:6]
print(f"2. {c}")

d = a[12:]
print(f"3. {d}")

e = a[::2]
print(f"4. {e}")


# Reversing the order of the values in a. 2 methods
print(np.flip(a))
print(a[::-1])

# Printing out the indices of the non-zero elements of an array
f = np.array([6,0,9,0,0,5,0])
no_zeros = np.nonzero(b)
print(no_zeros)

# Using NumPy to generate a 3*3*3 array with random numbers
rng = default_rng()
vals = rng.random((3, 3, 3))
print(vals)
print(vals.shape)

# Using .linspace to create a vector of 9 values, evenly spaced out between 0 & 100
x = np.linspace(0, 100, num=9)
print(x)
print(x.shape)

# Using .linspace to create a vector of 9 values, evenly spaced out between 0 & 100
x = np.linspace(0, 100, num=9)
print(x)
print(x.shape)

# Create a vector of 9 values between -3 to 3 using .linspace() and plot values
# in a line chart with Matplotlib
y = np.linspace(start=-3, stop=3, num=9)
plt.plot(x, y)
plt.show()

# Using NumPy to generate an array with a shape of 128*128*3 and has random values.
# Use Matplotlib's .imgshow() to display the array as an image.
noise = np.random.random((128,128,3))
print(noise.shape)
plt.imshow(noise)

# Broadcasting, Scalars and Matrix Multiplication

# Linear Algebra with Vectors

v1 = np.array([4, 5, 2, 7])
v2 = np.array([2, 1, 3, 3])

# Adding 2 vectors together will add together the elements in the same position
v1 + v2

# Python Lists vs ndarrays
list1 = [4, 5, 2, 7]
list2 = [2, 1, 3, 3]

# Adding 2 lists together will just concatenate the lists.
print(list1 + list2)

# Multiplying 2 vectors together will multiply the corresponding element in
# each vector
v1 * v2

# Multiplying lists will not work at all
# list1 * list2


# Broadcasting and Scalers

# Sometimes, we might want do some sort of operation between an array and a single
# number. In mathematics, this single number is often called a scaler. For example,
# multiplying an entire vector by 2.
# In order to achieve this result, NumPy will make a shape of the smaller array
# (the scaler) compatible with the larger array. The documentation refers to this
# as broadcasting.

array_2d = np.array([[1, 2, 3, 4],
                     [5, 6, 7, 8]])

array_2d + 10
array_2d * 5


# Matrix Multplication with @ and .matmul()

# Multiplying ndarrays by another vector or 2-dimentional array

a1 = np.array([[1, 3],
               [0, 1],
               [6, 2],
               [9, 7]])

b1 = np.array([[4, 1, 3],
               [5, 8, 5]])

print(f'{a1.shape}: a has {a1.shape[0]} rows and {a1.shape[1]} columns.')
print(f'{b1.shape}: b has {b1.shape[0]} rows and {b1.shape[1]} columns.')
print('Dimensions of result: (4x2)*(2x3)=(4x3)')

c1 = np.matmul(a1, b1)
print(f"Matrix c1 has {c1.shape[0]} rows and {c1.shape[1]} columns.")

#The @ operator can be used as a shorthand for np.matmul on ndarrays.
print(a1 @ b1)

# But how did the calculations arrive at 25 for c12 and 28 for c33?


# Manipulating Images as ndarrays

# Image of a racoon, taken from SciPy and displaying image with Matplotlib
img = misc.face()
plt.imshow(img)

print(img)
print(type(img))

# The shape of img
print(img.shape)

# The amount of dimensions
img.ndim

# There are three matrices stacked on top of each other - one for the red
# values, one for the green values and one for the blue values. Each matrix has
# a 768 rows and 1024 columns, which makes sense since 768x1024 is the
# resolution of the image.

# Converting an image to grayscale

# Step 1: Divishion by a scaler
# NumPy will use broadcasting to divide all values in the ndarray by 255
sRGB_array = img / 255

# Step 2: Use matrix multiplication to multiply the 2 ndarrays together
grey_vals = np.array([0.2126, 0.7152, 0.0722])

# Step 3: The values given by the above formula
img_grey = np.matmul(sRGB_array, grey_vals)
# img_grey = sRGB_array @ grey_vals  # Alternative of the above

# Step 4: Show the image with Matplotlib. cmap tells the imshow() funtion that
# it's dealing with a black and white image.
plt.imshow(img_grey, cmap="gray")

# What happens when the cmap argument isn't used
plt.imshow(img_grey)

# Upside down image
upside_down_grey_racoon = np.flip(img_grey)
plt.imshow(upside_down_grey_racoon, cmap="gray")

# Rotated image
print(plt.imshow(np.rot90(img)))

# inverting the colour image
solar_img = 255 - img
print(plt.imshow(solar_img))


# Using my own image
file_name = 'yummy_macarons.jpg'

# Using PIL to open
my_img = Image.open(file_name)

img_array = np.array(my_img)

# The dimensions and shape of image
print(img_array.ndim)
print(img_array.shape)
# image
print(plt.imshow(img_array))
# inverts colour
print(plt.imshow(255-img_array))



















































































