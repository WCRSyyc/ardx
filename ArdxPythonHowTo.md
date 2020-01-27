<!-- cSpell:enable -->
# The CircuitPython Experimenter’s Project

* [Objective](#block_objective)
* [Materials](#block_materials)
* [Setup](#block_setup)
* [Doing the LABs](#block_labs)
* [CIRC01](#block_circ01) Blinking LED
* [CIRC02](#block_circ02) 8 LEDs
* [CIRC03](#block_circ03) Transistor & Motor
* [CIRC04](#block_circ04) Servos
* [CIRC05](#block_circ05) Shift Registers
* [CIRC06](#block_circ06) Piezo Speaker
* [CIRC07](#block_circ07) Pushbuttons
* [CIRC08](#block_circ08) Potentiometers
* [CIRC09](#block_circ09) Photo Resistor
* [CIRC10](#block_circ10) Temperature Sensor
* [CIRC11](#block_circ11) Relays
* [CIRC12](#block_circ12) RRB LED

<!--
* [Link](#block_link)
## <a name="block_link">⚓</a> Link
-->

## <a name="block_objective">⚓</a> Objective

To do all of the LABs in the Arduino ARDX experimenter’s kit, but instead of using C++, substitute CircuitPython.

## <a name="block_materials">⚓</a> Materials

* an ARDX kit (except for the Arduino board)
* the [ARDX experiment instructions](https://wcrsyyc.github.io/ardx/)
* a Python capable micro controller board (These programs were tested using the [AdaFruit Grand Central M4](https://www.adafruit.com/product/4064) board.)
* a USB cable compatible with your micro controller board.
* a laptop or desktop workstation.

## <a name="block_setup">⚓</a> Setup

* [The Board](#block_board)
* [The IDE](#block_ide)

### <a name="block_board">⚓</a> The Board

Note: this is just a summary of the board setup procedure, if you need further detail: go to [AdaFruit](https://learn.adafruit.com/welcome-to-circuitpython) and follow their instructions.

* use a web browser to go to the CircuitPython [downloads](https://circuitpython.org/downloads) page, find your board and download the latest stable version of CircuitPython
  * For the `Grand Central` the file was:</br>
    adafruit-circuitpython-grandcentral_m4_express-en_US-4.1.0(1).uf2
  * For the `CircuitPythonExpress` the file was:</br>
    adafruit-circuitpython-circuitplayground_express-en_US-4.1.0(1).uf2
* connect your board to the laptop with the USB cable
* double click the reset button on your micro controller board.
* the board should show up in your Workstation’s file browser as a disk drive. The name/label of the drive should include `BOOT`.

Use your file browser to confirm that you see files something like these on the boards disk drive:

```tx
CURRENT.UF2
INDEX.HTM
INFO_UF2.TXT
```

If the disk label or files that you see look nothing like this: try double clicking the reset button again.

* In your file browser, drag the file (.UF2) that you downloaded from AdaFruit into the disk drive on your micro controller board.
* The board should reboot.

The previous disk drive should go away and a new disk drive show up. Its name/label should be: `CIRCUITPY`

Now use your file browser to confirm that you see files/directories something like this on the boards disk drive:

```tx
.fseventsd
lib
.metadata_never_index
boot_out.txt
```

* Now download the library bundle that matches the version of CircuitPython you just installed on the micro controller. This is a .zip file.

  * The library bundles are [here](https://circuitpython.org/libraries)

The bundle that matches the version of CircuitPython downloaded above is:
`adafruit-circuitpython-bundle-4.x-mpy-20191216.zip`

* There is not room for all of the available library files in the micro controllers onboard disk drive, so if you need one you will have to:
  * extract the library.zip file
  * find the directory that you need
  * copy it (file browser)
  * paste it into the lib folder on your micro controller.

You can defer this step until you get an error saying that a module cannot be found.

The board is now ready.

### <a name="block_ide">⚓</a> The IDE

If you haven't already installed the [MU editor/IDE](https://codewith.mu) on your Laptop/Workstation do that now.
(you can use other editors and other serial terminals but this one is the easiest.)

You will use the MU editor to write your program and save your program in a local file.
When you then want to try your program on the micro controller, save it to the disk drive on the micro controller board with a file name of `code.py`.

When running your Python programs you should open the serial terminal that is built into MU in order to see any error messages and to see any output from print statements in your program.

You can edit the file in the micro controller disk drive directory, but don’t forget to save a copy in your computer’s local drive when you are finished for the day.  Or at least before you copy a different `code.py` file to the micro controller.

## <a name="block_labs">⚓</a> Doing the LABs

Look at each LAB in the [Arduino ARDX experimenters guide](https://wcrsyyc.github.io/ardx/) and setup a similar hardware configuration, except for replacing the Arduino with a Python capable micro controller, and using Python code instead of the Arduino version of C++. You may also have to change the pin names in some of the LABs.

Also note that the ARDX experimenter’s guide assumes a 5 volt Arduino but most of the Python capable micro controllers have a 3.3 volt VCC. The I/O pins on most 3.3 volt micro controllers are not 5 volt tolerant, so be careful that you do not connect them to any signal or power supply higher than 3.3 volts.

Pin names: In Arduino the pins names are different than in MicroPython. In MicroPython the pins have  names like this:

```python
board.D13
board.A1
board.SCK
```

When you want to save a MU file to a different file name, start by double clicking on the tab in the editor. (There is a [MU editor command cheat sheet](https://cdn-learn.adafruit.com/assets/assets/000/067/029/original/Mu_CircuitPython_Mode_Cheat_Sheet_1.pdf) available at AdaFruit that you may want to keep handy.

You can edit `code.py` directly, but don’t forget that after you get your code working as `code.py` on the Micro controller board – you still have to save the new version with it’s own file name to the hard drive on your laptop/workstation.

## <a name="block_circ01">⚓</a> [CIRC01](CIRC01.html) Blinking LED

If your LED is not on pin board.D13 then revise the program appropriately. See the hardware documentation on the AdaFruit web site.

This code also works on the `CircuitPythonExpress`.

[View](code/CIRC01p-code.txt) or [download](code/CIRC01.py) the code

## <a name="block_circ02">⚓</a> [CIRC02](CIRC02.html) 8 LEDs

Choose the correct boardPins list for the micro controller that you have.

[View](code/CIRC02p-code.txt) or [download](code/CIRC02.py) the code

## <a name="block_circ03">⚓</a> [CIRC03](CIRC03.html) Transistor & Motor

Note: the motor goes to 5 volts (or whatever the motor’s voltage is) even though this is a 3.3 volt VCC board. Use a separate power supply for the motor. Remember to connect the ground from the separate power supply to the ground of the micro controller.

If you are using a 3.3 volt micro controller board, you should drop the value of resistor on the base of the transistor from 2.2 K ohm down to a 1.2K ohm resistor (or a 1K ohm resistor or two 560 ohm resistors in series, whatever you have available). This because the output from the pin will only go to a 3.3 volt high instead of approximately 5 volts the way it would on a 5 volt VCC board, and we want to be sure the transistor gets fully turned on (saturated).

[View](code/CIRC03p-code.txt) or [download](code/CIRC03.py) the code

Did you get: ImportError: no module named 'adafruit_motor' on the MU serial terminal?

There is not enough room for all of the library files available on this small board, so you will have copy individual library files as needed.

You will have to copy the file folder adafruit_motor from the library files you extracted in the setup above to the lib folder on your micro controller.

## <a name="block_circ04">⚓</a> [CIRC04](CIRC04.html) Servos

### CIRC04a

The servo should step up and back 5 degrees at a time.

Use a separate power supply for the servo. Remember to connect the ground from the separate power supply to the ground of the micro controller board. The servo’s power supply should be 5 or 6 volts.

[View](code/CIRC04p-code.txt) or [download](code/CIRC04.py) the code

Did you get: ImportError: no module named 'adafruit_motor'?

There is not room for all of the library files available on this small board so you will have copy individual library files as needed.

You will have to copy the file folder adafruit_motor from the library files you extracted in setup above to the lib folder on your micro controller board.

### CIRC04b

[View](code/CIRC04bp-code.txt) or [download](code/CIRC04b.py) the code

Do you see the print messages from the program on the serial terminal that is built into the MU editor?

You may have to tweak your program to adjust the control waveform depending on the exact type of servo used. The servos that I used seem to work best with a Min of 750 mSec and a Max of 2250 mSec. Adjust these values so that your servo moves from 0 degrees to 90 degrees and then to 180 degrees.

### CIRC04c

[View](code/CIRC04cp-code.txt) or [download](code/CIRC04c.py) the code

Experiment with the waveform timing until you find which is best for your servo. Don’t try to drive the servo below 0 degrees or past 180 degrees or you may damage the servo.

If you have an oscilloscope; view the servo control signal to see how it changes to move the servo to each position.

## <a name="block_circ05">⚓</a> [CIRC05](CIRC05.html) Shift Registers

Some boards have special internal hardware and pins for SPI and other protocols. In order to be able to use this special hardware we need to use the pins: board.SCK and board.MOSI for this Lab. If you do not know where they are on your board the print statements in the program may help you find them, or you can check the hardware documentation.

* The Grand Central M4 uses these pins:
  * SCK microcontroller.pin.D52
  * MOSI microcontroller.pin.D51
  * MISO microcontroller.pin.D50
* The CircuitPython Express uses these pins:
  * SCK microcontroller.pin.A1
  * MOSI microcontroller.pin.A3
  * MISO microcontroller.pin.A2

Use 3.3 volts for VCC on the shift register chip so there is no logic mismatch or chance of 5 volts getting to the 3.3 volt micro controller.

### CIRC05a

[View](code/CIRC05p-code.txt) or [download](code/CIRC05.py) the code

Did you get an error: ImportError: no module named 'adafruit_74hc595'? You will have to copy another library into your Micro controller LIB directory.

Go to the place where you extracted the library zip file and look in the lib directory for adafruit_74hc595.mpy.

Use your file browser to copy it and then go to the lib folder on your micro controller and paste it there.

### CIRC05b

[View](code/CIRC05bp-code.txt) or [download](code/CIRC05b.py) the code

### CIRC05c

[View](code/CIRC05cp-code.txt) or [download](code/CIRC05c.py) the code

### CIRC05d

[View](code/CIRC05dp-code.txt) or [download](code/CIRC05d.py) the code

Some loops make the code much cleaner, but it is still doing the same thing.

### CIRC05e

Lets count from 0 to 255 and do parallel writes to the library function. Do the LEDS count up in binary for you?

[View](code/CIRC05ep-code.txt) or [download](code/CIRC05e.py) the code

### CIRC05f

Lets try out the SPI library this time. Still counting from 0 to 255.

[View](code/CIRC05fp-code.txt) or [download](code/CIRC05f.py) the code

### CIRC05g

[View](code/CIRC05gp-code.txt) or [download](code/CIRC05g.py) the code

### CIRC05h

Lets ignore the special SPI hardware built into the CPU and instead use bit bang I/O. Now we do not have to use the pins that are connected to the micro controller’s internal SPI hardware. We can, for example on the Grand Central M4, use the same I/O pins as in the ARDX document.

[View](code/CIRC05hp-code.txt) or [download](code/CIRC05h.py) the code

## <a name="block_circ06">⚓</a> [CIRC06](CIRC06.html) Piezo Speaker

### CIRC06a

Lets play some music. And we’ll see a Python list.

[View](code/CIRC06p-code.txt) or [download](code/CIRC06.py) the code

### CIRC06b

Lets play a tune. Look at how a Python dictionary is used to link the note’s name to it’s frequency.

[View](code/CIRC06bp-code.txt) or [download](code/CIRC06b.py) the code

### CIRC06c

Musicians use 1/4 notes and 1/2 notes so let’s use them too. This should make transcribing music easier.

[View](code/CIRC06cp-code.txt) or [download](code/CIRC06c.py) the code

### CIRC06d

Musicians need rests too. Some subroutines help clean up the code.

[View](code/CIRC06dp-code.txt) or [download](code/CIRCd06.py) the code

## <a name="block_circ07">⚓</a> [CIRC07](CIRC07.html) Pushbuttons

### CIRC07a

Read a push button, use a pull up resistor just like in the ARDX documentation. Note that when the button is pushed the input goes False. Its opposite on the CPX version see below.

[View](code/CIRC07p-code.txt) or [download](code/CIRC07.py) the code

### CIRC07b

Separate turn on and turn off push buttons

[View](code/CIRC07bp-code.txt) or [download](code/CIRC07b.py) the code

### CIRC07c

We can remove the resistors and let the micro controller supply the pull up on the Grand Central M4.

[View](code/CIRC07cp-code.txt) or [download](code/CIRC07c.py) the code

If you are using a `CircuitPythonExpress`: use program `CIRC07cCPX`. This version uses the onboard LED and the onboard push buttons. These push buttons need a pull down and go to true on a button press.

[View](code/CIRC07cCPXp-code.txt) or [download](code/CIRC07cCPX.py) the code

### CIRC07d

We can also add some simple de-bouncing to the push buttons.

[View](code/CIRC07dp-code.txt) or [download](code/CIRC07d.py) the code

## <a name="block_circ08">⚓</a> [CIRC08](CIRC08.html) Potentiometers

### CIRC08a

Read an analogue value from a potentiometer. Don’t forget to try out the plotter built into MU.

The top of the pot should go the micro controller’s VCC: 3.3 volts in this case not 5 volts as the Arduino documents show. We do not want any voltages higher than the micro controller’s VCC to ever be applied to any of the micro controller’s pins.

[View](code/CIRC08p-code.txt) or [download](code/CIRC08.py) the code

### CIRC08b

Light a LED if we get above a threshold.

[View](code/CIRC08bp-code.txt) or [download](code/CIRC08b.py) the code

### CIRC08c

Use a servo to display the Pot setting.

[View](code/CIRC08cp-code.txt) or [download](code/CIRC08c.py) the code

## <a name="block_circ09">⚓</a> [CIRC09](CIRC09.html) Photo Resistor

Read a value from a photo resistor. Light a LED if we get above a threshold.
The top of the photo resistor / resistor voltage divider goes to 3.3 volts so that there is no change of 5 volts getting to the micro controller.

## <a name="block_circ10">⚓</a> [CIRC10](CIRC10.html) Temperature Sensor

Read the temperature and display with a servo.

The top of the temperature sensor should go the micro controller’s VCC: 3.3 volts in this case not 5 volts as the Arduino documents show. We do not want any voltages higher than the micro controller’s VCC to ever be applied to any of the micro controller’s pins. Use a separate power supply for the servo (5 or 6 volts).

[View](code/CIRC10p-code.txt) or [download](code/CIRC10.py) the code

Discuss why the servo jitters.

Hint: it is a low resolution Analog to digital conversion, even though the library pretends that it is a 16 bit conversion (how many bits of resolution are really in the A to D hardware?)

## <a name="block_circ11">⚓</a> [CIRC11](CIRC11.html) Relays

Same code as CIRC01

[View](code/CIRC11p-code.txt) or [download](code/CIRC11.py) the code

## <a name="block_circ12">⚓</a> [CIRC12](CIRC12.html) RRB LED

Note: if you are using a common anode LED on a 3.3 volt board, the LED anode should go to 3.3 volts not 5 volts as shown in the ARDX schematic. We do not want any voltages higher than the micro controller’s VCC to ever be applied to any of the micro controller’s pins.

Control a three colour LED. Look carefully at the dictionary of Lists, do you see how it works? Each colour name links to a list containing three values.

[View](code/CIRC12p-code.txt) or [download](code/CIRC12.py) the code

Look at the serial terminal built into MU, do the colour names match the LED? If not, check the wiring for each colour and try interchanging the values for COLOUR_ON and COLOUR_OFF. The correct value will depend on if the type of LED used is a common cathode or common anode type.

### CIRC12b

Note that the micro controller pins used have changed.

[View](code/CIRC12bp-code.txt) or [download](code/CIRC12b.py) the code

Look at the serial terminal built into MU, do the colour names match the LED? If not, check the wiring for each colour and try the opposite value for REVERSER. The correct value for REVERSER  will depend on if the type of LED used is a common cathode or common anode type.

Three modifications have been applied:

1. A subroutine cleans it up a bit.

2. Instead of just off/on we can now assign a value between 0 and 255 (00 to FF Hex) to each colour. Instead of being limited to just 8 colours we can now have 2 to the power of 24 colours in the dictionary.

   * I have added a new colour to the list. Can you add another?

   * Does FFAF00 (Hex) look like orange?
     * you could code it like this: 'Orange'  : [255   , 175  , 0  ],

   * Does 4B0082 (Hex) look indigo?

   * Does 7F00FF (Hex) look violet?
     * Or you could code it like this: 'Violet'  : [0x7F   , 0x00  , 0xFF  ],

   * Look up some other colours on the Internet, add them to the dictionary and then tweak them to look best on your LED.

   * Would a diffuser help? How about putting a LED sized hole in a ping-pong ball and putting the LED into the ball.

3. When you use a for loop to dump the contents of a dictionary, you do not know in which order that they will come out. So let’s use a list to get the rainbow’s colours to display in the correct order.

   * Expand the Rainbow list to include more colours. Does it look realistic?

<!-- cSpell:disable -->
<!-- cSpell:enable -->
<!--
# cSpell:disable
# cSpell:enable
cSpell:words ardx mosi leds piezo circuitpy
cSpell:ignore
cSpell:enableCompoundWords
-->
