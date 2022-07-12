
# Face-Detection.ipynb
#https://towardsdatascience.com/face-detection-in-just-5-lines-of-code-5cc6087cb1a9
import PIL.Image
import PIL.ImageDraw
import face_recognition

given_image = face_recognition.load_image_file('images/testing/trump-modi.jpg')
#given_image = face_recognition.load_image_file('kelas ML.jpg')

face_locations = face_recognition.face_locations(given_image)

number_of_faces = len(face_locations)
print("We found {} face(s) in this image.".format(number_of_faces))

We found 2 face(s) in this image.

pil_image = PIL.Image.fromarray(given_image)

for face_location in face_locations:
    top, left, bottom, right = face_location
    print("A face is detected at pixel location Top: {}, Left: {}, Bottom: {}, Right: {}".format(top, left, bottom, right))
    draw = PIL.ImageDraw.Draw(pil_image)
    draw.rectangle([left, top, right, bottom], outline="green", width=10)
    
    

A face is detected at pixel location Top: 56, Left: 275, Bottom: 146, Right: 185
A face is detected at pixel location Top: 116, Left: 504, Bottom: 206, Right: 414

pil_image.show()

