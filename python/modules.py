#alias (takma ad (as))
#import matematik as m  #------ > matematik dosyayını bu dosyaya aktardık
# matematik isimli dosyayı m ile çağırmamızı sağladı (alias(takma ad))
from matematik import topla
from day2 import sayHello
from human import Human
#built-in modules
import random
from selenium import webdriver

print(topla(10,20))

print(random.randint(0,100))

human1 = Human("Mirza")
human1.talk("Merhaba")

chromeDriver = webdriver.Chrome()
#packages
