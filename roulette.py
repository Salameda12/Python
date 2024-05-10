import random

def shoot():
  while True:
    N = input("총을 쏠까요(enter)")
    print(f"남은 총알 >> {len(bullet) - 1} ")
    if N == "":
      break

if __name__ == "__main__":
  bullet = ["생존", "생존", "생존", "생존", "생존", "죽음"]
  i = 5
  while True:
    idx_bullet = random.randint(0, i)
    shoot()
    a = bullet.pop(idx_bullet)
    print(a)
    if a == "죽음":
      print("아웃")
      break
    i = i - 1