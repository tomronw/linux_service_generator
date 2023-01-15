# Linux boot service generator

Python script to automatically generate a .service file in /systemd/system/ for a Python or Go program that will start on boot.
Depending on your go env you may have to replace the env path in create_go_service.py. Run `which go` on your terminal and 
make sure it matches `/snap/bin/go`, if it doesnt, replace it with your output.

*Warning:* **Please double check that it will not overwrite a current/default .service file** \
[-> Please see default .service files launched at boot](https://www.cyberciti.biz/faq/linux-default-services-which-are-enabled-at-boot/)

## Usage
**run as sudo**
```commandline
pip install -r requirements.txt
sudo python3 -m service_generator --help
```

Run inside /linux_service_generator
```commandline
sudo python3 -m service_generator create /home/user/Desktop/linux_service_generator/test_service.py
Creating service file for /home/user/Desktop/linux_service_generator/test_service.py
Activating service
run `sudo systemctl status linux_service_generator.service` to see status
Successfully created system service
```
This will create the file `lib/systemd/system/linux_service_generator.service`.

Which contains:
```commandline
[Unit]
Description=linux_service_generator system service at boot
After=multi-user.target

[Service]
User=boot
Type=simple
ExecStart=/usr/bin/python /home/user/Desktop/linux_service_generator/test_service.py
Restart=always

[Install]
WantedBy=multi-user.target
```

## Optional args
#### Custom user
Specify which Linux user the service will run from (Helps with python 'module not found errors') Linux runs a service file as `boot` by default.
```commandline
sudo python3 -m service_generator create /home/user/Desktop/linux_service_generator/test_service.py --user user2
```
#### Custom service name
Specify a custom name instead of the program dir name
```commandline
sudo python3 -m service_generator create /home/user/Desktop/linux_service_generator/test_service.py --s_name custom_service
```

#### Delete service
You can delete services by using the `delete` command and name of the service
```commandline
sudo python3 -m service_generator delete linux_service
```
