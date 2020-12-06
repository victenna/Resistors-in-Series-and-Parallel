import turtle,random
import time
wn=turtle.Screen()
wn.setup(1200,800)
wn.bgpic('bground4.gif')
TEXT_FONT=('Arial',25,'bold')
TEXT_FONT1=('Arial',35,'bold')
turtle.tracer(3)

#-----------------------------------------------------------------------------------------------
res_val=[]
res_pos=[]
r=[0,0,0]
for n in range (3):
    res_val.append(turtle.Turtle())
    res_pos.append(turtle.Turtle())
    res_val[n].up()
    res_pos[n].up()
    res_val[n].hideturtle()
    res_pos[n].hideturtle()
    n1=str(n+1)
    
A=True
while A==True:
    
    res_val[0]=wn.textinput('Интерактивный тест','Введите сопротивление #1')
    res_pos[0].goto(-340,80)
    res_pos[0].write(res_val[0],font=TEXT_FONT)

    res_val[1]=wn.textinput('Интерактивный тест','Введите сопротивление #2')
    res_pos[1].goto(-340,-30)
    res_pos[1].write(res_val[1],font=TEXT_FONT)

    res_val[2]=wn.textinput('Интерактивный тест','Введите сопротивление #3')
    res_pos[2].goto(-180,25)
    res_pos[2].write(res_val[2],font=TEXT_FONT)

    for n in range(3):
        r[n]=float(res_val[n])
        
    answer=wn.textinput('Результат','Ваше значение ?')

    Answer=turtle.Turtle()
    Answer.up()
    Answer.hideturtle()
    Answer.goto(-345,-280)
    Answer.write(answer,font=TEXT_FONT)

    r_eq=round(r[0]*r[1]/(r[0]+r[1])+r[2])
    r_eq1=str(r_eq)
    R_eq=turtle.Turtle()
    R_eq.hideturtle()
    R_eq.up()
    R_eq.goto(345,-280)
    R_eq.write(r_eq1,font=TEXT_FONT)
    
    error=turtle.Turtle()
    error.up()
    error.hideturtle()
    error.goto(0,-280)
    error.color('red')
    if r_eq==int(answer):
        error.write('Отлично',font=TEXT_FONT1)
        
    if r_eq!=int(answer):
        error.write('Oшибка',font=TEXT_FONT1)
       
    time.sleep(4)
    for s in range(3):
        res_pos[s].clear()
    R_eq.clear()
    Answer.clear()
    error.clear()
    activation=wn.textinput('Продолжаем?','введите да или нет')
    if activation=='да':
        A==True
    if activation=='нет':
        break
wn.bye()
   
    



