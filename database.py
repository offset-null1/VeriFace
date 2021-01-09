#!/usr/bin/python3
from backend.mysqlConnector import MysqlConnector
conn = MysqlConnector()

# conn.insert(execute=True, tableName='students', column={'usn': "'1SK18CS053'", 'fname': "'Dakshta'",    'lname': "'Tomar'  " ,'email':  "'dakshta@gmail.com'  "  ,'phone_no':  "'1234567891' ", 'sem':'5', 'branch': "'CSE'"  })
# conn.insert(execute=True, tableName='students', column={'usn': "'1SK18CS001'", 'fname': "'Aish'",       'lname': "'Singh'  " ,'email':  "'aish@gmail.com'     "  , 'phone_no': "'1234568881' ", 'sem':'5', 'branch': "'CSE'"  })
# conn.insert(execute=True, tableName='students', column={'usn': "'1SK20EC053'", 'fname': "'Ishika'",     'lname': "'Singh'  " ,'email':  "'ishi@gmail.com'     "  , 'phone_no': "'125567891'  ", 'sem':'2', 'branch': "'ECE'"  })
# conn.insert(execute=True, tableName='students', column={'usn': "'1SK18EC002'", 'fname': "'Shim'",       'lname': "'LA'     " ,'email':  "'shim@gmail.com'     "  ,'phone_no':  "'3334567891' ", 'sem':'5', 'branch': "'ECE'"  })
# conn.insert(execute=True, tableName='students', column={'usn': "'1SK18ME053'", 'fname': "'Daksh'",      'lname': "'A'      " ,'email':  "'daksh@gmail.com'    "  , 'phone_no': "'1134567891' ", 'sem':'1', 'branch': "'ME' "  })
# conn.insert(execute=True, tableName='students', column={'usn': "'1SK18CS003'", 'fname': "'Div'",        'lname': "'M'      " ,'email':  "'div@gmail.com'      "  , 'phone_no': "'1234567882' ", 'sem':'3', 'branch': "'CSE'"  })
# conn.insert(execute=True, tableName='students', column={'usn': "'1SK18CS004'", 'fname': "'Soum'",       'lname': "'N'      " ,'email':  "'soum@gmail.com'     "  , 'phone_no': "'1235567891' ", 'sem':'6', 'branch': "'CSE'"  })
# conn.insert(execute=True, tableName='students', column={'usn': "'1SK18CS005'", 'fname': "'Somya'",      'lname': "'Sain'   " ,'email':  "'somya@gmail.com'    "  , 'phone_no': "'1234888891' ", 'sem':'1', 'branch': "'CSE'"  })
# conn.insert(execute=True, tableName='students', column={'usn': "'1SK18CS006'", 'fname': "'Harley'",     'lname': "'Qinn'   " ,'email':  "'harley@gmail.com'   "  , 'phone_no': "'1234577891' ", 'sem':'5', 'branch': "'CSE'"  })
# conn.insert(execute=True, tableName='students', column={'usn': "'1SK18CS007'", 'fname': "'Shaily'",     'lname': "'Tanwar' " ,'email':  "'shaily@gmail.com'   "  , 'phone_no': "'1114567891' ", 'sem':'5', 'branch': "'CSE'"  })
# conn.insert(execute=True, tableName='students', column={'usn': "'1SK18CS008'", 'fname': "'Garima'",     'lname': "'Singh'  " ,'email':  "'garima@gmail.com'   "  , 'phone_no': "'1234667891' ", 'sem':'5', 'branch': "'CSE'"  })
# conn.insert(execute=True, tableName='students', column={'usn': "'1SK18CS009'", 'fname': "'Aishwarya'",  'lname': "'Ashtkar'" ,'email':  "'aishwarya@gmail.com'"  , 'phone_no': "'1111117891' ", 'sem':'5', 'branch': "'CSE'"  })
# conn.insert(execute=True, tableName='students', column={'usn': "'1SK18CS052'", 'fname': "'Jasmine'",    'lname': "'Jaz'    " ,'email':  "'jasmin@gmail.com'   "  , 'phone_no': "'1234566666' ", 'sem':'5', 'branch': "'CSE'"  })

# conn.insert(execute=True, tableName='students', column={'usn': "'1SK18CS0012'", 'fname': "'Somebody'",     'lname': "'T' " ,'email':  "'somebody@gmail.com'   "  , 'phone_no': "'1114567891' ", 'sem':'5', 'branch': "'CSE'"  })
# conn.insert(execute=True, tableName='students', column={'usn': "'1SK18CS0013'", 'fname': "'Alle'",     'lname': "'A' " ,'email':  "'alle@gmail.com'   "  , 'phone_no': "'1114567891' ", 'sem':'5', 'branch': "'CSE'"  })
# conn.insert(execute=True, tableName='students', column={'usn': "'1SK18CS0014'", 'fname': "'shaile'",     'lname': "'B' " ,'email':  "'shaile@gmail.com'   "  , 'phone_no': "'1114562891' ", 'sem':'5', 'branch': "'CSE'"  })
# conn.insert(execute=True, tableName='students', column={'usn': "'1SK18CS0015'", 'fname': "'Ishu'",     'lname': "'C' " ,'email':  "'ishu@gmail.com'   "  , 'phone_no': "'1114333331' ", 'sem':'5', 'branch': "'CSE'"  })
# conn.insert(execute=True, tableName='students', column={'usn': "'1SK18CS0016'", 'fname': "'Wazr'",     'lname': "'D' " ,'email':  "'wazr@gmail.com'   "  , 'phone_no': "'1114561891' ", 'sem':'5', 'branch': "'CSE'"  })
# conn.insert(execute=True, tableName='students', column={'usn': "'1SK18CS0017'", 'fname': "'Lemon'",     'lname': "'E' " ,'email':  "'lemon@gmail.com'   "  , 'phone_no': "'1111567891' ", 'sem':'5', 'branch': "'CSE'"  })
# conn.insert(execute=True, tableName='students', column={'usn': "'1SK18CS0018'", 'fname': "'All'",     'lname': "'F' " ,'email':  "'all@gmail.com'   "  , 'phone_no': "'1114567161' ", 'sem':'5', 'branch': "'CSE'"  })
# conn.insert(execute=True, tableName='students', column={'usn': "'1SK18CS0019'", 'fname': "'Kitty'",     'lname': "'G' " ,'email':  "'kitty@gmail.com'   "  , 'phone_no': "'1117267891' ", 'sem':'5', 'branch': "'CSE'"  })


# conn.insert(execute=True, tableName='semesters', column={'sub_id': "'18CS51'", 'sub_name': "'Management Entrepreneur for IT Industry'",    'sem_id': '5' ,'branch':  "'CSE'   "  , 'branch_name': "'Computer Science' " , 'lab': '0', 'proj':'0'})
# conn.insert(execute=True, tableName='semesters', column={'sub_id': "'18CS52'", 'sub_name': "'Computer Networks and Security'",    'sem_id': '5' ,'branch':  "'CSE'   "  , 'branch_name': "'Computer Science' "          , 'lab': '0', 'proj':'0'})
# conn.insert(execute=True, tableName='semesters', column={'sub_id': "'18CS53'", 'sub_name': "'Database Management system'",    'sem_id': '5' ,'branch':  "'CSE'   "  , 'branch_name': "'Computer Science' "              , 'lab': '0', 'proj':'0'})
# conn.insert(execute=True, tableName='semesters', column={'sub_id': "'18CS54'", 'sub_name': "'Automata Theory and Computability'",    'sem_id': '5' ,'branch':  "'CSE'   "  , 'branch_name': "'Computer Science' "       , 'lab': '0', 'proj':'0'})
# conn.insert(execute=True, tableName='semesters', column={'sub_id': "'18CS55'", 'sub_name': "'Application Development using Python'",    'sem_id': '5' ,'branch':  "'CSE'   "  , 'branch_name': "'Computer Science' "    , 'lab': '0', 'proj':'0'})
# conn.insert(execute=True, tableName='semesters', column={'sub_id': "'18CS56'", 'sub_name': "'Unix Programming'",    'sem_id': '5' ,'branch':  "'CSE'   "  , 'branch_name': "'Computer Science' "    , 'lab': '0', 'proj':'0'})
# conn.insert(execute=True, tableName='semesters', column={'sub_id': "'18CS57'", 'sub_name': "'Computer Network laboratory'",    'sem_id': '5' ,'branch':  "'CSE'   "  , 'branch_name': "'Computer Science' "    , 'lab': '1', 'proj':'0'})
# conn.insert(execute=True, tableName='semesters', column={'sub_id': "'18CS58'", 'sub_name': "'DBMS laboratory with mini project'",    'sem_id': '5' ,'branch':  "'CSE'   "  , 'branch_name': "'Computer Science' "    , 'lab': '1', 'proj':'1'})
# conn.insert(execute=True, tableName='semesters', column={'sub_id': "'18CIV58'", 'sub_name': "'Environmental Studies '",    'sem_id': '5' ,'branch':  "'CSE'   "  , 'branch_name': "'Computer Science' "    , 'lab': '0', 'proj':'0'})

conn.insert(execute=True,tableName='assignment_marks',column={'usn':"'1SK18CS053'" ,'sub_id': "'18CS54'",'marks':'34'})
conn.insert(execute=True,tableName='assignment_marks',column={'usn':"'1SK18CS003'" ,'sub_id': "'18CS54'",'marks':'45'})
conn.insert(execute=True,tableName='assignment_marks',column={'usn':"'1SK18CS001'" ,'sub_id': "'18CS54'",'marks':'19'})
conn.insert(execute=True,tableName='assignment_marks',column={'usn':"'1SK18CS002'" ,'sub_id': "'18CS54'",'marks':'13'})
conn.insert(execute=True,tableName='assignment_marks',column={'usn':"'1SK18CS004'" ,'sub_id': "'18CS54'",'marks':'46'})
conn.insert(execute=True,tableName='assignment_marks',column={'usn':"'1SK18CS005'" ,'sub_id': "'18CS54'",'marks':'42'})
conn.insert(execute=True,tableName='assignment_marks',column={'usn':"'1SK18CS006'" ,'sub_id': "'18CS54'",'marks':'20'})
conn.insert(execute=True,tableName='assignment_marks',column={'usn':"'1SK18CS007'" ,'sub_id': "'18CS54'",'marks':'50'})
conn.insert(execute=True,tableName='assignment_marks',column={'usn':"'1SK18CS008'" ,'sub_id': "'18CS54'",'marks':'45'})
conn.insert(execute=True,tableName='assignment_marks',column={'usn':"'1SK18CS009'" ,'sub_id': "'18CS54'",'marks':'33'})
conn.insert(execute=True,tableName='assignment_marks',column={'usn':"'1SK18CS052'" ,'sub_id': "'18CS54'",'marks':'10'})
conn.insert(execute=True,tableName='assignment_marks',column={'usn':"'1SK18CS0012'",'sub_id': "'18CS54'",'marks':'14'})
conn.insert(execute=True,tableName='assignment_marks',column={'usn':"'1SK18CS0013'",'sub_id': "'18CS54'",'marks':'39'})
conn.insert(execute=True,tableName='assignment_marks',column={'usn':"'1SK18CS0016'",'sub_id': "'18CS54'",'marks':'64'})
conn.insert(execute=True,tableName='assignment_marks',column={'usn':"'1SK18CS0017'",'sub_id': "'18CS54'",'marks':'24'})
conn.insert(execute=True,tableName='assignment_marks',column={'usn':"'1SK18CS0018'",'sub_id': "'18CS54'",'marks':'34'})
conn.insert(execute=True,tableName='assignment_marks',column={'usn':"'1SK18CS0019'",'sub_id': "'18CS54'",'marks':'40'})



# conn.insert(execute=True, tableName='attendance', column={'usn': "'1SK18CS004'", 'login': 'now()' ,'date':  "'2021-01-7'   "  , 'sub_id':   "'18CS54'"})
# conn.insert(execute=True, tableName='attendance', column={'usn': "'1SK18CS005'", 'login': 'now()' ,'date':  "'2021-01-7'   "  , 'sub_id':   "'18CS54'"})
# conn.insert(execute=True, tableName='attendance', column={'usn': "'1SK18CS006'", 'login': 'now()' ,'date':  "'2021-01-7'   "  , 'sub_id':   "'18CS54'"})
# conn.insert(execute=True, tableName='attendance', column={'usn': "'1SK18CS007'", 'login': 'now()' ,'date':  "'2021-01-7'   "  , 'sub_id':   "'18CS54'"})
# conn.insert(execute=True, tableName='attendance', column={'usn': "'1SK18CS008'", 'login': 'now()' ,'date':  "'2021-01-7'   "  , 'sub_id':   "'18CS54'"})
# conn.insert(execute=True, tableName='attendance', column={'usn': "'1SK18CS009'", 'login': 'now()' ,'date':  "'2021-01-7'   "  , 'sub_id':   "'18CS54'"})
# conn.insert(execute=True, tableName='attendance', column={'usn': "'1SK18CS052'", 'login': 'now()' ,'date':  "'2021-01-7'   "  , 'sub_id':   "'18CS54'"})
# conn.insert(execute=True, tableName='attendance', column={'usn': "'1SK18CS003'", 'login': 'now()' ,'date':  "'2021-01-7'   "  , 'sub_id':   "'18CS54'"})
# conn.insert(execute=True, tableName='attendance', column={'usn': "'1SK18CS053'", 'login': 'now()' ,'date':  "'2021-01-7'   "  , 'sub_id':   "'18CS54'"})
# conn.insert(execute=True, tableName='attendance', column={'usn': "'1SK18CS004'", 'logout': 'now()' ,'date':  "'2021-01-7'   "  ,'sub_id':   "'18CS54'" })
# conn.insert(execute=True, tableName='attendance', column={'usn': "'1SK18CS0053'",'login':'now()', 'logout': 'now()' ,'date':  "'2021-01-7'   "  ,'sub_id':   "'18CS54'"  })
# conn.insert(execute=True, tableName='attendance', column={'usn': "'1SK18CS006'", 'login':'now()','logout': 'now()' ,'date':  "'2021-01-7'   "  ,'sub_id':   "'18CS54'" })

# conn.insert(execute=True, tableName='attendance', column={'usn': "'1SK18CS004'", 'login_': 'now()' ,'date_':  "'2021-01-6'   "  , 'sub_id':   "'18CS54'"})
# conn.insert(execute=True, tableName='attendance', column={'usn': "'1SK18CS005'", 'login_': 'now()' ,'date_':  "'2021-01-6'   "  , 'sub_id':   "'18CS54'"})
# conn.insert(execute=True, tableName='attendance', column={'usn': "'1SK18CS006'", 'login_': 'now()' ,'date_':  "'2021-01-6'   "  , 'sub_id':   "'18CS54'"})
# conn.insert(execute=True, tableName='attendance', column={'usn': "'1SK18CS007'", 'login_': 'now()' ,'date_':  "'2021-01-6'   "  , 'sub_id':   "'18CS54'"})
# conn.insert(execute=True, tableName='attendance', column={'usn': "'1SK18CS008'", 'login_': 'now()' ,'date_':  "'2021-01-6'   "  , 'sub_id':   "'18CS54'"})
# conn.insert(execute=True, tableName='attendance', column={'usn': "'1SK18CS009'", 'login_': 'now()' ,'date_':  "'2021-01-6'   "  , 'sub_id':   "'18CS54'"})
# conn.insert(execute=True, tableName='attendance', column={'usn': "'1SK18CS052'", 'login_': 'now()' ,'date_':  "'2021-01-6'   "  , 'sub_id':   "'18CS54'"})
# conn.insert(execute=True, tableName='attendance', column={'usn': "'1SK18CS003'", 'login_': 'now()' ,'date_':  "'2021-01-6'   "  , 'sub_id':   "'18CS54'"})
# conn.insert(execute=True, tableName='attendance', column={'usn': "'1SK18CS053'", 'login_': 'now()' ,'date_':  "'2021-01-6'   "  , 'sub_id':   "'18CS54'"})
# conn.insert(execute=True, tableName='attendance', column={'usn': "'1SK18CS004'", 'logout': 'now()' ,'date_':  "'2021-01-6'   "  ,'sub_id':   "'18CS54'" })
# conn.insert(execute=True, tableName='attendance', column={'usn': "'1SK18CS0053'",'login_':'now()', 'logout': 'now()' ,'date_':  "'2021-01-6'   "  ,'sub_id':   "'18CS54'"  })
# conn.insert(execute=True, tableName='attendance', column={'usn': "'1SK18CS006'", 'login_':'now()','logout': 'now()' , 'date_':  "'2021-01-6'   "  ,'sub_id':   "'18CS54'" }

# conn.insert(execute=True, tableName='attendance', column={'usn': "'1SK18CS0012'", 'login_': 'now()' ,'date_':  "'2021-01-3'"  , 'sub_id':   "'18CS53'"})
# conn.insert(execute=True, tableName='attendance', column={'usn': "'1SK18CS0013'", 'login_': 'now()' ,'date_':  "'2021-01-3'"  , 'sub_id':   "'18CS53'"})
# conn.insert(execute=True, tableName='attendance', column={'usn': "'1SK18CS0014'", 'login_': 'now()' ,'date_':  "'2021-01-3'"  , 'sub_id':   "'18CS53'"})
# conn.insert(execute=True, tableName='attendance', column={'usn': "'1SK18CS0015'", 'login_': 'now()' ,'date_':  "'2021-01-3'"  , 'sub_id':   "'18CS53'"})
# conn.insert(execute=True, tableName='attendance', column={'usn': "'1SK18CS0016'", 'login_': 'now()' ,'date_':  "'2021-01-2'"  , 'sub_id':   "'18CS53'"})
# conn.insert(execute=True, tableName='attendance', column={'usn': "'1SK18CS0017'", 'login_': 'now()' ,'date_':  "'2021-01-2'"  , 'sub_id':   "'18CS53'"})
# conn.insert(execute=True, tableName='attendance', column={'usn': "'1SK18CS0018'", 'login_': 'now()' ,'date_':  "'2021-01-2'"  , 'sub_id':   "'18CS53'"})
# conn.insert(execute=True, tableName='attendance', column={'usn': "'1SK18CS0019'", 'login_': 'now()' ,'date_':  "'2021-01-2'"  , 'sub_id':   "'18CS53'"})
# conn.insert(execute=True, tableName='attendance', column={'usn': "' 1SK18CS001 '", 'login_': 'now()' ,'date_':  "'2021-01-6'   "  , 'sub_id':   "'18CS54'"})
# conn.insert(execute=True, tableName='attendance', column={'usn': "' 1SK18CS001 '", 'logout': 'now()' ,'date_':  "'2021-01-6'   "  ,'sub_id':   "'18CS54'" })
# conn.insert(execute=True, tableName='attendance', column={'usn': "' 1SK18CS001 '",'login_':'now()', 'logout': 'now()' ,'date_':  "'2021-01-6'   "  ,'sub_id':   "'18CS54'"  })
# conn.insert(execute=True, tableName='attendance', column={'usn': "' 1SK18CS001 '", 'login_':'now()','logout': 'now()' , 'date_':  "'2021-01-6'   "  ,'sub_id':   "'18CS54'" })


# conn.insert(execute=True, tableName='assignment_marks', column={'usn': "' 1SK18CS001 '", 'assignment_id':'1','assignment_marks': '20' ,'lab_id':"'18CS57'",'lab_marks':'50','ia_no': })
