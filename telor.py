from abc import ABC, abstractmethod
from produk import Produk

class Telor:
    
    def set_nama(self, nama : str):
        self.__nama = nama
        
    def get_nama(self):
        return self.__nama
    
    def set_harga(self, harga : float):
        self.__harga = harga
        
    def get_harga(self):
        return self.__harga
    
    def  show_info ( self):
        print(self.__nama)
        print(self.__harga)