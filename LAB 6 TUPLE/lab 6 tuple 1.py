name = [ ("ujju",), "silpa" , "jeni" , ("krishn",), "jeli" ,("niv",), "pal" , ("ram",),]
boy_count = 0
for nam in name:
    if isinstance(nam,tuple):
        boy_count = boy_count + 1
girl_count = len(name) - boy_count
print(boy_count)
print(girl_count)
