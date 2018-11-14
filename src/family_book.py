from queue import Queue


def get_chinese_number(number):
    if number == 1:
        return "一"
    elif number == 2:
        return "两"
    elif number == 3:
        return "三"
    elif number == 4:
        return "四"
    elif number == 5:
        return "五"
    elif number == 6:
        return "六"
    elif number == 7:
        return "七"
    elif number == 8:
        return "八"
    elif number == 9:
        return "九"
    elif number == 10:
        return "十"
    elif number == 11:
        return "十一"
    elif number == 12:
        return "十二"
    elif number == 13:
        return "十三"
    elif number == 14:
        return "十四"


def gen_book(member_dict, first_member_id, file_name):
    member_queue = Queue()

    member_obj = member_dict.get(first_member_id)
    if member_obj is None:
        print("member_id:{member_id} not exist".format(member_id=first_member_id))
        return

    file = open(file_name, "w", encoding='UTF-8')
    member_queue.put(member_obj)
    cur_descent_no = member_obj.descent_no
    file.write("## 第" + str(member_obj.descent_no) + '世\n')

    while not member_queue.empty():
        record_content = ""
        member_obj = member_queue.get()

        if member_obj.descent_no != cur_descent_no:
            record_content += "## 第"+str(member_obj.descent_no) + "世\n"
            print(member_obj.member_name)
            cur_descent_no = member_obj.descent_no

        record_content += "**<font size=4>" + member_obj.member_name + "</font>** <font size=3>"
        sex = "" if member_obj.sex == 1 else "女"

        if member_obj.sex == 0:
            record_content += "女，"

        # 父母
        father_id = member_obj.father_id
        father_obj = member_dict.get(father_id)
        if father_obj is None:
            print("111member_id:{member_id} not exist".format(member_id=father_id))
        else:
            if father_obj.sex == 1:
                father_name = father_obj.member_name
                mother_name = father_obj.spouse_name
            else:
                father_name = father_obj.spouse_name
                mother_name = father_obj.member_name
            if father_name is None:
                father_name = ""
            if mother_name is None:
                mother_name = ""

            record_content += "父" + father_name
            if mother_name != "":
                record_content += "，母" + mother_name.replace(";", "、")
            record_content += "，"

        # 配偶
        spouse_label = "妻" if member_obj.sex == 1 else '夫'
        if member_obj.spouse_name is not None:
            if member_obj.spouse_name.strip() != "":
                record_content += spouse_label+ member_obj.spouse_name.replace(";", "、") +"，"
        # 子女
        sons_list = member_obj.sons_list
        son_count  = 0
        daughter_count = 0

        if sons_list is None:
            continue
        son_member_list = []
        for son_member_id in sons_list:
            son_member_obj = member_dict.get(son_member_id)
            if son_member_obj is None:
                print("member_id:",son_member_id,"not exist")
                continue
            son_member_list.append(son_member_obj)

            if son_member_obj.sex == 1:
                son_count += 1
            else:
                daughter_count += 1

        son_member_list = sorted(son_member_list, key = lambda son: son.order_seq)
        son_names = ""
        for son_member_obj in son_member_list:
            member_queue.put(son_member_obj)
            son_names = son_names + son_member_obj.member_name
            if son_member_obj.sex == 0:
                son_names = son_names + "(女)"
            son_names = son_names + " "
        if son_names != "":
            record_content += "有"
            if son_count != 0:
                record_content += "{0}子".format(get_chinese_number(son_count))
            if daughter_count != 0:
                record_content += "{0}女".format(get_chinese_number(daughter_count))
            record_content += "：" + son_names[:-1].replace(" ", "、")

        if record_content[-1] == "，":
            record_content = record_content[:-1]
        record_content += "。"

        # 职业
        introduction = ""

        if member_obj.career is not None:
            if member_obj.career.strip() != "":
                introduction = member_obj.career
        # 描述
        if member_obj.description is not None:
            if member_obj.description.strip() != "":
                if introduction != "":
                    introduction += "，"
                introduction += member_obj.description
        if introduction != "":
            if introduction[-1] != "。":
                introduction = introduction + "。"
            record_content += introduction

        # 其配偶描述
        spouse_introduction = ""
        if member_obj.spouse_description is not None:
            spouse_introduction = member_obj.spouse_description.strip()

        if spouse_introduction != "":
            if spouse_introduction[-1] != "。":
                spouse_introduction = spouse_introduction + "。"
            if member_obj.sex == 0:
                record_content += "其夫系" + spouse_introduction
            else:
                record_content += "其妻系" + spouse_introduction

        record_content += "</font>"

        file.write(record_content + "\n")

    file.close()


