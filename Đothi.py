import os 
import cv2
from matplotlib import image


'''img1 = cv2.imread("d218.tif")
cv2.imshow("Input" , img1)


os.system('prostak.exe -o threshold -p 10.0 -s otsu d218.tif threshold1.tif,text_threshold.txt')
img2 = cv2.imread("threshold1.tif")
cv2.imshow("threshold1" , img2)

os.system('prostak.exe -o mul threshold1.tif,d218.tif mul1.tif')
img3= cv2.imread("mul1.tif")
cv2.imshow("mul1" , img3)

os.system('prostak.exe -o heq mul1.tif,threshold1.tif heqm1.tif ')
img4= cv2.imread("heqm1.tif")
cv2.imshow("heqm1" , img4)

os.system('prostak.exe -o andif -s 10,0.5,0.9,frac heqm1.tif andif1.tif')
img5= cv2.imread("andif1.tif")
cv2.imshow("andif1" , img5)

os.system('prostak.exe -o expand -p 2.0 andif1.tif expand1.tif')
img6= cv2.imread("expand1.tif")
cv2.imshow("expand1" , img6)

os.system('prostak.exe -o strel -s 9,9,square strel1.txt')
os.system('prostak.exe -o gerosion -r 1 expand1.tif,strel1.txt gerosion1.tif')
img7= cv2.imread("gerosion1.tif")
cv2.imshow("gerosion1" , img7)

os.system('prostak.exe -o reconstruct -r 4 expand1.tif,gerosion1.tif reconstruct1.tif')
img8= cv2.imread("reconstruct1.tif")
cv2.imshow("reconstruct1" , img8)


os.system('prostak.exe -o invert reconstruct1.tif invert1.tif')
img9 = cv2.imread("invert1.tif")
cv2.imshow("invert1" , img9)

os.system('prostak.exe -o gerosion -r 1 invert1.tif,strel1.txt gerosion2.tif')
img10= cv2.imread("gerosion2.tif")
cv2.imshow("gerosion2" , img10)


os.system('prostak.exe -o reconstruct -r 4 invert1.tif,gerosion2.tif reconstruct2.tif')
img11= cv2.imread("reconstruct2.tif")
cv2.imshow("reconstruct2" , img11)


os.system('prostak.exe -o cwtsd -r 4 reconstruct2.tif cwtsd1.tif')
img12= cv2.imread("cwtsd1.tif")
cv2.imshow("cwtsd1" , img12)


os.system('prostak.exe -o mul cwtsd1.tif,expand1.tif mul2.tif')
img13= cv2.imread("mul2.tif")
cv2.imshow("mul2" , img13)

os.system('prostak.exe -o threshold -p 3.0 -s plain mul2.tif threshold2.tif,text_threshold2.txt')
img14= cv2.imread("threshold2.tif")
cv2.imshow("threshold2" , img14)

os.system('prostak.exe -o strel -s 3,3,square strel2.txt')
os.system('prostak.exe -o gerosion -r 1 threshold2.tif,strel2.txt gerosion3.tif')
img15= cv2.imread("gerosion3.tif")
cv2.imshow("gerosion3" , img15)

os.system('prostak.exe -o median -r 1 threshold2.tif,strel2.txt median1.tif')
img16= cv2.imread("median1.tif")
cv2.imshow("median1" , img16)

os.system('prostak.exe -o gmag median1.tif gmag1.tif')
img17= cv2.imread("gmag1.tif")
cv2.imshow("gmag1" , img17)

os.system('prostak.exe -o threshold -p 1.0 -s plain -r 1 gmag1.tif threshold3.tif,text_threshold3.txt')
img18= cv2.imread("threshold3.tif")
cv2.imshow("threshold3" , img18)

os.system('prostak.exe -o expand -p 2.0 mul1.tif expand2.tif')
img19= cv2.imread("expand2.tif")
cv2.imshow("expand2" , img19)

os.system('prostak.exe -o movl -s magenta,yellow threshold3.tif,expand2.tif movl1.tif')
img20= cv2.imread("movl1.tif")
cv2.imshow("movl1" , img20)


###xu ly dau vao t2

img21 = cv2.imread("f218.tif")
cv2.imshow("Input2" , img21)

os.system('prostak.exe -o expand -p 2.0 f218.tif expand21.tif')
img22= cv2.imread("expand21.tif")
cv2.imshow("expand21" , img22)


os.system('prostak.exe -o invert expand21.tif invert21.tif')
img23 = cv2.imread("invert21.tif")
cv2.imshow("invert21" , img23)

os.system('prostak.exe -o heq invert21.tif heq21.tif')
img24 = cv2.imread("heq21.tif")
cv2.imshow("heq21" , img24)

os.system('prostak.exe -o despekle -r 4 heq21.tif despekle21.tif')
img25 = cv2.imread("despekle21.tif")
cv2.imshow("despekle21" , img25)


os.system('prostak.exe -o strel -s 3,3,square strel21.txt')
os.system('prostak.exe -o gerosion -r 1 despekle21.tif,strel21.txt gerosion21.tif')
img26 = cv2.imread("gerosion21.tif")
cv2.imshow("gerosion21.tif" , img26)


###xu ly dau vao t3
img31 = cv2.imread("r218.tif")
cv2.imshow("Input3" , img31)


os.system('prostak.exe -o expand -p 2.0 r218.tif expand31.tif')
img32= cv2.imread("expand31.tif")
cv2.imshow("expand31" , img32)

os.system('prostak.exe -o heq expand31.tif heq31.tif')
img33 = cv2.imread("heq31.tif")
cv2.imshow("heq31" , img33)

os.system('prostak.exe -o despekle -r 4 heq31.tif despekle31.tif')
img34 = cv2.imread("despekle31.tif")
cv2.imshow("despekle31" , img34)

os.system('prostak.exe -o gerosion -r 1 despekle31.tif,strel21.txt gerosion31.tif')
img35 = cv2.imread("gerosion31.tif")
cv2.imshow("gerosion31.tif" , img35)

###gop xu ly anh 2 va 3 

os.system('prostak.exe -o avg gerosion21.tif,gerosion31.tif avg2_1.tif')
img36 = cv2.imread("avg2_1.tif")
cv2.imshow("avg2_1.tif" , img36)

os.system('prostak.exe -o andif -s 20,0.3,0.7,frac avg2_1.tif andif31.tif')
img37= cv2.imread("andif31.tif")
cv2.imshow("andif31" , img37)

###gerosion 52 _ giua hinh 2 va 3 
os.system('prostak.exe -o strel -s 23,23,disk strel32.txt')
os.system('prostak.exe -o gerosion -r 1 andif31.tif,strel32.txt gerosion32.tif')
img38 = cv2.imread("gerosion32.tif")
cv2.imshow("gerosion32.tif" , img38)
#reconstruct 57
os.system('prostak.exe -o reconstruct -r 4 andif31.tif,gerosion32.tif reconstruct31.tif')
img39= cv2.imread("reconstruct31.tif")
cv2.imshow("reconstruct31" , img39)

#invert 54
os.system('prostak.exe -o invert reconstruct31.tif invert31.tif')
img40 = cv2.imread("invert31.tif")
cv2.imshow("invert31" , img40)

#gerosion 53
os.system('prostak.exe -o gerosion -r 1 invert31.tif,strel32.txt gerosion33.tif')
img41 = cv2.imread("gerosion33.tif")
cv2.imshow("gerosion33.tif" , img41)
#reconstruct 58
os.system('prostak.exe -o reconstruct -r 4 invert31.tif,gerosion33.tif reconstruct32.tif')
img42= cv2.imread("reconstruct32.tif")
cv2.imshow("reconstruct32" , img42)

os.system('prostak.exe -o strel -s 9,9,disk strel33.txt')
os.system('prostak.exe -o gclose -r 7 reconstruct32.tif,strel33.txt gclose31.tif')
img43 = cv2.imread("gclose31.tif")
cv2.imshow("gclose31" , img43)

#doan tach ra tu gmag
os.system('prostak.exe -o gmag gclose31.tif gmag31.tif')
img44= cv2.imread("gmag31.tif")
cv2.imshow("gmag31" , img44)


os.system('prostak.exe -o threshold -p 10.0 -s otsu gmag31.tif threshold31.tif,text_threshold31.txt')
img45 = cv2.imread("threshold31.tif")
cv2.imshow("threshold31" , img45)#hinh dau ra o cuoi cung 
#


os.system('prostak.exe -o invert median1.tif invert32.tif')
img46 = cv2.imread("invert32.tif")
cv2.imshow("invert32" , img46)
#mul 122
os.system('prostak.exe -o mul invert32.tif,gclose31.tif mul31.tif')
img47= cv2.imread("mul31.tif")
cv2.imshow("mul31" , img47)


os.system('prostak.exe -o cwtsd -r 4 mul31.tif cwtsd31.tif')
img48= cv2.imread("cwtsd31.tif")
cv2.imshow("cwtsd31" , img48)






#xu ly nhanh tren cua phan 3 bat dau tu reconstruct


os.system('prostak.exe -o reconstruct -r 4 cwtsd31.tif,median1.tif reconstruct33.tif')
img49= cv2.imread("reconstruct33.tif")
cv2.imshow("reconstruct33" , img49)




#xu ly nhanh duoi cua phan 3 bat dau tu minusabs 
os.system('prostak.exe -o minusabs reconstruct33.tif,cwtsd31.tif minusabs31.tif')
img50 = cv2.imread("minusabs31.tif")
cv2.imshow("minusabs31" , img50)

os.system('prostak.exe -o gclose -r 1 minusabs31.tif,strel2.txt gclose32.tif')
img51 = cv2.imread("gclose32.tif")
cv2.imshow("gclose32" , img51)
#invert137
os.system('prostak.exe -o invert gclose32.tif invert33.tif')
img52 = cv2.imread("invert33.tif")
cv2.imshow("invert33" , img52)

# xu ly doan tong hop mul 
os.system('prostak.exe -o mul reconstruct33.tif,invert33.tif mul32.tif')
img53= cv2.imread("mul32.tif")
cv2.imshow("mul32" , img53)

os.system('prostak.exe -o gerosion -r 1 mul32.tif,strel2.txt gerosion34.tif')
img54= cv2.imread("gerosion34.tif")
cv2.imshow("gerosion34" , img54)
#invert 129
os.system('prostak.exe -o invert gerosion34.tif invert34.tif')
img55 = cv2.imread("invert34.tif")
cv2.imshow("invert34" , img55)

#tong hop mul 
os.system('prostak.exe -o mul invert34.tif,invert33.tif mul33.tif')
img56= cv2.imread("mul33.tif")
cv2.imshow("mul33" , img56)

#gerosion 111
os.system('prostak.exe -o strel -s 5,5,square strel34.txt')
os.system('prostak.exe -o gerosion -r 1 median1.tif,strel34.txt gerosion35.tif')
img57= cv2.imread("gerosion35.tif")
cv2.imshow("gerosion35" , img57)

os.system('prostak.exe -o gmag gerosion35.tif gmag32.tif')
img58 = cv2.imread("gmag32.tif")
cv2.imshow("gmag32" , img58)

os.system('prostak.exe -o shrink -p 0.5 gmag32.tif shrink32.tif')
img59 = cv2.imread("shrink32.tif")
cv2.imshow("shrink32" , img59)

os.system('prostak.exe -o shrink -p 0.5 mul33.tif shrink33.tif')
img60 = cv2.imread("shrink33.tif")
cv2.imshow("shrink33" , img60)

os.system('prostak.exe -o shrink -p 0.5 expand21.tif shrink31.tif')
img61 = cv2.imread("shrink31.tif")
cv2.imshow("shrink31" , img61)

os.system('prostak.exe -o movl -s white,magenta,pink shrink31.tif,shrink32.tif,shrink33.tif out.tif')
img62= cv2.imread("out.tif")
cv2.imshow("Out" , img62)



cv2.waitKey()

'''
def Process(image1 , image2 , image3):
    img1 = cv2.imread(image1)
    cv2.imshow("Input" , img1)


    os.system('prostak.exe -o threshold -p 10.0 -s otsu '+ image1 +' threshold1.tif,text_threshold.txt')
    print('prostak.exe -o threshold -p 10.0 -s otsu '+ image1 +' threshold1.tif,text_threshold.txt')
    img2 = cv2.imread("threshold1.tif")
    cv2.imshow("threshold1" , img2)

    os.system('prostak.exe -o mul threshold1.tif,'+image1+' mul1.tif')
    img3= cv2.imread("mul1.tif")
    cv2.imshow("mul1" , img3)

    os.system('prostak.exe -o heq mul1.tif,threshold1.tif heqm1.tif ')
    img4= cv2.imread("heqm1.tif")
    cv2.imshow("heqm1" , img4)

    os.system('prostak.exe -o andif -s 10,0.5,0.9,frac heqm1.tif andif1.tif')
    img5= cv2.imread("andif1.tif")
    cv2.imshow("andif1" , img5)

    os.system('prostak.exe -o expand -p 2.0 andif1.tif expand1.tif')
    img6= cv2.imread("expand1.tif")
    cv2.imshow("expand1" , img6)

    os.system('prostak.exe -o strel -s 9,9,square strel1.txt')
    os.system('prostak.exe -o gerosion -r 1 expand1.tif,strel1.txt gerosion1.tif')
    img7= cv2.imread("gerosion1.tif")
    cv2.imshow("gerosion1" , img7)

    os.system('prostak.exe -o reconstruct -r 4 expand1.tif,gerosion1.tif reconstruct1.tif')
    img8= cv2.imread("reconstruct1.tif")
    cv2.imshow("reconstruct1" , img8)


    os.system('prostak.exe -o invert reconstruct1.tif invert1.tif')
    img9 = cv2.imread("invert1.tif")
    cv2.imshow("invert1" , img9)

    os.system('prostak.exe -o gerosion -r 1 invert1.tif,strel1.txt gerosion2.tif')
    img10= cv2.imread("gerosion2.tif")
    cv2.imshow("gerosion2" , img10)


    os.system('prostak.exe -o reconstruct -r 4 invert1.tif,gerosion2.tif reconstruct2.tif')
    img11= cv2.imread("reconstruct2.tif")
    cv2.imshow("reconstruct2" , img11)


    os.system('prostak.exe -o cwtsd -r 4 reconstruct2.tif cwtsd1.tif')
    img12= cv2.imread("cwtsd1.tif")
    cv2.imshow("cwtsd1" , img12)


    os.system('prostak.exe -o mul cwtsd1.tif,expand1.tif mul2.tif')
    img13= cv2.imread("mul2.tif")
    cv2.imshow("mul2" , img13)

    os.system('prostak.exe -o threshold -p 3.0 -s plain mul2.tif threshold2.tif,text_threshold2.txt')
    img14= cv2.imread("threshold2.tif")
    cv2.imshow("threshold2" , img14)

    os.system('prostak.exe -o strel -s 3,3,square strel2.txt')
    os.system('prostak.exe -o gerosion -r 1 threshold2.tif,strel2.txt gerosion3.tif')
    img15= cv2.imread("gerosion3.tif")
    cv2.imshow("gerosion3" , img15)

    os.system('prostak.exe -o median -r 1 threshold2.tif,strel2.txt median1.tif')
    img16= cv2.imread("median1.tif")
    cv2.imshow("median1" , img16)

    os.system('prostak.exe -o gmag median1.tif gmag1.tif')
    img17= cv2.imread("gmag1.tif")
    cv2.imshow("gmag1" , img17)

    os.system('prostak.exe -o threshold -p 1.0 -s plain -r 1 gmag1.tif threshold3.tif,text_threshold3.txt')
    img18= cv2.imread("threshold3.tif")
    cv2.imshow("threshold3" , img18)

    os.system('prostak.exe -o expand -p 2.0 mul1.tif expand2.tif')
    img19= cv2.imread("expand2.tif")
    cv2.imshow("expand2" , img19)

    os.system('prostak.exe -o movl -s magenta,yellow threshold3.tif,expand2.tif movl1.tif')
    img20= cv2.imread("movl1.tif")
    cv2.imshow("movl1" , img20)


    ###xu ly dau vao t2

    img21 = cv2.imread(image2)
    cv2.imshow("Input2" , img21)

    os.system('prostak.exe -o expand -p 2.0 '+image2+' expand21.tif')
    img22= cv2.imread("expand21.tif")
    cv2.imshow("expand21" , img22)


    os.system('prostak.exe -o invert expand21.tif invert21.tif')
    img23 = cv2.imread("invert21.tif")
    cv2.imshow("invert21" , img23)

    os.system('prostak.exe -o heq invert21.tif heq21.tif')
    img24 = cv2.imread("heq21.tif")
    cv2.imshow("heq21" , img24)

    os.system('prostak.exe -o despekle -r 4 heq21.tif despekle21.tif')
    img25 = cv2.imread("despekle21.tif")
    cv2.imshow("despekle21" , img25)


    os.system('prostak.exe -o strel -s 3,3,square strel21.txt')
    os.system('prostak.exe -o gerosion -r 1 despekle21.tif,strel21.txt gerosion21.tif')
    img26 = cv2.imread("gerosion21.tif")
    cv2.imshow("gerosion21.tif" , img26)


    ###xu ly dau vao t3
    img31 = cv2.imread(image3)
    cv2.imshow("Input3" , img31)


    os.system('prostak.exe -o expand -p 2.0 '+image3+' expand31.tif')
    img32= cv2.imread("expand31.tif")
    cv2.imshow("expand31" , img32)

    os.system('prostak.exe -o heq expand31.tif heq31.tif')
    img33 = cv2.imread("heq31.tif")
    cv2.imshow("heq31" , img33)

    os.system('prostak.exe -o despekle -r 4 heq31.tif despekle31.tif')
    img34 = cv2.imread("despekle31.tif")
    cv2.imshow("despekle31" , img34)

    os.system('prostak.exe -o gerosion -r 1 despekle31.tif,strel21.txt gerosion31.tif')
    img35 = cv2.imread("gerosion31.tif")
    cv2.imshow("gerosion31.tif" , img35)

    ###gop xu ly anh 2 va 3 

    os.system('prostak.exe -o avg gerosion21.tif,gerosion31.tif avg2_1.tif')
    img36 = cv2.imread("avg2_1.tif")
    cv2.imshow("avg2_1.tif" , img36)

    os.system('prostak.exe -o andif -s 20,0.3,0.7,frac avg2_1.tif andif31.tif')
    img37= cv2.imread("andif31.tif")
    cv2.imshow("andif31" , img37)

    ###gerosion 52 _ giua hinh 2 va 3 
    os.system('prostak.exe -o strel -s 23,23,disk strel32.txt')
    os.system('prostak.exe -o gerosion -r 1 andif31.tif,strel32.txt gerosion32.tif')
    img38 = cv2.imread("gerosion32.tif")
    cv2.imshow("gerosion32.tif" , img38)
    #reconstruct 57
    os.system('prostak.exe -o reconstruct -r 4 andif31.tif,gerosion32.tif reconstruct31.tif')
    img39= cv2.imread("reconstruct31.tif")
    cv2.imshow("reconstruct31" , img39)

    #invert 54
    os.system('prostak.exe -o invert reconstruct31.tif invert31.tif')
    img40 = cv2.imread("invert31.tif")
    cv2.imshow("invert31" , img40)

    #gerosion 53
    os.system('prostak.exe -o gerosion -r 1 invert31.tif,strel32.txt gerosion33.tif')
    img41 = cv2.imread("gerosion33.tif")
    cv2.imshow("gerosion33.tif" , img41)
    #reconstruct 58
    os.system('prostak.exe -o reconstruct -r 4 invert31.tif,gerosion33.tif reconstruct32.tif')
    img42= cv2.imread("reconstruct32.tif")
    cv2.imshow("reconstruct32" , img42)

    os.system('prostak.exe -o strel -s 9,9,disk strel33.txt')
    os.system('prostak.exe -o gclose -r 7 reconstruct32.tif,strel33.txt gclose31.tif')
    img43 = cv2.imread("gclose31.tif")
    cv2.imshow("gclose31" , img43)

    #doan tach ra tu gmag
    os.system('prostak.exe -o gmag gclose31.tif gmag31.tif')
    img44= cv2.imread("gmag31.tif")
    cv2.imshow("gmag31" , img44)


    os.system('prostak.exe -o threshold -p 10.0 -s otsu gmag31.tif threshold31.tif,text_threshold31.txt')
    img45 = cv2.imread("threshold31.tif")
    cv2.imshow("threshold31" , img45)#hinh dau ra o cuoi cung 
    #


    os.system('prostak.exe -o invert median1.tif invert32.tif')
    img46 = cv2.imread("invert32.tif")
    cv2.imshow("invert32" , img46)
    #mul 122
    os.system('prostak.exe -o mul invert32.tif,gclose31.tif mul31.tif')
    img47= cv2.imread("mul31.tif")
    cv2.imshow("mul31" , img47)


    os.system('prostak.exe -o cwtsd -r 4 mul31.tif cwtsd31.tif')
    img48= cv2.imread("cwtsd31.tif")
    cv2.imshow("cwtsd31" , img48)






    #xu ly nhanh tren cua phan 3 bat dau tu reconstruct


    os.system('prostak.exe -o reconstruct -r 4 cwtsd31.tif,median1.tif reconstruct33.tif')
    img49= cv2.imread("reconstruct33.tif")
    cv2.imshow("reconstruct33" , img49)




    #xu ly nhanh duoi cua phan 3 bat dau tu minusabs 
    os.system('prostak.exe -o minusabs reconstruct33.tif,cwtsd31.tif minusabs31.tif')
    img50 = cv2.imread("minusabs31.tif")
    cv2.imshow("minusabs31" , img50)

    os.system('prostak.exe -o gclose -r 1 minusabs31.tif,strel2.txt gclose32.tif')
    img51 = cv2.imread("gclose32.tif")
    cv2.imshow("gclose32" , img51)
    #invert137
    os.system('prostak.exe -o invert gclose32.tif invert33.tif')
    img52 = cv2.imread("invert33.tif")
    cv2.imshow("invert33" , img52)

    # xu ly doan tong hop mul 
    os.system('prostak.exe -o mul reconstruct33.tif,invert33.tif mul32.tif')
    img53= cv2.imread("mul32.tif")
    cv2.imshow("mul32" , img53)

    os.system('prostak.exe -o gerosion -r 1 mul32.tif,strel2.txt gerosion34.tif')
    img54= cv2.imread("gerosion34.tif")
    cv2.imshow("gerosion34" , img54)
    #invert 129
    os.system('prostak.exe -o invert gerosion34.tif invert34.tif')
    img55 = cv2.imread("invert34.tif")
    cv2.imshow("invert34" , img55)

    #tong hop mul 
    os.system('prostak.exe -o mul invert34.tif,invert33.tif mul33.tif')
    img56= cv2.imread("mul33.tif")
    cv2.imshow("mul33" , img56)

    #gerosion 111
    os.system('prostak.exe -o strel -s 5,5,square strel34.txt')
    os.system('prostak.exe -o gerosion -r 1 median1.tif,strel34.txt gerosion35.tif')
    img57= cv2.imread("gerosion35.tif")
    cv2.imshow("gerosion35" , img57)

    os.system('prostak.exe -o gmag gerosion35.tif gmag32.tif')
    img58 = cv2.imread("gmag32.tif")
    cv2.imshow("gmag32" , img58)

    os.system('prostak.exe -o shrink -p 0.5 gmag32.tif shrink32.tif')
    img59 = cv2.imread("shrink32.tif")
    cv2.imshow("shrink32" , img59)

    os.system('prostak.exe -o shrink -p 0.5 mul33.tif shrink33.tif')
    img60 = cv2.imread("shrink33.tif")
    cv2.imshow("shrink33" , img60)

    os.system('prostak.exe -o shrink -p 0.5 expand21.tif shrink31.tif')
    img61 = cv2.imread("shrink31.tif")
    cv2.imshow("shrink31" , img61)

    os.system('prostak.exe -o movl -s white,magenta,pink shrink31.tif,shrink32.tif,shrink33.tif out.tif')
    img62= cv2.imread("out.tif")
    cv2.imshow("Out" , img62)



    cv2.waitKey()
    return img62


Out = Process("d218.tif","f218.tif" , "r218.tif")
cv2.imshow("Out" , Out)
cv2.waitKey()