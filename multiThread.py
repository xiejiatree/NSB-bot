import multiprocessing

#enables multiple python threads to run at once. 
botFiles = ['shutdown','sleeplessLoser']
for botFiles in ('shutdown','sleeplessLoser'):
    p = multiprocessing.Process(target=lambda: __import__(botFiles))
    p.start()
