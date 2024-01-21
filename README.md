# Face_Recognition
This is a OpenCV based Face Recognition system.

run image.py to Start!!

To Start:

1. Login as Admin:
     username: admin
     password: admin1234
2. Add user/dataset:
     This will execute in server terminal:
     Enter the name of the user:
     Then it will use a camera module (if running in PC it uses a webcam) to take 20 pictures of the user.
       (It works even with 10 pictures but we prefer 20 for stronger systems)

   // Code for editing no of pictures can be found in recog.py line 24 

3. When complete verify a new user is added by clicking view dataset and a new window with data of your user can be seen.
4. Go to root screen.
5. Press Login!

This will train the dataset to our system and enable the camera module to detect faces. 
When a camera module detects a face, it will recognize it and send a user name. Else returns null and the camera module remains active.




