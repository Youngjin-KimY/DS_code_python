list = ["CS","EE","ME","CE","IE","CH","BZ","DE","PH"]

with open("sample_query","w") as text_file:
    for i in range(20000):
        text_file.write("CREATE TABLE student%d (name CHAR, age INT, dept CHAR, grade INT);\n" %i)
        for j in range(10):
            idx = j%9
            text_file.write('INSERT INTO student%d VALUES ("kimjihyeok%d",'%(i,j)+str(j)+',"'+list[idx]+'",'+str(100+j)+");\n")

text_file.close()