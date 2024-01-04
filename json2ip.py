from colorist import ColorRGB
import sys

logo ="""
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
"""
line = '-'*100

# My favorite colors
RED =           ColorRGB(255,0,0)
TEAL =          ColorRGB(0,128,128)
GREEN =         ColorRGB(102,255,0)
SILVER =        ColorRGB(192,192,192)
HOTPINK =       ColorRGB(255,105,180)
ROSEWOOD =      ColorRGB(101,0,11)
ROYALBLUE =     ColorRGB(65,105,225)
DEEPSKYBLUE =   ColorRGB(0,191,255)

# Colorful print functions
print_red = lambda args : print(f"{RED}{args}{RED.OFF}", end="")
print_teal = lambda args : print(f"{TEAL}{args}{TEAL.OFF}", end="")
print_green = lambda args : print(f"{GREEN}{args}{GREEN.OFF}", end="")
print_gray = lambda args : print(f"{SILVER}{args}{SILVER.OFF}", end="")
print_pink = lambda args : print(f"{HOTPINK}{args}{HOTPINK.OFF}", end="")
print_rose = lambda args : print(f"{ROSEWOOD}{args}{ROSEWOOD.OFF}", end="")
print_royalblue = lambda args : print(f"{ROYALBLUE}{args}{ROYALBLUE.OFF}", end="")
print_skyblue = lambda args : print(f"{DEEPSKYBLUE}{args}{DEEPSKYBLUE.OFF}", end="")

def ln():
    print_gray(line)
    print()

def error(arg):
    print_red("[-] "+arg)

def help(flag, caption, example=None):
    print_pink(flag)
    print()
    print_skyblue(caption)
    print()
    if not example==None:
        print_gray(example)
        print()
    # print()
    # print()

def main_help():
    ln()
    help(
         flag='-f\t--file', 
         caption='Enter the input file path in front of this flag; its default value is: shodan.json',
         example='\tpython json2ip.py -f file.json\n\tpython json2ip.py -f ./files/file.json'
         )
    ln()
    
    help(
         flag='-o\t--out', 
         caption='Enter the output file path in front of this flag; its default value is: ip.txt',
         example='\tpython json2ip.py -o outfile.txt\n\tpython json2ip.py -o ./files/outfile.txt'
         )
     
    ln()
    
    help(
         flag='-p\t--port', 
         caption='With this flag, you can put the port in output -> IP:Port,\nalso you can put your custom ports!    -> IP:CustomPort\nThis flag cannot be used at the same time as -fp',
         example='\tpython json2ip.py -p\n\tpython json2ip.py -p 445\n\tpython json2ip.py -p 445,446,447,10443'
         )
    print_red('\n')
    
    ln()

    help(
         flag='-fp\t--fillterport', 
         caption='With this flag, you can filter output on one or more ports!\nThis flag cannot be used at the same time as -p',
         example='\tpython json2ip.py -fp 445\n\tpython json2ip.py -fp 445,10443,443'
         )
    
    ln()

    help(
         flag='-v\t--verbose', 
         caption='With this flag, you can print IPs/ports in cli',
         example='\tpython json2ip.py -v'
         )
    
    ln()

    print_skyblue("Example:")
    print_gray("\n\tpython json2ip.py -f filename.json -v -o data.txt -p")
    print_gray("\n\tpython json2ip.py -f filename.json -v -o data.txt -p 445")
    print_gray("\n\tpython json2ip.py -f filename.json -v -o data.txt -p 445,443,10443,100")
    print_gray("\n\tpython json2ip.py -f filename.json -v -o data.txt -fp 443,10443,445,1000\n")
    
    ln()

def worker(fname, ver, addport, oname, userPort, filter_list):
    s1 = '"ip_str": "'
    s2 = '"'
    try:
        with open(fname, 'r+') as f:
            data = f.read()
    except:
        print_red(logo+"\n\n\n\n")
        error("Wrong file name! [{}] dosen't exist!\n".format(fname))
        return

    ans = ''
    ls1 = data.split(s1)
    for i in range(1,len(data.split(s1))):
        ip = ls1[i].split(s2)[0]
        if userPort:
            tmp2 = ''
            ls2 = ls1[i-1].split('"port": ')
            ports = []
            for j in range(1,len(ls2)):
                tmp = ls2[j].split(',')[0]
                ports.append(tmp)
            
            for port in ports:
                tmp2 += ip+":"+port+"\n"
        
        elif addport != '':
            tmp2 = ''
            addports = addport.split(',')
            if len(addports)>1:
                for port in addports:
                    tmp2 += ip+":"+port+'\n'
            else:
                tmp2 = ip+":"+addport+'\n'

        else:
            tmp2 = ip + '\n'

        ans += tmp2

    print_green(logo)

    final_list = ans.split('\n')
    counter = 0
    with open(oname, 'w+') as f:
        if len(filter_list) > 0:
            for element in final_list:
                if element == '':
                    break
                if element.split(':')[1] in filter_list:
                    counter+=1
                    f.write(element + "\n")
                    if ver:
                        print(element)
        else:
            counter = len(ans.split('\n'))-1
            f.write(ans)
            if ver:
                print(ans)
    
    print("\n")
    print_green("[+] DONE!\n")
    print_green("{} ip writed on [{}]\n".format(counter, oname))
    ln()

def do_nothing():
    pass

def bad_input():
    print_red(logo)
    print()
    error('Bad input! use -h or --help for more...\n')
    
def EntryPoint(): 
    ln()
    args = sys.argv[1:]
    if len(args) == 0:
        print_red(logo)
        main_help()
        error("Missing CommandLine argument! use -h or --help for more...")
        return
    
    if args[0]=='-h' or args[0]=='--help':
        print_pink(logo)
        main_help()
        return
    
    args.append('')
    fileName = 'shodan.json'
    outFile = 'ip.txt'
    additionalPort = ''
    userPort = False
    verbose = False
    filter_list = []

    try:
        for i in range(0, len(args)):

            if args[i]=='':
                break

            if args[i][0] == '-' and args[i][1:] not in ['f', 'o', 'h', 'v', 'p','fp', '-file', '-out', '-help', '-verbose', '-port', '-fillterport']:
                error(args[i])
                print()
                bad_input()
                return
            
            if args[i] == '-f' or args[i] == '--file':
                if args[i+1]=='':
                    bad_input()
                    error('-f or ---file\n')
                    return
            
                if args[i+1][0]!='-' :
                    fileName = args[i+1]

                else:
                    bad_input()
                    error('-f or ---file\n')
                    return
            
            if args[i] == '-o' or args[i] == '--out':
                if args[i+1]=='':
                    bad_input()
                    error('-o or --out\n')
                    break

                if args[i+1][0]!='-' :
                    outFile = args[i+1]
                
                else:
                    error('-o or --out\n')
                    bad_input()
                    return
            

            if args[i] == '-fp' or args[i] == '--fillterport':
                if args[i+1]=='':
                    bad_input()
                    error('-fp or --fillterport')
                    return  

                if args[i+1][0]!='-':
                    filter_list = args[i+1].split(',')
                    userPort = True

                else:
                    print('here: ')
                    bad_input()
                    return  

            if args[i] == '-p' or args[i] == '--port':
                additionalPort = ''
                userPort=True
                if args[i+1]!='':
                    if args[i+1][0]!='-':
                        additionalPort = args[i+1]
                        userPort=False
            
            if args[i] == '-v' or args[i] == '--verbose':
                verbose = True
            
            if args[i] == '-h' or args[i] == '--help':
                print_pink(logo)
                print("\n")
                main_help()
                return

    except:
        print_red(logo)
        print()
        error('Bad input! use -h or --help for more...\n')
        return

    worker(fileName, verbose, additionalPort, outFile, userPort, filter_list)
                
EntryPoint()