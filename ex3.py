# ex3.py
    
import turtle as t

def tri(tri_len):
    if tri_len <= 10:  # tri_len <= 10:
        for i in range(0,3):  #range(0,3):
            t.forward(tri_len)
            t.left(120)  # t.left(120)
        return

    new_len=tri_len/2
    tri(new_len)
    t.forward(new_len)
    tri(new_len)
    t.backward(new_len)
    t.left(60)
    t.forward(new_len)
    t.right(60)
    tri(new_len)
    t.left(60)
    t.backward(new_len)
    t.right(60)

t.speed(30)
tri(180) # 20부터 160까지 변화하면서 살펴봄
t.hideturtle()
t.done()

