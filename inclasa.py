with open("lista.txt", "r")as f:
    x=list(eval(f.readline()))
x.sort(reverse=True)
y=sorted(x)
with open("output.txt", "w") as f:
    f.write("Lista: "+ str(x) +"\n")
    f.write("Lista sortata "+str(y)+"\n")
    f.write("Lista sortata iners" +str(x)+"\n")
    f.write("Numarul de elemente din lista: " + str(len(x))+"\n")
    f.write("Elementul maxim din lista: " + str(max(x))+"\n")
    f.write("Elementul minim din lista: " + str(min(x))+"\n")
    f.write("Lista cu elementul 111 la sfarsit "+str(x+[111])+"\n")
    x.insert(1, 222)
    f.write("Lista cu elementul 222 pe pozitia a doua"+str(x))

