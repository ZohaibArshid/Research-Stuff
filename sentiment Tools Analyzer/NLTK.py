# -*- coding: utf-8 -*-
"""
Created on Sun Jan 17 10:57:03 2021

@author: Zobi Tanoli
"""
import string
from collections import Counter
import re
import matplotlib.pyplot as plt
from nltk.corpus import stopwords
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.stem import WordNetLemmatizer
from nltk import word_tokenize
import nltk
from sklearn.metrics import classification_report
import csv
#nltk.download('wordnet')


'''


text = open('data.csv', encoding='utf-8').read()

lower_case = text.lower()
cleaned_text = lower_case.translate(str.maketrans('', '', string.punctuation))

print(len(cleaned_text))
  
# Using word_tokenize because it's faster than split()
tokenized_words = word_tokenize(cleaned_text, "english")

# Removing Stop Words
final_words = []
for word in tokenized_words:
    if word not in stopwords.words('english'):
        final_words.append(word)

print(len(final_words))

# Lemmatization - From plural to single + Base form of a word (example better-> good)
lemma_words = []
for word in final_words:
    word = WordNetLemmatizer().lemmatize(word)
    lemma_words.append(word)
    
print(len(lemma_words))   

#words = [w for w in nltk.corpus.state_union.words() if w.isalpha()]
finder = nltk.collocations.TrigramCollocationFinder.from_words(lemma_words)

#finder.ngram_fd.most_common(2)


sia = SentimentIntensityAnalyzer()
sia.polarity_scores("Wow, NLTK is really powerful!")

emotion_list = []
with open('emotions.txt', 'r') as file:
    for line in file:
        clear_line = line.replace("\n", '').replace(",", '').replace("'", '').strip()
        word, emotion = clear_line.split(':')

        if word in lemma_words:
            emotion_list.append(emotion)

print(emotion_list)
w = Counter(emotion_list)
print(len(w))




s=[]


'''


text='''
Such an easy app to use, really quick and easy to set up and had absolutely no problems with drivers.
The drivers and the services have been exceptional since ever.
All rides have been enjoyable.
Driver very knew where I was.
most driver's are child friendly and patient.
Quick and easy to use and drivers are quite friendly ðŸ˜Š.
I Love this App its easyâ˜®ï¸shows you the person who will drive for u and his Name too.
Best drivers ever.
Good travel with the app.
Cabs r clean & drivers too.
Love the rides.
Fast, affordable & efficient means to get to any destination in Nairobi.
Perfect transport.
But the rider are vey wicked there use to add money on it.
Its an easiest way to find a transport and its safer.
Safe to travel with.
Always a good ride and very good drivers.
The kids loved the spacious ride.
I enjoyed my ride.
Clean cars.
Best service and best prices.
Fast and convenient, friendly drivers with a smile.
I have never encounted any bad experience even the drivers are professional.
Most convenient way of moving around ever.
Nice ride's â˜ºï.
Always satisfied, and the drivers come on time.
Excellent rides and good driving skills been displayed.
My ride with bold and use of bolt had been nothing but exceptionally great.
Good driver ever.
Awesome and driver very good.
Other cars are super clean.
Great drivers; hospitable.
You dont wait longer than 15 mins I love it and the prices are reasonable.
Very efficient Drivers are awesome.
Great drivers and cars.
Its nice drivers are always friendly.
cheapeat rate in Saudi.
Drivers are always profesional.
They give you a waiting time, but it is never respected, and not by 1 min, or 2.
The drivers shouldn t be aloud to give impossible pickup time.
Generally okay but wait time could be better.
drivers are friendly and cars are clean.
As a regular user, they have definitely spiked the prices to be ridiculous amounts.
I requested for help on the app but still no reply.
Utterly disappointed Will be deleting my account with bolt.
Answer to CS  I already sent a message in the app.
Have recieved multiple emails of someone using my email address for their rides as there is no email verification etc would be extremely worried to use this service and put payment details into it.
I don't think i can trust the app again or request a cab it feels just feel bad.
This app keeps getting expensive by the day im gonna download uber once your drivers are even rude.
The last time I used this app it was terrible driver talks too much driver has a body odour the car was terrible and I even saw a cockroach in the car this is apparently the worse ride ever.
It a Kak application drivers cancel to much I can't take this any longer.
Some of your drivers they want this promotion for to pay with account they will tell you cancel i can't.
It looks like you guys don't care about the scam that happens with your drivers and u don't answer your built_in app support chat.
A driver who did NOT pick me up, said that he picked me up and drove all the way to my destination just to collect the money.
I wasn't happy cause it was my 1st time and it was suppose to be a free ride but i had to pay.
I lost my phone in a trip from a local mall to my home and when i phoned a few times the driver put of the phone.
The guy arrived, refused to come to the spot I actually requested him to come and then requested the journey as it was my friend not me even though I called him and confirmed her details.
I still got charged Â£8, 80 for a Â£5 journey because of 'waiting time' which kept adding up bevause he was not cancelling.
Drivers on this app are useless.
The app is not capturing the pickup point clearly thereby misleading the driver hence increasing the response time.
I recently had all my money withdrawn from my account.
You guys have a very wrong estimation of charges.
I normally select a bolt at CBD, telling me its a two minute wait time only to find out that the driver is in Westlands or south B for an instance.
Terrible ride sharing app.
Most times good and efficient but we getting more unclean drivers, dirty cars and rude drivers.
I(female) requested a ride yesterday (29 February 2020) around 10pm at night .
The driver came with a man sitting in the passenger side of his car.
The driver called me to get into his car and I refused.
Very efficient service, takes away any stress of booking a cab.
Thnks and nice trip.
LOVE their ride.
Their cars are always in good clean condition.
I have always had good, friendly drivers.
The prices are also always reasonable.
Fantastic ride.
Drivers are polite, trustworthy and very helpful.
Just sometimes prices are too high and too expensive for me.
Do you have a weekly service option we can use fro.
Drivers are respectful and humbe and finding a ride is so easy.
Response is highly recommended and drivers are accommodative to my wheelchair bound son,even thou cars are so small but they always make a way for us and the wheelchair.
Awesome and enjoyed my ride.
Best convenient for students and adults who are in need of transportation.
It okay pls just upgrade your Gps cos i on wifi for most of the drivers just to end my trip.
Safe travels.
The driver was just normal.
Great driver great music , love it.
Clean,,good driver and lower prices.
Nice app, the drivers are quick to response.
Pathetic, got charged over twice the estimated price (other taxi companies are able to provide estimates very accurately, I have never had 1 problem with uber in over 200 trips) , customer support came up with some poor excuse, complete nonsense.
Please cancel ny trip.
Taxify is a reliable way of transportation but recently they at every month end time they pick up the prices to ridiculously high amounts.
Some taxi drivers are extremely rude and disrespectful.
I don't understand why prices have to change on peak hours.
Drivers are very good at cancelling trips, Why accept then cancel.
Worked great for about 3 days, i use bolt to get to work and back, but now I can't seem to find a ride no matter what time of day or night.
The price is too much.
Then the driver promised to bring the phone back the next day.
Most drivers are very nice and ok with GPS.
Love this app it's safe, it quick, it reasonably in prices.
Despite a few hiccups the app is great nd the drivers are great too.
It's good having so many driver s, waiting time is less.
I once had a driver cancel my ride when the weather was very cold because I didn't know he was my taxi and not just another car parking as he drove further up from where I was waiting.
Very good app, always useful updates ment to to ease the user interface, the waiting time is quite approximate, could be improved.
Quality vehicles and good drivers.
Please work on your GPS.
For the company, the prices are better with good service.
My main complaint is the battery usage which can be 7 to 15 percent when it's not even being used, this is a problem.
Great app overall, although the Activities section is a little cumbersome.
Worst syncing of data.
Database is slow and clunky for contacts.
Poor sync.
VERY POOR SYNCHRONIZATION OF DATA.
Very slow to sync data, but ok app.
Just barely functional this app is extremely slow to load on start-up, sometimes taking up to 2 minutes just for the main screen to show up.
While you can import your contacts from your phone, it is manual.
Lay out very good, easy to use but it is so frustratingly slow.
I expected to manage my emails through the app as I do on the desktop version.
I can't check the analytics on Android app.
Nice app but can't find out how to log my calls(.
Also, I have to use discard menu, not simply click the left arrow icon on the header.
On the mobile app I actually have to type of the address manually which is a massive chore.
So I am just using the desktop app for adding companies.
You have to go find the listing again to to call report & schedule a new activity.
You can not see note and future activities easily from the phone when you are in the field to see if another rep is calling on a particular business already.
When any call in your BASE database comes IN or goes OUT, the Base app pops up a & asks if you want to call report.
That means no deals with products can be created.
Pipedrive simply will not allow a lead to fade into no man's land.
After any communication with a customer, it instantly forces me to create another activity so that Everyone has a next steps plan in place at all times.
I HIGHLY recommend the integration with Gmail.
The app works with Google Assistant as well, read out your tasks, take notes, logs incoming and outgoing calls to your contacts (if you want) and do much more.
Love the voice transcription function.
As soon as I speak with a client I'm able to add a note to their file upon handing up.
Helps me to keep track of all client updates.
Easy to use, captures everything, exports easily, Intuitive, Nice.
Pipedrive helps keep us on track with our customers.
Especially with followup on repeat sales.
Can easily add and remove seats as required.
it helps me coordinate my sales on it , activities ,contact , companies and many more , it's the best CRM I have ever used.
Keeps my deals on track and helps me manage my day.
Best ðŸ‘ðŸ’¯ for managing all business department activities.
Intuitive UI, makes it very easy to keep track of things without feeling too forced.
Pipeline approach for managing deals is exactly what our business needs.
Assists on keeping me in top of my deals and in touch with clients.
Seamless experience managing the full pipeline.
Killer feature caller ID and logging.
Its easy to us, the design makes it easy to see your pipeline status.
Brilliant sales funnel and pipeline, very user friendly, uncomplicated and seriously effective.
our implementation of PD cover sales and production so all custom field are visible across all pipelines.
we have 200+ custom fields so it can be time consuming for guys in the field to track down the field they need.
I'm able to see how my sales team is doing and better predict sales in addition tp providing better customer service.
I especially love that the software links to other services like mailchimp.
Poor sync.
Also good for tracking your teams performance.
Great app well sync and Google support.
Best and most intuitive sales pipeline tool I've used.
I love that I can click on a contact call them and it logs the call.
This ranked above the rest due to the great ux/ui and how well it works to automate, assign and convert prospects with its features.
The outgoing call feature is excellent but the text message button doesn't seam to connect with my android.
I very much like the automatic phone call log after each conversation.
Love the new call log feature.
Task and team management along with the sales and other activities.
I wanted something were I could easily see all my leads, whether or not there was a task assigned to the person  (which I could easily discern) and pipedrive delivered and at $12 a month so far I love it and I have actually picked up 3 clients that I had been neglecting because they "fell through the cracks" no complaints at this point, LOVE THE PRODUCT.
I had a simple question with something small regarding importing my contacts online and a lady on their support line not only helped me, but spent just under 2 hours on the phone with me 'holding my hand' showing me not only how the CRM worked, but the app.
They advertise integration with Outlook 365.
Works fine and has all the basic features, but didn't tell me it would hold my information hostage after the trial runsout with no way to export your data without paying.
It's so slow just like their desktop version.
I tried searching company wide and just myself.
The app itself is really good, but is extremely slow.
So slow.
Bad sinchronizing.
Installation is quick and easy, especially email.
It helps me keep organize the activities to follow up it makes repetitive info emails easy w templates.
i've been working with pipedrive for 2 weeks and till now it's been very useful on keeping track deals.
There are some functions, however, that are not as user-friendly such as attaching files (which must be done one at a time, cannot upload multiple files simultaneously.
I've come up with a functional workaround using tags, but it's cumbersome.
So I'm new to the CRM, seems like a great program so far, but here's my question  Just logged in with my Galaxy Tab S2, which I use in Landscape with a keyboard.
The second I logged in it switched me to portrait, which makes it unusable with the keyboard, and for me, my tablet as a whole.
Helps us in keeping a track of all leads.
Only if you open the profile or change to the view list.
The concept of tags, projects and folders is oh so incoherent.
Time selector is horrible, if you don't want to use timers and prefer registering manually, you'll make lots of mistakes.
You submit less important data is via "save" - it doesn't save anything, though, as the whole record is saved by "done".
You set report parameters by clicking outside modal.
Adding entries to the past is suddenly hard to find and weird to set its details.
Changing the date of entries is weirdly hard to find.
I keep accidentally starting new timers when I only want to view/review the details of existing entries, yet again I started a new timer, can we just revert back a year or so.
It does track time, but is non-intuitive.
It's quick to add in time entries which I appreciate.
Having to go in to the app each time to stop the timer is a bit of a hastle.
Time tracking is buggy.
-Tags are worthless since they don't stick when you restart a timer.
It's just tracker, but even to open it or add new task from previous, takes a lot of time.
And it uses hashtags in your text fields to trigger project names and description tags.
Turns out that I created a duplicate tag which caused validation errors.
Account needed even for quick try out.
It's time tracking, why can't we figure this out.
Not much help on how to use, didn't make any sense on tracking projects, as I was only able to create one project  Also I couldn't see calendar 8n typical monthly calendar format.
Perhaps, I didn't know the correct gestures on getting to do these tasks, but I didn't find this app intuitive.
App doesn't work offline.
I have to do refresh multiple times, it loads the tasks I added from the web slowly on device even on Wi-Fi connection.
Why i cant sign up .
Why is it acceptable to only target phones and not just phones but only portrait mode.
The apps main feature, tracking time, is sketchy at best, and if you are tracking important things like I was, I would definitely suggest looking elsewhere.
After all it's not usable for time tracking - which would be its primary function.
The ability to track my time on specific projects has helped give me the data necessary to bill for hours worked.
A little sluggish but still one of the best time trackers.
Login via Google.
Tracking different projects is easy with the tag system.
The reports system works exactly how I would want it to.
Love the new calendar feature.
Great platform, also a free account provides a useful professional time tracking experience.
I like the weekly reports and live syncing between devices.
It's to annoying that we must stay online with desktop browser to export report to PDF.
Also, dark theme finally works permanently.
It really changed the way I track my work.
Dark mode is working.
It can work online and offline.
Nice to use with the Toggl time tracking tool.
Unfortunately, the reporting is not as comprehensive as it is in similar apps.
No breakdown of time spent on specific tasks within projects.
Just uninstalled for the 2nd time, it doesn't always sync, hard to change clients, constant loading icon for no reason etc.
It bothers my OCD a little, and sometimes it prevents me from selecting the task I want to edit if it's underneath other tasks.
But finding a way to create a new project is awkward (almost hidden) and I couldn't create one, because it didn't do anything once I inserted all the info and pressed 'create'.
But apart from that Toggl is the best time tracker I've come across.
invoicing and categorizing work are very helpful.
UI/UX could improve a bit.
The idea behind the app is great, easy-to-use timers to track your work time.
Clean, simple interface makes it easy to read, edit, and add entries, and the button in the options menu (with WiFi, Bluetooth, etc), makes it even easier to track time on the move.
The calendar is the best way to double check.
This is a good time tracking app and I have really enjoyed using it.
On the whole it's inflexible, and doing anything to try to optimize your workflow with it just ends in frustration and arbitrary barriers.
For example, can I install this on my baby sitters phone to track her hours, with out using my own email and password in her phone.
I love this app for my time management.
I just hate haveing to retype everything repeatedly because its trying to predict what im typing, so it ends up deleting what i did type.
It gives you weekly reports.
I have been using toggl for years and at some points, I was even tracking my sleep hours with toggl.
It's easy to use, I don't waste time by tracking time ).
best free time tracker .
Love the chrome extension and the windows application.
I have tried other time trackers and this one is the best (for me).
It's a great help that you can link your calendars here.
I have mostly used the app in the event I forget to log out/track my day, and it's been very responsive.
Great time tracking ap.
This is Handy to have in case I leave a timer running.
Just good time tracker.
I miss the old function where you could pause your timer, rather than having to stop and restart for small interruptions.
A well designed and easy to use time tracker.
Best time tracking app for me.
Great free app for freelancers to track their time by client and project.
Great tool to track time.
Really helps you track the number of hours you're working.
This app helps me stay on track and calculate how many hours that are contributing to productivity.
This is a great app to keep track of your time.
I would recommend this to anybody that freelances our just wants to find out where their time is being spent.
User friendly and an easy way to track time, along with fun reports and a pomodoro add on.
Best time tracker.
This app has been great for tracking hours for my small business.
Awesome app to keep Track of time.
Best time management app.
Still using Toggl for time tracking, but the mobile experience has been awful.
Amazing tool for tracking time.
This app has given me some really needed insights.
The new version is really wonderful with its ability to not just register but also predict some of my activities.
Great app, I use it to keep track of my study ND personal project great.
Quick to use, nice data and charts.
I have been using it to track my time for few weeks now.
The calendar section of the app is exactly what I am looking for.
I use this for tracking just about every structured activity, not just client work.
Particularly having the widget to hand on the home screen and having the ability to auto populate previous activities, and stop and restart them.
I really like the weekly report summary that comes to me by email.
However, I can't figure out how to get this report on demand from the dashboard.
Helps a lot with timesheets, very easy to use as well.
Good timer UX among the other times i have used so far.
Easy-to-use time tracking app with web app and browser add-on.
simple time tracker easy to use.
A quick and easy way to track time.
Very functional for tracking and reporting hourly billing.
Makes keeping track of time very easy.
I have struggled with other time trackers but never had a problem using toggl.
How do I make it stay in dark mode alll the time though.
Absolutely essential app that lets me know where I'm at on hits towards a task per week.
I use this to track my part time studying and applying to jobs efforts.
Great app to track your progress, it helps me in tracking my new year resolutions.
Simple, intuitive and effective tracking of time spent on various projects and areas of work.
I particularly appreciate the integration with the Google Calendar on mobile and the Desktop App and the Chrome extension.
I track my time all day with Toggl.
I really like the calendar view where i can visually see my use of time over the day.
I now track 168 hours using Toggl.
This works exactly how I want it to, clearly made by people who've had freelance experience trying to track hours.
Super easy to quickly adjust a running timer if you happened to lose too much time to your sister calling in the middle of work.
Everything is very "one button, done" making time tracking as painless as possible.
Reports are helpful for quickly seeing how productive certain days are and getting project hour totals.
I am so grateful for being able to use this app to manage time â¤ï¸ thank you so much for creating this ðŸ™.
Super quick to load to start tracking.
It's easy to use and the ability to export time entries allows me to perform my own data analysis on my data.
That's my time recorder.
Usefull for time tracking.
Very useful to record bits of work done on the go.
Swapping and changing between several clients each day, Toggl has made invoicing clients so much easier.
I find it very helpful to time my hours put in for odd jobs and creative projects that i do.
Amazing time tracking tool.
Calendar integration is neat.
Great simple timetracker app.
Works well for lawyer and paralegal timekeeping.
This app has made tracking time at work so much easier.
Easist way to teack my time without hindering my workflow.
A great app for simple time keeping.
The only problem I have is the time it takes to load which makes it difficult to swiftly switch between tasks and update on Toggl.
Super intuitive and useful, especially when billing clients and helping me be more aware of how i use your time.
Handy tool for tracking time, creating reports, etc for multiple clients.
Simple to use, nice overview and task breakdown.
Toggl has been my go-to tool for tracking my effort at work over two years.
Effortless time tracking.
does exactly what I need, which is count time I spend on different tasks for clients.
Options to tag projects and clients seperately as well as timing Non billable hours is really helpful.
Well designed and easy to use time tracker with good integration between devices.
the UX is a little wonky in places (website is better) but it is amazingly useful to stnc up my timers across all my devices.
really helpful when it comes to personal tasks and time management.
So quick and handy for tracking work on complex projects.
Very low rate and costly to send in bangladesh and India.
It takes them couple of days to activate your account, the fees they charge are too big and their app is poorly designed.
A friend of mine recently sent me money from USA on Friday.
It used to be my favorite money transfer app, however it is in the last transfer so terrible.
They said I authorized them to credit the money directly to my borderless account.
It's a decend app but it's really annoying that sometimes the transfer takes 2 minutes and the other time 3 days no logic behind it.
The app is good, but they close my account with them for no reason, I can't tell why them deactivated my account.
Iv been using this app for a little over 6 months now for day to day spending, online transfers, direct debits and having my salary paid into.
But this morning iv woken up to an email saying my account has been deactivated all funds are locked for at least 60 days (all the money i need to live off at this moment) they are withholding any information on why my account has been closed down.
They claim they pay the highest rate but it is lie.
It is an excuse to charge higher fees.
this application is not working fine I made a transfer since three day now my transaction was cancelled and I requested for refund they reply me it will take up to 3 - 5 days to refund it back and they didn't refund it up still now TransferWise need to work on this here is my membership number (p8096266).
After nearly two years of transferring, my bank is no longer on your list.
Sorry we currently don't convert Malaysian Ringgit to PKR (OR ANY OTHER CURRENCY) WHAT IS THAT.
I was hoping to make all my international transfer using this but this is so disappointing.
I made 2 transfers on the 17th Feb using the app.
Sent money, and only after I paid app tell me that money will send yo reciever only after they check documents which is take 1-2 days, what for then you even let people send without verification.
Been trying to send money for the passed two hours and it's not very user friendly.
You signup and verify your account and when someone sends money to one of the borderless account .
You create and Account and verify it.
They will just deactivated your account without any notice.
I can't send money to my home country, is not included in the options.
Very odd process of estimating transfer cost and then defaulting to an unrelated transfer.
I really dislike having to contact the support to get my account closed.
someone hacked & tried to login to my #TRANSFERWISE account.
transferring money delays initially they promised an hour of transfer.
This application is  for my liking how can you guys just block someone with out a reason and customer care is frustrating, and my unpending transfer ow we i get my money back.
I made  multiple transfers totaling over 10k in euros.
Thanks for letting me know when I sent the money already.
After a week of transmitting my money the app confirmed that it was sent to the recipient.
Great way to transfer money between international and local accounts.
Wow awesome this good apps, I can shared my money to my family it's very fast with cheaper fee.
Excellent rates available.
Just requies 2 to 3 minutes to complete your transaction.
Great transfer/exchange rates.
Very convenient for sending money home once you get set up.
This app is the second app am using to send money to Nigeria and it is the fastest and best.
So so easy to use and really good rates.
Sending money back home has never been this easy and more efficient.
So easy to use, costumer service is brilliant and transfer money to any countries is cheaper than any banks.
Easy to use, excellent customer service and great rates.
I'm happy by this app very fast transfer and working excellent.
I recently transfered my tax return to the Philippines without any issues.
I have seen many negative issues but this last transfer sealed the deal for me.
Not only do they offer the best rates on the currency transfer market, they can be trusted with your hard earned money.
I was amazed by how promptly the money was transfered, within 4 hours.
I highly recommend this company for all your international currency transactions.
100 percent genuine, very good exchange rates and very rapid money transfer.
fastest transfers money from Aud to Thai baht.
Ideal for multi-currency accounts.
Very flexible and allows easy cross currency transactions your bank will normally gouge you on or take days to complete.
Knowing the rate you get removes all uncertainty and the rates are great.
Flipping between currencies is easy.
Best rate and efficiency.
After few feedback and they get back to me promply,i know its bit frustrating where some guide is availableðŸ˜.can trust this app for your money transfer via country now making a 2nd transfer due to covid-19 spreading without we notice and unable to travel home.
Have not used my card but I love that Green.
I just felt surprised, how efficient this platform to transfer money to other countries.
My experience is transferred money from Malaysia to Indonesia only took less than 8 hour until the money received by 3rd party.
And i dare to say this, the best exchange rate I ever seen compare to banks.
Easy to use and an excellent exchange rate.
Easy sending money, the app easy to use, good customer service, cheap fee and the best rate.
I frequently explore it to check FX rates.
So very simple to make transactions, it's scary.
I have used this app to transfer money to my brother in Sri Lanka.
Excellent app to transfer money.
Easy to use,transfer was quick enough and fee for transfer was reasonable.
I couldn't believe the speed of the transfer when I sent money last time to Sri Lanka.
Money was received in the same day in Sri Lanka.
It's clear to see what currencies you hold, and easy to convert when you see an exchange rate that you like.
Maybe I do not travel a great of a deal but it has made my life of exchanging money SO much more comfortable.
All transactions have been seemless.
I've even just opened a business account to run my business and clients through this too.
Well structured app, great rates and flawless execution.
Minimal fees and instant international transfers.
I hope I will give a 5 star in the future registration easy done ,,approved after less than 2 hours, email confirmation fast done,my card is on the way,,,(10 days,,,inside in Europe) everything looks smooth.
The best and most uncomplicated app for money transfer that I had dealed with.
Good app for transfer money abroad.
I like this app very fast transfer money when you send other account.
Very reasonable charge, up to date exchange rate and money gets transferred within minutes.
Very easy to use & reasonable rates.
Excellent rates and instant transfers enabled through Transferwise.
Perfect for all sort of transfers better and faster than bank transfer.
this is the best money sending app.
i always transfer money to south korea and i tried out other apps but they all either do not transfer to KRW or the bank account.
i've tried transferring money to other HKD & JPY as well, and they were all successfully sent.
verified payments fast & also transferred fast.
Really great and much better rates than traditional banks.
A great, cheap way of accepting payments from abroad, transferring money, and spending in other currencies.
This is the best ever current account since I have opened this account very happy 10 stars from Cristian Buzan very convenient app and customer support are in the top.
Great App.Easy to use with low tax rates.
The best money transfer app.
Great transfer rates and easy to use app.
I was worried because it was so easy, every other way I've tried to transfer money was difficult, complicated and expensive.
Love the low international fees.
Smooth Transactions, fair transfer fee's and very fast.
Doesn't matter whether weekends or weekdays, your get your money the same day ðŸ‘ðŸ‘ðŸ‘ Kinda hard during first transactions but after that, it was smooth sailing ðŸ‘ŒðŸ‘ŒðŸ‘Œ good job.
Nice It gives exact value for exchange and transfer fee is also good And it is quit fast.
4,000,000 limit not enough.
At least 20million per transfer when sending to Nigeria bank.
I like the way it gves you the progress of the transfer, so you know the status and you know exactly where your money is.
Nice app for overseas transactions.
Fast signup and verification and good transfer rates.
It's easy faster and secure app to send money it's very good app.
Very useful and best rate.
The Mastercard and virtual UK, POLISH, US account is absolutely wonderful.
Best Financial services for transfers worldwide.
Quick and easy to use and great rates.
I use my card to buy things and send money abroad too.
Very practical card and app.
Great app and easy to manage your money Sorry for incorrect comment previously.
Super fast internationals transfers at great clear rates with no hidden costs.
And to top it a free card and local bank account.
Have used many times, the first transaction takes a little long but since then I have not had a single problem.
Very good app, fast and secure transfer.
Being a frequent traveler and months of working in difirent countries every year Transferwise is by far the best thing that could happen to me for transfering my money to my accounts.
Easy to send money from another country.
Amazing, trustworthy, fastest, competitive rate Thankyou transferwiseðŸ˜ŠðŸ’ž.
Great way to transfer money between countries, without getting ripped off by the banks and their ridiculous rates.
this company is great for sending money.
quick transfers, less bureaucracy.
Amazing instant money transfer awesome.
Very easy use to the app and can send our money in fraction of second.
Very easy to use, lowest rates by far.
Good rate and fast.
It was fabulous My family received money some few minutes.
This is a good one for transfers your money in whole world.
Easy as once do afew transfers Great app.
Best ever money transfer app.
Just a heads up on weekends you will not get instant transfers.
The first transfer was smooth, however a bit slow, but so far I'm satisfied.
The best way to change my Eur to Huf.
Best and fastest way to send money across the world,with the best fees,if you choose fast transfer,it will arrive in a matter of hours not days.
Also you can get free bank accounts in TransferWise.
This is an awesome, transparent and clearly thought out application with the best rates you'll get.
(It even tells you if there's a better rate elsewhere) The application is not only intuitive but extremely impressive.
This is what money transfer should feel like.
Its really a best app to send money home.
The best and best app ever to send money overseas.
Borderless account is the bank account of the future, available today.
My first international transfer was so smooth and seamless.
Need to verify my ID.
Always loved the app, and now with Debit Card, really nice.
I can only edit the description.
Also, I would like to know if it's possible to edit a repeat transaction.
First transaction was good.
Everything else work fine (from notifications to reactivity).
Transferwise has good FX rates, especially compared to traditional banks.
Once bank account details are set-up it is easy to move currency around.
For example, each currency has two separate "add" and "convert" actions, but non of them can be used to convert *to* that currency using your TransferWise balance.
I haven't received my my debit card yet( requested 21st of January.
they brag about themselves on their debit card and hou cheap than any other company, but I just have no other way to use my money on transferwise's account.
Updated I ordered again and have received the debit card.
Is it possible to transfer money from India to Malaysia.
Overall good but still chargers are too high and exchange rate better but not so awesome.
Because on Sundays and Saturdays It does not transfer money.What if a fellow needs money on Saturday and Sunday in Emergency.
The transfer process is quick and smooth, and my money arrives right away.
Why can't I see my account details.
And why can't I see the bank details of my activities.
page where you choose the method of payment, presumably the higher the fee, the faster the delivery to your destination.
App experience is smooth for fast transfers, but they charges thrice the fee which they showed at the confirmation screen.
When I raised the support ticket, they are saying it's an international card.
With out customer consent or also not showing at confirmation screen how they can charge that huge fee.
Update, Sorry to say it was Never showed me the updated Fee, Only I got to know after completing the transfer.
iOS users can see incoming funds from the app.
If I try to add currency my bank sends an email with a verification code.
I want transfer money from India but it says the application is on beta.
Another thing is the minimum i could transfer is Rs 50k, you gotta be joking.
My MasterCard Platinum and Visa Gold from a Nigerian bank, which works without any issues in any operations, are not working with this app ***EDITED*** After reviewing the issue with both my bank and TransferWise none can explain why it happens (seems I'm the only one) So I could only make transactions of max.
500 doller at once through my debit card But still there is also a daily limit for debit cards of 2,000 doller, and also a 5 percent commission fee added to the payment, making imho the transactions not interesting through this service and I'm ending with same cost of a traditional transfer, or even higher.
Now you have to search for the logout button.
Lowest fees of any provider.
Easy to find valuable information and reviews as well as add reviews.
Perfect for travelers, I always look for places to eat here.
Good suggestions.
Easy to find the best deals in the area your going to whether its finding hotels, dining, or things to do.
How can an excellent Android app go from bad to worse to mediocre it's like a golfer changing his or her championship swing several times then not being able to break par again the tablet app is useless where are we to find one's saved trips or whatever.
This is now my travel buddy and always helps as reviews here are genuine by people so it helps you to choose better place till now whenever I compared and decided based on TripAdvisor I never regret keep up team.
I love using Trip advisor I post a lot of places where I've eaten and I also have found some amazing places to try other people have shared their experiences.
Always use this app for booking hotels and restaurants, especially on holiday.
Awesome app, helped us in booking best hotels, best day trip packs App reviews helped us to decide.
Sometimes it helps to choose best option among other options available with best cost and quality.
Very interesting to know what people think of resorts, hotels etc.
Love the restaurant rating feature.
Besides my wife's cousin, this is our favorite way to plan a trip.
This is my go to source for honest feedback and tips.
I tend to write reviews of places as I go, good or bad.
Very good app 2 have like 2 c persons different reviews of hotels apartments and destinations.
Great deals use it often.
Love using trip advisor as a tool to plan trips The forums are really useful.
I've found some of the best restaurants and hotels on this app.
always use the information provided to assess, and plan my destinations .
Gives unbiased reviews of places so I know what they're like before I go.
Always has places I want to check.
Really enjoy the reviews, is my go to source for lodging info while traveling.
Great place to look up new and exciting places to go.
I can always find great restaurants, hotels, and things to do.
Excellent app to plan your trip.
I planned by tours of Bali and Jaipur with the help of this app.
Very useful easy to navigate full of all the info you could ever need for planning an evening out with a loved one or booking a far away vacation for the family.
Great App, helped me alot to check oit giod deals for hotels and restaurants.
Great app to find things to do or where to stay.
So we use this app everywhere we go to find places to eat.
Great reviews great rooms.
Always honest opinions, and a great reviewer of hotels etc.
Excellent It gives clear cut vision of hotels ,places to visit ,what all are best we can visit.
Great place to find reputable vendors.
Excellent Information and easy comparison.
They'll even recommend other sites with cheaper rates.
Best app for hotels,places, restaurants and bars.
Love this this is my go to, especially forums and booking activities, very helpful.
I like having this easily distinguishable icon on my phone to quickly access all the info I need to find what I'm looking for and write an on the spot review, before I've forgotten.
The application provides user reviews that I read to find local eatery or attractions when I'm on vacation.
Very helpful hotel reviews.
When reading other reviews, I take both negative and overly positive reviews with a grain of salt.
Great that i can keep notes as wellðŸ˜Ž.
Always had good recommendations from real experiences.
Love to share both good and bad experiences on TripAdvisor.
Enjoy finding new places to go,things to do and places to eat.
Useful app to find restaurants and accommodation.
You just have to take some of the review with a pinch of salt.
Makes holidays so much easier to plan.
If you go for a meal, tour, show or shopping, you get the address and reviews so it takes out the unknown element.
This app makes finding a great place to eat so easy.
I always go to Trip Advisor to find accommodations and things to do in any place I plan on visiting.
Very easy to use and very useful when travelling to find good restaurants.
This app is great to use to plan your trips.
It tell you all the top attractions and give you reviews on restaurants and bars and other places you want to go.
Always great hotels prices restaraunts and any other help you need with the revewes.
I can choose restaurants that people have given good reviews and I can put my own reviews in so next time in that area I can remember which places were best.
Great app awesome information on trips and hotels etc.
For me, the most useful part is reading the travel forums where you get local expert's advice and answers to questions.
Informative and highly recommended for hotels and trip reservations.
for writing reviews, & reading other people's reviews regarding their opinions on places they've visited, dined at & stayed at.
I have found real gems (especially restaurants) this way.
I love the advices.
Very helpful when booking holidays.
I always check trip advisor reviews before I visit any place.
Love this hotel.
Easy to use and handy just to leave a brief description of one's experience at a location.
Always check this app and its reviews before I make a final decision.
It is very informative and reviews honest not filtered.
First time I used it I was led to many different restaurants to choose from in the city I was currently staying.
Love to use as a guide and the see whats going on Easy to use too.
Always use TripAdvisor when planning a trip.
The reviews and pictures are very helpful.
Great for finding restaurants and activities near you.
I enjoy the app when planning vacations and get-a-ways.
It's more than just hotel reviews.
I enjoy reading the reviews, recommdations and tips from others on the destinations.
Such a great help with finding local restaurants and hotels to stay at.
Fake reviews continue to appear.
We stayed in the Hotel Tuntas in Altinkum in Turkey attracted by reviews which I now realise are written by management and staff.
Dozens of one off reviews all phrased in a similar way with poor English constantly 'bigging up' the staff.
One so called English person seems to be there every few months for the last eight years and only writes reviews about the hotel Tuntas.
Sometimes you can even find a lower priced hotel offers here.
An every day tool while travelling or planning to travel.
One can easily find new places worth visiting.
I use this app to share my experiences to help others and to guide me in places I have never been to enhance my travel.
Thanks to all the reviewers, the reviews are really helpful when traveling to unknown places.
This is my go to when validating destinations for most travel; it adds a lot of great options by opening doors to new places and experiences.
My favorite feature is the "search this area" on the map for restaurants and hotels.
Great way to find and check out places.
Great app use it loads to find restaurants and hotels.
I highly recommend it for ALL your travel arrangements.
Use this app all the time to see where to go and which restaurant to book.
Doesn't work well if you don't give location permission.
I love traveling and so far this app is really helping me plan travel, learn different stuffs that I needed about specific places etc.
Reviews are perfect for help making the correct choice when going to an area you don't know.
Not user friendly enough, but very helpful for finding places to eat, wanted to leave a review for the hotel but there's no button for it, I guess you can review only if you got the hotel thru the app.
This site might not post your review and that shouldn't be The comment I made would be very helpful for anybody thinking of going to this restaurant.
Poor account settings.
Lots of promoted paid activities.
Abit hard to manage the business stuff.
It's a good app to discover the places, but the trip planning need some improvements and the app screen must be more clean.
Seeing them in reviews.
Love that you can be apart of Forums.
When I look at restaurants they compare then to those I have done reviews on.
When spending $$$$ you want to compare to other restaurants.
I need to take more time to leave review on places where I live.
Very good app for hotel and travel.
Very helpful when planning to book hotel or places to visit.
You save reviews as a draft and finish atca later date, but not now.
Good app for planning trips.
Fairly easy to use and a tool to use when researching places.
Honestly my favorite thing about this app is the ability to save places I want to visit on a particular vacation I'm planning.
I am also struggling to upload new reviews.
Have found great deals with this app.
Where ever i want to go, i check on trip advisor first to read the reviews.
Very helpful, this app serves as my reference for our family's hotel booking and trips.
Fairly easy to use I use it for out of state restaurants and fun places to go .
It has been smooth and i really enjoy the recommendations.
But the down side is that, the users may have the option to edit their reviews or posts.
Always use trip advisor before we go and always use it to review after we have been.
Highly recommended for planning trips etc.
The app helps me to manage my property and it also helps me to find the new trends in the world regarding travel and tourism.
Useful to share opinions.
Good for reviewing and reding reviews,.
I always check TripAdvisor reviews for any Hotel I book before I go on Holiday I think TripAdvisor is excellent.
Great advice for travellers.
I love the comments.
Great info for travel planning.


'''



tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')



sentences = tokenizer.tokenize(text)


s=[]





sid= SentimentIntensityAnalyzer()

for sentence in sentences:
    print(sentence)
    score = sid.polarity_scores(sentence)
    for key in sorted(score):
        print('{0}: {1}, '.format(key, score[key]), end='')
    #print(score)
    if score['neg'] > score['pos']:
        s.append('Negitive')
        print("Negative")
    elif score['neg'] < score['pos']:
        s.append('Positive')
        print("Positive")
    else:
        s.append('Neutral')
        print("Neutral")


print(s)
'''
with open("data.csv", "w", newline= "") as csvfile:
    writer = csv.writer(csvfile, lineterminator='\n')
    for row in s:
    #for i in range(len(senti6)):
        writer.writerow([row])
'''