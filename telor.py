from abc import ABC, abstractmethod
from product import Product

class Telor:
    
    def set_nama(self, nama : str):
        self.__nama = nama
        
    def get_nama(self):
        return self.__nama
    
    def set_harga(self, nama : str):
        self.__harga = harga
        
    def get_harga(self):
        return self.__harga
    
    def  show_info ( self,nama,harga ):
        print(self.__nama)
        print(self.__harga)