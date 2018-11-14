from member import Member
from treelib import Node, Tree
from load_members import load_members


def draw_tree(member_dict):
    tree = Tree()
    tree.create_node('张伍陆', 1)  # root node

    for member_id, member_obj in member_dict.items():
        print(member_obj.member_name)
        if member_id == 1:
            continue
        if member_obj.father_id is not None:
            if tree.get_node(member_obj.father_id) is None:
                print("not find")
                continue
            tree.create_node(member_obj.member_name, member_id,father=member_obj.father_id)

    tree.save2file("../data/tree_out")

