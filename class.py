class Solution(object):
    def romanToInt(self, s):
        temp = s
        tot = 0
        tot += 4*int(temp.count('IV'))
        temp = temp.replace('IV', "")
        tot += 9*int(temp.count('IX'))
        temp = temp.replace('IX', "")
        tot += 40*int(temp.count('XL'))
        temp = temp.replace('XL', "")
        tot += 90*int(temp.count('XC'))
        temp = temp.replace('XC', "")
        tot += 400*int(temp.count('CD'))
        temp = temp.replace('CD', "")
        tot += 900*int(temp.count('CM'))
        temp = temp.replace('CM', "")

        tot += int(temp.count('I'))
        tot += 5*int(temp.count('V'))
        tot += 10*int(temp.count('X'))
        tot += 50*int(temp.count('L'))
        tot += 100*int(temp.count('C'))
        tot += 500*int(temp.count('D'))
        tot += 1000*int(temp.count('M'))
        return(tot)
