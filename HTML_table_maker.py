import os

# takes number  of rows and columns, returns a blank html table
def make_HTML_table(rows, cols):
    table ='<table> \n'
    for row in range(rows):
        table += "  <tr>\n"
        for col in range(cols):
            if col == 0:
                table += "    <td></td>"
            else:
                table += "<td></td>"
        table += "\n  </tr>\n"
    return table

#
def data_2_HTMLrow(data=[]):
    output = ''
    for i in range(len(data)):
        output += ('<td>'+str(data[i])+'</td>')
    return output


def put_data_in_table_cell(cell='<td></td>', dataIn=None):
    if cell == '<td></td>':
        return '<td>'+str(dataIn)+'</td>'
    else:
        if cell.count("td") != 2:
            pass #need to raise error
        elif (True):
            #add other error checking
            pass
    if not (cell.find("><")):
        #handle cell with existing data
        pass
    open_tag = cell[0:cell.find(">")+1]
    close_tag = cell[cell.find("</"):]
    # inbetween_stuff = cell[cell.find(">")+1:cell.find("</")]
    return open_tag+str(dataIn)+close_tag


def HTMLrow_2_list(input_row):
    cells = input_row("</td>")


# def fill_table_row(input_HTMLrow, data=[]):
    #
    # if len(data) == 0:
    #     return input_HTMLrow
    # else:
    #     num_td_tags = input_HTMLrow.count("td")
    #     num_fields = num_td_tags/2
    #     for
    #
    #     for item in range(len(data)):
    #         input_row[item] = data[item]
    # return input_row

# print(make_HTML_table(4,4))

# in_row = "<td></td><td></td><td></td><td></td>"

# print(data_2_row([]))

x = put_data_in_table_cell("<td>4</td", 5)
print("hello", x)