from database import Database

db = Database('smdb', load=True)

#def full_outer(left_table, right_table, column_left_table, column_right_table, condition = '=='):
    #db.full_outer(left_table, right_table, column_left_table+condition+column_right_table)

def left_outer(left_table, right_table, column_left_table, column_right_table, condition = '=='):
    db.left_outer(left_table, right_table, column_left_table+condition+column_right_table)

def right_outer(left_table, right_table, column_left_table, column_right_table, condition = '=='):
    db.right_outer(left_table, right_table, column_left_table+condition+column_right_table)