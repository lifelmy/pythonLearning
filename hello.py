def function(name):
    print('hello',name)
    if(__name__=='__main__'):
        print('在自己模块运行')
    else:
        print('在其他模块运行')
    return
