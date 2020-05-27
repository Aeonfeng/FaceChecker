
####Imports#######
import face_recognition as fr ##import facial recognition module
import os ##import os
import cv2 ##import open cv2
import face_recognition ##import face recognition 
import numpy as np ##import numpy module 
from time import sleep ##import time and sleep
from tkinter import * ##import tkinter for GUI
from PIL import Image, ImageTk ##import pillow for GUI images
from tkinter.ttk import * ##import ttk for progress bar
import time ##import time 
from tkinter import filedialog ##import filedialog to open files


###Functions#####
def capture_Face(event):  ##create a function to capture a image form the web cam
    cam = cv2.VideoCapture(0,cv2.CAP_DSHOW) ##set the webcam to be used to capture a image
    retval, frame = cam.read() ##call the cam funtion to read image
    if retval != True:
        raise ValueError("Can't read frame") ## error handling if not imgage is found
    cv2.imwrite('face.jpg', frame) ## save the captured image as face.jpg
    image = Image.open("face.jpg") ##import the image as ttk image
    photo = ImageTk.PhotoImage(image) ##import image to photo image
    label = Label(image=photo) ## set the image label up
    label.image = photo ## set the image with a refrence
    label.pack(side= LEFT) ##place image capoturned from webcam to the left on the application window
    
def get_encoded_faces(): ##create a function to  encode all the faces in the known directory
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
    bar() ##start the bar loading function
    get_encoded_faces() ##call the above functin to get the encoded faces from the
    def unknown_image_encoded(img): ##create a function to encode unkown faces
        face = fr.load_image_file("employees/" + img) ##encode unknown face as non employee.
        encoding = fr.face_encodings(face)[0]

        return encoding ##return encoded faces in a dict 
        
    def classify_face(im):  ##find the faces in the image and label them
        faces = get_encoded_faces()  #get the encoded faces functiuon from above
        faces_encoded = list(faces.values()) #faces encoded is the values
        known_face_names = list(faces.keys()) #names are the keys

        img = cv2.imread(im, 1)  #read in the img
    
        face_locations = face_recognition.face_locations(img) ##pass img, read by open cv to find loctaion of the faces in the img
        unknown_face_encodings = face_recognition.face_encodings(img, face_locations) ##encode the unkown faces
        face_names = []

        for face_encoding in unknown_face_encodings: ##compare if the faces in the directory are a match for the known faces in 
            matches = face_recognition.compare_faces(faces_encoded, face_encoding)                      ###### the given img
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
                 
        
        # save the resulting image and diplay o the right side of aplication 
        cv2.imwrite("result.jpg", img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            return face_names 
        result = Image.open("result.jpg")
        photo_2 = ImageTk.PhotoImage(result)
        result_label = Label(image=photo_2)
        result_label.image = photo_2 
        result_label.pack(side= RIGHT)
           
    
    print(classify_face("face.jpg")) ##run calassify face function on selected picture. 

def loading_text():
    #progress bar loading label
    load_label = Label(bottomFrame,text="LOADING BAR")
    load_label.pack(side=TOP)

def bar():

    time.sleep(3) 
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

def open_File():
    global my_newPic
    root.filename = filedialog.askopenfilename(initialdir="/faces", title="Select A File",filetypes=(("jpg files","*.jpg"),("png files","*.png"),("all files","*.*")))

    #file_label = Label(root, text=root.filename).pack() ##display file path
    
    my_newPic = ImageTk.PhotoImage(Image.open(root.filename)) ## use photoimage module and open the selected image at filepath
    
    my_newpic_label = Label(image=my_newPic) ##label the image
    my_newPic.image = my_newPic ##keep a ref of the image
    my_newpic_label.pack(side= LEFT) ##add the image to screen

    new_image = cv2.imread(root.filename) ##set filepath for file to be saved
    cv2.imwrite('face.jpg', new_image ) ##save image as new file to be checked


#### Main Program ####
root = Tk() ##set up a window and start the main program
root.geometry('1920x1040') # w and h
#root.attributes("-fullscreen",True) ##optional full screen from load
root.title("Face Checker") ##set title of window


####create Borders -
#Top canvas
my_canvasTop = Canvas(width=1900, height=150, bg = "light blue" , bd=0 ,highlightthickness=0)
my_canvasTop.pack(side=TOP,fill=X)
rndfont = 50 ## font size for title
my_canvasTop.create_text(1000, 75, font=("Purisa", rndfont), text= "Welcome To FaceChecker!!") ##create the text tile (x,y, font, text)


#Left canvas
my_canvasSide = Canvas(width=150, height=1, bg = "light blue", bd=0 ,highlightthickness=0)
my_canvasSide.pack(side=LEFT, fill=Y)

#Right canvas
my_canvasSide = Canvas(width=150, height=1, bg = "light blue", bd=0 ,highlightthickness=0)
my_canvasSide.pack(side=RIGHT, fill=Y)

#Bottom canvas
my_canvasBottom = Canvas(width=150, height=150, bg = "light blue", bd=0 ,highlightthickness=0)
my_canvasBottom.pack(side=BOTTOM, fill=X)

##create a top frame in the window
topFrame = Frame(root) #create a top frame in the window
topFrame.pack() ##place frame in window

##create a bottom frame in the window
bottomFrame = Frame(root) #create a bottom frame
bottomFrame.pack(side = BOTTOM) ##place frame in botom of screen

##logo###
myLogo = ImageTk.PhotoImage(Image.open("D://3rd Year Plymouth Uni//My Project//Super Final Version//logo.png")) ##location of he logo
logoLabel = Label(image=myLogo) ##set up logo attributes
logoLabel.pack(side=LEFT) ##place logo on screen left
logoLabel_2 = Label(image=myLogo) ##set up logo attributes
logoLabel_2.pack(side=RIGHT) ##place logo on screen right 

##scan face button
button_1 = Button(topFrame, text="Scan Face" ) ##create the button, customize button
button_1.bind("<Button-1>", capture_Face) ##button for left click , function 
button_1.pack(side=LEFT,padx=(30, 30),pady=(20,0)) ##place the scan picture button in the window 


##open file button 
button_1 = Button(topFrame, text="Open File", command=open_File)
button_1.bind("<Button-1>") ##button for left click , function 
button_1.pack(side=RIGHT,pady=(20,0))


##check employee button
button_2 = Button(bottomFrame, text="Check Details") 
button_2.bind("<Button-1>", check_Face) 
button_2.pack( side=LEFT,padx=(25, 1000)) ##add x padding for button plcement on the screen
 
##quit button
#button_quit = Button(bottomFrame, text="Exit", command=root.quit ,height = 4, width = 30, bg="red")
button_quit = Button(bottomFrame, text="Exit", command=root.quit) ##set command as quit window
button_quit.pack(side=RIGHT, padx=(0, 25), pady=10)

##Progress bar to indicate laoad time 
loading_text() ## use loading text function 
progress = Progressbar(bottomFrame, orient = HORIZONTAL, length = 400, mode = 'indeterminate')  ##set up progress bar
progress.pack( side=RIGHT ,pady = (0,10) ,padx=100) ##place progress bar in window 

root.mainloop() ##end tkinter window loop 
#### End of Main prgoram
    
    





    




















