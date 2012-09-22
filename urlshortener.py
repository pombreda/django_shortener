# -*- coding: utf-8 -*-
"""
   create a simple random string 
"""
import random
class urlshortener():
    __range_str = "abcdefghijklmnopqrstuvwxyz"
    __range_str_up = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    __range_int = "0123456789"
    __shuffle = ''
    __length = 0 

    """
        let's shake the char to use
    """
    def to_shake(self):
        a = list(self.__range_str)
        b = list(self.__range_str_up)
        c = list(self.__range_int)
        char =  a+b+c
        random.shuffle( char )
        self.__shuffle = ''.join(char)
        return self
    """
        get random char from the shake
    """
    def do_run(self):
        rand = '';
        for i in range(self.__length):
            rand += self.get_random_char();
        return rand;
    """
        get the shuffle string initializes from to_shake        
    """
    def get_random_char(self):
        limit = len(self.__shuffle) - 1;
        return self.__shuffle[random.randint(0,limit)];
    """
        set the length of the random string
        then launch do_run to get the random char
    """
    def run(self,length):
        self.__length = length        
        return self.do_run()
    """
        start by shaking your hand all togethers
    """
    def __init__(self):
        self.to_shake()
        
if __name__ == "__main__":
    shrt = Urlshortener()
    print shrt.run(10)