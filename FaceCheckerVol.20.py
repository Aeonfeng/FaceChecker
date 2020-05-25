import face_recognition as fr
import os
import cv2
import face_recognition
import numpy as np
from time import sleep
from tkinter import *
from PIL import Image, ImageTk
from tkinter.ttk import *
import time 
#bartime = TRUE


def capture_Face(event):  ##create a function to capture a image form the web cam
    cam = cv2.VideoCapture(0,cv2.CAP_DSHOW)
    retval, frame = cam.read()
    if retval != True:
        raise ValueError("Can't read frame")
    cv2.imwrite('face.jpg', frame) ## save the captured image as face.jpg
    image = Image.open("face.jpg")
    photo = ImageTk.PhotoImage(image)
    label = Label(image=photo)
    label.image = photo # keep a reference!
    label.pack(side= LEFT)
    #cv2.imshow("Checking Face", frame) ## display the image taken


def get_encoded_faces(): ##create a function to  encode all the faces in the nown directory
    """
    looks through the faces folder and encodes all
    the faces

    :return: dict of (name, image encoded)
    """
    encoded = {}

    for dirpath, dnames, fnames in os.walk("./employees"): ##look at employees folder to encode images of employees 
        for f in fnames:
            if f.endswith(".jpg") or f.endswith(".png"): ##look at jpeg or png files
                face = fr.load_image_file("employees/" + f)
                encoding = fr.face_encodings(face)[0]
                encoded[f.split(".")[0]] = encoding ##take the name of the img

    return encoded  ##return encoded faces in a dict with name and image encoded


def check_Face(event):
    print("checking now ") ##test print
    bar()
    get_encoded_faces()
    def unknown_image_encoded(img): ##create a function to encode unkown faces
        """
        encode a face given the file name
        """
        face = fr.load_image_file("employees/" + img) ##encode unkonw face as unknown.
        encoding = fr.face_encodings(face)[0]

        return encoding ##return encoded faces in a dict with unknown as name
        #unknown_image_encoded(img)
    def classify_face(im):  ##find the faces in the image and label them
        """
        will find all of the faces in a given image and label
        them if it knows what they are

        :param im: str of file path
        :return: list of face names
        """
        faces = get_encoded_faces()  #get the encoded faces functiuon from above
        faces_encoded = list(faces.values()) #faces encoded is the values
        known_face_names = list(faces.keys()) #names are the keys

        img = cv2.imread(im, 1)  #read in the img
        #img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)
        #img = cv2.resize(img, (0, 0), fx=0.9, fy=0.9)
        #img = img[:,:,::-1]
    
        face_locations = face_recognition.face_locations(img) ##pass img, read by open cv to find loctaion of the faces in the img
        unknown_face_encodings = face_recognition.face_encodings(img, face_locations) ##encode the unkown faces

        
        face_names = []
        for face_encoding in unknown_face_encodings: ##compare if the faces in the directory are a match for the known faces in the given img
            matches = face_recognition.compare_faces(faces_encoded, face_encoding)
            name = "Non Employee"

            # use the known face with the smallest distance to the new face
            face_distances = face_recognition.face_distance(faces_encoded, face_encoding)
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                name = known_face_names[best_match_index]

            face_names.append(name) ##append the name to either unknown or the face name

            ## Draw box around faces on the imges and label them with the names
            for (top, right, bottom, left), name in zip(face_locations, face_names):
                # Draw a box around the face
                cv2.rectangle(img, (left-20, top-20), (right+20, bottom+20), (255, 0, 0), 2)

                # Draw a label with a name below the face
                cv2.rectangle(img, (left-20, bottom -15), (right+20, bottom+20), (255, 0, 0), cv2.FILLED)
                font = cv2.FONT_HERSHEY_SIMPLEX
                cv2.putText(img, name, (left -20, bottom + 15), font, 0.7, (255, 255, 255), 2)
                 
        
        # Display the resulting image
        #cv2.imshow('output', img)
        cv2.imwrite("result.jpg", img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            return face_names 
        #cv2.imwrite("test", img)
        result = Image.open("result.jpg")
        photo_2 = ImageTk.PhotoImage(result)
        result_label = Label(image=photo_2)
        result_label.image = photo_2 
        result_label.pack(side= RIGHT)
           
    
    print(classify_face("face.jpg"))

# def bar(): 
    
#     progress['value'] = 20
#     root.update_idletasks() 
#     time.sleep(4)
  
#     progress['value'] = 40
#     root.update_idletasks() 
#     time.sleep(4)
  
#     progress['value'] = 50
#     root.update_idletasks() 
#     time.sleep(4)
  
#     progress['value'] = 60
#     root.update_idletasks() 
#     time.sleep(4)
  
#     progress['value'] = 80
#     root.update_idletasks() 
#     time.sleep(4)
#     progress['value'] = 100

#     progress['value'] = 120
#     root.update_idletasks() 
#     time.sleep(4)
  
#     progress['value'] = 140
#     root.update_idletasks() 
#     time.sleep(4)
  
#     progress['value'] = 150
#     root.update_idletasks() 
#     time.sleep(4)
  
#     progress['value'] = 160
#     root.update_idletasks() 
#     time.sleep(4)
  
#     progress['value'] = 180
#     root.update_idletasks() 
#     time.sleep(4)
#     progress['value'] = 200

def loading_text():
    #progress bar loading label
    load_label = Label(bottomFrame,text="LOADING BAR")
    load_label.pack(side=TOP)

def bar():
    progress['value'] = 0
    root.update_idletasks() 
    time.sleep(0.5) 

    progress['value'] = 10
    root.update_idletasks() 
    time.sleep(0.5) 

    progress['value'] = 20
    root.update_idletasks() 
    time.sleep(0.5) 

    progress['value'] = 30
    root.update_idletasks() 
    time.sleep(0.5) 

    progress['value'] = 40
    root.update_idletasks() 
    time.sleep(0.5) 

    progress['value'] = 50
    root.update_idletasks() 
    time.sleep(0.5) 

    progress['value'] = 60
    root.update_idletasks() 
    time.sleep(0.5) 

    progress['value'] = 70
    root.update_idletasks() 
    time.sleep(0.5) 

    progress['value'] = 80
    root.update_idletasks() 
    time.sleep(0.5)

    progress['value'] = 90
    root.update_idletasks() 
    time.sleep(0.5)  

    progress['value'] = 100
    root.update_idletasks() 
    time.sleep(0.5) 

    progress['value'] = 90
    root.update_idletasks() 
    time.sleep(0.5) 

    progress['value'] = 80
    root.update_idletasks() 
    time.sleep(0.5) 

    progress['value'] = 70
    root.update_idletasks() 
    time.sleep(0.5) 

    progress['value'] = 60
    root.update_idletasks() 
    time.sleep(0.5) 

    progress['value'] = 50
    root.update_idletasks() 
    time.sleep(0.5) 

    progress['value'] = 40
    root.update_idletasks() 
    time.sleep(0.5) 

    progress['value'] = 30
    root.update_idletasks() 
    time.sleep(0.5)

    progress['value'] = 20
    root.update_idletasks() 
    time.sleep(0.5)

    progress['value'] = 10
    root.update_idletasks() 
    time.sleep(0.5)   
   
    progress['value'] = 0
    root.update_idletasks() 
    time.sleep(0.5) 

    progress['value'] = 10
    root.update_idletasks() 
    time.sleep(0.5) 

    progress['value'] = 20
    root.update_idletasks() 
    time.sleep(0.5) 

    progress['value'] = 30
    root.update_idletasks() 
    time.sleep(0.5) 

    progress['value'] = 40
    root.update_idletasks() 
    time.sleep(0.5) 

    progress['value'] = 50
    root.update_idletasks() 
    time.sleep(0.5) 

    progress['value'] = 60
    root.update_idletasks() 
    time.sleep(0.5) 

    progress['value'] = 70
    root.update_idletasks() 
    time.sleep(0.5) 

    progress['value'] = 80
    root.update_idletasks() 
    time.sleep(0.5)

    progress['value'] = 90
    root.update_idletasks() 
    time.sleep(0.5)  

    progress['value'] = 100
    root.update_idletasks() 
    time.sleep(0.5) 

    progress['value'] = 90
    root.update_idletasks() 
    time.sleep(0.5) 

    progress['value'] = 80
    root.update_idletasks() 
    time.sleep(0.5) 

    progress['value'] = 70
    root.update_idletasks() 
    time.sleep(0.5) 

    progress['value'] = 60
    root.update_idletasks() 
    time.sleep(0.5) 

    progress['value'] = 50
    root.update_idletasks() 
    time.sleep(0.5) 

    progress['value'] = 40
    root.update_idletasks() 
    time.sleep(0.5) 

    progress['value'] = 30
    root.update_idletasks() 
    time.sleep(0.5)

    progress['value'] = 20
    root.update_idletasks() 
    time.sleep(0.5)

    progress['value'] = 10
    root.update_idletasks() 
    time.sleep(0.5)   
   
    progress['value'] = 0
    root.update_idletasks() 
    time.sleep(0.5) 




   


root = Tk() ##set up a window   
root.geometry('1920x1040') # w and h
#root.attributes("-fullscreen",True)
root.title("Face Checker")





w = 150
h = 9




####Borders -
#Top
my_canvasTop = Canvas(width=1900, height=150, bg = "light blue" , bd=0 ,highlightthickness=0)
my_canvasTop.pack(side=TOP,fill=X)

#Left
my_canvasSide = Canvas(width=w, height=h, bg = "light blue", bd=0 ,highlightthickness=0)
my_canvasSide.pack(side=LEFT, fill=Y)

#Right
my_canvasSide = Canvas(width=w, height=h, bg = "light blue", bd=0 ,highlightthickness=0)
my_canvasSide.pack(side=RIGHT, fill=Y)

#Bottom
my_canvasBottom = Canvas(width=w, height=150, bg = "light blue", bd=0 ,highlightthickness=0)
my_canvasBottom.pack(side=BOTTOM, fill=X)


# topFrame = Frame(root) #create a top frame in the window
# topFrame.pack() ##place frame in window
bottomFrame = Frame(root) #create a bottom frame
bottomFrame.pack(side = BOTTOM) ##place frame in botom of screen

##logo###
myLogo = ImageTk.PhotoImage(Image.open("D://3rd Year Plymouth Uni//My Project//Test software//NewFaceChecker//logo.png"))
logoLabel = Label(image=myLogo)
logoLabel.pack(side=LEFT)
logoLabel_2 = Label(image=myLogo)
logoLabel_2.pack(side=RIGHT)

##take picture button
#button_1 = Button(root, text="Scan Face",height = 4, width = 30, bg="green" )
button_1 = Button(root, text="Scan Face" )
button_1.bind("<Button-1>", capture_Face) ##button for left click , function 
button_1.pack(side=TOP)
#button_1.Place(side=TOP) 


##check employee button
#button_2 = Button(bottomFrame, text="Check Details",command = bar, height = 4, width = 30, bg="blue" )
button_2 = Button(bottomFrame, text="Check Details")
button_2.bind("<Button-1>", check_Face) ##button for left click , function 
button_2.pack( side=LEFT,padx=(25, 1000))
 
##quit button
#button_quit = Button(bottomFrame, text="Exit", command=root.quit ,height = 4, width = 30, bg="red")
button_quit = Button(bottomFrame, text="Exit", command=root.quit)
button_quit.pack(side=RIGHT, padx=(0, 25), pady=10)

loading_text()

# Progress bar widget 
#progress = Progressbar(bottomFrame, orient = HORIZONTAL, length = 400, mode = 'determinate') 
progress = Progressbar(bottomFrame, orient = HORIZONTAL, length = 400, mode = 'indeterminate') 
progress.pack( side=RIGHT ,pady = (0,10) ,padx=100) 



root.mainloop()
    
    
    






# theLabel = Label(root, text = "this is too easy") ##create label widget
# theLabel.pack()
# topFrame = Frame(root) #create a top frame in the window
# topFrame.pack() ##place frame in window
# bottomFrame = Frame(root) #create a bottom frame
# bottomFrame.pack(side = BOTTOM) ##place frame in bptom of screen

# button1 = Button(topFrame, text="Button 1", fg = "red" ) ## add button   were to place, value/text  , text colour 
# button2 = Button(topFrame, text="Button 2", fg = "blue" ) ## add button   were to place, value/text  , text colour 
# button3 = Button(topFrame, text="Button 3", fg = "green" ) ## add button   were to place, value/text  , text colour 
# button4 = Button(bottomFrame, text="Button 4", fg = "purple" ) ## add button   were to place, value/text  , text colour 

# ##display buttons 
# button1.pack(side=LEFT)
# button2.pack(side=LEFT)
# button3.pack(side=LEFT)
# button4.pack(side=BOTTOM)

# one = Label(root,text="one", bg="red", fg="white")
# one.pack()
# two = Label(root,text="Two", bg="green", fg="black")
# two.pack(side=TOP, fill=X)
# three = Label(root,text="Three", bg="blue", fg="white")
# three.pack(side=LEFT, fill=Y)

# label_1 = Label(root,text="Name")
# label_2 = Label(root,text="Password")
# entry_1 = Entry(root)
# entry_2 = Entry(root)

# label_1.grid(row=0,column=0, sticky=E) ## name of text input box
# label_2.grid(row=1, column=0, sticky=E) ## compass alligment  n = top e = right s = bottom w = left

# entry_1.grid(row=0, column=1) ## text input box
# entry_2.grid(row=1, column=1) ## text input box 

# c = Checkbutton(root, text="Keep Me Logged In")
# c.grid(columnspan = 2)

#######################binding functins to widgits
# def printName():
#     print("chello my name is dom")
# button_1 = Button(root, text="Print my name", command=printName)
# button_1.pack()

# def printName(event):
#     print("chello my name is dom")


# button_1 = Button(root, text="Print my name")
# button_1.bind("<Button-1>", printName) ##button for left click , function 
# button_1.pack()
#########################binding functions to widhets 





    




















