import numpy, imageio, math, sys
#func for checking domain and return new cordinate
def f(x, y, r):
    if r == 0 or 1 - r**2 < 0:
        return -2, -2
    d = 1 - math.sqrt(1 - r**2)
    r2 = (r + d) / 2
    return (x / r)*r2, (y / r)*r2
def main(arg):
    img = imageio.imread(arg[0])
    #pic size
    sz = img.shape
    w, h, ks= sz
    #create new black pic with same size
    de = numpy.zeros_like(img)
    for i in range(w//1):
        for j in range(h//1):
            #normalize
            ind = (2*i - w)/w
            jnd = (2*j - h)/h
            rd = math.sqrt(ind**2 + jnd**2)
            #check domain
            xu, yu = f(ind, jnd, rd)
            xu = int(((xu + 1)*w)//2)
            yu = int(((yu + 1)*h)//2)
            #check limits of pic edges
            if 0 <= xu < img.shape[0] and 0 <= yu < img.shape[1]:
                #check for change pic method
                #normal to fish eye
                if arg[2] == 'ntof':
                    de[int(xu)][int(yu)] = img[i][j]
                #fish eye to normal
                elif arg[2] == 'fton':
                    de[i][j] = img[xu][yu]
    #overload pic in resault image for save
    res = de.astype(numpy.uint8)
    #save in given path
    imageio.imwrite(arg[1] + '.jpg', res)
if __name__ == "__main__":
    #run main with terminal args
    main(sys.argv[1:])
