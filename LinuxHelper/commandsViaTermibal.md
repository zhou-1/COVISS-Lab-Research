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

