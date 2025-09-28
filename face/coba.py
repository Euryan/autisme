import cv2
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array

model = load_model('Bismillahya/face/p.h5')

def preprocess_frame(frame):
    frame_resized = cv2.resize(frame, (256, 256))
    img_array = img_to_array(frame_resized)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = img_array / 255.0
    return img_array

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    input_data = preprocess_frame(frame)
    prediction = model.predict(input_data)

    label = 'Normal' if prediction > 0.010 else 'Autisme'

    cv2.putText(frame, f'Result: {label}', (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    cv2.imshow('Autism Detection', frame)

    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()