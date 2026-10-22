# shadow-lamp-generator
Generates a 3D model of a shadow lamp from an image of the shadow it is meant to project. Works best with a silhouette image.

# How to use
Replace the file locations in lines 7, 120 and 124 with your input and 2 output files respectively.
It would be best if your input image was passed through a silhouette generator first but the program will attempt to do this anyway.
Then simply run the file and you will see 3 plots. 

<img width="685" height="822" alt="image" src="https://github.com/user-attachments/assets/351e103f-809b-43e9-9b0e-f3da37dbda72" />
<br>The first plot is a 2d plot of the outline of the silhouette and a red circle that represents the location of the lamp relative to the shadow. You may need to manually adjust the centering in line 14 if the image is no symmetrical.

<img width="681" height="595" alt="image" src="https://github.com/user-attachments/assets/d2346daa-1eb8-4bf1-9bd9-0c8640d0d92e" />
<br>The second plot is a 3d plot of what the final lamp would look like.

<img width="1957" height="123" alt="image" src="https://github.com/user-attachments/assets/e81fe7ac-f5d7-482b-950f-5b10ea23979c" />
<br>The last plot is a 2d plot which is the previous plot but "unfolded" on to a 2d plane. The idea is that this 2d plot could be saved as a dxf using third party tools and then, embossed around a cylinder in a 3d modeling software to then be 3d printed.
<img width="865" height="886" alt="image" src="https://github.com/user-attachments/assets/38a748d4-5c05-445b-b948-53667610faec" />
Final result in autodesk fusion
