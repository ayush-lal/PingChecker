# PingChecker

Simple Python application to ping Google's IP and output either a "Network Up" or "Network Down" response in the MacOS Taskbar.

![PingChecker Preview](assets/preview.gif)

## Getting Started

### Installation

To run this application you will need Python 3 and the 'Rumps' library. If you wanted to convert this .py to .app, you will also need the Py2App library as well.

`Pip3 install rumps`

`Pip3 install py2app`

### Usage

To run the script: <br>
`Python3 taskbar_app.py`

To convert the .py into a .app: <br>
`Python3 setup.py py2app`

setup.py contains all the code used to build the tasbar_app.py file into an application.

To take this application one step further, you could implement a 'notification' function feature that will notify you when you have lost/regained internet connectivity:
```python
rumps.notification(
    title=self.config["app_name"], message='Connectivity lost/regained')
```
### Contributing

1. Fork the master branch
2. Create your feature branch: `git checkout -b my-new-feature`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin my-new-feature`
5. Submit a pull request! 
---

### Author/ Contact
**Ayush Lal** <br>
hello@ayushlal.com.au | [Portfolio website](http://www.ayushlal.com.au) | [GitHub](https://github.com/ayush-lal)

*// If you have any queries please feel free to get in touch.*

