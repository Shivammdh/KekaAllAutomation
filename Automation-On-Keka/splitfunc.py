lst1=['No Time Entries Logged\nMar 11, Fri',
 'No Time Entries Logged\nMar 10, Thu',
 'No Time Entries Logged\nMar 09, Wed',
 'No Time Entries Logged\nMar 08, Tue',
 'No Time Entries Logged\nMar 07, Mon',
 'Full day Weekly-off\nMar 06, SunW-OFF',
 'Full day Weekly-off\nMar 05, SatW-OFF',
 'Holiday\nMar 01, TueHLDY',
 'Full day Weekly-off\nFeb 27, SunW-OFF',
 'Full day Weekly-off\nFeb 26, SatW-OFF',
 'Full day Weekly-off\nFeb 20, SunW-OFF',
 'Full day Weekly-off\nFeb 19, SatW-OFF',
 'Full day Weekly-off\nFeb 13, SunW-OFF',
 'Full day Weekly-off\nFeb 12, SatW-OFF']
lst2=[]
for i in lst1:
    l1=i.split("\n")
    if(l1[0]=='No Time Entries Logged'):
        l2=l1[1].split(",")
        l3=l2[0].split(" ")
        lst2.append(l3[1])
lst2.sort()
print(lst2[0].lower()=='07'.lower())