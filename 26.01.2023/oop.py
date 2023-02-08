#  Inkapsulyatsiya  va klassga oid  xususiyat va metodlar

from uuid import uuid4
class Avtoi:
    """Avtomobil klassi"""
    def __init__(self, make, model, rang, yil, narh, km = 0):
        """Avtomobil xususiyatlari"""
        self.make = make
        self.model = model
        self.rang = rang
        self.yil = yil 
        self.narh = narh
        self.__km = km 
        self.__id = uuid4

    def get_km(self):
        return self.__km

    def get_id(self):
        return self.__id
print(uuid4())