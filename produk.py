from abc import ABC, abstractmethod

class Produk:
    
    
    def set_nama(self, nama : str):
        self.__nama = nama
        
    def get_nama(self):
        return self.__nama
    
    def set_harga(self, harga :float):
        self.__harga = harga
        
    def get_harga(self):
        return self.__harga
        
    @abstractmethod
    def show_info(self):
        pass