import os
import shutil


def main():

    try:
        # Create an array with carrying three log files
        files = ['system.log', 'wifi.log', 'install.log']

        # Define the folder name to save the above three logs inside
        folder = 'LogCapture'

        # Create a new directory for the named folder
        os.mkdir(folder)

        # Add the folder to the current path where you want the logs to save
        newDir = os.path.join(os.getcwd(), folder)

        print(newDir)

        # Check all files inside of the array
        for file in files:

            # Define the path and specify the file what you want to capture
            src = r'/var/log/{}'.format(file)

            # Copy the specified file to the current directory you just created
            shutil.copy(src, newDir)

    except Exception as e:
        print(str(e))


main()
