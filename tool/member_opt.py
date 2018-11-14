from member import Member
import csv

def get_order(dict, father_id):
    father_obj = dict.get(father_id)
    if father_obj is None:
        print("father_id",father_id)
        return -1

    sons_info = father_obj.sons_info
    sons = sons_info.split(";")
    sons = [item.split(":")[0] for item in sons]
    if member_name in sons:
        return sons.index(member_name)+1
    else:
        print("ERROR")
        return -2

if __name__ == "__main__":
    dict = {}
    #打开文件，用with打开可以不用去特意关闭file了，python3不支持file()打开文件，只能用open()
    with open("../data/test.csv","r",encoding="utf-8") as csvfile:
         #读取csv文件，返回的是迭代类型
         read = csv.reader(csvfile)
         for i in read:
             member_obj = Member(i[0],i[1],i[2],i[3],i[4])
             dict[i[0]] = member_obj

    for key, member_obj in dict.items():
        member_id = member_obj.member_id
        member_name = member_obj.member_name

        father_id = member_obj.father_id
        if father_id == "":
            order = ""
        else:
            order = get_order(dict, father_id)

        step_father_id = member_obj.step_father_id
        if step_father_id == "":
            step_order = ""
        else:
            step_order = get_order(dict, step_father_id)
        print(member_id+","+member_name+","+str(order)+","+str(step_order))
