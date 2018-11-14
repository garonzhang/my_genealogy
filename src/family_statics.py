from load_members import load_members
from collections import defaultdict


def wife_static(member_dict):
    first_name_dict = defaultdict(int)

    for member_id, member in member_dict.items():
        spouse_name = member.spouse_name if member.spouse_name is not None else ''
        wife_list  = spouse_name.split(";")
        if wife_list == []:
            continue

        for wife_item in wife_list:
            if wife_item == "":
                continue
            wife_first_name = wife_item[:1]
            first_name_dict[wife_first_name] += 1

    for k,v in first_name_dict.items():
        print("['"+k+"',"+str(v) +"],")


if __name__ == "__main__":
    member_dict = load_members()
    wife_static(member_dict)

