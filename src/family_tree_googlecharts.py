import member

def get_pre_part_old():
    pre_part = """<html>
                        <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />

                         <head>
                           <script type="text/javascript" src="../js/loader.js"></script>
                           <script type="text/javascript">
                             google.charts.load('current', {packages:["orgchart"]});
                             google.charts.setOnLoadCallback(drawChart);
                 """
    return pre_part

def get_pre_part():
    pre_part = """<html>
                        <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />

                         <head>  
   <script type='text/javascript' src='../js/jsapi'></script>  
   <script type='text/javascript'>  
    google.load('visualization', '1', {packages:['orgchart']});  
    google.setOnLoadCallback(drawChart);  
                 """
    return pre_part


def draw_node(member_id, member_dict, records):
    member_obj = member_dict.get(member_id)
    if member_obj is None:
        print("member_id:{member_id} not exist".format(member_id = member_id))
        return

    member_node  = MemberNode()
    #father_id = member_obj.father_id if member_obj.father_id is not None else ""
    spouse_name = member_obj.spouse_name
    if spouse_name is None or spouse_name == '':
        spouse_name = "&nbsp"
    bgcolor = "#AFEEEE" if member_obj.sex == 1 else "##FFFAF0"
    print("in draw_node() member_name is {member_name}".format(member_name=member_obj.member_name))
    record = [{'v': str(member_id),
                'f': "<table width=100%  align=center border=1px bordercolor=black bgcolor="+bgcolor+">" +
                        "<tr><th nowrap>" + member_obj.member_name + "</th></tr>" +
                        "<tr><th>" + str(member_obj.descent_no) + "</th></tr>" +
                        "<tr><th nowrap>" + spouse_name + "</th></tr>"
                    "</table>"
               },
              str(father_id),
              '']
    records.append(record)
    member_obj.sons_list.sort(key=lambda m_id:member_dict.get(m_id).order_seq)
    for son_member_id in member_obj.sons_list[::-1]:
        draw_node(son_member_id, member_dict, records)


def get_nodes(member_dict):
    records = []
    draw_node(1, member_dict, records)
    return str(records)


def get_data_part(member_dict):
    data_part = """ function drawChart() {
                        var data = new google.visualization.DataTable();
                        data.addColumn('string', 'Member');
                        data.addColumn('string', 'Father');
                        data.addColumn('string', 'ToolTip');

                        data.addRows(""" + get_nodes(member_dict) + """);"""
    return data_part


def get_post_part():
    post_part = """
                // Create the chart.
                var chart_div = document.getElementById('chart_div');
                var chart = new google.visualization.OrgChart(chart_div);    

                // Draw the chart, setting the allowHtml option to true for the tooltips.
                chart.draw(data, {allowHtml:true,allowCollapse:true});
                      }
                   </script>
                    </head>
                  <body>
                    <div id="chart_div"></div>
                  </body>
                </html>
                """
    return post_part


def draw_tree(member_dict):
    pre_part = get_pre_part()
    data_part = get_data_part(member_dict)
    post_part = get_post_part()

    html_content = pre_part + data_part + post_part
    file = open("../data/google_tree.html", "w", encoding='UTF-8')
    file.write(html_content)
    file.close()
