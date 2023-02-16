# AceClaimDaily
AceClaimDaily in 24 hourly and 12 hourly using proxy

How to Use
----------

1.  Clone this repository to your computer in the terminal.
2.  Make sure Python 3.x is installed on your computer.
3.  Install all required packages by running the command "pip install -r requirements.txt" in the terminal.
4.  Make sure the Chrome driver that matches your version of Chrome is installed. If not, install it by running the command "webdriver-manager install" in the terminal.
5.  Prepare a file "list_akun.txt" that contains the list of addresses to be processed. Make sure this file is located in the same directory as the "global\_browser.py" file.
6.  Run the command "python run.py" in the terminal to run the application. The application will read addresses from the "list_akun.txt" file, process them, and display the result in the Google Chrome browser.

Data
----

The data is assumed to be in the list_akun.txt file, and the user should prepare this file with the necessary information before running the code. The file should contain one or more lines of data, where each line represents one set of information. Each set of information should be structured as follows:
Format: pharse;host:port:user:password
Example: public passs somble dune phone nominee deny find glove member mobile start;60.137.14.111:2233:user:pass

Contribution
------------

If you find any issues or have any suggestions for improvement, please feel free to contribute to this project by submitting a pull request.
