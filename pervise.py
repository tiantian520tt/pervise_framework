import color
from pervise_api import *

if __name__ == '__main__':
    logo1 = """
  ____   U _____ u   ____   __     __           ____   U _____ u 
U|  _"\\ u\\| ___"|/U |  _"\\ u\\ \\   /"/u  ___    / __"| u\\| ___"|/ 
\\| |_) |/ |  _|"   \\| |_) |/ \\ \\ / //  |_"_|  <\\___ \\/  |  _|"   
 |  __/   | |___    |  _ <   /\\ V /_,-. | |    u___) |  | |___   
 |_|      |_____|   |_| \\_\\ U  \\_/-(_/U/| |\\u  |____/>> |_____|  
 ||>>_    <<   >>   //   \\\\_  //   .-,_|___|_,-.)(  (__)<<   >>  
(__)__)  (__) (__) (__)  (__)(__)   \\_)-' '-(_/(__)    (__) (__) 
    """
    logo2 = """
 _______                                 __                     
|       \\                               |  \\                    
| $$$$$$$\\  ______    ______  __     __  \\$$  _______   ______  
| $$__/ $$ /      \\  /      \\|  \\   /  \\|  \\ /       \\ /      \\ 
| $$    $$|  $$$$$$\\|  $$$$$$\\\\\\$$\\ /  $$| $$|  $$$$$$$|  $$$$$$\\\\
| $$$$$$$ | $$    $$| $$   \\$$ \\$$\\  $$ | $$ \\$$    \\ | $$    $$
| $$      | $$$$$$$$| $$        \\$$ $$  | $$ _\\$$$$$$\\| $$$$$$$$
| $$       \\$$     \\| $$         \\$$$   | $$|       $$ \\$$     \\\\
 \\$$        \\$$$$$$$ \\$$          \\$     \\$$ \\$$$$$$$   \\$$$$$$$

    """
    logo3 = """
     _ __       ,----.                     ,-.-. .=-.-.  ,-,--.     ,----.  
  .-`.' ,`.  ,-.--` , \\  .-.,.---.  ,--.-./=/ ,//==/_ /,-.'-  _\\ ,-.--` , \\ 
 /==/, -   \\|==|-  _.-` /==/  `   \\/==/, ||=| -|==|, |/==/_ ,_.'|==|-  _.-` 
|==| _ .=. ||==|   `.-.|==|-, .=., \\==\\,  \\ / ,|==|  |\\==\\  \\   |==|   `.-. 
|==| , '=',/==/_ ,    /|==|   '='  /\\==\\ - ' - /==|- | \\==\\ -\\ /==/_ ,    / 
|==|-  '..'|==|    .-' |==|- ,   .'  \\==\\ ,   ||==| ,| _\\==\\ ,\\|==|    .-'  
|==|,  |   |==|_  ,`-._|==|_  . ,'.  |==| -  ,/|==|- |/==/\\/ _ |==|_  ,`-._ 
/==/ - |   /==/ ,     //==/  /\\ ,  ) \\==\\  _ / /==/. /\\==\\ - , /==/ ,     / 
`--`---'   `--`-----`` `--`-`--`--'   `--`--'  `--`-`  `--`---'`--`-----``  
    """
    logo4 = """


PPPPPPPPPPPPPPPPP                                                                 iiii                                       
P::::::::::::::::P                                                               i::::i                                      
P::::::PPPPPP:::::P                                                               iiii                                       
PP:::::P     P:::::P                                                                                                         
  P::::P     P:::::P  eeeeeeeeeeee    rrrrr   rrrrrrrrrvvvvvvv           vvvvvvviiiiiii     ssssssssss       eeeeeeeeeeee    
  P::::P     P:::::Pee::::::::::::ee  r::::rrr:::::::::rv:::::v         v:::::v i:::::i   ss::::::::::s    ee::::::::::::ee  
  P::::PPPPPP:::::Pe::::::eeeee:::::eer:::::::::::::::::rv:::::v       v:::::v   i::::i ss:::::::::::::s  e::::::eeeee:::::ee
  P:::::::::::::PPe::::::e     e:::::err::::::rrrrr::::::rv:::::v     v:::::v    i::::i s::::::ssss:::::se::::::e     e:::::e
  P::::PPPPPPPPP  e:::::::eeeee::::::e r:::::r     r:::::r v:::::v   v:::::v     i::::i  s:::::s  ssssss e:::::::eeeee::::::e
  P::::P          e:::::::::::::::::e  r:::::r     rrrrrrr  v:::::v v:::::v      i::::i    s::::::s      e:::::::::::::::::e 
  P::::P          e::::::eeeeeeeeeee   r:::::r               v:::::v:::::v       i::::i       s::::::s   e::::::eeeeeeeeeee  
  P::::P          e:::::::e            r:::::r                v:::::::::v        i::::i ssssss   s:::::s e:::::::e           
PP::::::PP        e::::::::e           r:::::r                 v:::::::v        i::::::is:::::ssss::::::se::::::::e          
P::::::::P         e::::::::eeeeeeee   r:::::r                  v:::::v         i::::::is::::::::::::::s  e::::::::eeeeeeee  
P::::::::P          ee:::::::::::::e   r:::::r                   v:::v          i::::::i s:::::::::::ss    ee:::::::::::::e  
PPPPPPPPPP            eeeeeeeeeeeeee   rrrrrrr                    vvv           iiiiiiii  sssssssssss        eeeeeeeeeeeeee  







    """
    color.printGreen('[*] Loading libraries...')
    result = load_libraries()
    if result < 0:
        color.printRed(status.get(result))
    else:
        color.printGreen(status.get(result))
    logos = [logo1, logo2, logo3, logo4]
    color.printGreen(logos[random.randint(0, 3)])
    color.printYellow('[!] Used: '+str(sys.argv))
    commands = {
        "help":show_help,
        "info":show_info,
        "make":make_trojan,
        "list":make_list,
        "connect":connect,
        "server":start_server,
        'search':search_module
    }
    while True:
        command = input("Pervise> ")
        if command.lower() == "exit":
            color.printGreen('[*] Goodbye.')
            exit()
        try:
            commands.get(command.split()[0].lower())(command,commands)
        except:
            color.printRed('[-] Bad command.')
