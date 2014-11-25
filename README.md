# introspeqt

[![Code Health][landscape]][landscape_repo] 
[![Build Status][travis]][travis_repo] 

Simple introspector for PySide applications.



##Installation

At the moment `instrospeqt` is not available to be installed from the Python Package Index. Having said that, you can use one of the following methods.

### Clone the repository

Providing that you've got `git` installed in your computer, you can clone the repository by running the following from the command line:

	git clone https://github.com/davidmartinezanim/introspeqt.git

### Manual Installation

Download the zip file for the latest version from [HERE](https://github.com/davidmartinezanim/introspeqt/archive/master.zip).

## Usage

Check the wiki for information about `introspeqt`'s [Usage] and the [Output] that you can expect.

##Current Status

### What it does

* Outputs a text file listing all widgets of a given `QApplication` and the amount of times they've been clicked. 

### Limitations

* Does not output data to other formats other than text files.
* The only event supported at the moment is `QtCore.QEvent.MouseButtonPress`.
* Unable to specify which widgets we want to get information from.
* Output is for one session only. Running the application again replaces output.
* Works with standalone applications but not in hosts that have an event loop already running.

[travis]: https://travis-ci.org/davidmartinezanim/introspeqt.svg
[travis_repo]: https://travis-ci.org/davidmartinezanim/introspeqt
[landscape]: https://landscape.io/github/davidmartinezanim/introspeqt/master/landscape.svg
[landscape_repo]: https://landscape.io/github/davidmartinezanim/introspeqt/master
[usage]: https://github.com/davidmartinezanim/introspeqt/wiki/Usage
[output]: https://github.com/davidmartinezanim/introspeqt/wiki/Output