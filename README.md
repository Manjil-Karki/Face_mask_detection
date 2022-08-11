# Face_mask_detection
YOLO v3 mask detection

**Introduction**

This is a small project on mask detection using yolo_v3. This project was carried out by scraping the
photos of people wearing mask in the internet and those photos were labeled using labelImg and a yolo_v3
model was trained on google colab.


**About scripts**

✅ delete_files.py to to preprocess the scarped images and delete unlabeled images.
 
✅ Train_YoloV3.py to to load darknet and train on our data and store in google drive.

✅ YOLO_models_operations/batch_test.py to test the working of our model in batch images.

✅ YOLO_models_operations/test_on_video.py to test on current input video stream to the pc.
