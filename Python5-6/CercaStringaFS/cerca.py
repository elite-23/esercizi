import os
import PyPDF2

Sroot=input("Inserisci la directory in cui cercare. ")
SParola=input("Inserisci la parola da cercare. ")
SOutDir=input("Inserisci la directory di output. ")
X=0
for root,dirs,files in os.walk(Sroot):
    print(f"Sto guardando {root}, che contiene {len(dirs)} subdirs, {len(files)} files.")
    for file in files:
        if file.find(SParola) != -1:
            X+=1
        else:
            print("sono nel file")
            f=os.path.join(root,file)
            n,ext=os.path.splitext(f)
            if ext.lower() == ".txt":
                print("Il file è txt")
                with open(f,"r") as txt:
                    line=txt.readline()
                    while(len(line)>0):
                        if line.lower().find(SParola)!=-1:
                            X+=1
                            break
                        line=txt.readline()
            elif ext.lower() == ".pdf":
                
                object = PyPDF2.PdfReader(f)
                numPages = len(object.pages)
                for i in range(0, numPages):
                    pageObj = object.pages[i]
                    text = pageObj.extract_text()
                    text = text.lower()
                    if(text.find(SParola)!=-1):
                        X+=1   
print(f"Sono stati trovati {X} file con la parola '{SParola}'")