# Common-Color-Correction-Techniques
This Python code uses the OpenCV library to perform color correction by adjusting the brightness and contrast of an image. The main function of the code is implemented through a while loop that ensures each frame is adjusted for brightness without affecting its color balance.

The code starts by converting the frame from BGR to LAB color space using the 'cv2.cvtColor()' function. This conversion allows the code to adjust the brightness of the frame.

Next, the "L" channel is extracted from the LAB color space. The brightness of this channel is then adjusted using the "lift", "gamma", and "gain" parameters. These three arguments are used to shift, scale, and amplify the brightness values respectively. The "np.clip()" function is used to ensure that pixel values remain within the valid range of 0 to 255.

The corrected "L" channel is then merged with the "A" and "B" channels, and the resulting LAB frame is converted back to the initial color space format, BGR. The resulting corrected frame is then displayed alongside the original frame using "cv2.imshow()".

The while loop will continue until all frames in the video have been processed, or until the user presses the "q" key to quit. Lastly, the VideoCapture object is released, and any created windows are destroyed.

To access the Python code, you can find it in the "Code" file. Simply click on the file to use it. 
