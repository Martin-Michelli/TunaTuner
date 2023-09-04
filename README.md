# TunaTuner
In order to expose myself to a variety of skills related to my field of study, I have chosen to embark on the journey of creating a personal project. 
After brainstorming and weighing the skills that I currently possess (microcontroller programming and debugging in C++, breadboard prototyping),
along with those that I wanted to learn (PCB design, soldering, 3D modelling, and more micrcontroller programming but in CircuitPython),
I came up with the idea to create an instrument tuner with macro-pad style sample tone outputs. The device itself will resemble a macro-pad, but will also include a small screen that can be purchased from Adafruit.
As a user plays a note into the microphone, the screen will determine what pitch is being played, and indicate whether the note that the user is playing is sharp or flat.
The microcrontroller being used is the Adafruit KB2040, which is based on the Raspberry Pi RP2040, and programmed in circuitPython.
Notes will be read in as analog inputs, then assigned A-G and ♭, ♯, or ♮ using whichever value is the nearest. The note will be displayed on the screen along with a slider to indicate which direction the user should tune towards.
This functionality alone would be sufficient in making an instrument tuner, but since I'm going through this much effort, I have decided to morph additional functionality into this device.
Next to the microphone and screen will be 9 keys, A-G, a sharp key, and a flat key.
When a key is pressed, the respective pitch (in its natural form) will be played from a speaker, and displayed on the screen.
With a tone being played from the device, one has the option to hear pitches to aid in their tuning process.
The firmware will be tested on a breadboard version of the device, then a PCB version will be designed, and finally, with a functioning PCB prototype, an exterior case will be 3D printed and the project will be complete.
