
class Member:
    def __init__(self,member_id):
        self.member_id = member_id
        self.sons_list = []

    def add_son(self, son_id):
        self.sons_list.append(son_id)

class MemberNode:
    def __init__(self,member_id, member_name, sex, descent_no,spouse_name, className):
        """

        :rtype:
        """
        self.member_id = member_id
        self.member_name = member_name
        self.sex = sex
        self.descent_no = descent_no
        self.spouse_name = spouse_name
        self.children = []
        self.className = className

    def add_son(self, child_node):
        self.children.append(child_node)