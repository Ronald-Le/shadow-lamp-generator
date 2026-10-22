
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import csv
# loads image as array of hex values
img = Image.open(r"C:\Users\lenha\Downloads\output.png").convert("RGB") #insert file path to the image, works best with silhouette images 
pixels = np.array(img)
print(pixels.shape)
# grab size of the image
arShape = np.array(pixels.shape)
r = 40 #radius of lamp
h = 20 #height of the light at the center of the lamp
center = np.array([((arShape[1]/2)-30), (arShape[0]/2)]) #manually adjust the center so the lamp is centered on the silhouette, not the image as a whole


# puts the image into black and white only

pixels = np.where(np.linalg.norm(pixels,axis=2,keepdims=True)>400,[255,255,255],[0,0,0])

# save the location of edge pixels
edgePix = np.empty((0, 2), dtype=int) 

black = np.all(pixels == [0, 0, 0], axis=2)
white = np.all(pixels == [255, 255, 255], axis=2)

edge_mask = (
    black[1:-1, 1:-1] &
    (
        white[2:, 1:-1] |       # below
        white[:-2, 1:-1] |      # above
        white[1:-1, 2:] |       # right
        white[1:-1, :-2]        # left
    )
)

x9, y9 = np.where(edge_mask)

edgePix = np.column_stack((y9, arShape[0] - x9))


edgePix=np.array(edgePix)

# plots the edge pixels and location of the shadow lamp
fig=plt.figure(figsize=(6,6))
left,bottom,width,height=0.1,0.1,0.8,0.8
ax=fig.add_axes((left,bottom,width,height))
ax.scatter(edgePix[:,0],edgePix[:,1], s=1)
ax.set_aspect('equal', adjustable='box')

'''
Imagine a cylindircal shell with the radius of the lamp and lines connecting from
the edgepixels to the light source. Where every those lines intersect with the shell
is considered a "wall cross"

This section calculates wall crosses in 3d space by first finding "circle crosses"
which use the same idea but in 2d space looking onto the xy plane from a bird's eye 
view to see where the lines cross the radius of the lamp. Then the z value of the wall
cross is calculated using proportionality.
'''
wallCross = np.empty((3,))
m = np.array((edgePix[:,1]-center[1])/(edgePix[:,0]-center[0]))
b = np.array(center[1] - m*center[0])
A = m**2 + 1
B = 2 * m * (b - center[1]) - 2 * center[0]
C = center[0]**2 + (b - center[1])**2 - r**2
discriminant = B**2 - 4 * A * C
discriminant = np.maximum(discriminant, 0) 
ccx1 = np.transpose((-B + np.sqrt(discriminant)) / (2 * A))
ccx2 = np.transpose((-B - np.sqrt(discriminant)) / (2 * A))
ccy1 = m * ccx1 + b
ccy2 = m * ccx2 + b
roots1 = np.array([ccx1,ccy1])
roots2 = np.array([ccx2,ccy2])

circleCross = np.transpose(np.where(abs(ccx1-edgePix[:,0])<abs(ccx2-edgePix[:,0]),roots1,roots2))
print(circleCross.shape)



d = np.array(np.sqrt(((edgePix[:,0]-center[0])**2)+(edgePix[:,1]-center[1])**2))
z = np.array((h/d)*(d-r))

wallCross = np.transpose(np.array([circleCross[:,0]-center[0], circleCross[:,1]-center[1], z]))

#plots circle cross onto the same graph as before
#if done correctly it should leave a red circle that represents the radius of the shadow lamp 
ax.scatter(circleCross[:,0],circleCross[:,1], s=1, color = "red")

#3d plot of the wall crosses which visualises the final shape of the lamp
fig2 = plt.figure()
ax2 = plt.axes(projection='3d')
ax2.scatter3D(wallCross[:,0],wallCross[:,1],wallCross[:,2], s=1, alpha=0.3)

# Takes the 3d lamp and "unfolds" it so it is in 2d
# this can then be embossed over a cylinder in 3d modeling software and 3d printed
polar = [np.atan2((circleCross[:,1]-center[1]),(circleCross[:,0]-center[0]))*(r),wallCross[:,2]]
polar = np.transpose(np.array(polar))

nanRow = np.where(np.isnan(polar[:, 0]))[0]
polar = np.delete(polar, nanRow, axis=0)

#plots the unfolded lamp
fig3=plt.figure(figsize=(6,6))
left,bottom,width,height=0.1,0.1,0.8,0.8
ax3=fig3.add_axes((left,bottom,width,height))


ax3.scatter(polar[:,0],polar[:,1], s=1)
ax.set_aspect('equal', adjustable='box')
ax3.set_aspect('equal', adjustable='box')
plt.show()





# save the data for wall crosses and the "unfolded" lamp

with open(r"C:\Users\lenha\Downloads\output.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(wallCross)
    
with open(r"C:\Users\lenha\Downloads\viksil.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(polar) 
    