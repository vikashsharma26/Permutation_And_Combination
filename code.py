def combo():
    x = input("Stirng: ")
    if x=="":
        raise ValueError("Plzz enter word")
    x1 = x[0]
    x = x[1:]
    for v in x:
        try:
            a = new
        except:
            a = [x1]
        new = []
        for i in a:
            for j in range(len(i)+1):
                try:
                    k = list(i)
                    k.insert(j,v)
                except:
                    k.insert(j,v)
                new.append("".join(k))
        del(a)
    for jk in new:
        print(jk)
combo()
