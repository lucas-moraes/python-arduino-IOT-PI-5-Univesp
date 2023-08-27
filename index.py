import face_recognition
import cv2
import numpy as np
import serial
from functions import training_manager
from functions import face_colorizer

class Face_recognition():
    def __init__(self):
        
        video_capture = cv2.VideoCapture(0)
        
        #porta arduíno - colocar a porta de referencia
        arduino = serial.Serial('COM3', 9600) 
        
        known_face_encodings = []
        known_face_names = []
        face_locations = []
        face_encodings = []
        face_names = []
        process_this_frame = True
        color = (255, 0, 0)
        
        list_images = training_manager.list_image_files("training")

        for file_name, file_extension in list_images:
            image_path = "training/" + file_name +  file_extension;
            image = face_recognition.load_image_file(image_path)
            face_encoding = face_recognition.face_encodings(image)[0]
            
            known_face_encodings.append(face_encoding)
            known_face_names.append(file_name)
            
        while True:
            ret, frame = video_capture.read()

            if process_this_frame:
                small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

                rgb_small_frame = np.ascontiguousarray(small_frame[:, :, ::-1])
                
                face_locations = face_recognition.face_locations(rgb_small_frame)
                face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

                face_names = []
                for face_encoding in face_encodings:
                    matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
                    name = "Desconhecido"
                    
                    face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
                    best_match_index = np.argmin(face_distances)
                    if matches[best_match_index]:
                        name = known_face_names[best_match_index]
                        
                        #susbstituir pela lógica do arduino
                        arduino.write(b'ligar_ar_condicionado') 

                    face_names.append(name)
                    
            process_this_frame = not process_this_frame
                  
            face_colorizer.face_target(color, frame, face_locations, face_names)

            cv2.imshow('Video', frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        arduino.close()
        video_capture.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    app = Face_recognition()
