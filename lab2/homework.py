time=6.52
minutes_time=6*60+52
easy_peace=8
tempo=6
running_time=1*easy_peace+3*tempo+2*easy_peace
hour=(minutes_time+running_time)//60
minute=(minutes_time+running_time)%60
print(hour,":",minute)
