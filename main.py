from tkinter import *                                                       # Importing Tkinter
import tkinter.messagebox                                                   # Importing MessageBox function
from PIL import ImageTk, Image                                              # Importing Image & Pillow for image manipulation



def Spotify():                                                              # Defining Spotify Function
    rootLayout = Tk()
    rootLayout.title("Spotify")                                             # Creating a root Layout
    rootLayout.geometry("{0}x{1}+0+0".format(rootLayout.winfo_screenwidth(), rootLayout.winfo_screenheight()))              # Creating
    rootLayout.overrideredirect(False)                                      # Showing windows borders Initially
    rootLayout.attributes("-fullscreen", True)                              # Setting fullscreen mode
    rootLayout.config(bg="#2f2f2f")                                         # Setting background color
    rootLayout.attributes("-alpha", 0.95)                                   # Setting Transparency
    rootLayout.iconbitmap("images/spotifyLogo.ico")

    controlBox = Frame(rootLayout,                                          # Creating a control box
                       height=50,                                           # Setting height
                       relief="solid",                                      # Setting border style
                       highlightthickness=1,                                # Setting border thickness
                       background="#000000",                                # Setting background color
                       highlightbackground="#2F2F2F")                       # Setting border color
    controlBox.pack(side=TOP, anchor=NE, fill="x")                          # Placing the control box


    #---------- Inserting control box Images ------------#
    closeImage          = Image.open("images/close.png")                    # Opening Close Image
    resizeClose         = closeImage.resize((30, 30))                       # Resizing Original Image
    newClose            = ImageTk.PhotoImage(resizeClose)                   # Assigning Image to Object

    maximizeImage       = Image.open("images/maximize.png")                 # Opening maximize image
    resizeMazimixe      = maximizeImage.resize((30, 30))                    # Resizing Original Image
    newMaximize         = ImageTk.PhotoImage(resizeMazimixe)                # Assigning Image to object

    minimizeImage       = Image.open("images/minimize2.png")                # Opening minimize image
    resizeMinimize      = minimizeImage.resize((30, 30))                    # Resizing Original Image
    newMinimize         = ImageTk.PhotoImage(resizeMinimize)                # Assigning Image to object

    appLogo             = Image.open("images/spotifyLogo.ico")              # Opening Logo Images
    resizeLogo          = appLogo.resize((30, 30))                          # Resizing Original Image
    newLogo             = ImageTk.PhotoImage(resizeLogo)                    # Assigning Image to object

    # ----------- Creating Control Box Button -------- #
    closeButton = Button(controlBox,                                        # Creating close button
                         bg="#000000",                                      # Setting background color
                         width=50,                                          # Seting width
                         height=50,                                         # Seting height
                         image=newClose,                                    # Setting Image
                         border=0,                                          # Removing border
                         command="",                                        # Assigning Image to object
                         cursor="Hand2")                                    # Setting Curso
    closeButton.image = newClose                                            # Assigning Image to object
    closeButton.pack(side=RIGHT)                                            # Placing the close button

    maximizeButton = Button(controlBox,
                            bg="#000000",
                            width=50,
                            height=50,
                            image=newMaximize,
                            border=0,
                            command="",
                            cursor="Hand2")
    maximizeButton.image = newMaximize                                      # Assigning Image to object
    maximizeButton.pack(side=RIGHT)                                         # Placing the maximize button

    minimizeButton = Button(controlBox,
                            bg="#000000",
                            width=50,
                            height=50,
                            image=newMinimize,
                            border=0,
                            command="",
                            cursor="Hand2")
    minimizeButton.image = newMinimize
    minimizeButton.pack(side=RIGHT)                                        # Placing the minimize button

    logoButton = Button(controlBox,
                              bg="#000000",
                              width=50,
                              height=50,
                              image=newLogo,
                              border=0,
                              command="",
                              cursor="hand2")
    logoButton.image = newLogo
    logoButton.pack(side=LEFT)                                                  # Placing the logo button

    imageGrid(rootLayout)                                                       # Calling ImageGrid function
def imageGrid(rootLayout):                                                  # Defining imageGrid function
    imageFrame = Frame(rootLayout,                                          # Creating image frame
                        bg='#2F2F2F')                                        # Setting background colour
    imageFrame.place(relx=0.06, rely=0.18, relwidth=0.9, relheight=0.75)    # Placing image frame to occupy 90

    images = []                                                             # Loading & arranging 12 images
    for i in range(12):                                                     # Looping 12 times
        img = Image.open(f"images/image{i + 1}.png").resize((250, 250))     # Opening images
        images.append(ImageTk.PhotoImage(img))                              # Assigning Image ot object

    for i in range(6):                                                      # Placing images 6 at the top
        (Label(imageFrame, image=images[i],
                bg="#2F2F2F")
            .grid(row=0, column=i, padx=10, pady=10))

    for i in range(6, 12):                                                  # Placing images at the top
        (Label(imageFrame, image=images[i],
                bg="#2F2F2F")
            .grid(row=1, column=i - 6, padx=10, pady=10))

    rootLayout.images = images
    musicControls(rootLayout)

def musicControls(rootLayout):

    controlFrame = Frame(rootLayout, bg="#1c1c1c", height=100)               # Creating control frame
    controlFrame.pack(fill=X, side=BOTTOM)                                   # Placing control frame


    buttonFrame = Frame(controlFrame, bg="#1c1c1c")                          # Placing button frame
    buttonFrame.pack(pady=10, side=TOP)                                     # Placing button frame in control frame

    seekBarWidth = int(rootLayout.winfo_screenwidth() * 0.8)  # Corrected width of seek bar


    # Adding a seekbar (scale) at the bottom, designed to look like a music seek bar
    seekBar = Scale(controlFrame, from_=0, to=100,
                    orient=HORIZONTAL,
                    bg="#1c1c1c",
                    fg="#ffffff",
                    length=seekBarWidth,
                    troughcolor="#444444",
                    sliderlength=15,
                    highlightthickness=0,
                    showvalue=0,
                    bd=0,
                    tickinterval=0, width=8)
    seekBar.pack(side=BOTTOM, pady=10)                                         # Placing seek bar in control frame

    repeatImage = ImageTk.PhotoImage(Image.open("images/repeat.png").resize((25, 25)))       # Opening repeat image
    prevImage   = ImageTk.PhotoImage(Image.open("images/previous.png").resize((25, 25)))         # Opening prev image
    playImage   = ImageTk.PhotoImage(Image.open("images/play.png").resize((25, 25)))             # Opening play image
    stopImage   = ImageTk.PhotoImage(Image.open("images/stop.png").resize((25, 25)))             # Opening stop image
    nextImage   = ImageTk.PhotoImage(Image.open("images/next.png").resize((25, 25)))           # Opening next image

    # creating repeat, previous, play, (with larger size and round shape), next, stop buttons
    (Button(buttonFrame,                                                                         # Creating repeat button
            image=repeatImage,                                                                   # assigning image
            bg="#1c1c1c",                                                                        # setting background color
            fg="#ffffff",                                                                        # setting text color
            border=0)                                                                            # removing border
     .grid(row=0, column=1, padx=20))                                                             # placing the button

    (Button(buttonFrame,
            image=prevImage,
            bg="#1c1c1c",
            border=0)
     .grid(row=0, column=4, padx=20))                                                               # Placing the stop button

    # creating a play button with a larger, round shape and a border
    playButton = Button(buttonFrame,
                        image=playImage,
                        bg="#1c1c1c",
                        borderwidth=3,
                        relief="solid",
                        width=60,
                        height=60,
                        highlightbackground="white",
                        highlightthickness=2,                                                     # Removing highlight
                        activebackground="#1c1c1c",
                        activeforeground="#ffffff")
    playButton.grid(row=0, column=2, padx=20)                                                     # Placing the play button

    (Button(buttonFrame,
            image=nextImage,
            bg="#1c1c1c",
            border=0)
    .grid(row=0, column=3, padx=20))                                                             # Placing the next button

    (Button(buttonFrame,
            image=stopImage,
            bg="#1c1c1c",
            border=0)
    .grid(row=0, column=4, padx=20))                                                             # Placing the stop button

    rootLayout.repeatImage = repeatImage                                                       # Assigning seek bar to object
    rootLayout.stopImage = stopImage
    rootLayout.prevImage = prevImage
    rootLayout.nextImage = nextImage
    rootLayout.playImage = playImage
    welcomeBox()

def welcomeBox():
    welcomeBox    = tkinter.Toplevel()                                      # Creating a welcome box
    welcomeBox.title = "Welcome"                                            # Title for welcome box
    box_width = 500                                                         # Width of box
    box_height = 500                                                        # Height of box
    screen_width = welcomeBox.winfo_screenwidth()                           # Width of screen
    screen_height = welcomeBox.winfo_screenheight()                         # Height of screen
    x = int((screen_width)/2 - (box_width/2))                               # Width of x
    y = int((screen_height)/2 - (box_height/2))                             # Height of y
    welcomeBox.geometry("{}x{}+{}+{}".format(box_width, box_height, x, y))  # Setting geometry
    welcomeBox.config(bg="#000000")                                         # Setting background color
    welcomeBox.overrideredirect(True)                                       # Hiding windows borders
    welcomeBox.resizable(False, False)                                      # Disabling window resize
    welcomeBox.attributes('-alpha', 1.0)                                    # Setting Transparency

    spotifyLogo = Image.open("images/spotifyLogo.ico")
    resizedLogo = spotifyLogo.resize((50, 50))
    logo = ImageTk.PhotoImage(resizedLogo)
    spotifyLabel = Label(welcomeBox,
                         image=logo,
                         bg="#000000")
    spotifyLabel.image = logo
    spotifyLabel.pack(side=LEFT, anchor=N, padx=170, pady=50)

    spotifyLabel2 = Label(welcomeBox,
                          text="Spotify",
                          font=("Arial", 20),
                          bg="#000000",
                          fg="#ffffff")
    spotifyLabel2.place(x=220, y=50)


Spotify()                                                                   # Calling Spotify Function
mainloop()                                                                  # Running mainloop