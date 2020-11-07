import tkinter as tk  # 使用Tkinter前需要先导入
import time
#实例化窗口
window = tk.Tk()
 
# 给窗口的可视化起名字
window.title('选择运动模式')
 
# 设定窗口的大小(长 * 宽)
window.geometry('400x200')  

# 加载提示标题
l = tk.Label(window, text='请选择运动模式', font=('宋体', 12), width=30, height=3).place(x=75,y=10)

#定义按钮函数
def back_to_sign_up():
    window.destroy()
    open ('登录窗口.py')
#深蹲
def sd():
  window.destroy()
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
#俯卧撑
def fwc():
    window.destroy()
    open('俯卧撑.py')
#仰卧起坐
def ywqz():
    window.destroy()
    open('仰卧起坐.py')
    
b1= tk.Button(window, text='退出', font=('宋体', 12), width=9, height=1, command=back_to_sign_up).place(x=300,y=150)
b2= tk.Button(window, text='深蹲', font=('宋体', 12), width=9, height=1, command=sd).place(x=50,y=100)
b3= tk.Button(window, text='俯卧撑', font=('宋体', 12), width=9, height=1, command=fwc).place(x=150,y=100)
b4= tk.Button(window, text='仰卧起坐', font=('宋体', 12), width=9, height=1, command=ywqz).place(x=250,y=100)

window.mainloop()