#改良前
a,b,c,d,e,f,x = map(int,input().split())

def takahashi_run(a,b,c,x):
  t_flag = True
  takahashi = 0
  while t_flag:
    if a <= x:
      x -= a
      takahashi += a*b
      if c <= x:
        x -= c
      else:
        t_flag = False
    else:
      takahashi += x*b
      t_flag = False
  return takahashi

def aoki_run(d,e,f,x):
  a_flag = True
  aoki = 0
  while a_flag:
    if d <= x:
      x -= d
      aoki += d*e
      if f <= x:
        x -= f
      else:
        a_flag = False
    else:
      aoki += x*d
      a_flag = False
  return aoki

if takahashi_run(a,b,c,x) > aoki_run(d,e,f,x):
  print("Takahashi")
elif takahashi_run(a,b,c,x) < aoki_run(d,e,f,x):
  print("Aoki")
else:
  print("Draw")

#改良後
A,B,C,D,E,F,X = map(int,input().split())

def run_dis(a,b,c,x):
  t_flag = True
  dis = 0
  while t_flag:
    if a <= x:
      x -= a
      dis += a*b
      if c <= x:
        x -= c
      elif c > x:
        t_flag = False
    elif a > x:
      dis += x*b
      t_flag = False
  return dis

t = 0
a = 0
t = run_dis(A,B,C,X)
a = run_dis(D,E,F,X)

if t > a:
  print("Takahashi")
elif t < a:
  print("Aoki")
else:
  print("Draw")