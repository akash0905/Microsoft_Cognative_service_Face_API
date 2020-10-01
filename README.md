# Microsoft_Cognitive_Services_Face_API
 This folder contains the codes in python for face API
 
 software Used: Spyder(Python 3.7)
 
 Note:
 1) Replace subscription_Key with your own Subscription_Key provided by Microsoft Cognitive Services Face API.
 2) Replace your url_endpoint with your own url_endpoit provided by Microsoft Cognitive Services Face API. 
 
 Steps to run this project:
 
 Run the code in the following manne(as mentioned below):
 
1) "person_group_create.py": This will be used to create the person group.
2) "persongroup_person_create.py": After running "person_group_create.py" we will create person in the person group.
3) "create_dataset.py": Create a folder "dataSet" (or user-defined) and run this code, it will capture 200 images and this images will be stored in the folder..
                        Enter different user id for different person(Recommended starting with user id:1)
4) "add_faces_to_person.py": Now above stored faces will be added into the person.
5) "persongroup_train.py": After adding the faces into the person, Now we will train the person_group.
6) "person_group_train_status.py": This code will be used to get the status of trained person group.
7) "person_group_get.py": This will provide the details about the person group.
8) "person_group_delete.py" : This is used to delete the person group.
9) "face_detect.py": This code is used to detect face in real time and in return we will get faceID with faceAttributes, faceLandmarks.
10) "face_identify.py": This will identify the person face.
11) "face2face_verify.py": This code is to verify whether two faces are same or not.
12) "face2person_verify.py": This code is use to verify whether the face is belong to same person or not.
13) "face_and_emotion_recognition.py": This code recognize face and emotion in real time.
 
 Extra Codes:
 
1) "creat_facelist.py"
2) "delete_facelist.py"
3) "add_face_in_list.py"
4) "open_image_opencv.py"

 