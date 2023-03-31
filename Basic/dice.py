import random
def streak():
    dice=['1','2','3','4','5','6']
    selection=random.choices(dice,k=3)
    if selection[0]==selection[1]==selection[2]:
        return selection, "You win"
    else:
        return selection, ""

ans,msg=streak()
print('Rolling the dices.....')
print(" ".join(ans))
print(msg)