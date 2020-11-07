import tkinter as tk  # 使用Tkinter前需要先导入
#实例化窗口
window = tk.Tk()
 
# 给窗口的可视化起名字
window.title('运动结束')
 
# 设定窗口的大小(长 * 宽)
window.geometry('640x360')

#显示数据
l1 = tk.Label(window, text='您本次锻炼项目为：', font=('宋体', 15), width=30, height=3).place(x=30,y=50)

l2 = tk.Label(window, text='您本次锻炼时长为：', font=('宋体', 15), width=30, height=3).place(x=30,y=100)

l3 = tk.Label(window, text='您本次锻炼消耗卡路里为：', font=('宋体', 15), width=30, height=3).place(x=30,y=150)

l4 = tk.Label(window, text='您本次锻炼动作标准数为：', font=('宋体', 15), width=30, height=3).place(x=30,y=200)

l5 = tk.Label(window, text='您本次锻炼动作不标准数：', font=('宋体', 15), width=30, height=3).place(x=30,y=250)


#定义函数
def quit():
    window.destroy()
    open('登录窗口.py')

def back_to_choose():
    window.destroy()
    open('运动模式选择.py')

#功能按钮
b1= tk.Button(window, text='继续锻炼', font=('宋体', 15), width=10, height=1, command=back_to_choose).place(x=500,y=100)
b2= tk.Button(window, text='生成报告', font=('宋体', 15), width=10, height=1).place(x=500,y=150)
b3= tk.Button(window, text='退出', font=('宋体', 15), width=10, height=1, command=quit).place(x=500,y=200)

window.mainloop()