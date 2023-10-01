"""
用if语句实现百分制转等级制
"""
grade=int(input("请输入您的成绩(满分100分):"))
print("您的等级为：",end="")
if(grade<60):
    print("不及格")
elif(grade>=60 and grade<75):
    print("及格")
elif(grade>=75 and grade<90):
    print("良好")
elif(grade>=90):
    print("优秀")