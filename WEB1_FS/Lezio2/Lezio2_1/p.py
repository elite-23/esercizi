from pathlib import Path


p=Path(__file__).with_name('pag.html')

with p.open("w") as f:
    pag11 = """<html> 
    <head> 
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
        <title>Canile FS</title> 
    </head> 
    <body style="background-image:url('parco.jpg'); background-repeat: no-repeat; background-attachment: fixed; background-size: cover;"> 
        <div class="container my-5 text-center" style="max-width:580px;">
            <h2>Benvenuto al canile FullStack!!</h2> 
            <p>Scegli un cane da adottare.</p> 
        </div>
        <div class="container">
            <div class="row">
            """

    pag13="""</div>
        </div>
    </body> 
</html> 
""" 
    N=12
    f.write(pag11)
    nomi=[["Pippo","dog.jpg"],["Ciccio","dog2.jpeg"],["Lefty","dog3.jpg"],["Freddy","dog4.jpeg"],["Trappy","dog5.jpg"],["Tasty","dog6.jpeg"],["Tiger","dog7.jpeg"],["Pallino","dog8.jpeg"]]
    for i in range(N):
        if i<len(nomi):
            pag12=f"""   <div class="col-sm">
                    <div class="card" style="width: 18rem; margin-bottom:5%;">
                        <img src={nomi[i][1]} class="card-img-top" alt="...">
                        <div class="card-body">
                            <h5 class="card-title">{nomi[i][0]}</h5>
                            <p class="card-text">Questo cane ha un disperato bisogno di una famiglia che lo ami, aiutalo.</p>
                            <a href="#" class="btn btn-primary">Adottami</a>
                        </div>
                    </div>
                </div>
            """
        else:
            j=i
            while j>=len(nomi):
                j-=len(nomi)
            pag12=f"""    <div class="col-sm">
                    <div class="card" style="width: 18rem; margin-bottom:5%;">
                        <img src={nomi[j][1]} class="card-img-top" alt="...">
                        <div class="card-body">
                            <h5 class="card-title">{nomi[j][0]}</h5>
                            <p class="card-text">Questo cane ha un disperato bisogno di una famiglia che lo ami, aiutalo.</p>
                            <a href="#" class="btn btn-primary">Adottami</a>
                        </div>
                    </div>
                </div>
            """
        f.write(pag12)
    f.write(pag13)
    f.close()