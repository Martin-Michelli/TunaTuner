# TunaTuner
In order to expose myself to a variety of skills related to my field of study, I have chosen to embark on the journey of creating a personal project. 
After brainstorming and weighing the skills that I currently possess (microcontroller programming and debugging in C++, breadboard prototyping),
along with those that I want to learn (PCB design, soldering, 3D modelling, and more micrcontroller programming but in CircuitPython),
I came up with the idea to create an instrument tuner with macro-pad style sample tone outputs. The device itself will resemble a macro-pad, but will also include a small screen.
As a user plays a note into the microphone, the screen will determine what pitch is being played, and indicate whether the note that the user is playing is sharp or flat.
The microcrontroller being used is the Adafruit KB2040, which is based on the Raspberry Pi RP2040.
Notes will be read in as analog inputs, then assigned A-G and ♭, ♯, or ♮ using whichever value is the nearest. The note will be displayed on the screen along with a slider to indicate which direction the user should tune towards.
This functionality alone would be sufficient in making an instrument tuner, but since I'm going through this much effort, I have decided to morph additional functionality into this device.
Next to the microphone and screen will be 9 keys, A-G, a sharp key, and a flat key, these 9 keys should look just like a macro-pad.
When a key is pressed, the respective pitch (in its natural form) will be played from a speaker, and displayed on the screen.
Pressing the same key again will toggle the pitch, pressing flat or sharp will toggle the respective pitch, and pressing a new key while a pitch is being played will cause the device to play the new pitch.
If I can figure it out, I would like to include a rotary encoder to increase or decrease octaves of a certain pitch.
The main purpose of the sample tones is that with a tone being played from the device, one has the option to hear pitches to aid in their tuning process.
Additionally, the challenge of including the optional sample tone functionality makes the project more useful for me (I'm selfish) because it makes the PCB design more complicated.
The firmware will be tested on a breadboard version of the device, then a PCB version will follow, and finally, with a functioning PCB prototype of the Tuna, an exterior case will be 3D printed and the project will be complete.
