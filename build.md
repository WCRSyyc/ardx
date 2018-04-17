# Building circuit pages

A circuit needs:
* CIRC«nn».html
* code/CIRC«nn»-code.txt
  * from Arduino sketch
* img/CIRC«nn»-bb.svg
* img/CIRC«nn»-schem.svg
  * From Fritzing, possibly adjusted to enhance and repair image
* img/«circuit-header-image».jpg
  * cleanest with rounded transparent corners on right
* fritzing/CIRC«nn».fzz
* resources: ?optional?
  * CIRC«nn»-sheet-WCRS.pdf
  * youtube video

The svg images are exported directly from a Fritzing document.  The scaling and offset will need to be manually hardcoded in the html to get the desired views.

## common html blocks
* shell.html
  * head.html
  * topnav.html
  * sidebar.html

### shell.html standard edits
* «circuit_number»
  * 6 places?
* «description»
* «title_line_1»
* «title_line_2»
* img/«circuit_name»-100.jpg
* alt="«circuit_alt»"
* «whatDoing»
* table
  * fill in the parts: each with
    * 60x36 img
    * up to 3 lines of text in single td
* schematic svg image
  * x, y, scale
* breadboard svg image
  * x, y
* populate or delete Resources
* «raw_code»
* «nw_count»
* repeat
  * «nw_title»
  * «nw_description»
* repeat
  * «mb_title»
  * «mb_description»
