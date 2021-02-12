# Flask-SocketIO-ChatApp
A simple and super minimalistic Chat App, for easy use!
<br>

To use this project first of all download the files using(make sure you are in the project directory to access requirements.txt)-<br>
```
> pip install -r requirements.txt
```

**IMPORTANT- FOR LOCAL USE ON A IPv4 Address**<br>
Under Flask-ChatApp/app, you will find a ```__init__.py``` which has the ```create_app``` method and in that method you should see the env variables, you can edit those accordingly but the most important step here is that the env variable ```HOST``` has to be set specifically. In your command prompt

```cmd
Drive:\Folder\Flask-ChatApp>ipconfig
...
...
...
```

After you typed that you should get some network information about your PC that I cannot show here about my PC but you should see your IPv4 it look like something 192.168.X.X
Don't worry IPv4 are only used for communication so if even someone sees your IPv4 they can't do anything do with the security of your PC. Then in our ```__init__.py``` file simply change the my IPv4 address to your own IPv4 address.

After all that, simply run the flask sever using-
```
> python chat.py
```

Then Go to the directed server address!
