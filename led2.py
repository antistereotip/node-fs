from gpiozero import LED
import time
import keyboard

zeleno = LED(18)
zuto = LED(17)
crveno = LED(23)
crveno_indikator = LED(21)


def dva():
   crveno.on()
   time.sleep(K)
   zuto.on()
   time.sleep(K)
   crveno.off()
   zuto.off()

def jedan():
   zeleno.on()
   time.sleep(K)
   zeleno.off()
   zuto.on()
   time.sleep(K)
   zuto.off()
   crveno.on()
   time.sleep(K)

while True:
   K = input("Sleep for: ")
   if K == 1 :
      while True :
         dva()
         jedan()
         if keyboard.is_pressed('q'):
            break

   elif K == 2 :
      while True :
         jedan()
         if keyboard.is_pressed('q'):
            break

   else :
      while True :
         crveno_indikator.on()
         if keyboard.is_pressed('q'):
            break
