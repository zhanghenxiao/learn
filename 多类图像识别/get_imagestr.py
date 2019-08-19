from PIL import Image
import pytesseract
import re,cv2

# https://ocr.wdku.net/ 在线文字识别转换
"""
text = pytesseract.image_to_string(Image.open("./pic/mefw.png"))
print(text)
#res = re.findall('^(?=.*\d)(?=.*[a-zA-Z])(?=.*[\u4E00-\u9FA5])[\u4E00-\u9FA5A-Za-z0-9]*$',text)
res = re.findall(r'([a-zA-Z])',text)
#print(res)
wenzi = ''.join(res)
print(wenzi)
"""

#二值化
"""
s = cv2.imread("./482.png",cv2.IMREAD_GRAYSCALE)  #二值化处理
threshold, crop = cv2.threshold(s, 0, 255, cv2.THRESH_OTSU)
cv2.imshow('test',crop)
cv2.waitKey(0)
text = pytesseract.image_to_string(crop)
print(text)
"""

# s1 = "01070812180307"
# s2 = "04121323310410"
# s3 = "01020415170412"
# s4 = "01093234350508"
# s5 = "07163227351012"
# txt = [s1,s2,s3,s4,s5]
# for i in txt:
#     print(re.findall('[0-9][0-9]',i))
test = ['12', '31', '3','19', '17', '2', '6']   #中奖号码

four82 = ['04', '05', '07', '11', '27', '01', '06']
nine70 = ['08', '18', '22', '24', '33', '04', '05']
seven78= ['01', '07', '22', '12', '63', '20', '30']
there241 = ['01', '12', '13', '14', '27', '04', '05']
there242 = ['12', '20', '25', '29', '31', '02', '08']
eight561= ['05', '15', '20', '30', '31', '04', '07']
eight562= ['05', '08', '15', '23', '24', '06', '11']

six801 = ['06', '07', '10', '25', '35', '01', '02']
six802 = ['05', '09', '16', '19', '31', '05', '07']
six803 = ['08', '24', '25', '27', '28', '00', '30']
six804 = ['01', '04', '18', '32', '35', '01', '05']
six805 = ['08', '22', '24', '31', '34', '02', '11']

four921 = ['08', '09', '14', '22', '27', '09', '10']
four922 = ['18', '21', '25', '28', '31', '01', '09']
four923 = ['08', '13', '20', '24', '30', '09', '12']
four924 = ['10', '15', '19', '22', '35', '07', '10']
four925 = ['09', '16', '25', '28', '33', '08', '11']

one891 = ['08', '15', '17', '26', '30', '08', '09']
one892 = ['05', '08', '11', '17', '25', '06', '10']
one893 = ['10', '23', '24', '26', '33', '01', '06']
one894 = ['03', '10', '11', '20', '26', '03', '07']
one895 = ['13', '14', '17', '32', '34', '01', '04']

one331 = ['01', '07', '08', '12', '18', '03', '07']
one332 = ['04', '12', '13', '23', '31', '04', '10']
one333 = ['01', '02', '04', '15', '17', '04', '12']
one334 = ['01', '09', '32', '34', '35', '05', '08']
one335 = ['07', '16', '32', '27', '35', '10', '12']

alllist = [four82,nine70,seven78,there241,there242,eight561,eight562,
           six801,six802,six803,six804,six805,
           four921,four922,four923,four924,four925,
           one891,one892,one893,one894,one895,
           one331,one332,one333,one334,one335]
for i in alllist:
    print(i)
    hong = (list(set(i[:5]).intersection(set(test[:5]))))
    lang = (list(set(i[5:7]).intersection(set(test[5:7]))))
    print(len(hong),len(lang))
    print( "红球对上%s组"%len(hong),"蓝球对上%s组========="%len(lang))

#奖项设置
    if len(hong) == 5 and len(lang) == 2:
        print(i,"一等奖 哈哈哈哈")
    elif len(hong) == 5 and len(lang) == 1:
        print(i,"二等奖 哈哈哈哈")
    elif len(hong) == 5 and len(lang) == 0:
        print(i, "三等奖 哈哈哈哈")
    elif len(hong) == 4 and len(lang) == 2:
        print(i,"四等奖 哈哈哈哈")
    elif len(hong) == 4 and len(lang) == 1:
        print(i, "五等奖 哈哈哈哈")
    elif len(hong) == 3 and len(lang) == 2:
        print(i, "六等奖 哈哈哈哈")
    elif len(hong) == 4 and len(lang) == 0:
        print(i,"七等奖 哈哈哈哈")
    elif len(hong) == 3 and len(lang) == 1:
        print(i, "八等奖 哈哈哈哈")
    elif len(hong) == 2 and len(lang) == 2:
        print(i, "八等奖 哈哈哈哈")
    elif len(hong) == 3 and len(lang) == 0:
        print(i, "九等奖 哈哈哈哈")
    elif len(hong) == 1 and len(lang) == 2:
        print(i, "九等奖 哈哈哈哈")
    elif len(hong) == 2 and len(lang) == 1:
        print(i, "九等奖 哈哈哈哈")
    elif len(lang) == 2 and len(lang) == 0:
        print(i, "九等奖 哈哈哈哈")
