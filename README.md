# CardinalDraw

This is a mini-language intended to simplify the process of drawing lines and shapes via the usage of one character commands.

The CardinalDraw.py module serves as the main interpreter, while all other modules contain either function handlers or syntax details used by the interpreter. Sample code is contained within the [_test.txt_](./test.txt) file.

## Commands

#### _D_

Short for _down_, this command ensures that the "pen" is touching the "paper". Without using this command before calling other commands, there is no guarantee that anything will be drawn on-screen.

#### _U_

Short for _up_, this command ensures that the "pen" is not touching the "paper". This allows the user to move the pen without drawing anything on-screen.

#### _N [pixels]_

Short for _north_, this command moves the "pen" toward the top of your screen by the number of _pixels_ provided. If the "pen" is down, it will draw this many _pixels_ north. If it is _up_, this command will move the pen this many _pixels_ north.

#### _S [pixels]_

Short for _south_, this command moves the "pen" toward the bottom of your screen by the number of _pixels_ provided.

#### _E [pixels]_

Short for _east_, this command moves the "pen" toward the right of your screen by the number of _pixels_ provided.

#### _W [pixels]_

Short for _west_, this command moves the "pen" toward the left of your screen by the number of _pixels_ provided.


##### NOTE: brackets indicate a required argument. All arguments are separated from their commands by a single space, with no brackets present.


