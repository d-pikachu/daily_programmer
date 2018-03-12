#time = input("")
nums = ["twleve","one","two","three","four","five","six","seven","eight","nine","ten","eleven","twelve"]
tens = ["","","twenty","thirty","fourty","fifty","sixty"]
teens = ["thir","","fif"]

'''
def clock(time):
        time = time.split(":")
        h = nums[int(time[0])]
        m = int(time[1])
        mt = int(m/10)
        mt = tens[mt] + (" " if mt!=0 else "")
        mo = m%10
        mo = nums[mo] if mo>0 else ""
        print(mt + mo)
'''

'''
for i in range(61):
        m = i
        
        mt = int(m/10)
        mo = m%10
        
        if m==10: mt=nums[10]
        elif mt==1:
                if mo<3: mt = nums[mo+10];
                else:
                        if mo==3: mt="thir"
                        elif mo==5: mt="fif"
                        elif mo==8: mt="eigh"
                        else: mt = nums[mo]
                        mt += "teen"
                
        else : mt = tens[mt] + (" " if mt>1 else "")

        if mo==0 or int(m/10)==1: mo=""
        else: mo = nums[mo] if mo>0 and mt!=1 else ""

        m = mt + mo
        print(m)
'''
def clock(time):
        time = time.split(":")
        h = nums[int(time[0]) %13]
        m = int(time[1])
        mt = int(m/10)
        mo = m%10
        
        if m==10: mt=nums[10]
        elif mt==1:
                if mo<3: mt = nums[mo+10];
                else:
                        if mo==3: mt="thir"
                        elif mo==5: mt="fif"
                        elif mo==8: mt="eigh"
                        else: mt = nums[mo]
                        mt += "teen"
                
        else : mt = tens[mt] + (" " if mt>1 else "")

        if mo==0 or int(m/10)==1: mo=""
        else: mo = nums[mo] if mo>0 and mt!=1 else ""

        m = ("oh " if int(m/10)==0 else "" )+ mt + mo
        print(h +" "+ m)
