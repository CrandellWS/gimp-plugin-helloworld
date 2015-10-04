# used for os.getcwd() see -> (PF_DIRNAME, "p28", "DIRNAME:", os.getcwd())
# used for os.getcwd() see -> (PF_FILENAME, "file-choice", "User Selected File:", os.getcwd()),
import os

# using from gimpfu import *
# Allows this module to get all the commonly used symbols into the plug-in's namespace
from gimpfu import *

def helloParameterWorldFn():

    #Next @todo is helloParameterWorldRetrieval
    return

register(
    "helloParameterWorldPlugin",
    "Hello Parameter World",
    "Hello Parameter World display of standard user inputs.",
    "William Crandell <william@crandell.ws>",
    "William Crandell <william@crandell.ws>",
    "2015",
    "Hello Parameter World",
    "", # image types: "" means plugin will not push the current image as a variable
    [
      # Plugin parameter tuples: (type, name, description, default, [extra])
      # Note these determine both the type of the parameter and the GUI widget displayed.
      # Note the underbar in the description tells what letter is the shortcut key.
      #
      # Editable text boxes

      # PF_INT8, PF_INT16, PF_INT32 has no difference in Python but is used in C plugins.
      (PF_INT, "intParam", "Integer Input:", 0), #<PF_INT> is synonymous to <PF_INT32>.
      # (Type, name, label, initial-Value)

      # PF_FLOAT is to define a variable with a fractional value
      (PF_FLOAT, "floatParam", "Float Input:", 3.14),
      # (Type, name, label, initial-Value)

      # Literal text string single line field
      (PF_STRING, "stringParam", "Sting Input:", "Default String"),  # alias PF_VALUE
      # (Type, name, label, initial-Value)

      # Literal text string multiline line field
      (PF_TEXT, "textParam", "Text Input:", "Text Default \n With extra line."),
      # (Type, name, label, initial-Value)

      # Select list style choice returns indexed value
      (PF_OPTION, "option-param", "Select List:", 2, ["Option 0", "Option 1", "Option 2"]),
      # (Type, name, label, initial-Value ["List", "Of", "Options"])

      # Use [] for lists and () for tuples [see ->](http://stackoverflow.com/a/8900189/1815624)

      # PF_RADIO radio button group.
      (PF_RADIO, "radio-param", "Radio Choices:", 0, (("0th", 0),("1st",'1'),("1st","3xs"))),
      # (Type, name, label, initial-Value (Tuple))
      # If you don't know about tuples, now is a good time to learn
      # [see ->](https://en.wikibooks.org/wiki/Python_Programming/Tuples)

      # PF_TOGGLE boolean
      (PF_TOGGLE, "toggle-param", "True or False(0,1):", 1), # Alias PF_BOOL
      # (Type, name, label, initial-Value)

      # PF_SLIDER horizontal slide
      (PF_SLIDER, "slider-Name", "Slider Option:", 15, (0, 30, 3)), # required parameters (min, max, step)
      # (Type, name, label, initial-Value, (min, max, step))


      (PF_SPINNER, "spinner-Option-Name", "Spinner Selection:", 50, (1, 100, 2)),  # alias PF_ADJUSTMENT
      # (Type, name, label, initial-Value, (min, max, step))


      # Pickers ie combo boxes ie choosers from lists of existing Gimp objects
      (PF_COLOUR, "color-choice", "Pick a Color:", (100, 21, 40)), # alias PF_COLOUR required (R, G, B)
      # (Type, name, label, initial(red, green, blue)Value)

      # PF_FONT Font Selection Dialog
      (PF_FONT, "some-name-Of-this-Font-Param", "Choose a Font:", 'Sans'),
      # (Type, name, label, initial-Font-Value)

      # PF_BRUSH Paint Brush Selection Dialog
      (PF_BRUSH, "brush-Type-Picked", "Select a Brush:", "2. Star"),
      # (Type, name, label, initial-Brush-Value)

      # PF_PATTERN Pattern Selection Dialog
      (PF_PATTERN, "user-Pattern-Choice", "Choose a Pattern:", "3D Green"),
      # (Type, name, label, initial-Pattern-Value)

      # PF_GRADIENT Gradient Selection Dialog
      (PF_GRADIENT, "gradient-Chosen", "Gradient of Choice:", "Blinds"),
      # (Type, name, label, initial-Gradient-Value)

      # PF_PALETTE Palette Selection Dialog
      (PF_PALETTE, "picked-Palette", "Palette Pick:", "Firecode"),
      # (Type, name, label, initial-Palette-Value)

      (PF_FILENAME, "file-choice", "User Selected File:", os.getcwd()),
      # (Type, name, label, initial-Filename-Value)
      # initial-Filename-Value might be 0, None, False, /, or just ""
      # Preference could be to get current work directory with os.getcwd()
      # [See ->](https://docs.python.org/2/library/constants.html#None)

      ## Windows systems does not always play nice
      # with the file/directory options PF_FILE, PF_FILENAME, PF_DIRNAME
      # Better to use PF_FILENAME or PF_DIRNAME as needed respectively over PF_FILE
      # (PF_FILE, "file-or-directory", "File or Directoy:", ''),
      # Depending on default user can choose a file or a directory


      (PF_DIRNAME, "directoy-choice", "Directory of Choice:", os.getcwd())
      # (Type, name, label, initial-DirectoryName-Value)
      # initial-DirectoryName-Value might be 0, None, False, /, or just ""
      # Preference could be to get current work directory with os.getcwd()
      # [See ->](https://docs.python.org/2/library/constants.html#None)

    ],
    [],
    helloParameterWorldFn,
    menu = "<Toolbox>/Hello/")
main()
