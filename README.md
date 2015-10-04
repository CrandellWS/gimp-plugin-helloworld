# GIMP Hello World Examples

These scripts are writen primarily in Python and dictate how to create a basic plugin for GIMP. The main highlights include:

  - Basic Structure
  - Displaying Messages
  - Adding Parameters
  - Preparing for batch processing
  - Handling Messages in Batch Processing

### Installation

Copy the contents of the plugin directory to the approprate location for the core functions such as menu options. The contents in the script directory complement the plugins and are not required except for batch processing.

### Plugins

Dillinger is currently extended with the following plugins

* helloWorld (shows what could be done but should not)
* helloBatchWorldMessages (show a better alternative to displaying messages)

Basic Batch Call:
```cmd
gimp -i -b "(call_helloWorld)"
```

Alternative Message Display using 3rd option:
```cmd
gimp -i -b "(call_helloBatchWorldMessages 3)"
```

With verbose output and no extra data:
```cmd
gimp --verbose -d -i -b "(call_helloBatchWorldMessages 3)"
```

In the above example the integer 3 reflects the messageOptions:
```python
messageOptions = {0:noMessage,1:terminalMessage,2:gtkMessage,3:gimpMessage}
```

License
----

MIT
