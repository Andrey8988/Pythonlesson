from time import sleep
class Ampeln:
    __farbe = 0
    def gehen(self):
        while True:
            print("\033[91m rot")
            sleep(7)
            print("\033[93m gelb")
            sleep(7)
            print("\033[92m gruen")
            sleep(7)
            print("\033[93m gelb")
            sleep(7)
ampeln = Ampeln()
ampeln.gehen()