from PIL import Image  
import face_recognition
import cv2

image = face_recognition.load_image_file("profile.png")
face_locations = face_recognition.face_locations(image)
print(face_locations)

left = int(face_locations[0][0])
top = int(face_locations[0][1])
right = int(face_locations[0][2])
bottom = int(face_locations[0][3])

print(left)
print(top)
print(right)
print(bottom)

cropped = image[left:right,bottom:top]


im = Image.fromarray(cropped)
im.save("your_file_111.jpeg")
