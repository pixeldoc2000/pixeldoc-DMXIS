#===============================================================
# DMXIS Python Macro
# pixeldoc81 (http://pixeldoc.kicks-ass.net/)
#===============================================================

# Open "File > Macro output console" for Output.

found = False

for i in range(0, 512):
    if not GetChVal(i) == 0:
        chNum = i + 1
        #print 'Channel %d value = %d' % (chNum, GetChVal(i))
        #print 'Channel %03d value = %d' % (chNum, GetChVal(i))
        print 'Channel %03d value = %03d' % (chNum, GetChVal(i))
        found = True

if not found: print 'No Channels with none 0 values'

# New Line
print ''
