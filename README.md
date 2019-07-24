# Minecraft-User-Stats
A Python script that calculates how many hours of your life you've wasted on your own Minecraft server.
## Setup
 * Note: Python 3.x must be installed prior to running the script
 * Download `mcUserTime.py` and move the file to the folder of your Minecraft Server
 * Run the script
     * For Windows users, I recommend creating a batch file with the contents `python mcUserTime.py` as a convenient way to run the program
## How to use
 * The script will display a list of all users who have played on the server
 * Type in the name of the user to query their total playtime
## How it works
 * The script displays a list of users found in the `usercache.json` file in the server folder
 * It analyzes all of the server's log files to calculate a user's total playtime
     * All of the log files except the latest have been compressed in gzip format, so the script extracts the files that are compressed
     * The script calculates the length of each play session using the timestamps of the user's logins and logouts
