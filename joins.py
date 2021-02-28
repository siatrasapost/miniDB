from database import Database

db = Database('smdb', load=True)

def full_outer(left_table, right_table, column_left_table, column_right_table, condition = '=='):
    #db.inner_join(left_table, right_table,'dept_name==dept_name')
    #db.inner_join(left_table, right_table,column_left_table+condition+column_right_table)
    db.full_outer(left_table, right_table, column_left_table+condition+column_right_table)

def left_outer(left_table, right_table, column_left_table, column_right_table, condition = '=='):
    db.left_outer(left_table, right_table, column_left_table+condition+column_right_table)