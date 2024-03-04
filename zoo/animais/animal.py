from abc import ABC, abstractclassmethod

class Animal():

    @abstractclassmethod
    def _nascer(self):
        print("Nascendo... ")

animal = Animal()
