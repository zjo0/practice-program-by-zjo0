from tkinter import *
from tkinter import filedialog
from 考勤 import unionrecord
import datetime

class Application(Frame):
    def __init__(self,master=None):
        Frame.__init__(self,master)
        self.pack()
        self.officepath=StringVar()   
        self.dingdingpath=StringVar()
        self.workoffpath=StringVar()
        self.dingdingonpath=StringVar()
        self.year_=IntVar()
        yearget=datetime.datetime.now().year
        self.year_.set(yearget)
        self.month_=IntVar()
        monthget=datetime.datetime.now().month
        self.month_.set(monthget)
        self.createWidgets()

    def createWidgets(self):
        self.officeLabel=Label(self,text='指纹打卡文件').grid(row=0,column=0)
        self.entry=Entry(self, textvariable=self.officepath).grid(row=0, column=1)
        self.selectButton1=Button(self,text='路径选择',command=self.select_office_path).grid(row=0,column=3)
        self.dingdingLabel = Label(self, text='钉钉签到文件').grid(row=1, column=0)
        self.entry = Entry(self, textvariable=self.dingdingpath).grid(row=1, column=1)
        self.selectButton2 = Button(self, text='路径选择', command=self.select_dingding_path).grid(row=1, column=3)
        self.dingdingonLabel = Label(self, text='钉钉考勤文件').grid(row=2, column=0)
        self.entry = Entry(self, textvariable=self.dingdingonpath).grid(row=2, column=1)
        self.selectButton3 = Button(self, text='路径选择', command=self.select_dingdingon_path).grid(row=2, column=3)
        self.workoffLabel = Label(self, text='icome请假文件').grid(row=3, column=0)
        self.entry = Entry(self, textvariable=self.workoffpath).grid(row=3, column=1)
        self.selectButton3 = Button(self, text='路径选择', command=self.select_workoff_path).grid(row=3, column=3)
        self.officeLabel=Label(self,text='考勤年份').grid(row=4,column=0)
        self.entry=Entry(self, textvariable=self.year_).grid(row=4, column=1)
        self.officeLabel=Label(self,text='考勤月份').grid(row=4,column=2)
        self.entry=Entry(self, textvariable=self.month_).grid(row=4, column=3)
        self.createButton=Button(self,text='生成汇总文件',command=lambda : unionrecord(self.officepath.get(),self.dingdingpath.get(),self.workoffpath.get(),self.dingdingonpath.get(),self.year_.get(),self.month_.get())).grid(row=4)
    def select_office_path(self):
        path1_=filedialog.askopenfilename()
        path1_=path1_.replace('/','\\\\')
        self.officepath.set(path1_)
    def select_dingding_path(self):
        path2_=filedialog.askopenfilename()
        path2_=path2_.replace('/','\\\\')
        self.dingdingpath.set(path2_)
    def select_workoff_path(self):
        path3_=filedialog.askopenfilename()
        path3_=path3_.replace('/','\\\\')
        self.workoffpath.set(path3_)
    def select_dingdingon_path(self):
        path4_=filedialog.askopenfilename()
        path4_=path4_.replace('/','\\\\')
        self.dingdingonpath.set(path4_)
app=Application()
app.master.title('感谢健哥')
app.mainloop()
