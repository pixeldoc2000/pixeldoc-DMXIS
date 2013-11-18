#===============================================================
# DMXIS Python Macro
# pixeldoc81 (http://pixeldoc.kicks-ass.net/)
#===============================================================

sel = GetAllSelCh(False)
if len(sel) < 1:
    print 'No Channels selected'
else:
    n = GetNumSelCh()
    for i in range(n):
        chNum = GetSelCh(i)
        chNumH = chNum + 1
        print 'Channel %d value = %d' % (chNumH, GetChVal(chNum))

# New Line
print ''
