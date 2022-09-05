# iMaze-practice-Arena

This is a repository which contains practice arena for the competition **iMaze** conducted by [Robotics Club, IIT BHU](https://github.com/Robotics-Club-IIT-BHU).

* [Installation](#Installation)
* [Usage](#Usage)

## Installation

As this competition is going to be conducted in webots simulator, you may follow these instructions to install webots and python locally

### Webots Installation

#### Windows

* Download webots setup file(shown below) from the official website - <https://cyberbotics.com/>

  ![win-1](images/win-1.jpg)

* Open the file and choose *Install for me only* option

  ![win-2](images/win-2.jpg)

* And then follow the prompts (*Next*, *Next*, ..., *Install*).

#### Python installation : (If Python is not already installed)

* Open the <https://www.python.org/downloads/>  in your web browser. Navigate to the Downloads tab for Windows. Choose any Python 3.7.x

* Click on the link to download **Windows x86 executable installer** if you are using a 32-bit installer. In case your Windows installation is a 64-bit system, then download **Windows x86-64 executable installer**(shown below).

* Once the installer is downloaded, run the Python installer.

* Make sure you select **"Add Python3.7 to PATH"** option before starting the installation.

* You can now start the installation of Python by clicking on **Install Now**.

#### Linux

* Download .deb file (shown below) from the official website - <https://cyberbotics.com/>

  ![lin-1](images/lin-1.jpg)

* Go to the directory where you have downloaded the file and just double click the file. You can see something like below, just click *install*

  ![lin-2](images/lin-2.jpg)
  
#### Python installation : (Only if python is not installed previously)

* Update the packages list and install the prerequisites:

  ~~~bash
  sudo apt update
  sudo apt install software-properties-common
  ~~~
  
* Add the deadsnakes PPA to your system’s sources list:

  ~~~bash
  sudo add-apt-repository ppa:deadsnakes/ppa
  ~~~

* you can install Python 3.7 by executing:

  ~~~bash
  sudo apt install python3.7
  ~~~

* Verify that the installation was successful by typing:

  ~~~bash
  python3 --version
  ~~~

## Usage

Now that you have downloaded webots in your computer, you may follow these instruction to clone this repository, load the arena, create a custom controller and connect it to robot.

If you don't have git pre installed in your system,then simply download the zip file by clicking the green 'code' button above and then extract it.

### Clone this repository

* Firstly, install git in your computer. You may follow these tutorials - [Windows](https://phoenixnap.com/kb/how-to-install-git-windows) | [Linux](https://www.atlassian.com/git/tutorials/install-git#linux)

* Then open command prompt (*in windows*) or terminal (*in linux*) and clone this repository

  ~~~shell
  git clone https://github.com/Robotics-Club-IIT-BHU/iMaze-practice-Arena.git
  ~~~

### Load the arena

* Open the webots simulator and you are expected to see a window as shown below

  ![web-1](images/web-1.jpg)

* Click on *File* then *Open World* as shown below

  ![web-2](images/web-2.jpg)

* Go to the folder where you have cloned this repository and select `PraticeArena.wbt` file (inside the folder named worlds) as shown below

  ![web-3](images/web-3.jpg)
  
### Making a Custom Controller

* Once you have opened the World, click on Wizards -> New Robot Controller

  ![one](images/Custom-Controller-I.png)

* Click on Next

  ![two](images/Custom-Controller-II.png)

* Select **Python** and then click Next

  ![three](images/Custom-Controller-III.png)

* Provide a Name for your Controller

  ![four](images/Custom-Controller-IV.png)

* Click on Finish

  ![five](images/Custom-Controller-V.png)

### Connecting your Controller to the Robot

* On the left side of the screen navigate to E-puck -> controller "PS2_controller" and then click on Select

  ![six](images/Connect-to-Robot-I.png)

* From the available options choose your controller and then click OK

  ![seven](images/Connect-to-Robot-II.png)
  
### Helper Functions in Webots

*Loading the device* - You can load the necessary devices, by using these functions.

~~~python
left_motor = robot.getDevice('left wheel motor')
right_motor = robot.getDevice('right wheel motor')
ir_sensor = robot.getDevice('ps0')
camera = robot.getDevice('camera')
~~~

*Initializing the motors* - Each motor's position is set to infinity, as if it set to a real number then the motors will stop after they have rotated by the number of radians specified.
Initially, the velocity is set to 0, to ensure the robot is at a stop and not moving.

~~~python
left_motor.setPosition(float('inf'))
right_motor.setPosition(float('inf'))
left_motor.setVelocity(0.0)
right_motor.setVelocity(0.0)
~~~

*Actuation of the motors* - You'll be using velocity control method, to control the motors of the robot.

~~~python
left_motor.setVelocity(speed)
right_motor.setVelocity(speed)
~~~

*Initializing the sensors and reading values*

~~~python
ir_sensor.enable(timestep)
ir_sensor.getValue()
~~~

*Initializing the camera and reading values*

~~~python
camera.enable(timestep)
camera.getImageArray()
~~~

### An Add On - Low GPU memory on Windows

One thing you may have noticed on your first initialization of the Webots software is a warning which says "GPU Memory is less than 2 GB". You can check the number and type of GPUs in your computer using the Task Manager. If, like in the picture shown below, you do have more than one GPU(which is given by GPU 0 and GPU 1), any of which have a memory of greater than 2GB, and you still get the 2 GB warning, you will have to switch the GPU used to run this software, from your Integrated GPU to the Dedicated GPU.

  ![Task Manager](images/task_mgr.jpg)

* Copy the location of the place where *webotsw.exe* is installed(You can find this by right-clicking on the desktop icon, and clicking on "Open File Location")

* Now, open "Graphics Settings" in Windows by using Windows Search. Select your preference as "Classic App", and click on browse. Paste the copied file path in the address bar and select the *webotsw.exe* file.

  ![Graphics Settings](images/graphics_sett.jpg)

* Now the icon will have been added below in the settings. Click on options and select "High Performance" and save.

  ![High Performance](images/high_perform.jpg)

* Restart your computer. The next time you open webots, this warning should not appear and the application will run smoother and faster.
