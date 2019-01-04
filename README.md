# CardinalDraw

This is a mini-language intended to simplify the process of drawing lines and shapes via the usage of one character commands.
The CardinalDraw.py module serves as the main interpreter, while all other modules contain either function handlers or syntax details.
Sample code is contained within the test.txt file.

## Commands

#### _D_

Short for _down_, this command ensures that the "pen" is touching the "paper". Without using this command before any others, there is no guarantee that anything will be drawn on-screen.

#### _U_

Short for _up_, this command ensures that the "pen" is not touching the "paper". This allows the user to move the pen without drawing anything.

#### _N [units]_

Short for _north_, this command moves the "pen" toward the top of your screen by the number of _units_ provided. If the "pen" is down, it will draw this many _units_ north. If it is _up_, this command will move the pen this many _units_ north.

#### _S [units]_

Short for _south_, this command moves the "pen" toward the bottom of your screen by the number of _units_ provided.

#### _E [units]_

Short for _east_, this command moves the "pen" toward the right of your screen by the number of _units_ provided.

#### _W [units]_

Short for _west_, this command moves the "pen" toward the left of your screen by the number of _units_ provided.




