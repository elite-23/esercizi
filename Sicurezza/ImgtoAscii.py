from pathlib import Path
pin=Path(__file__).with_name('pitone.png')
pout=Path(__file__).with_name('bytes.txt')
with open(pin,'rb') as img:
    content = img.read()
    with open(pout,"w") as t:
        for i in content:
            t.write(str(i)+"\n")


pout=Path(__file__).with_name('pitone2.png')
pin=Path(__file__).with_name('bytes.txt')
with open(pin,'r') as txt:
    content = txt.read()
    with open(pout,"wb") as i:
        content.replace("\n","")
        print(content)
        b=bytes(content,encoding="")
        i.write(b)