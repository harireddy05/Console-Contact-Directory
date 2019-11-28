# Console-Contact-Directory

Description:

This is a contact directory application that runs on a console terminal powered by SQLite 3. 
The python code for the application filters inputs in a specific format by employing regular expressions.

Compilation Instructions:

The source code from Python is compiled into a much simpler form called bytecode. The implementation compiles the files as needed.
There is no need to manually compile the program before running.  

To Run > python app.py

Assumptions:
- Running on the Windows OS (The platform wouldn't really matter but was developed on a Windows machine)
- Application isn't intended to run with Python version below 3.x since the sqlite3 module is included in the standard library (since Python 2.5).
- 

Pros:
- Prepared statement helps avoid injections.
- All invalid formats are discarded.
- Whitelisted by regex (better than blacklisting patterns).

Cons:
- Some name formats, if doesn't match the format wouldn't be allowed in the system.

Developed with:
- Python 3
- SQLite 3
- Visual Studio Code
- Anaconda




