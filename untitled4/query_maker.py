list = ["CS","EE","ME","CE","IE","CH","BZ","DE","PH"]
building=["Sang","Gong","Mun","Med","Ground"]
school = ["Yonsei","Korea","Seoul","Po","Kai","Hangyang"]
hobby = ["soccer","Sing","ComputerGame","basketball"]
nation = ["Korea","japan","china","USA","UK","Taiwan","TridadTobacco"]
home = ["Georgia","Beijing","Hongkong","Shanghai","morroco","Kairo","Paris","Guam"]

with open("sample_query_v3","w") as text_file:
    for i in range(1000):
        text_file.write("CREATE TABLE student%d (name CHAR, age INT, dept CHAR, grade INT,building char,school char, numberFamiliy int, hobby char,nationality char, expected_age int,home char);\n" %i)
        for j in range(10):
            idx_list = j%9
            idx_b = j%5
            idx_s = j%6
            idx_h = j%4
            idx_n = j%7
            idx_home = j%8
            text_file.write('INSERT INTO student%d VALUES ("kimjihyeok%d",'%(i,j)+str(j)+',"'+list[idx_list]+'",'+str(100+j)+',"'+building[idx_b]+'",'+'"'+school[idx_s]+'",'+str(5)+',"'+hobby[idx_h]+'","'+nation[idx_n]+'",'+
                            str(j+100)+',"'+home[idx_home]+'"'+");\n")

text_file.close()