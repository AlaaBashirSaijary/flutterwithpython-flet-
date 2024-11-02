from flet import *
import sqlite3
con=sqlite3.connect('data.db',check_same_thread=False)
cursor=con.cursor()
cursor.execute("""
               CREATE TABLE IF NOT EXISTS student(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   stdName TEXT,
                   stdEmail TEXT,
                   phone TEXT,
                   stdadres TEXT,
                   stmath INTEGER,
                   stdarabic INTEGER,
                   france INTEGER,
                   enlish INTEGER,
                   sport INTEGER,
                   draw INTEGER
               )
               """)
con.commit()
def main(page:Page):
    page.title='إدارة شؤؤن طلاب'
    page.scroll='auto'
    page.window.top=1
    page.window.left=960
    page.window.width=390
    page.window.height=740
    page.bgcolor='white'
    page.theme_mode=ThemeMode.LIGHT
    table_name='student'
    query=f'SELECT COUNT(*) FROM {table_name}'
    cursor.execute(query)
    result=cursor.fetchone()
    row_count=result[0]
    def add(student):
        cursor.execute("INSERT INTO student(stdName,stdEmail,phone,stdadres,stmath,stdarabic,france,enlish,sport,draw) VALUES (?,?,?,?,?,?,?,?,?,?)",(tname.value,taddres.value,temail.value,tphone.value,mathmatic.value,arabic.value,english.value,francr.value,drow.value,sport.value))
        con.commit()
    def show(student):
        c=con.cursor()
        c.execute("SELECT * FROM student")
        user=c.fetchall()
        print(user)
        if not user=="":
            keys=['id','stdName','stdEmail','phone','stdadres','stmath','stdarabic','france','enlish','sport','draw']
            result=[dict(zip(keys,values)) for values in user]
            for x in result:
             page.add(
                Card(
                    color='black',
                    content=Container(
                        content=Column([
                            ListTile(
                               
                                leading=Icon(icons.PERSON),
                                title=Text('Name:'+x['stdName'],color='white')
                            ),
                             Row([
                                    Text('phone:',color='white'),
                            Text(x['phone'],color='red'),
                            ],alignment=MainAxisAlignment.CENTER),
                            Row([
                                    Text('Email:',color='white'),
                                 Text(x['stdEmail'],color='red'),
                            ],alignment=MainAxisAlignment.CENTER),
                             Row([
                                    Text('Address:',color='white'),
                            Text(x['stdadres'],color='red'),
                            ],alignment=MainAxisAlignment.CENTER),
                            Row([
                                Text('عربي'+str(x['stdarabic']),color='red',rtl=True),
                                  Text('رياضيات'+str(x['stmath']),color='red',rtl=True),
                                    Text('فرنسي'+str(x['france']),color='red',rtl=True),
                                     Text('لغة'+str(x['enlish']),color='red',rtl=True),
                                      Text('رسم'+str(x['draw']),color='red',rtl=True),
                                       Text('رياضة'+str(x['sport']),color='red',rtl=True)
                            ],alignment=MainAxisAlignment.CENTER)
                        
                        
                        ]))))
                           
    tname=TextField(rtl=True,height=38,label='اسم الطالب',icon=icons.PERSON)
    taddres=TextField(rtl=True,height=38,label='عنوان الطالب',icon=icons.LOCATION_CITY)
    temail=TextField(rtl=True,height=38,label='إيميل الطالب',icon=icons.EMAIL)
    tphone=TextField(rtl=True,height=38,label='رقم الطالب',icon=icons.PHONE)
    marktext=Text("علامات الطالب",text_align='center',weight='bold')
    mathmatic=TextField(rtl=True,height=38,label='رياضيات',width=110)
    arabic=TextField(rtl=True,height=38,label='عربي',width=110)
    english=TextField(rtl=True,height=38,label='لغة',width=110)
    francr=TextField(rtl=True,height=38,label='فرنسي',width=110)
    drow=TextField(rtl=True,height=38,label='رسم',width=110)
    sport=TextField(rtl=True,height=38,label='رياضة',width=110)
    addButton=ElevatedButton('إضافة طالب جديد',width=170,style=ButtonStyle(
        bgcolor='blue',color='white',padding=15),on_click=add)
    showButton=ElevatedButton('عرض كل الطلاب ',width=170,style=ButtonStyle(
        bgcolor='blue',color='white',padding=15),on_click=show)
    page.add(
        Row( [
        Image(src='logo.jpg') ],  
        alignment=MainAxisAlignment.CENTER),
        Row(
        [Text(' تطبيق الطالب والمعلم',size=20,font_family="IBM Plex Sans Arabic",color='black')], alignment=MainAxisAlignment.CENTER),
       Row(
        [Text('عدد الطلاب المسجلين',size=20,font_family="IBM Plex Sans Arabic",color='black'),
         Text(row_count,size=20,font_family="IBM Plex Sans Arabic",color='black')], alignment=MainAxisAlignment.CENTER,rtl=True),
       tname,
       temail,
       tphone,
       taddres,
       Row([marktext],alignment=MainAxisAlignment.CENTER,rtl=True),
        Row([mathmatic,arabic,english],alignment=MainAxisAlignment.CENTER,rtl=True),
        Row([francr,drow,sport],alignment=MainAxisAlignment.CENTER,rtl=True),
        Row([showButton,addButton],alignment=MainAxisAlignment.CENTER))
    
app(main)