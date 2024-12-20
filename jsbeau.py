import sys
import os  

def main():
    fileDir = sys.argv[1]    
    for root, dirs, files in os.walk(fileDir):   
        for file in files:  
            if(file.endswith(".js")):
                print(os.path.join(root, file))
                os.system("js-beautify -r %s" % (os.path.join(root, file)))
    print("Done!") 
    os.system("pause")    
  
if __name__ == '__main__':
    main()