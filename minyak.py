from abc import ABC, abstractmethod

class Minyak:
    
    def  __init__ ( self , nama, harga ):
         self. __nama  =   nama
         self. __harga  =  harga
        
    
    @abstractmethod
    def  show_info ( self ):
        pass