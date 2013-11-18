#===============================================================
# DMXIS Python Macro
# pixeldoc81 (http://pixeldoc.kicks-ass.net/)
#===============================================================

# Open "File > Macro output console" for Output.

for i in range(300, 400):
    chNum = i + 1
    #print 'Channel %d value = %d' % (chNum, GetChVal(i))
    #print 'Channel %03d value = %d' % (chNum, GetChVal(i))
    print 'Channel %03d value = %03d' % (chNum, GetChVal(i))

# New Line
print ''
