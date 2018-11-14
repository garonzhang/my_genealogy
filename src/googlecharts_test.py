def get_pre_part():
    pre_part = """<html>
                        <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
                         <head >
                           <script type="text/javascript" src="https://www.gstatic.com/charts/loader.js"></script>
                           <script type="text/javascript">
                             google.charts.load('current', {packages:["orgchart"]});
                             google.charts.setOnLoadCallback(drawChart);
                 """
    return pre_part


def get_data_part():
    data_part = """
                      function drawChart() {
                        var data = new google.visualization.DataTable();
                        data.addColumn('string', 'Name');
                        data.addColumn('string', 'Manager');
                        data.addColumn('string', 'ToolTip');

                        // For each orgchart box, provide the name, manager, and tooltip to show.
                        data.addRows([
                          [{v:'1', f:'张伍陆'},'', ''],
                          [{v:'2', f:'张亨'},'1', 'VP'],
                          [{v:'3', f:'张兴'}, '1', ''],
                          [{v:'4', f:'Bob'}, '2', ''],
                          [{v:'5', f:'Carol'}, '4', '']
                        ]);
                     """
    return data_part


def get_post_part():
    post_part = """
                        // Create the chart.
                        var chart = new google.visualization.OrgChart(document.getElementById('chart_div'));
                        // Draw the chart, setting the allowHtml option to true for the tooltips.
                        chart.draw(data, {allowHtml:true});
                      }
                   </script>
                    </head>
                  <body>
                    <div id="chart_div"></div>
                  </body>
                </html>
                """
    return post_part


if __name__ == "__main__":
    pre_part = get_pre_part()
    data_part = get_data_part()
    post_part = get_post_part()

    html_content = pre_part + data_part + post_part
    print(html_content)
    #html_content="彰武路"
    file= open("../data/google_tree.html","w", encoding='UTF-8')
    file.write(html_content)
    file.close()
