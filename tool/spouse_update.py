import csv


def process_one(member_id, spouse_name, descent_no):
    spouse_list = spouse_name.split(";")
    if int(descent_no) < 10:
        spouse_list.reverse()

    spouses = ""
    for spouse in spouse_list:
        if spouse == '氏':
            spouses += ";"
            continue

        if len(spouse) == 1:
            spouses += spouse +"氏"+";"
        else:
            spouses += spouse +";"
    spouses = spouses[:-1]
    print(member_id +"," + spouses )


if __name__ == "__main__":
    dict = {}
    #打开文件，用with打开可以不用去特意关闭file了，python3不支持file()打开文件，只能用open()
    with open("../data/spouse.csv","r",encoding="utf-8") as csvfile:
         #读取csv文件，返回的是迭代类型
         read = csv.reader(csvfile)
         for i in read:
             process_one(i[0],i[1],i[2])


