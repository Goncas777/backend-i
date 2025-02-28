def soma(*args):
    return sum(args)

print(soma(1,2,5,2,1,5))

def filtro(tr,**kwargs):
    return{v for v in kwargs.values() if v < tr}

print(filtro(4,a=5,b=2,c=3,d=4))

