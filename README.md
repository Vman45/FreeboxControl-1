FreeboxControl
==============

Control your Freebox with Python 2.7 (thanks to Freebox API v3.0)


Install
-------
Download and install with:

    $ git clone https://github.com/nemoz28/FreeboxControl
    $ cd FreeboxControl
    $ sudo python setup.py install


Obtaining an app\_token
-----------------------
This is the first step, the application will ask for an app_token using the following call. A message will be displayed on the Freebox LCD asking the user to grant access to the requesting application.

Once the application has obtained a valid app\_token, it will not have to do this procedure again unless the user revokes the app_token.

```python
from freeboxctrl import FreeboxCtrl

myBox = FreeboxCtrl('test.id')
app_token = myBox.register('My application name')
```

Reference
---------

### Get Freebox Host / Smartphone / Ipad online (status True / False)
```python

    mac = sys.argv[1]
    jsonform = myBox.state_lan_host(mac)
    jsonlist = myBox.configuration_lan_browser()

    #json.dumps(data, indent=4, separators=(',', ': '), sort_keys=True)
    for key in jsonlist:
        for item, value in key.iteritems():
		
		if str(item) == "primary_name":
            		print json.dumps(value)

        	if str(item) == "host_type":
            		print json.dumps(value)

        	if str(item) == "last_activity":
            		print json.dumps(value)

        	if str(item) == "active":
            		print json.dumps(value)
	
		if str(item) == "id":
                        print json.dumps(value)		


```

### Usekey list or detecte host active by mac address
```python
cd fbx-zalarmPi/

~.FreeboxControl/fbx-zalarmPi# python presence.py

"workstation"
1476369939
true
"BIGFAT"
"ether-00:08:9b:c8:b3:f7"
------------
"freebox_player"
1476369974
true
"Freebox Player"
"ether-f4:ca:e5:71:15:46"
------------

~.FreeboxControl/fbx-zalarmPi# python presence.py ether-84:b1:53:e4:91:54 

------------
"smartphone"
1476367995
false
"iPhonedAMAROCZY"
------------
```

