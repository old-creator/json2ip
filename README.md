# Shodan .Json 2 IP
By using this Python script, you can clean your .json export data from Shodan website and extract the IP and ports.

```
 ____  _               _
/ ___|| |__   ___   __| | __ _ _ __
\___ \| '_ \ / _ \ / _` |/ _` | '_ \
 ___) | | | | (_) | (_| | (_| | | | |
|____/|_| |_|\___/ \__,_|\__,_|_| |_|
   _                 ____  _
  (_)___  ___  _ __ |___ \(_)_ __
  | / __|/ _ \| '_ \  __) | | '_ \
  | \__ \ (_) | | | |/ __/| | |_) |
 _/ |___/\___/|_| |_|_____|_| .__/
|__/                        |_|

```
## Installation
Download project and install requirements using pip.
```bash
git clone https://github.com/old-creator/json2ip.git
```
```bash
pip insstall -r requirements.txt
```

## Usage
_FLAGS_:

***
```
-f  --file
```
Use this flag to specify the input file path to the program, this file must be in **.json** format and output from **Shodan** site.

If you don't specify the input file path to the program, the following address will be automatically set for the file:

**./shodan.json**

***
```
-o  --out
```
Use this flag to specify the output file of the program, this file must be in text format.

If you do not specify the output file of the program, the following address will be automatically set for the file:

**./ip.txt**

***
```
-p  --port
```
By using this flag, you can see the ports in the data in addition to the IPs in the output of the program.

```
# command:
python json2ip.py -p

# out:
111.111.111.111:2222
```

Also note that if there are multiple ports for the IP, different lines of output will be provided.

```
# command:
python json2ip.py -p

#out:
111.111.111.111:2222
111.111.111.111:3333
```
You can also put your desired ports in the output for all IPs by putting the desired ports after this flag.

```
#command:
python json2ip.py -p 445

#out:
111.111.111.111:445
```
```
#command:
python json2ip.py -p 445,446,447

#out:
111.111.111.111:445
111.111.111.111:446
111.111.111.111:447
```

***
```
-fp  --fillterport
```
Using this flag, you can filter the output on ports, for example, only see a combination of IP and ports that have specific ports.

***
```
-v  --verbose
```
By using this flag, you can see the output data in addition to the output file in the command line.

***
```
-h  --help
```
Use this flag to view the program's help on the command line.
