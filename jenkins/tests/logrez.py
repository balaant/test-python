import sqlite3
import sys
con = sqlite3.connect('labsstat.db')
name = sys.argv[1]
id = sys.argv[2]
group = sys.argv[3]
link = sys.argv[4]
state = sys.argv[5]

try:
    with con:
        con.execute("create table IF NOT EXISTS stat (id integer primary key, nme varchar unique, labid integer, grp unique, link varchar unique, stat varchar unique)")
        con.execute("CREATE INDEX IF NOT EXISTS unique_lab ON stat (nme,labid, grp)")
except sqlite3.IntegrityError:
    print("stat table exists")


if state == "init":
    try:
        with con:
            con.execute("insert into stat(nme,labid,grp,link,stat) values (?,?,?,?,'initial')", (name,id,group,link))
    except sqlite3.IntegrityError:
        print("Already exists "+name+" "+group+" Lab"+id)
if state == "pass":
    try:
        with con:
            con.execute("update stat set stat='passed' where nme=? and id=? and grp=?", (name,id,group))
    except sqlite3.IntegrityError:
        print("failed to update "+name+" "+group+" Lab"+id)


