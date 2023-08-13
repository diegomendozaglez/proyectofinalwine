Deliverable number 2 (Instructions in README.md file in a repository)

Instructions in README.md file in a repository.

To create a virtual environment in Windows, follow these steps:

To create a virtual environment in the Windows CMD, you can follow these steps:

Open CMD: Go to the start menu, type "cmd" in the search bar and select "Command Prompt" to open the CMD window.

Navigate to the location where you want to create the virtual environment: Use the cd command to navigate to the desired folder. For example, if you want to create the virtual environment in the "Projects" folder, you can use the cd Projects command to access that folder.

Create the virtual environment: Use the command python -m venv environment_name to create the virtual environment. Replace "environment_name" with whatever name you want to give your virtual environment. For example, if you wanted to call it "myenv", the command would be python -m venv myenv.


Activate the virtual environment: Use the command environment_name\Scripts\activate.bat to activate the virtual environment. Replace "environment_name" with whatever name you've given your virtual environment. For example, if your virtual environment is called "myenv", the command would be myenv\Scripts\activate.bat.
Once you have activated the virtual environment, you will be able to install packages and work on your project without affecting the overall installation of Python on your system.

Remember that these steps are specific to creating a virtual environment using the Windows CMD.

Command summary:

py -m venv venv
venv3_7\Scripts\activate
call venv\Scripts\activate
py -m pip freeze
