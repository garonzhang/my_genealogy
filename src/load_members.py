from dbmanager import DbManager
from member import Member


def load_members():
    member_dict = {}

    db_manager = DbManager()
    cur = db_manager.conn.cursor()
    cur.execute("SELECT member_id,\
                        member_name,\
                        descent_no,\
                        sex,\
                        spouse_name,\
                        father_id,\
                        order_seq,\
                        step_father_id, \
                        step_order_seq,\
                        career,\
                        description,\
                        spouse_description "
                "from tb_members "
                "where descent_no < 30 and descent_no >0")
    for r in cur:
        member_id = r[0]

        # 获得当前 member 的对象实体。
        # 若不存在，则创建，同时将其存储入 member 词典中
        member_obj = member_dict.get(member_id, None)
        if member_obj is None:
            member_obj = Member(member_id)
            member_dict[member_obj.member_id] = member_obj

        # 更新 member 实体的其余属性，用来应对根据儿子而被动产生的父亲对象的更新
        member_obj.member_name = r[1] if len(r[1]) > 3 or r[1][0:1] != '张' else r[1][1:]
        member_obj.descent_no = r[2]
        member_obj.sex = r[3]
        member_obj.spouse_name = r[4]

        if r[7] is not None:
            father_id = r[7]
            order_seq = r[8]
        else:
            father_id = r[5]
            order_seq = r[6]
        member_obj.career = r[9]
        member_obj.description = r[10]
        member_obj.spouse_description = r[11]
        member_obj.father_id = father_id
        member_obj.order_seq = order_seq if order_seq is not None else 1
        #print(member_obj.order_seq)

        # 将当前 member 对象的 member_id 挂载至其父亲对象上
        if member_obj.father_id is None:
            continue
        father_obj = member_dict.get(member_obj.father_id, None)
        if father_obj is None:
            father_obj = Member(member_obj.father_id)
            member_dict[father_obj.member_id] = father_obj
        father_obj.add_son(member_id)

    cur.close()
    db_manager.close()

    return member_dict
