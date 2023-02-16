# Common-Color-Correction-Techniques
This code is commonly used in the field of "Color Correction" when it comes to adjusting the brightness and contrast of an image, implemented using the OpenCV library in Python.

A Brief Explanation on how it works:
My code conduct a while loop to ensure each of the frame using the read method of the VideoCapture object, and undergoes a brightness adjustment without affecting the color balance.

It first converts the frame from the BGR color spcae to the LAB color space using the 'cv2.cvtColor()' function. This allows the code the make an adjust on the brightness of the frame as I mentioned above.

Next, extract the "L" channel from the LAB color space, "L" stands for lightness here. Then applies a brightness adjustment to this channel using the lift, gamma, and gain parameters. The purpose of these 3 arguments is to shift, scale, and amplify the brightness values respectively. The "np.clip()" function is used to ensure that the pixel values stay within the valid range of 0 to 255.

Afterward, the code will merges the L, A, and B channels back into a single LAB frame, then converts the frame back to its initial color space format, BGR. The resulting corrected frame is displayed alongside the original frame using "cv2.imshow()".

Regarding the while loop, it will continues until all frames in the video have been processed, or until the user pressed the "q" key to quit. Last, the VideoCapture object will get released and destroys any windows that were created.
