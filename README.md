# Minecraft-User-Stats
A Python script that calculates how many hours of your life you've wasted on your own Minecraft server.
## Setup
 * Download `mcUserTime.py` and move the file to the folder of your Minecraft Server
 * Run the script
     * For Windows users, I recommend creating a batch file with the contents `python mcUserTime.py` as a convenient way to run the program
## How to use
 * The script will display a list of all users who have played on the server
 * Type in the name of the user to query their total playtime
 * You can choose to either run the program again or exit
## How it works
 * The script displays a list of users found in the `usercache.json` file in the server folder
 * It analyzes all of the server's log files to calculate a user's total playtime
     * All of the log files except the latest are compressed in gzip format, so the script extracts the files that are compressed
     * In each log file, the script detects all instances where the user has logged in and out
     * The timestamps of these events are converted into seconds and the difference between when a user has logged out and when they logged in is the time played in that session
     * Total playtime is the sum of all sessions, which is converted from seconds to hours
