# copy files  
1) By using -i for interactive you will be asked if you would like to replace the file:  
cp -i /home/levan/kdenlive/untitelds.mpg /media/sda3/SkyDrive/  
or you can use -b to create a backup of your file:  
cp -b /home/levan/kdenlive/untitelds.mpg /media/sda3/SkyDrive  

2) Same as the above:  
cp (-i or -b) /media/sda3/SkyDrive/untitelds.mpg /home/levan/kdenlive  

3) Use -R for recursive and -i for interactive:  
cp -Ri ~/MyFolder /sda3/  

# Move files like cutting  
This last one can be done via the mv command, move is like cutting:  
mv -i ~/MyFile ~/OtherFolder/MyFile  
if you want to move a directory, use:  
mv -Ri ~/MyDirectory ~/OtherDirectory/   


# File & Directory Commands   

pwd: The pwd command will allow you to know in which directory you're located (pwd stands for "print working directory"). Example: "pwd" in the Desktop directory will show "~/Desktop". Note that the GNOME Terminal also displays this information in the title bar of its window. A useful gnemonic is "present working directory."   

ls: The ls command will show you ('list') the files in your current directory. Used with certain options, you can see sizes of files, when files were made, and permissions of files. Example: "ls ~" will show you the files that are in your home directory.    

cd: The cd command will allow you to change directories. When you open a terminal you will be in your home directory. To move around the file system you will use cd. Examples:   

To navigate into the root directory, use "cd /"   

To navigate to your home directory, use "cd" or "cd ~"   

To navigate up one directory level, use "cd .."    

To navigate to the previous directory (or back), use "cd -"   

To navigate through multiple levels of directory at once, specify the full directory path that you want to go to. For example, use, "cd /var/www" to go directly to the /www subdirectory of /var/. As another example, "cd ~/Desktop" will move you to the Desktop subdirectory inside your home directory.   

cp: The cp command will make a copy of a file for you. Example: "cp file foo" will make an exact copy of "file" and name it "foo", but the file "file" will still be there. If you are copying a directory, you must use "cp -r directory foo" (copy recursively). (To understand what "recursively" means, think of it this way: to copy the directory and all its files and subdirectories and all their files and subdirectories of the subdirectories and all their files, and on and on, "recursively")  

mv: The mv command will move a file to a different location or will rename a file.   
Examples are as follows: "mv file foo" will rename the file "file" to "foo". "mv foo -/Desktop" will move the file "foo" to your Desktop directory, but it will not rename it. You must specify a new file name to rename a file.  
To save on typing, you can substitute '-' in place of the home directory.  

Note that if you are using mv with sudo you can use the ~ shortcut, because the terminal expands the ~ to your home directory. However, when you open a root shell with sudo -i or sudo -s, ~ will refer to the root account's home directory, not your own.   

rm: Use this command to remove or delete a file in your directory.  

rmdir: The rmdir command will delete an empty directory. To delete a directory and all of its contents recursively, use rm -r instead.  

mkdir: The mkdir command will allow you to create directories. Example: "mkdir music" will create a directory called "music". 
