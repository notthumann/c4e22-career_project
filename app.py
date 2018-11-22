from flask import Flask,render_template, request
import mlab
from quiz import *
app = Flask(__name__)
mlab.connect()


# name_list = ["The Mediator","The Protagonist","The Provider","The Virtuoso","The Dynamo"]
# des_list = [
#     "You are a sensitive idealist motivated by your deeper personal values. You see the potential of a better future, and pursue truth and meaning with your own particular flair. You love motivating others to becom better.",
#     "You are people loving and driven, with lots of energy and a desire to express yourself. You always seem to be tuned in to the needs of others, but remain optimistic and forward-looking",
#     "Motivated to help others, you find yourself always attracted to roles and duties that benefit others. With family and friends your top priority in life, you are generous with your time, effort and emotions.",
#     "You are straightforward and honest, a firm believer that action is better than words. Your observant and troubleshooting nature means you approach life with flexible logic, looking for solutions to the problems at hand.",
#     "You are an energetic thrill seeker, happiest when you can fix problems. You love the excitement and uncertainty that comes with crisis management and problem solving, anything that requires you to be resourceful",
# ]
# suited_list = [
#     "Graphics Designer, Psychologist, Writer, Artist, Editor, Therapist, HR development manager, Councillor",
#     "Advertising executive, Public Relations specialist, Corporate Coach, Personal Trainer, Teacher, Motivational speaker, Headhunter, Fashion Design",
#     "Sales rep, Doctor/nurse, Life coach, Loan officer, Policeman/woman, Social worker, Government worker, Paramedic",
#     "Mechanic, Engineer, Economist,  Auditor, Pilot, Data analyst, Scientist, Landscape planner",
#     "Detective, Corporate banker, Business analyst, Investor, Sport Coach, Builder, Software developer, Air traffic controller",
# ]
# point_list = [
#     20 , 40 , 60, 80,100
# ]
# for i in range (5):
#     name = name_list[i]
#     des = des_list[i]
#     suited = suited_list[i]
#     total_points = point_list[i]
#     p = PersonType(name = name, des = des, suited = suited, total_points= total_points)
#     p.save()

# (https://images.unsplash.com/photo-1536659492859-625ab2c75c4a?ixlib=rb-0.3.5&ixid=eyJhcHBfaWQiOjEyMDd9&s=789a9d004ca9a17c085f549ececf4a3c&auto=format&fit=crop&w=1498&q=80 appearance)
# 1
# (https://images.unsplash.com/photo-1432611185496-76ccd1dc5efe?ixlib=rb-0.3.5&ixid=eyJhcHBfaWQiOjEyMDd9&s=481b134d4fc95af548cbddd67f0d6d6f&auto=format&fit=crop&w=800&q=80 artificial)
# 2
# (https://images.unsplash.com/photo-1507679799987-c73779587ccf?ixlib=rb-0.3.5&ixid=eyJhcHBfaWQiOjEyMDd9&s=2f2507356905735cb7d15583034c7faa&auto=format&fit=crop&w=1351&q=80 career)
# 3
# (https://images.unsplash.com/photo-1536604673810-81370412626d?ixlib=rb-0.3.5&ixid=eyJhcHBfaWQiOjEyMDd9&s=3d8d7119042038472ff44dc29d29220d&auto=format&fit=crop&w=1266&q=80 classic)
# 4
# (https://images.unsplash.com/photo-1542042179-1fc836a4089f?ixlib=rb-0.3.5&ixid=eyJhcHBfaWQiOjEyMDd9&s=be760a70b526370ef81e74c9c98f2ba2&auto=format&fit=crop&w=634&q=80 energy drink)
# 5
# (https://images.unsplash.com/photo-1504780361545-d1ce834be3a9?ixlib=rb-0.3.5&ixid=eyJhcHBfaWQiOjEyMDd9&s=8c7df6cb3e6a79c23c68d8c08ccae8b9&auto=format&fit=crop&w=1489&q=80 work alone)
# 6
# (https://images.unsplash.com/photo-1506377170913-e1d634babf96?ixlib=rb-0.3.5&ixid=eyJhcHBfaWQiOjEyMDd9&s=910fc1a8df066c995a13e7acc6bee6c0&auto=format&fit=crop&w=634&q=80 enjoy)
# 7
# (https://images.unsplash.com/photo-1510022079733-8b58aca7c4a9?ixlib=rb-0.3.5&ixid=eyJhcHBfaWQiOjEyMDd9&s=6da2c9e985e56b6a43209d7b1d46c8ca&auto=format&fit=crop&w=701&q=80 family)
# 8
# (https://images.unsplash.com/photo-1534367507873-d2d7e24c797f?ixlib=rb-0.3.5&ixid=eyJhcHBfaWQiOjEyMDd9&s=d4b5ecbd9836b3db586d65cddbd06bab&auto=format&fit=crop&w=1350&q=80 indoor excercise)
# 9
# (https://images.unsplash.com/photo-1534318002854-72e10bf140ed?ixlib=rb-0.3.5&ixid=eyJhcHBfaWQiOjEyMDd9&s=3a987deddb37a8045edc1db7e5a30baa&auto=format&fit=crop&w=634&q=80 juice)
# 10
# (https://images.unsplash.com/photo-1496171367470-9ed9a91ea931?ixlib=rb-0.3.5&ixid=eyJhcHBfaWQiOjEyMDd9&s=1296a4419a6c84e28281db0a564071ef&auto=format&fit=crop&w=1350&q=80 modern)
# 11
# (https://images.unsplash.com/photo-1523430237819-5fdfeb4f5604?ixlib=rb-0.3.5&ixid=eyJhcHBfaWQiOjEyMDd9&s=f5314a7fa18a4ec6909d4cbda5687ada&auto=format&fit=crop&w=1237&q=80 moneymaker)
# 12
# (https://images.unsplash.com/photo-1502176747191-3354e2597a5f?ixlib=rb-0.3.5&ixid=eyJhcHBfaWQiOjEyMDd9&s=a47195ab105472213f9e589e92c2df74&auto=format&fit=crop&w=1036&q=80 natural)
# 13
# (https://images.unsplash.com/photo-1516902663607-8d25785663fe?ixlib=rb-0.3.5&ixid=eyJhcHBfaWQiOjEyMDd9&s=bc6788eaa314999002ccb4dc3f1ce190&auto=format&fit=crop&w=628&q=80 outdoorex)
# 14
# (https://images.unsplash.com/photo-1504955236898-44c735157f4f?ixlib=rb-0.3.5&ixid=eyJhcHBfaWQiOjEyMDd9&s=b2e933821d0ae3d8eb2cfa489037a30b&auto=format&fit=crop&w=1350&q=80 rural area)
# 15
# (https://images.unsplash.com/photo-1525422847952-7f91db09a364?ixlib=rb-0.3.5&s=da13a911783ae00ee9093e562c4a485e&auto=format&fit=crop&w=1365&q=80 teamwork)
# 16
# (https://images.unsplash.com/photo-1430609098125-581618d0482f?ixlib=rb-0.3.5&ixid=eyJhcHBfaWQiOjEyMDd9&s=233388fe77509387a00a139deec2adde&auto=format&fit=crop&w=1350&q=80 urban city)
# 17
# (https://images.unsplash.com/photo-1538992691511-a64e9c9034dd?ixlib=rb-0.3.5&ixid=eyJhcHBfaWQiOjEyMDd9&s=d9de182134a5109157f3366cb5f4a9ea&auto=format&fit=crop&w=1350&q=80 value contributer)
# 18
# (https://images.unsplash.com/photo-1501876991173-f9c47cd28268?ixlib=rb-0.3.5&ixid=eyJhcHBfaWQiOjEyMDd9&s=11822fe6ab2de36ee07cd74486dbdaf4&auto=format&fit=crop&w=1306&q=80 work hard)
# 19
# (https://images.unsplash.com/photo-1538157245064-badfdabb7142?ixlib=rb-0.3.5&ixid=eyJhcHBfaWQiOjEyMDd9&s=dfa50d5dd51b85f25ca03f2b2667752a&auto=format&fit=crop&w=500&q=60 sporty)
# 20
# name_list = ["career","family","indoor ex","outdoor ex","nature","material","function","classic","money_maker","value_contribute","energy_drink","fruit_fuice","workaholic","enjoyable","appearance","sporty","countryside","city","individual","teamwork"]
# link_list = [
#   "https://images.unsplash.com/photo-1507679799987-c73779587ccf?ixlib=rb-0.3.5&ixid=eyJhcHBfaWQiOjEyMDd9&s=2f2507356905735cb7d15583034c7faa&auto=format&fit=crop&w=1351&q=80",
#   "https://images.unsplash.com/photo-1510022079733-8b58aca7c4a9?ixlib=rb-0.3.5&ixid=eyJhcHBfaWQiOjEyMDd9&s=6da2c9e985e56b6a43209d7b1d46c8ca&auto=format&fit=crop&w=701&q=80",
#   "https://images.unsplash.com/photo-1534367507873-d2d7e24c797f?ixlib=rb-0.3.5&ixid=eyJhcHBfaWQiOjEyMDd9&s=d4b5ecbd9836b3db586d65cddbd06bab&auto=format&fit=crop&w=1350&q=80",
#   "https://images.unsplash.com/photo-1516902663607-8d25785663fe?ixlib=rb-0.3.5&ixid=eyJhcHBfaWQiOjEyMDd9&s=bc6788eaa314999002ccb4dc3f1ce190&auto=format&fit=crop&w=628&q=80",
#   "https://images.unsplash.com/photo-1502176747191-3354e2597a5f?ixlib=rb-0.3.5&ixid=eyJhcHBfaWQiOjEyMDd9&s=a47195ab105472213f9e589e92c2df74&auto=format&fit=crop&w=1036&q=80",
#   "https://images.unsplash.com/photo-1432611185496-76ccd1dc5efe?ixlib=rb-0.3.5&ixid=eyJhcHBfaWQiOjEyMDd9&s=481b134d4fc95af548cbddd67f0d6d6f&auto=format&fit=crop&w=800&q=80",
#   "https://images.unsplash.com/photo-1496171367470-9ed9a91ea931?ixlib=rb-0.3.5&ixid=eyJhcHBfaWQiOjEyMDd9&s=1296a4419a6c84e28281db0a564071ef&auto=format&fit=crop&w=1350&q=80",
#   "https://images.unsplash.com/photo-1536604673810-81370412626d?ixlib=rb-0.3.5&ixid=eyJhcHBfaWQiOjEyMDd9&s=3d8d7119042038472ff44dc29d29220d&auto=format&fit=crop&w=1266&q=80",
#   "https://images.unsplash.com/photo-1523430237819-5fdfeb4f5604?ixlib=rb-0.3.5&ixid=eyJhcHBfaWQiOjEyMDd9&s=f5314a7fa18a4ec6909d4cbda5687ada&auto=format&fit=crop&w=1237&q=80",
#   "https://images.unsplash.com/photo-1538992691511-a64e9c9034dd?ixlib=rb-0.3.5&ixid=eyJhcHBfaWQiOjEyMDd9&s=d9de182134a5109157f3366cb5f4a9ea&auto=format&fit=crop&w=1350&q=80",
#   "https://images.unsplash.com/photo-1542042179-1fc836a4089f?ixlib=rb-0.3.5&ixid=eyJhcHBfaWQiOjEyMDd9&s=be760a70b526370ef81e74c9c98f2ba2&auto=format&fit=crop&w=634&q=80",
#   "https://images.unsplash.com/photo-1534318002854-72e10bf140ed?ixlib=rb-0.3.5&ixid=eyJhcHBfaWQiOjEyMDd9&s=3a987deddb37a8045edc1db7e5a30baa&auto=format&fit=crop&w=634&q=80",
#   "https://images.unsplash.com/photo-1501876991173-f9c47cd28268?ixlib=rb-0.3.5&ixid=eyJhcHBfaWQiOjEyMDd9&s=11822fe6ab2de36ee07cd74486dbdaf4&auto=format&fit=crop&w=1306&q=80",
#   "https://images.unsplash.com/photo-1506377170913-e1d634babf96?ixlib=rb-0.3.5&ixid=eyJhcHBfaWQiOjEyMDd9&s=910fc1a8df066c995a13e7acc6bee6c0&auto=format&fit=crop&w=634&q=80",
#   "https://images.unsplash.com/photo-1536659492859-625ab2c75c4a?ixlib=rb-0.3.5&ixid=eyJhcHBfaWQiOjEyMDd9&s=789a9d004ca9a17c085f549ececf4a3c&auto=format&fit=crop&w=1498&q=80",
#   "https://images.unsplash.com/photo-1538157245064-badfdabb7142?ixlib=rb-0.3.5&ixid=eyJhcHBfaWQiOjEyMDd9&s=dfa50d5dd51b85f25ca03f2b2667752a&auto=format&fit=crop&w=500&q=60",
#   "https://images.unsplash.com/photo-1504955236898-44c735157f4f?ixlib=rb-0.3.5&ixid=eyJhcHBfaWQiOjEyMDd9&s=b2e933821d0ae3d8eb2cfa489037a30b&auto=format&fit=crop&w=1350&q=80",
#   "https://images.unsplash.com/photo-1430609098125-581618d0482f?ixlib=rb-0.3.5&ixid=eyJhcHBfaWQiOjEyMDd9&s=233388fe77509387a00a139deec2adde&auto=format&fit=crop&w=1350&q=80",
#   "https://images.unsplash.com/photo-1504780361545-d1ce834be3a9?ixlib=rb-0.3.5&ixid=eyJhcHBfaWQiOjEyMDd9&s=8c7df6cb3e6a79c23c68d8c08ccae8b9&auto=format&fit=crop&w=1489&q=80",
#   "https://images.unsplash.com/photo-1525422847952-7f91db09a364?ixlib=rb-0.3.5&s=da13a911783ae00ee9093e562c4a485e&auto=format&fit=crop&w=1365&q=80",
# ]
# point_list = [0,10,0,10,0,10,10,0,10,0,10,0,10,0,0,10,0,10,0,10]
# q = Question()
# q.save()
# while True:
#     i = (1,21)
#     name = name_list[i-1]
#     link = link_list[i-1]
#     point = point_list[i-1]
#     answer = Answer(name = name, link = link, point = point)
#     answer.save()
    
#     q.update(push__question=answer)
    


@app.route("/quiz")
def quiz():
    link_list = Answer.objects()
    link_list_list = []
    for i in range(0,20,2):
      link1 = link_list[i]
      link2 = link_list[i+1]
      link_list_list.append(link1)
      link_list_list.append(link2)
      return render_template("quiz.html",l1 = link_list_list[i],l2 = link_list_list[i+1])
  # elif request.method == "POST":
if __name__ == '__main__':
  app.run(debug=True)