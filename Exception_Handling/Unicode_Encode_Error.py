try:
    file = open("demo.txt","w", encoding = "ascii") 
    file.write("ನಮಸ್ಕಾರ")
except UnicodeDecodeError:
    print("Encoding error while writing.")  
