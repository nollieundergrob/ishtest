import colorama
import sys


class ISHbar():
    def __init__(self, maximum:int,desc=''):
        self.desc=desc
        self.maximum = maximum
        self.load_symb = '█'
        self.unload_symb ='▒'
        self.count = 1
    @staticmethod
    def stdprint(msg):
        sys.stdout.write(f'\r{msg}')
        sys.stdout.flush()
    def next(self):
        load_bar = self.count*100//self.maximum
        unload_bar = 100 - load_bar
        if load_bar <= 20:
            msg = f'{colorama.Fore.RED}{self.desc}\t{colorama.Style.RESET_ALL}{self.load_symb*(load_bar//4)}{self.unload_symb*(unload_bar//4)} - {load_bar}%{colorama.Style.RESET_ALL}'  
            
        elif load_bar > 20 and load_bar <= 60:
            msg = f'{colorama.Fore.YELLOW}{self.desc}\t{colorama.Style.RESET_ALL}{self.load_symb*(load_bar//4)}{self.unload_symb*(unload_bar//4)} - {load_bar}%{colorama.Style.RESET_ALL}'
        elif load_bar > 60:
            msg = f'{colorama.Fore.GREEN}{self.desc}\t{colorama.Style.RESET_ALL}{self.load_symb*(load_bar//4)}{self.unload_symb*(unload_bar//4)} - {load_bar}%{colorama.Style.RESET_ALL}'    
        self.stdprint(msg)
        
        
        self.count+=1


if __name__ == '__main__':
    bar = ISHbar(5000,'Loading')
    for i in range(5000):
        bar.next()