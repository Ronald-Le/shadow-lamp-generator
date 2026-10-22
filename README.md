# shadow-lamp-generator
Generates a 3D model of a shadow lamp from an image of the shadow it is meant to project. Works best with a silhouette image.

# How to use
Replace the file locations in lines 7, 120 and 124 with your input and 2 output files respectively.
It would be best if your input image was passed through a silhouette generator first but the program will attempt to do this anyway.
Then simply run the file and you will see 3 plots. 

<img width="820" height="820" alt="image" src="https://github.com/user-attachments/assets/b0cc1a87-3317-40e6-9b38-aeee76ba2520" />
The first plot is a 2d plot of the outline of the silhouette and a red circle that represents the location of the lamp relative to the shadow. You may need to manually adjust the centering in line 14 if the image is no symmetrical.

<img width="742" height="592" alt="image" src="https://github.com/user-attachments/assets/62c8d0bc-ca0d-4345-b299-a02e30907dc4" />
The second plot is a 3d plot of what the final lamp would look like.

<img width="1900" height="124" alt="image" src="https://github.com/user-attachments/assets/a444630d-7f25-4017-b446-a8e78881bffe" />
The last plot is a 2d plot which is the previous plot but "unfolded" on to a 2d plane. The idea is that this 2d plot could be saved as a dxf using third party tools and then, embossed around a cylinder in a 3d modeling software to then be 3d printed.
