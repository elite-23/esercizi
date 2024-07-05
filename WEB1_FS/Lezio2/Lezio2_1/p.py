with open("pag.html","w")as f:
    pag11 = """<html> 
    <head> 
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
        <title>Title</title> 
    </head> 
    <body> 
        <div class="container my-5 text-center" style="max-width:580px">
            <h2>Benvenuto al canile FullStack!!</h2> 
            <p>Scegli un cane da adottare.</p> 
        </div>
        <div class="container">
            <div class="row">
                """

    pag12="""<div class="col-sm">
                <div class="card" style="width: 18rem; margin-bottom:5%;">
                    <img src="dog.jpg" class="card-img-top" alt="...">
                    <div class="card-body">
                        <h5 class="card-title">Numero1</h5>
                        <p class="card-text">Questo cane ha un disperato bisogno di una famiglia che lo ami, aiutalo.</p>
                        <a href="#" class="btn btn-primary">Adottami</a>
                    </div>
                </div>
            </div>
        """

    pag13="""
            </div>
        </div>
    </body> 
</html> 
"""
  
    # writing the code into the file 
    N=10
    f.write(pag11+(pag12*N)+pag13) 

    f.close()
  
with open("pag.html") as f:
    print(f.read())
    f.close()
