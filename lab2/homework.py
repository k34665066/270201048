#If I leave my house at 6:52 am and run 1 mile at an easy pace (8 minutes per mile), then 3 miles at tempo (6 minutes per mile) and 2 mile at easy pace again, what time do I get home for breakfast?
time=6.52
minutes_time=6*60+52
easy_peace=8
tempo=6
running_time=1*easy_peace+3*tempo+2*easy_peace
hour=(minutes_time+running_time)//60
minute=(minutes_time+running_time)%60
print(hour,":",minute)
