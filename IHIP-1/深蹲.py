import tkinter as tk  # 使用Tkinter前需要先导入
import time

def sd():
#实例化窗口
  windowsd = tk.Tk()
 
# 给窗口的可视化起名字
  windowsd.title('开始运动')
 
# 设定窗口的大小(长 * 宽)
  windowsd.geometry('1280x720')

#定义函数
##时间
  def gettime():
    # 获取当前时间并转为字符串
    timestr = time.strftime("%H:%M:%S")
    # 重新设置标签文本
    lb.configure(text=timestr)
    # 每隔一秒调用函数gettime自身获取时间
    windowsd.after(1000, gettime)
 
##设置字体大小颜色
  lb = tk.Label(windowsd, text='', fg='blue', font=("黑体", 80))
  lb.pack()
  gettime()

#定义函数
  def finish():
    windowsd.destroy()
    open('运动结束.py')

  def back_to_choose():
    windowsd.destroy()
    open('运动模式选择.py')

#功能按钮
  b1= tk.Button(windowsd, text='开始', font=('宋体', 24), width=10, height=1).place(x=1100,y=100)
  b2= tk.Button(windowsd, text='暂停', font=('宋体', 24), width=10, height=1).place(x=1100,y=200)
  b3= tk.Button(windowsd, text='结束', font=('宋体', 24), width=10, height=1, command=finish).place(x=1100,y=300)
  b4= tk.Button(windowsd, text='返回', font=('宋体', 24), width=10, height=1, command=back_to_choose).place(x=1100,y=400)

  windowsd.mainloop()