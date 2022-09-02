###################### Created by Siddharth #######################
###################### Free to use and edit #######################
############### To use commercially just credit me ################
################## https://github.com/kingsiddhu ##################
################### This is not the encryptor, ####################
#to send encrypted morse code encrypt phrase then convert to morse#

def MorseC(string, dot="•",dash="–", lexi_to_morse=True):
    list =["a","•–",
            "b","–•••",
            "c","–•–•",
            "d","–••",
            "e","•",
            "f","••–•",
            "g","––•",
            "h","••••",
            "i","••",
            "j","•–––",
            "k","–•–",
            "l","•–••",
            "m","––",
            "n","–•",
            "o","–––",
            "p","•––•",
            "q","––•–",
            "r","•–•",
            "s","•••",
            "t","–",
            "u","••–",
            "v","•••–",
            "w","•––",
            "x","–••–",
            "y","–•––",
            "z","––••",
            "1","•–",
            "2","••–",
            "3","•••–",
            "4","••••–",
            "5","•••••",
            "6","–••••",
            "7","––•••",
            "8","–––••",
            "9","––––•",
            "0","–––––",
            ",","––••––",
            ".","•–•–•–",
            " ","/"
            ]
    text = ""
    string = string.lower()
    
    if lexi_to_morse == True:
        
        for l in string:
            if list.index(l) == -1:
                print()
                text += l + " "
            else:
                print(list.index(l), l)
                text += list[list.index(l) + 1] + " "
    elif lexi_to_morse == False:
        string = [word.lower() for word in string.split()]
        for key in string:
            if list.index(key) == -1:
                text += key + " "
            else:
                text += list[list.index(key) - 1]
    
    if dot != "•":
        text = text.replace(dot)
    if dash != "–":
        text.replace(dash)
    return text
