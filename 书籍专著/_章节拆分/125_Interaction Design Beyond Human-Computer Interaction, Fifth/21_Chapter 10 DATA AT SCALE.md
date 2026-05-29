> 来源：Interaction Design Beyond Human-Computer Interaction, Fifth Edition (Helen Sharp, Jenny Preece, Yvonne Rogers)
> 原始文件：C:\Users\lenovo\Documents\Codex\2026-05-29\书籍专著\Interaction Design Beyond Human-Computer Interaction, Fifth Edition (Helen Sharp, Jenny Preece, Yvonne Rogers)\Interaction Design Beyond Human-Computer Interaction, Fifth Edition (Helen Sharp, Jenny Preece, Yvonne Rogers).md
> 识别方式：强章节标记

# Chapter 10 DATA AT SCALE

10.1 Introduction

10.2 Approaches for Collecting and Analyzing Data

10.3 Visualizing and Exploring Data

10.4 Ethical Design Concerns

## Objectives

The main goals of the chapter are to accomplish the following:

Provide an overview of some of the potential impacts of data at scale on society.

Introduce key methods for collecting data at scale.

Discuss how data at scale becomes meaningful.

Review key methods for visualizing and exploring data at scale.

Introduce design principles for making data at scale ethical.

## 10.1 Introduction

How do you start your day? How much data do you encounter when first looking at your smartphone, switching on your laptop, or turning on another device? How much do you knowingly create and how much do you create unknowingly? Upon waking up, many people routinely will ask their personal assistant, something like, “Alexa, what is the weather today?” or “Alexa, what is the news?” or “Alexa, is the S-Bahn train to Schönefeld Airport running on time?” Or, they will ask Siri, “What is my first meeting?” or “Where is the meeting?”

Having oriented themselves for the day, people will walk a few blocks to the subway entrance, dip their Metro Card in the turnstile to pay the fare, exit the station at their stop, grab their favorite morning beverage at a nearby cafe, and proceed to their office where they check in with the employee card at a security gate and take the elevator to their floor.

These are just a few of the things that many of us do to start our workdays. Each activity involves creating, searching, and storing data in some way or another. We may know that this is happening, we may suspect that it is happening, or we may be totally unaware of the data that we are generating and with which we are interacting.

There is also increasing concern about exactly what data is collected about us through personal assistants such as Amazon Echo, Google Home, Cortana, and Siri. We also know that many large cities, such as New York and London, have an enormous number of surveillance cameras (CCTV) spread around, especially in busy places such as subway stations and shopping malls. The video footage from these sources is kept for two weeks or more. Similarly, we experience being checked into an office, so we know that our movements are being tracked by security personnel. Our activities are also being tracked more surreptitiously through the technology that we use such as smartphones and credit cards.

What happens to all the data collected about us? How does it improve the services provided by society? Does it make traveling more efficient? Does it reduce traffic congestion? Does it make the streets safer? Moreover, how much of the data collected from our smartcards, smartphone Wi-Fi signals, and CCTV footage can be tracked back to us and pieced together to reveal a bigger picture of who we are and where we go? What might that data reveal about us?

Data at scale, or as it is often called big data, describes all kinds of data including databases of numbers, images of people, things and places, footage of conversations recorded, videos, texts, and environmentally sensed data (such as air quality). It is also being collected at an exponential rate; for example, 400 new YouTube videos are uploaded every minute, while millions of messages circulate through social media. Furthermore, sensors collect billions of bytes of scientific data.

Data at scale has huge potential for grounding and elucidating problems, and it can be collected, used, and communicated in a wide variety of ways. For example, it is increasingly being used for improving a whole range of applications in healthcare, science, education, city planning, finance, world economics, and other areas. It can also provide new insights into human behavior by analyzing data collected from people, such as their facial expressions, movements, gait, and tone of voice. These insights can be enhanced further by using machine learning and machine vision algorithms to make inferences. This includes people's emotions, their intent, and well-being, which can then be used to inform technology interventions aimed at changing or improving people's health and well-being. However, beyond societal benefits, data can also be used in potentially harmful ways.

As mentioned in Chapter 13, “Data Gathering,” and Chapter 9, “Data Analysis,” data can be either qualitative or quantitative. Some of the methods and tools used to collect, analyze, and communicate data can be carried out manually or using quite simple tools. What makes this chapter on data at scale different is that it considers how huge volumes of data can be analyzed, visualized, and used to inform new interventions. While having access to large volumes of data enables analysts, designers, and researchers to address large, important issues such as climate change and world economic issues, assuming that there are tools to do this, they also raise a number of user concerns. These include whether someone's privacy is being violated by the data being collected about them and whether the data corpora being used to make decisions about people, such as the provision of insurance and loans, are fair and transparent.

Furthermore, the combination of vast amounts of data from many sources and the availability of increasingly powerful data analytic tools to analyze that data is now making it possible to discover new information that is not available from any single data source. This is enabling new kinds of research to be conducted for understanding human behavior and environmental problems.

## 10.2 Approaches to Collecting and Analyzing Data

Collecting data has never been easier. What is challenging is knowing how best to analyze, collate, and act upon the data in ways that are socially acceptable, beneficial to society, and ethically sound. Are there certain rules or policies in place on what to reveal about people or when certain patterns, anomalies, or thresholds are reached in a data stream? For example, if people-tracking technology is used at an airport, how is that revealed to those at the airport? Is it enough only to show data that can help manage people flows and bottlenecks? For example in an airport terminal showing a public display in which one section of the terminal is detected to be much busier than another (Figure 10.1), do travelers ever stop and wonder how this data is being collected? What else is being collected about them? Do they care?

![](../../Interaction Design Beyond Human-Computer Interaction, Fifth Edition (Helen Sharp, Jenny Preece, Yvonne Rogers)/images/881608447f4a03f538133331964edc5761fecabd5ffb37d0b857e0f7174dcded.jpg)  
Figure 10.1 Heathrow Airport Terminal 5 Public Display in top-right corner of image showing the relative level of activity using an infographic of North vs. South Security

Source: Marc Zakian / Alamy Stock Photo

Another technique for analyzing what people are doing on websites and social media is to examine the trail of activity that they leave behind. You can see this by looking at your own Twitter feed or by looking at someone else's whom you are following, for example, a friend's, a political leader, or a celebrity. You can also examine discussions about a

particular topic such as climate change, reactions to comments made by comedians like John Oliver or Stephen Colbert, or a topic that is trending on a particular day. If there are just a few posts, then it is easy to see what is going on, but often the most interesting posts are those that generate lots of comments. When examining thousands or tens of thousands of posts, analysts use automated techniques to do this (Bostock et al., 2011; Hansen et al., 2019).

## 10.2.1 Scraping and “Second Source” Data

One way to extract data is by “scraping” it from the web (assuming that this is allowed by the application). Once the data is scraped, it can be entered into a spreadsheet for study and analyzed using data science tools. The focus from an interaction design perspective is how one can interact with that data and the way it is displayed rather than the actual scraping process per se, so that it can be analyzed and sense can be made of it.

In addition, the openly available big data that Google and other companies now provide for researchers to mine offers a “second source” methodology, meaning search terms, Facebook posts, Instagram comments, and so on. Analysis of this data can indirectly reveal new insights about the users' concerns, desires, behaviors, and habits. For example, the Google Trends tool can be used for exploring and examining the motivation behind what people ask when they type something into Google Search. Seth Stephens-Davidowitz (2018) has used it extensively to reveal what people are interested in finding out. From his analysis of Google Search data, he discovered that people type into the search box all sorts of intimate questions about their health among other topics. Moreover, he found that his analysis of search data revealed things that people would not freely admit to when asked using other research methods, such as surveys and interviews. He also makes an important assertion: to obtain new insights from big data, it requires asking the right questions of the data. Furthermore, it is not how much data can be collected or mined but what is done with the new data that has been made available. Simply mining it because there is a tool available may yield surprising results, but well-honed questions that guide and are used to interpret the data that is found will be more valuable (see Chapter 13, “Data Gathering”).

How do researchers know what are the right questions to ask of this data? This is particularly pertinent for HCI researchers to understand, especially in terms of how users will relate, trust, and confide in the next generation of technologies, including domestic robots, bots, and virtual agents.

## ACTIVITY 10.1

What insights do Google Trends searches tell us about ourselves?

Go to Google Trends (https://trends.google.com). Then try typing into the search box statements such as “I hate my boss,” “I feel sad,” or “I eat too much.” See how many people have typed this into Google over the last month, year, and for different countries. Then type in the opposite statements: “I love my boss,” “I am happy,” or “I never eat enough.” How do the results compare? Which is asked more often?

Then type in your name and see what Google returns.

## Comment

It is surprising how many people confide such personal statements in Google. Some people will tell it anything. Google Trends provides a way of comparing the search data across time, country, and other topics. When you type in your name (unless you have the same name as a famous person), it often comes back with “hmm, your search doesn't have enough data to show here.”

## 10.2.2 Collecting Personal Data

Personal data collection started becoming popular through the quantified-self (QS) movement in 2008 where monthly “show and tell” meetings were organized to enable people to come together to share and discuss their various self-tracking projects. Nowadays, many apps and wearable devices exist that people can buy off the shelf, which can collect all sorts of personal data and visualize it. These results can be matched against targets reached, and recommendations, hints, or tips can also be provided about how to act upon it. Many apps now come prebundled on a smartphone or smartwatch, including those that quantify health, screen time, and sleep. Some also allow multiple activities to be tracked, aggregated, and correlated. The most common types of apps are for physical and behavioral tracking, including mood changes, sleep patterns, sedentary behavior, time management, energy levels, mental health, exercise taken, weight, and diet. A common motivation for deciding to embark on tracking some aspect of one's personal data over time is to see how well they are doing compared to a set threshold or level (that is, a set target, a comparison with the week before, and so on). The aggregate data may raise awareness and be revealing to the extent that someone feels compelled to act upon it (for example, changing their sleeping habits, eating more healthily, or going to the gym more regularly).

Self-tracking is also increasingly being used by people who have a condition or disease as a form of self-care, such as monitoring blood glucose levels for those who have diabetes (O'Kaine et al., 2015) and the occurrence of migraine triggers (Park and Chen, 2015). This kind of self-care monitoring has been found to help people engage in reflection when looking at their data and then learning to associate specific indicators with patterns of behavior. Making these connections can increase self-awareness and provide them with early warning signs. It can also lead them to avoid certain events or adjust their behavior accordingly. Many people are also happy to share their tracked data with others in their social networks, which has been found to enhance their social networking and motivation (Gui et al., 2017).

Quantified-self projects generate lots of data. New kinds of health data can now be collected by mobile health monitors, such as heart rate, generating masses of data per person each month, which was simply heretofore unavailable. This raises questions as to how much data should be kept and for how long? Also, how can this data be used to best effect? Should it signal to the user when their heart rate deviates from normal levels? Given that masses of data are being collected from many individuals using the same

devices, it is possible to collate all of the data. Would it be useful for health clinicians and the individuals alike to have access to all of this data in order to see trends and comparisons? How can this be made to be both informative and reassuring? Translating someone's heart rate data that is sampled many times per second along with their electroencephalogram (EEG) streamed brainwave data into an early warning sign with an appropriate form of intervention is challenging (Swan, 2013). It can easily lead to increased anxiety. Much thought needs to go into providing information into an interface that will not cause unnecessary panic. New tools should also provide flexibility in how the user might want to customize or annotate their data to meet their specific needs (Ayobi et al., 2018).

## 10.2.3 Crowdsourcing Data

Increasingly, people crowdsource information or work together using online technologies to collect and share data. The idea of a crowd working together has been taken one step further in Crowd Research, where many researchers from all over the world come together to work on large problems, such as climate science (Vaish et al., 2018). The goal of this approach is potentially to enable hundreds of people to contribute, through collecting data, ideating, and critiquing each other's designs and research projects. Conducting research on a massive scale enables potentially hundreds or thousands of people to work on a single project, which can help address large problems, such as migration or climate change at scale.

There are also many citizen science and citizen engagement projects (see Chapter 5, “Social Interaction”) that crowdsource data at scale and in doing so amass billions of different types of data (photos, sensor readings, comments, and discussion), which are collected by millions of people across the world. Most of this data is stored in the cloud as well as on local machines. Examples of large citizen science projects include iSpotNature, eBird, iNaturalist, and the Zooniverse. There are also thousands of much smaller projects that together generate huge amounts of data.

eBird.org, for example, collects data about bird sightings that is contributed by naturalists—amateurs ranging from beginning birders to highly experienced expert birders and professional scientists. The site was launched in 2002 as a collaboration effort between Cornell University's Lab of Ornithology and the National Audubon Society. The data includes bird species data, the abundance of each species, geolocation data indicating where observations are made, profiles of the people who contribute, comments, and discussion. There are also smartphone apps and a website with links to many resources, including identification guides, data analysis tools, maps and visualizations, reports, and scientific articles. As of June 2018, there were more than 500 million bird observations recorded in a global database. eBird feeds data into aggregator sites such as the Global Biodiversity Information Facility (GBIF) so that it is available for scientists. It also provides several maps, many of which are interactive (see Figure 10.2) and other graphic representations of its data that are available for anyone to access.

![](../../Interaction Design Beyond Human-Computer Interaction, Fifth Edition (Helen Sharp, Jenny Preece, Yvonne Rogers)/images/47e93e3d808df4e6fa35252303174e78e1e1ce6894c9abaae361a1e07706fb46.jpg)

Figure 10.2 Abundance map for the common raven. The darkest area indicates where ravens are most abundant.

Source: https://ebird.org/science/status-and-trends/comrav. This link will allow you to see how abundance changes during each week of the year (purple indicates high abundance and yellow indicates low abundance).

Crowd projects raise a number of issues as to who owns and manages the data. This is especially pertinent when the data collected can be mined to unearth details about the people who contribute the data as well as about the endangered species, for example. For researchers and UX designers, there are interesting questions about how to balance making data available for education and research while protecting the privacy of those contributing the data and the location of endangered species in this example. Box 10.1 discusses how one citizen science project, iNaturalist.org, tries to manage this balance.

## Citizen Science and UX Design for Privacy

How privacy is interpreted by citizen scientists and their desire and need for privacy regulations differs across projects (Bowser et al., 2017). Being able to share citizen science data has many advantages as well as some privacy concerns. For example, participants can see what others are observing in their area. Bird enthusiasts also often like to share first sightings, for instance, when the first swallows appear in spring or the first snow geese arrive in winter. They may also want to check identifications with each other. The downside of this community interaction is that personal profile and location data can be used to identify particular contributors and their patterns of behavior. The latter can be especially problematic, as many participants visit the same places regularly. It is, therefore, important to ask how important is privacy in citizen science compared with the benefits of community engagement? And how might UX design help protect both participants and rare species, while supporting open engagement?

Many citizen science projects and societies post privacy policies like the one shown in the following link. Other strategies involve making images and locations fuzzy so that they are not exact. This is also a good strategy for keeping the location of rare species' observations confidential. For example, iNaturalist.org has a geoprivacy setting that can be set to “open,” “obscure,” or “private.” Obscured observations are used to hide the exact location of endangered species, as shown in Figure 10.3.

![](../../Interaction Design Beyond Human-Computer Interaction, Fifth Edition (Helen Sharp, Jenny Preece, Yvonne Rogers)/images/669e0165e49c409f04748ece267d16d53ce0630b66c60dbd5df542baaac06f5d.jpg)  
Figure 10.3 iNaturalist.org geoprivacy obscures the location of an observation.

In the above example: 1. EN indicates that the organism is endangered, so its location needs to be obscured, 2.   
indicates that obscuring is done by randomly placing the marker for the location within the broader area, and 3.   
allows the contributor to verify that this observation has been observed within iNaturalist.

Source: https://www.inaturalist.org

The European Citizen Science Organization's Data and Privacy Policy can be seen at https://ecsa.citizen-science.net/about-us/privacy-policy.

## BOX 10.2

## A Human-Data Design Approach to Sensing Data

There are a number of off-the-shelf sensor toolkits available now that can be placed in someone's home or local community to measure air quality or other aspects of the environment. One of the earliest open platforms developed was Smart Citizen (Diez and Posada, 2013). A compact device was built with a number of embedded sensors in it that could measure nitrogen dioxide $\left( \mathrm { N O } _ { 2 } \right)$ , carbon monoxide (CO), sunlight, noise pollution, temperature, and humidity levels. The data being collected from the platform was connected to a live website that could be accessed by anyone. The various data streams were presented via a dashboard using canonical types of visualisations, such as time-series graphs (see Figure 10.4a). Data streams from other Smart Citizen devices, set up throughout the world, could also be viewed via the dashboard (https://smartcitizen.me/) making it easy to compare data collected from different locations. While the mass of environmental data accumulating was fascinating to data scientists and researchers, this was not the case for many of the householders who had set up a smart citizen device in their home. They found the visualizations presented via the dashboard to be difficult to understand and were unable to connect the data being sensed with what was happening in their homes (Balestrini et al., 2015). As a result, they did not find it useful and quickly stopped looking at it.

![](../../Interaction Design Beyond Human-Computer Interaction, Fifth Edition (Helen Sharp, Jenny Preece, Yvonne Rogers)/images/d2b37c05c3654fdd1e2760fdc8affe7c59d4c56bc135a0d4aeb0ce7077955e0c.jpg)

Figure 10.4 (a) Smart Citizen's dashboard and visualization, (b) a PhysiMove cube set up in a householder's home, and (c) the components of the Physikit toolkit (Houben et al., 2016).

Source: (a) https://www.citizenme.com, (b) and (c) Yvonne Rogers

The Physikit project took this user problem as its starting point (Houben et al., 2016). A human-data design approach was adopted; the goal is to transform sensed data being collected into something that is meaningful to the general public. The goal is to provide a way of enabling users to engage with their sensed data, by giving it a physical ambient presence in the location where it is being collected. A set of colorful physical cubes were designed that could light up, move parts or vibrate, depending on how they were configured (see Figure 10.4c). Householders could easily configure a set of rules to decide which cubes to connect with which data streams and what each cube should do depending on levels or thresholds being sensed. This was intended to let them select aspects of their home that they were interested in knowing more about.

For example, one of the PhysiCubes had a rotating disk on the top that could be set to move clockwise or counterclockwise and at different speeds. One household decided to use it to measure the level of humidity in their kitchen throughout the day. They placed a basil plant on top of the cube (see Figure 10.4b) as a way of visibly showing the level of humidity in the kitchen. The rule they set up for the cube was for it to rotate only if the humidity level detected was below 60 percent. At the end of each day, they could tell how humid it had been in the room by the extent to which the plant remained upright. If it was leaning toward the window, this suggested to them that the humidity level in the kitchen had been high throughout the day because the disk had not moved the plant around for the leaves to get an even amount of light. The household, had in effect, created a naturally growing physical visualization that held historical data.

## 10.2.4 Sentiment Analysis

Sentiment analysis is a technique that is used to infer the effect of what a group of people or a crowd is feeling or saying. The phrases that people use when offering their opinions or views are scored as being negative, positive, or neutral. The scales used vary along a continuum from negative to positive, for example, –10 to +10 (where –10 is the most negative, 0 is neutral, and +10 is the most positive). Some sentiment systems provide more qualitative measures by identifying if the positive or negative sentiment is associated with a specific feeling, for example anger, sadness, or fear (negative feelings) or happiness, joy, or enthusiasm (positive feelings). The scores are extracted from people's tweets and texts, online reviews, and social media contributions. Their facial expressions (see Chapter 6, “Emotional Interaction”) when looking at ads, movies, and other digital content and customer's voices can also be analyzed and classified using the same scales. Algorithms are then applied to the labeled data in order to identify and classify them in terms of the level of effect that has been expressed. There are a number of online tools that can be used to do this, such as DisplayR and CrowdFlower. MonkeyLearn provides a detailed tutorial on sentiment analysis

(https://monkeylearn.com/sentiment-analysis/).

Sentiment analysis is commonly used by marketing and advertising companies to decide on what types of ads to design and place. In addition, it is increasingly being used in research to study social science phenomena. For example, Veronikha Effendy (2018) used sentiment analysis to study people's opinions about the use of public transportation from their tweets. In particular, she was interested in determining what were the positive and negative opinions toward it, which could then be used as evidence for making a case on how to improve public transportation to increase its use in Indonesia, where there are huge traffic congestion problems.

However, sentiment analysis as a technique is not an exact science and should be viewed more as a heuristic than as an objective evaluation method. Giving a word a score from −10 to +10 is quite a crude way to measure. To assess how good sentiment analysis is as a method, Nicole Watson and Henry Naish (2018) compared human judgment with computer-based sentiment analysis for evaluating positive articles about the U.S. economy. They found that the computer was more often wrong than right compared with the human participants. Their analysis indicates that humans express their optimism about a topic in much richer ways. Moreover, it also shows that by focusing on emotive words in phrases, sentiment analysis misses the nuances of expression that humans understand intuitively. For example, how would sentiment analysis score the phrase written by a teen in a text to their friends that said, “I am weak”? It would probably give it a negative score. In fact, the phrase is teen slang for “That is funny,” which is completely the opposite.

## 10.2.5 Social Network Analysis

Social network analysis (SNA) is a method based on social network theory (Wellman and Berkovitz, 1988; Hampton and Wellman, 2003) for analyzing and evaluating the strength of social ties within a network. While understanding social ties has been a strong interest of sociologists for many years, (for example, Hampton and Wellman, 2003; Putnam, 2000), as social media became increasingly successful, it also became a key interest for computer and information scientists (for example, Wasserman and Faust, 1994; Hansen et al., 2019). They want to understand the relationships that form among people and groups within and across different social media platforms, and with offline social networks too. Online, trillions of messages, tweets, pictures, and videos are posted and responded to every second of every day via Weibo, Tencent, Baidu, Facebook, Twitter, Instagram, and YouTube. Some examples include families posting pictures of their kids' birthday parties and family outings, discussion of hot political issues, and friends and colleagues chatting and keeping in contact with each other's travel experiences, hobbies, life's challenges, and successes.

Social network analysis enables these relationships to be seen more clearly. It helps to reveal who is most active in a group, who belongs to which groups, and how the groups do or do not interact and relate to each other. Analyses can also show which topics are hot and throw light on when, how, and why some topics go viral. Managers, marketers, and politicians are especially interested in how these activities can influence them, their companies, and their constituents. Many other people like to try to make their posts or YouTube videos go viral, as discussed in Chapter 5.

So, how does social network analysis work? It is a big topic, but broadly, as the name suggests, a network is a collection of things and their relationships to each other. A social network is a network of people and groups with relationships to each other. Human beings, like other primates, have formed networks for as long as our species has existed. Many other species, such as elephants, wolves, and meerkats, to name just a few, also rely on social networks for safety, for collaboratively rearing their young, and when foraging or hunting for food.

Two main entities make up a social network. Nodes, which are also sometimes called entities or vertices, represent people and topics. The connections between the nodes are called edges, which are also known as links or ties. The edges show the connections among nodes, for example, the members of a family. They can show the direction of relationships; for instance, parents may have a line with an arrow-head that points to their children, indicating the direction of the relationship between the two nodes. Similarly, an arrow in the opposite direction indicates that children have parents. These are known as directional edges. Edges can also indicate relationships in both directions by having arrows at each end. Edges that do not have an arrowhead are nondirectional; that is, the direction of the relationship between two nodes is not shown.

Drawing on algorithms and based in statistics, social network analysis offers a range of metrics for describing the properties of networks. One of the most important sets of metrics for visualizing networks in big data is measures of centrality. Several different measures of centrality exist based on different statistical formulae. These and other metrics are used to create visualizations like the ones shown in Figure 10.5 that show overlapping clusters. The clusters indicate voting patterns by members of the U.S. Senate in 1989, 1997, and 2013. Red represents Republicans, and blue represents Democrats. The graphs indicate how, over almost 25 years, the voting behavior of members of the two parties has become increasingly siloed, with fewer and fewer members voting with members from the other party. The nodes representing members on the far right and far left are only connected to the nodes of senators in their own party, indicating that they don't vote with members from the other party. The nodes in the middle indicate that those members sometimes vote with members of the other party. From being united on some issues back in 1989, bipartisan voting behavior has decreased over the years as indicated by the social network graphs. By 2013, few members of the two parties voted with members from the other party.

![](../../Interaction Design Beyond Human-Computer Interaction, Fifth Edition (Helen Sharp, Jenny Preece, Yvonne Rogers)/images/9e1e4e27faa36c7dbc42327243090e1f05ce2f3e68e0d4c26de3fbecb5e55262.jpg)  
Figure 10.5 Voting behavior of U.S. Senators in 1989, 1997, and 2013. Red represents Republicans, and blue represents Democrats.

Some other topics that have been studied using social network analysis include communication during the flood in Louisiana, where Jooho Kim and Makarand Hastak (2018) examined the role of social media in flood victims' communication, both with each other and with emergency services. They found that Facebook was used particularly effectively to disseminate information. Other studies include one by Dinah Handel and her colleagues on teachers' tweets on Twitter (Handel et al, 2016), and Diane Harris Cline has used social network analysis for a number of studies to examine the relationships between historical characters (Cline, 2012). In addition, there are many other examples related to a diversity of topics, including business communication, and even the relationships and activities of characters in Shakespeare's plays (Hansen et al., 2019). Revealing as many of these social network graphs are, using the tools effectively to separate and display clusters, outliers, and other network features takes practice. However, increasing attention to the UX design and support provided by such tools enables beginners to do straightforward analyses. Two of the most well-known social network analysis tools are NodeXL (Hansen et al., 2019), which runs on Windows-based machines, and Gephi, which runs on both Windows and macOS. Many YouTube videos are available that describe how to use these tools.

This video is an introductory tutorial about Gephi (2016) by Jen Golbeck, professor at the University of Maryland. It is one of a series, so if you continue watching at the end of the video, the next one progresses to describe more advanced features of Gephi, including how to use color to highlight particular features of interest in the network graphs: https://www.youtube.com/watch?v=HJ4Hcq3YX4k.

In this YouTube video, Marc Smith, a sociologist and director of the Social Media Foundation, shares with the relationship mapping workgroup how he has used NodeXL for social media network analysis and visualization: https://www.youtube.com/watch?v=Ftssu\_5x7Zk.

## DILEMMA

## How to Probe People's Reactions to Tracking

There is often a gulf between the benefits provided to society through tracking and the level of individual privacy that is being sacrificed. It is important, therefore, to have an open debate about the costs versus the benefits of using future tracking and monitoring technologies. Ideally, this should take place before any deployment of the new technology. However, just asking people what they think about a future tracking technology may not reveal the true extent of their concerns and feelings. What other methods could be used? One approach is to use a provocative probe.

For example, a project called the Quantified Toilets did this by setting up a fake service in a public place to disrupt the accepted state of affairs. The team was interested in how a community would react to having their urine analyzed in a public toilet with the goal of improving public health. They pretended to be a commercial company called the Quantified Toilets, which had created a new urine analysis technology infrastructure and installed it in the public toilets at a convention center. Signage was placed throughout the public toilets at a convention center explaining the rationale for the initiative (see Figure 10.6). In addition, the team created a website (quantifiedtoilets.com) that presented fake real-time data feeds from each of the toilets in the convention center showing the results of the urine analysis, including details such as blood alcohol levels, drugs detected, pregnancy, and odor (see Figure 10.7). All sampled data were anonymized. In addition, a link to a survey was added, and the general public was invited to give their feedback.

Access your live data at quantifiedtoilets.com

Quantified Toilets

![](../../Interaction Design Beyond Human-Computer Interaction, Fifth Edition (Helen Sharp, Jenny Preece, Yvonne Rogers)/images/0ef24690ebd9d431f3b211307f1d27b6a03c5df77cbcea5727aa54e5b341925f.jpg)

Figure 10.6 Signage posted in the convention center Quantified Toilets Source: Used courtesy of Quantified Toilets
<table><tr><td colspan="10">Recent anonymized random data feed</td></tr><tr><td>Time</td><td>Toilet ID</td><td>Sex</td><td>Deposit</td><td>Odor</td><td></td><td>Drugs Blood alcohol detected</td><td>Pregnancy</td><td></td><td>Infections</td></tr><tr><td>09:39:34 AM</td><td>T205</td><td>female</td><td>205ml</td><td>neutral</td><td>0.061%</td><td>no</td><td>no</td><td>none</td><td></td></tr><tr><td>09:33:20 AM</td><td>T109</td><td>female</td><td>175ml</td><td>neutral</td><td>0.054%</td><td>no</td><td>no</td><td></td><td>none</td></tr><tr><td>09:23:07 AM</td><td>T706</td><td>female</td><td>185ml</td><td>nutty</td><td>0.000%</td><td>no</td><td>no</td><td></td><td>none</td></tr><tr><td>09:19:02 AM</td><td>T715</td><td>female</td><td>75ml</td><td>neutral</td><td>0.000%</td><td>no</td><td>no</td><td></td><td>none</td></tr><tr><td>09:18:07 AM</td><td>T704</td><td>female</td><td>100ml</td><td>neutral</td><td>0.000%</td><td>no</td><td>no</td><td></td><td>none</td></tr><tr><td>09:11:56 AM</td><td>T706</td><td>female</td><td>80ml</td><td>neutral</td><td>0.000%</td><td>no</td><td>no</td><td></td><td>none</td></tr><tr><td>09:07:09 AM</td><td>T211</td><td>male</td><td>150ml</td><td>neutral</td><td>0.001%</td><td>no</td><td>no</td><td></td><td>gonorrhea</td></tr><tr><td>09:05:30 AM</td><td>T312</td><td>male</td><td>250ml</td><td>neutral</td><td>0.001%</td><td>no</td><td>no</td><td></td><td>none</td></tr><tr><td>09:00:39 AM</td><td>T314</td><td>female</td><td>245ml</td><td>neutral</td><td>0.002%</td><td>no</td><td>no</td><td></td><td>chlamydia</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td>0.000%</td><td></td><td></td><td></td><td></td></tr><tr><td>08:57:22 AM</td><td>T107</td><td>male</td><td>160ml</td><td>neutral</td><td></td><td>no</td><td>no</td><td></td><td>none</td></tr></table>

Figure 10.7 The real-time data provided on the quantifiedtoilets.com website Source: Used courtesy of Quantified Toilets

The goal was to observe people's reactions when coming across this new service on going to the toilet. Would they become upset, surprised, or outraged, or wouldn't they mind? Would they question the reality of the situation and tell others?

So, what happened? A diverse range of responses were observed. These included disapproval (for example, “Health advice? It does not get any creepier.”); approval (“Privacy is important. But I would like to know if I was sick and this is a good way to do so.”); concern (for instance, “Imagine if your employer could find out how hard you had partied last night.”; resignation (“I am sure the government has been collecting this data for years.”; voyeurism (“I just spent the last 10 minutes watching the pee-pee logs. Can't stop watching them.”); and even humor, where some people tried to match people entering and exiting the toilets with the data appearing on the website.

Within an hour of the project going live, #quantifiedtoilets went viral on social media, triggering a snowball of tweets and retweets. Many face-to-face discussions took place at the convention center, and articles and blogs were written, some appearing in magazines and newspapers. Some visitors were duped and tweeted how incensed they were. Arguably, this range of responses and level of discussion would never have happened if the researchers had just asked people in the street would they mind if their urine were analyzed in a public toilet.

What do you think of this type of study? Do you think it is a good way to open up debate about data tracking in society, or is it a step too far?

## 10.2.6 Combining Multiple Sources of Data

A number of researchers have started collecting data from multiple sources by combining automatic sensing and subjective reporting. The goal is to obtain a more comprehensive picture about a domain, such as a population's mental health, than if only one or two sources of data were used (for instance, interviews or surveys). One of the first comprehensive studies to do this was Studentlife (Harari et al., 2017), which was concerned with learning more about students' mental health. In particular, the research team wanted to know why some students do better than others under times of stress, why some students burn out, and still others drop out. They were also interested in the effect of stress, mood, workload, sociability, sleep, and mental health on the students' academic performance. They were especially interested in how the students' moods change in response to their workload (such as their assignments, mid-terms, finals).

During a 10-week term, the researchers collected masses of data about a cohort of 48 students studying at Dartmouth College in the United States (Harari et al., 2017). They developed an app that ran on the students' phones, without the students needing to do anything, to measure the following:

Wake up time, bed time, and sleep duration

The number of conversations and duration of each conversation per day

The kind and amount of physical activity (walking, sitting, running, standing, and so on)

• Where they were located and how long they stayed there (that is, in the dorm, in class, at a party, in the gym, and so forth)

The number of people around the student throughout the day

Student mobility outdoors and indoors (in campus buildings)

Their stress levels throughout the day, week, and term

Positive affects (how good they felt about themselves)

Eating habits (where and when they ate)

App usage

Their comments on campus about national events (for example, the Boston bombing)

They also used a number of pre- and post-mental health surveys and collected the students' grades. These were used as ground truth for evaluating mental health and academic performance, respectively. The researchers went to great lengths to ensure that all of the data stored was anonymized in a dataset to protect the privacy of the participants. Having achieved this, the researchers then opened up the dataset for others to examine and use to conduct further analyses   
(http://studentlife.cs.dartmouth.edu/dataset.html).

The researchers were able to mine the data that they had collected automatically from the students' smartphones and learn several new things about their behavior. In particular, they found that a number of the behavioral factors that had been tracked from their smartphones were correlated to their grades, including activity, conversational interaction, mobility, class attendance, studying, and partying.

Figure 10.8 shows a graph indicating the relationship between activity, deadlines, attendance, and sleep. It shows that students are very active at the beginning of the term and get very little sleep. This suggests that they are out partying a lot. They also have high attendance rates at the beginning of term. As the term progresses, however, their behavior changes. Toward the end of term, sleep, attendance, and activity all drop off dramatically!

![](../../Interaction Design Beyond Human-Computer Interaction, Fifth Edition (Helen Sharp, Jenny Preece, Yvonne Rogers)/images/23c4f4531858a6d1302b73e11242bb9b2f157a2eaf43fd2610c9b08286e486e8.jpg)  
Figure 10.8 Student's activity, sleep, and attendance levels against deadlines during a term  
Source: StudentLife Study

## ACTIVITY 10.2

From the two graphs shown in Figure 10.9, what can you say about the students' activity, their stress levels, and their level of socializing in relation to deadlines over the course of the term?

![](../../Interaction Design Beyond Human-Computer Interaction, Fifth Edition (Helen Sharp, Jenny Preece, Yvonne Rogers)/images/6a4749da764f8594c6254c28c31ed17ff9059eeb2bffc8f6f665eee225221d57.jpg)

![](../../Interaction Design Beyond Human-Computer Interaction, Fifth Edition (Helen Sharp, Jenny Preece, Yvonne Rogers)/images/6a591a120141a55a52d98cbaa97a55f7b758fe8ad2984d75ec2d95a6493edb31.jpg)  
Figure 10.9 Student behavioral measures over the course of a term Source: StudentLife Study

## Comment

The top figure shows that students start the term by having long social conversations. This begins to tail off as mid-term approaches. Students resort to having fewer and shorter conversations. After the deadlines are met, students switch back to having many more and longer conservations. The bottom figure shows students started out all upbeat, having returned from vacation feeling good about themselves. They appear relaxed (high mood level) and are active (going to the gym a lot). These attributes all start going downhill as the term comes to an end —presumably as their stress levels rise because of looming deadlines.

## 10.3 Visualizing and Exploring Data

Every day, people interact with different kinds of visualizations, including road signs, maps, medical images, mathematical abstractions, tables of figures, schematic diagrams, graphs, scatter plots, and many more. These representations are intended to help us make sense of the world we live in, but for them to be useful, they have to be presented in ways that are understandable for the people who use them. Being able to take meaning from data involves being able to see it and understand the way that it is represented and its context. What kind of data is it? What is the data about? Why was it collected? Why was it analyzed and represented in a particular way? The skills needed to understand and interpret visualizations are referred to as visual literacy. As with any skill, different people exhibit different levels of visual literacy, depending on their experience of using visual representations (Sarikaya et al., 2018). Figure 10.10 shows a simplified path that is followed when data is meaningful. Starting with the analyzed data, which is represented in some way, the user perceives and interprets the data representation taking into account the context of the data. The user is then able to understand and communicate what the data shows to others.

![](../../Interaction Design Beyond Human-Computer Interaction, Fifth Edition (Helen Sharp, Jenny Preece, Yvonne Rogers)/images/4283824cb0333a4e4a2a5014bb2d6edb671e6795f272cecce33ec9f372215a5d.jpg)  
Figure 10.10 A simplified path for data to be meaningful  
Source: Lugmayr et al. (2017). Used courtesy of Dr Artur Lugmayr

Even graphical representations of small amounts of data (for example 20–100 items) can be hard to interpret if the people trying to make sense of them don't understand the way that the data is being displayed. Furthermore, sometimes representations, such as bar graphs, line graphs, and scatter plots, are displayed in misleading ways. Danielle Szafir (2018), for example, asks, “How can we craft visualizations that effectively communicate the right information from our data?” She describes how data displays can mislead users when designers show axes with truncated scales, or they show data in 3D bars making it hard to read exact values from the bar because it isn't obvious which side of the 3D column is the place to read. Interactive visualizations typically include all of the canonical forms of representations (for instance, bar charts or pie charts) along with tree maps and advanced visualization techniques that enable users to interact with the data online by panning and zooming in and out of the displays. With the increased tendency to develop more complex visualizations to display increasingly large volumes of data, the question about how to craft the data representations and tools to develop and explore the data is even more relevant.

As Stu Card and his colleagues explained two decades ago, the goal of data visualization tools is to amplify human cognition so that users can see patterns, trends, correlations, and anomalies in the data that lead them to gain new insights and make new discoveries (Card et al., 1999). Many of the data visualizations and tools that have been developed since then are now being used by practitioners and researchers from fields including health and wellness, finance, business, science, educational analytics, decision-making, and personal exploration. For example, millions of people use interactive maps to find their way, benefitting from their integration into car navigation and car-sharing apps. Physicians and radiologists compare images from thousands of patients, and financiers examine trends in the stocks of hundreds of companies. Data visualization tools can help users change and manipulate variables to see what happens; for example, they can zoom in and out of the data to see an overview or to get details. Ben Shneiderman (1996) summarizes this behavior in his mantra “overview first, zoom and filter, and then details on demand.”

While the early UX research on information visualizations still guides UX designers in their pursuit of designing new interactive visualizations, tools are needed for interacting with large volumes of data (Whitney, 2012). Many of these tools require expertise beyond that of most casual users in order to use them effectively. Typically, the data displays consist of many of the common techniques mentioned earlier (such as graphs and scatter plots) coupled with 3D interactive maps, time-series data, trees, heat maps, and networks (Munzner, 2014). Sometimes these visualizations were developed for uses other than those for which they are used today. For example, tree maps were originally developed to visualize file systems, enabling users to understand why they are running out of disk space on their hard drives by seeing how much space different applications and files were using (Shneiderman, 1992). However, tree maps were soon adopted by media and financial reporters for communicating changes in the stock market, and they became known as “market maps” (see Figure 10.11). Like interactive maps, tree maps have become a general-purpose tool embedded in most widely used applications, such as Microsoft's Excel (Shneiderman, 2016).

![](../../Interaction Design Beyond Human-Computer Interaction, Fifth Edition (Helen Sharp, Jenny Preece, Yvonne Rogers)/images/25e097566e2d8623be432be50afe519ec98a32f3cb7540aaefccaf5045495df9.jpg)  
Figure 10.11 A market map of the S&P 500, which is a financial index for stocks. Green indicates stocks that increased in value, and red indicates stocks that decreased in value that day.

## Source: Used courtesy of FINVIZ

The ability to collect and store large amounts of data easily has encouraged the development of visualizations that display different types of data. For example, Figure 10.12 shows segments of sounds recorded from birds and other organisms collected by Jessie Oliver and her colleagues (2018). These researchers wanted to see how people investigated and annotated this data and in turn how this approach can be used to find and identify birds and other animals in the wild by recording their songs and calls. When the visualizations, known as spectrograms, were shown to birders, the researchers were intrigued to see how they evoked memories of hearing the birds in the field. The birders also found this data visualization to be helpful in corroborating their identifications of birds with other birders. From a UX design perspective, Jessie Oliver and her colleagues faced the challenge of how to display long sound recordings visually. They used a technique developed by Michael Towey and his colleagues (2014) in which algorithms compress the spectrograms so that one pixel represents one minute of sound recording. The resulting spectrograms enable birders to get an overview of the recordings that in turn allows them to see patterns in the bird songs.

![](../../Interaction Design Beyond Human-Computer Interaction, Fifth Edition (Helen Sharp, Jenny Preece, Yvonne Rogers)/images/0d4af2136260048e44feb94d5971488d757645522d90d799c347c8953aeee434.jpg)  
Figure 10.12 Visualization of different sounds, including birds, owls, and insects, from three areas of Australia that are displayed so they can be interpreted and compared Source: Oliver et al. (2018). Reproduced with permission of ACM Publications

## ACTIVITY 10.3

This video by Jeff Heer (2017) from University of Washington gives an overview of different types of data visualizations and data visualization tools: https://www.youtube.com/watch?v=hsfWtPH2kDg.

Watch this video and then describe (a) some of the benefits of using interactive visualizations and (b) some of the UX challenges in designing interactive visualizations.

## Comment

1. By working with interactive visualizations, users can interact with data to explore aspects of interest by going deeper into particular parts of the data. This is demonstrated in the visualization of airline on-time performance in which a user can filter portions of the data to view which flights arrive late. From this exploration, the user will discover that flight delays are associated with it being late in the day. In other words, the data reveals that as time goes by, the actual arrival times of flights tend to fall further behind the scheduled arrival times. Also, by being able to filter and manipulate particular parts of the data, users can answer questions that would be difficult to investigate without data visualization tools, such as what causes flights to arrive early?

2. In the video, Jeff Heer talks about some of the human perceptual and cognitive issues about which UX designers must be aware when they create

visualizations. For example, he mentions the importance of using color appropriately in a visualization of arteries. He also talks about the challenge of knowing how much detail to include in the visualization about the structure of the arteries.

In addition, Jeff mentions the power of many current tools for investigating many different variables, but he notes that using some of these tools proficiently requires programming and data analytics skills. UX visualization tool designers therefore need to find ways to support users who may not have these skills. He describes how some designers are tempted to get around this problem by automating the analyses. He points out, however, that a careful balance is needed in deciding how much automation should be provided and how much control should be left in the hands of users. Making this judgment is challenging for designers.

Jeff also mentions that there is much more to analyzing data than to visualizing it. Data has to be cleaned and prepared, a task referred to as data wrangling, which can take up to 80 percent of a data scientist's time. Issues of privacy also need to be considered. As a UX data visualization tool designer, Jeff suggests that all of these issues are challenges that must be considered when designing visualizations and data viz tools.

Powerful tools and platforms for analyzing and making predictions from large volumes of data have been designed for marketing, scientific and medical research, finance, business, and other kinds of professional use. To use these tools typically requires data analytic skills and statistical knowledge, which makes the potential benefits they offer out of reach for many people (Mittlestatd, 2012).

Many of these tools have been developed by large companies and research labs (Sakr et al., 2015). Some examples include Tableau, Qlik, Datapine, Voyager 2, Power BI, Zoho, and D3. To use these tools effectively, business managers often partner with analysts who assist them in interactive explorations that can lead to new insights. Together the analysts and managers identify widgets in the form of icons that represent their underlying functionality, from those made available in the tool, and then they create a customized “interactive dashboard” for use by the manager.

The dashboard is an interactive panel of control widgets that contains sliders, checkboxes, radio buttons, and coordinated multiple window displays of different kinds of graphical representations, such as bar and line graphs, heat maps, tree maps, infographics, word clouds, scatterplots, and other kinds of visualizations. Managers can then use these customized dashboards to explore the data and make informed decisions. All of the items in the dashboard are coordinated and draw from the same data selected to investigate particular questions of interest. In other words, the components of the dashboard are interactive and linked together so that they are coordinated (see Figure 10.13). This enables their users to benefit from seeing data displayed in different ways and to explore how these representations change as they manipulate sliders and other controls. The displays produced by tools like Microsoft's Power BI, Tableau, and similar products are used by managers who can make the same dashboards available to other employees across their company. Everyone can then see, discuss, and interact with the same data.

![](../../Interaction Design Beyond Human-Computer Interaction, Fifth Edition (Helen Sharp, Jenny Preece, Yvonne Rogers)/images/6a7f15dceae72e8334d0889bde1b56fa5ee711377f4328c5c5e8d087cf29e1d8.jpg)

Figure 10.13 A dashboard that was created to show changes in sales information Source: https://www.zoho.com/analytics/tour.html

For an overview of Tableau that shows how it is used and how Tableau dashboards are created, watch this video clip: https://www.tableau.com/#hero-video.

Another technique for creating interactive visualizations is Data-Driven Documents (D3) (Bostock et al., 2011). This tool is used to create web-based interactive displays. It is a powerful, specialist tool that extends JavaScript, and it requires programming expertise to use it effectively. It is used by journalists to create displays that appear in traditional news print and you can also interact with it online (see Figure 10.14).

![](../../Interaction Design Beyond Human-Computer Interaction, Fifth Edition (Helen Sharp, Jenny Preece, Yvonne Rogers)/images/1d08498eb911bd516bcc193c34e2b009db2aa83f92c77953723825d71ff26875.jpg)

Figure 10.14 An interactive graphic produced using D3 for the New York Times. It shows the tax rate paid by the different kinds of companies that form the S&P 500 financial index.

Source: Reproduced with permission of PARS International

Watch this New York Times graphic for an article entitled “Across U.S. Companies, Tax Rates Vary Greatly.” (Navigate to the following link to interact with the graphic. Try panning over the display.)

https://archive.nytimes.com/www.nytimes.com/interactive/2013/05/25/s review/corporate-taxes.html.

A challenge is how to make powerful tools available to people who want to explore such topics as personal finance and health data but who are not trained as analysts and who do not want to employ or work with an analyst. Furthermore, some products are expensive and are unaffordable for many individuals and nonprofit organizations.

In a recent study, Alper Sarikaya and colleagues (2018) pointed out that the term dashboard requires more precise description and a deeper understanding of how the context of its use can impact the UX design of dashboards. They challenge UX designers to develop dashboards for different types of use cases for a wide range of users. In their study, they analyzed a range of dashboards, first by reviewing published papers written by other researchers and then through a qualitative study in which they classified the features of different dashboards and how they are used.

They characterized the dashboards according to their design goals, levels of interaction, and the ways in which they are used. Figure 10.15 shows examples of the seven kinds of dashboards that they identified. Each type is named according to how it is used: strategic decision-making, quantified self, static operational, static organizational, operational decision-making, communication, and dashboards evolved, which was a catchall category that included features that did not fit into other categories. They state that many of these examples visually appeared as dashboards but may not fit the strictest definition of dashboard functionality.

![](../../Interaction Design Beyond Human-Computer Interaction, Fifth Edition (Helen Sharp, Jenny Preece, Yvonne Rogers)/images/28beb6e3a0dc3cf04e45655c06e279a438b25b128efea06f8fa9fd1f5fca92df.jpg)  
Figure 10.15 Exemplar dashboards (Sarikaya et al., 2018). Dashboard 1 and Dashboard 5 specifically target decision-making, while Dashboard 3 and Dashboard 4 target consumer awareness. Dashboard 2 represents the quantified self (such as a smart home), while Dashboard 6 represents those dashboards targeting communication. Dashboard 7 captures some novel extensions of traditional dashboards.

Source: Sarikaya et al. (2018), Graph 1. Reproduced with permission of IEEE.

Sarikaya et al. also advocate ways of supporting users by telling stories that can help illustrate the context that the data visualizations represent. They point out the challenges that users encounter when interacting with visualizations such as enabling them to have more control over how they configure and use dashboards. A further challenge involves finding ways to support users in developing data and visual and analytic literacy. They also point out that there is a new opportunity for UX designers that involves finding ways to support users in making choices about which data and representations to use in different contexts. This includes understanding the broader social impact of dashboards.

## ACTIVITY 10.4

Study Figure 10.16(a) from the weather site https://www.wunderground.com. It shows weather data for December 19, 2018, at Washington D.C. in the United States. Particularly take note of the temperature, precipitation, and wind data. What information do they provide? Now compare this visualization with that depicted in the “wundermap” (see Figure 10.16b). How do the two displays differ, and which do you prefer?

![](../../Interaction Design Beyond Human-Computer Interaction, Fifth Edition (Helen Sharp, Jenny Preece, Yvonne Rogers)/images/da355c071b3ba45b3515be23a5cbdb727b0b1ef5b2338f1ba1769cdeb32f755b.jpg)  
Figure 10.16 (a) Actual weather data and (b) a wundermap of the same area and time

Source:https://www.wunderground.com

## Comment

The first display in Figure 10.16(a) contains representations that are fairly standard for conveying weather information. The green ring shows the maximum and minimum temperatures for now and what it feels like. A diagram of a sun indicates that it is a sunny day with some clouds, even though it is quite cold. It is also easy to see that the wind is from the south, and presumably the circle represents a compass and the pointed wedge indicates the wind direction.

The display in Figure 10.16(b) provides similar data, but it is harder to get an overview of weather in the Washington D.C. area. It uses conventional meteorological symbols to show temperature and wind. It is easier to see local effects but harder to get an overview of weather of the entire area. (If you are able to access the website, try clicking “layer” and selecting other options not shown in the figures.) Which display is preferable probably depends on how much detail you want—an overview or detail about a specific area in the Washington D.C. region— and your tolerance for clutter.

## BOX 10.3

## Visualizing the Same Sensor Data by Using Different Kinds of Representations for Environmentalists and the General Public

One of the parks in London that was used to stage the Olympics in 2012 has been transformed into a “smart park.” By this it is meant that a number of sensors were placed throughout the park to measure the health and use of the park. One type used throughout the park was bat call sensors. The goal was to ensure that the park's bat conservation program was effective, as well as connecting visitors and residents to the wildlife around the park (https://naturesmartcities.com/). Monitoring bat calls is also a technique that was used to assess the general health of the park.

The data collected was primarily provided to the scientists in the form of spectrograms (see Figure 10.17b), but it was also presented in a more accessible form to the public via an interactive display (see Figure 10.17a). As part of a public kiosk, a schematic map was provided that showed where in the park the bat call data had been collected (Matej et al., 2018). A slider was provided to enable visitors to interact with the data: moving it to the left showed bat call data from the night before, while moving it to the right showed bat call data from the previous 10 nights. The LEDs on the map changed in color and intensity, representing the varying levels of bat calls. The total number was also shown in the digital display. The kiosk was deployed in the park, and many passersby stopped for a considerable length of time to learn about bats and interact with the data. The physical act of using the slider provided an engaging way of exploring the data rather than just looking at a static visualization or dashboard.

![](../../Interaction Design Beyond Human-Computer Interaction, Fifth Edition (Helen Sharp, Jenny Preece, Yvonne Rogers)/images/b53b07dabdf16a6adae7f88a74fca1e6e09b2d49bf19fff84c276bf85aeba906.jpg)

![](../../Interaction Design Beyond Human-Computer Interaction, Fifth Edition (Helen Sharp, Jenny Preece, Yvonne Rogers)/images/fdabbba37d70fc46f244d00cabde6909ba08eb713287464fc70673c68d4271de.jpg)  
Figure 10.17 The same bat call data was made accessible (a) to the general public via an interactive visualization and (b) as a spectrogram intended for environmental scientists.  
Source: (a) Used courtesy of Matej Kaninsky and (b) Used courtesy of Sarah Gallacher

## 10.4 Ethical Design Concerns

In the introduction to this chapter, we mentioned how masses of data are now regularly being collected from people for a variety of reasons, including improving public services, reducing congestion, and enhancing security measures. It is usually anonymized and sometimes aggregated to make it publicly available, for example showing the energy consumption data for a given space such as a floor of a building. Figure 10.18 shows a

floor-by-floor comparison for a University of Melbourne building, where the red bar for the basement is the worst performer in terms of energy usage and the green bar for Level 1 is the best performer. The idea is to provide feedback on energy consumption in the building to increase awareness among the inhabitants to encourage them to reduce their energy consumption. However, what if localized occupancy rates or energy consumption for each office were shown? It would not take much to figure out who was in that space. Would that be a step too far and an invasion of their privacy? Would people mind?

![](../../Interaction Design Beyond Human-Computer Interaction, Fifth Edition (Helen Sharp, Jenny Preece, Yvonne Rogers)/images/94d021634e810d4390cba023600b4d8a6d2467a16181f135e6cbe712713502ba.jpg)  
Figure 10.18 Average daily energy consumption depicted on a public display for a building at the University of Melbourne. Green is best performer, yellow is in the middle, and red is the worst performer.

Source: Helen Sharp

When deciding on how to analyze data and act upon data that has been automatically collected from different sensors, it is important to consider how ethical the data collection and storage processes are and how the data analysis will be used. By “ethics,” this is usually taken to mean “the standards of conduct that distinguish between right and wrong, good and bad, and so on” (Singer, 2011, p. 14). There are many codes of ethics available from official bodies that provide guidance. For example, the ACM (2018) and IEEE (2018) have both developed sets of ethics (https://ethics.acm.org/2018-codedraft-1/; IEEE Ethically Aligned Design, 2018). They point out that central to any ethical discussion is the importance of protecting fundamental human rights and to respect the diversity of all cultures. They also state the need to be fair, honest, trustworthy, and

respectful of privacy.

To use data ethically, researchers and companies can limit the data they collect in the first place. Rather than trying to collect as much data as possible (as has often been the situation in research—just in case it might be useful for subsequent analysis), it has been proposed that researchers and data practitioners follow an approach called privacy by design (Crowcroft et al., 2018). That way, they can avoid collecting excessive data that might be sensitive but not needed (see also Chapter 13 and Chapter 14). Furthermore, it may be possible to collect and analyze the data on the device itself, rather than uploading it to the cloud (Lane and Georgiev, 2015).

## ACTIVITY 10.5

Watch the following TEDx talk by Jen Golbeck (the author of the Atlantic article on the Quantified Toilets) where she discusses why social media “likes” say more than you think. The talk was given in 2013 and since then has had more than 2.25 million views. Even though the TEDx talk is a few years old, the issues raised in it are still relevant today. In particular, she discusses how people's behavior online enables companies to predict what they like, what they might be interested in buying, and even their political views.

https://www.ted.com/talks/jennifer\_golbeck\_the\_curly\_fry\_conundrum\_why\_social language=en&utm\_campaign=tedspread&utm\_medium=referral&utm\_source=tedco

What do you think the privacy issues are here?

## Comment

Jen Golbeck provides two compelling examples in her talk. The first is the wellknown example of how a teenage girl's pregnancy was predicted from her online purchases of things like vitamins. The second example was how data on liking crinkly fries coupled with a knowledge of the theory of homophily was used to predict that a group of people have above average intelligence. By understanding that the theory of homophily explains that people who are similar tend to like the same things, trust each other, and seek out each other's company, Jen Golbeck was able to look for relationships in data about “liking” crinkly fries. The crinkly fries example indicates that even though it is absurd that liking crinkly fries is a predictor of above average intelligence, in this particular example, the person who created the post attracted “likes” from friends who were also of above average intelligence. It is an amusing example, but the main point is to illustrate that information that people contribute in social media, often unknowingly, can be used to infer all kinds of things about them, such as their ethnicity, age, gender, shopping behavior, and what they like.

The concerns highlighted in the video are prescient for politicians and others looking for ways to protect the general public by controlling what social media companies can and cannot do with personal data. For example, GDPR is a law introduced by the European Union that seeks to protect data privacy (discussed in

Chapter 13, “Data Analysis,” and Chapter 14, “Introducing Evaluation”). Within the United States and in other countries, the need for controlling how personal data is used is being debated by governments and consumer protection groups, such as the Electronic Privacy Information Center (EPIC; www.epic.org), with the goal of finding ways to protect data privacy.

An ethical strategy that can be adopted for systems that analyze data is to have an explicit agreement in place as to how it will be used and acted upon. Such an agreement can include in what way is the analysis trustworthy. Trustworthiness is usually taken to mean how credible are the analyses being performed on the data (see Davis, 2012). When a decision is made on behalf of a human based on classifying their data using some machine learning algorithm, can the user be sure that the decision made is trustworthy?

Another ethical concern is whether the form of data analysis being used by a system is socially acceptable (Harper et al., 2008). Have clear boundaries been established between what is acceptable and not acceptable, especially when it is personal data that is being analysed and classified, such as health data or criminal history? Is there a clear understanding about the data that is being analyzed to provide information about a phenomenon versus that which is performed to make a decision about someone's future? Are there agreed policies in place? How much do the boundaries shift and change over time as new technology becomes more mainstream and authorities change?

## ACTIVITY 10.6

Shoplifting cost U.S. retailers \$44 billion in 2014. To help combat shoplifting, DeepCam developed an intelligent system that passively monitors people coming into a store by using CCTV video footage that identifies potential suspects (see Figure 10.19). To do this, it uses AI algorithms and facial recognition software. Do you think this practice is socially acceptable? What might be the privacy concerns? To find out more about their system, check out their website at https://deepcamai.com/.

![](../../Interaction Design Beyond Human-Computer Interaction, Fifth Edition (Helen Sharp, Jenny Preece, Yvonne Rogers)/images/541bee90363b0c36f0881ccb54d0838774c16d423d2423a9a90a02c8b7a9a18a.jpg)  
Figure 10.19 DeepCam's face-tracking software used in a store

Source: https://deepcamai.com

## Comment

To address privacy concerns, the company developed its system so that it does not identify customers or link them to any sensitive information such as name, address, or date of birth. It only recognizes faces and identifies patterns of behavior that potentially are worth investigating. The video footage is indexed and structured similar to how web pages are set up for quick searching. This enables store detectives to be able to notice potential threats in real time. Many people might find this form of data analysis creepy, knowing that their faces are being matched to a database each time they enter a store. Others might find it more socially acceptable because it has the potential to reduce crime considerably.

The Open Data Institute (https://www.theodi.org) has provided a set of questions to help researchers, system developers, and data scientists to formulate a set of ethical questions to begin to address these concerns. These are grouped as sets of questions as part of a framework called the data ethics canvas. For example, two subsets are about the positive and negative effects that a project can have on people. The questions include “Which individuals, demographics, and organizations will be positively affected by the project?” and “How is positive impact being measured?” The negative questions include “Could the manner in which the data is collected, shared, and used cause harm?” and “Could people perceive it to be harmful?” Working through each set of questions is intended to help researchers identify potential ethical issues for a data project or activity and to encourage explicit reflection and debate within a project team as to who the project will impact and the steps needed to ensure that the project is ethical. The framework provided on the ODI website is intended to help organizations identify

potential ethical issues associated with their data project.

In Chapter 1, “What Is Interaction Design?” we outlined a number of usability and UX design principles that were transformed into questions, criteria, and examples showing how to use them in the design process. Here, we introduce some other principles that relate to the ethics of collecting and using data at scale and that are often talked about in the literature on ethics, data science, HCI, and AI (see Cramer et al., 2008; Molich et al., 2001; Crowcroft et al., 2018; Chuang and Pfeil, 2018; and van den Hoven, 2015). We call these data ethics principles (see Box 10.4). Four principles that often appear in the reports, handbooks, and articles on ethics and interaction design are fairness, accountability, transparency, and explainability (FATE). They are also included as key principles that lie at the heart of the general data protection regime (GDPR). For example, Article 5 of the GDPR requires that personal data shall be “processed lawfully, fairly, and in a transparent manner in relation to individuals.” Within the context of HCI, Abdul et al. (2018) have proposed an agenda for how HCI researchers can help to develop more accountable intelligent systems that don't just explain their algorithms but are also usable and useful to people.

It should be noted that the ethics principles are not mutually exclusive but interrelated as described next.

## BOX 10.4

## Data Ethics Principles (FATE)

Fairness Fairness refers to impartial and just treatment or behavior without favoritism or discrimination. While this is something to which organizations adhere in areas such as promotion and hiring, in the context of data analysis, it refers to how fair a dataset is and what the impact will be from using the results. For example, sometimes, the dataset is biased toward a particular demographic that results in unfair decisions being made. If these could be identified and revealed by the system, it would make it possible to rectify them while also developing new algorithms that can make the system fairer.

Accountability Accountability refers to whether an intelligent or automated system that uses AI algorithms can explain its decisions in ways that enable people to believe they are accurate and correct. This involves making clear how decisions are made from the datasets that are used. A question that arises is who is accountable for doing this? Is it the person providing the data, the company coding the algorithms, or the organization that is deploying the algorithms for its own purposes?

Transparency Transparency refers to the extent to which a system makes its decisions visible and how they were derived (see Maurya, 2018). There has been much debate about whether AI systems, which typically depend on large datasets when making a decision, should be designed to be more transparent (see Brkan, 2017). Examples include medical decision-making systems that can diagnose types of cancer and media service providers (for instance, Netflix)

that suggest new content for you to watch based on their machine learning algorithms. Currently, many are black-box in nature; that is, they come up with solutions and decisions without any explanation as to how they were derived. Many people think this practice is unacceptable, especially as AI systems are given more responsibility to act on behalf of society, for example, deciding who goes to prison, who gets a loan, who gets the latest medical treatment, and so on. Some of the rules of the GDPR on automated decision-making are also concerned with how to ensure the transparency of decisions made by machine learning algorithms (Brkan, 2017).

Explainability Explainability refers to a growing expectation in HCI and AI that systems, especially those that collect data and make decisions about people, provide explanations that laypeople can understand. Research into what is a good explanation to provide has been the subject of much research since expert systems came into being in the 1980s. Following this early work, there was research into what context-aware systems should provide. For example, Brian Lim et al. (2009) conducted a study that provided different kinds of explanations for a system that made automated decisions. They found that explanations describing why a system behaved in a certain way resulted in a better understanding and stronger feelings of trust. In contrast, explanations describing why the system did not behave a certain way resulted in lower understanding. More recently, research has investigated the kinds of explanations that are appropriate and helpful for users of automated systems (see Binnes et al., 2018).

The FATE framework suggests that the design of future systems, which use AI algorithms in combination with personal or societal data, should ensure that they are fair, transparent, accountable, and explainable. Achieving this goal is complex, and it involves being aware of the potential for bias, discrimination in big data and algorithms, ethics in big data, legal and policy implications, data privacy, and transparency (Abdul et al., 2018).

Achieving this objective is inevitably difficult. For example, as pointed out by Cynthia Dwork at a panel on big data and transparency (transcribed by Maurya, 2018), it is difficult to know what a good explanation of a decision might be for human beings. She uses the example of what should a system say when a user asks, “Why was I turned down for the loan?” to illustrate this. The system might be able to reply, “There is a classifier, we feed your data into it, and the outcome was that you were turned down.” However, that is of little help to a user, and it is likely to be more annoying than not having any explanation.

Reuben Binnes et al. (2018) conducted an experiment to determine what kinds of explanations users found to be fair, accountable, and transparent for an automated system. In particular, they compared four different styles of explanation, ranging from being largely numerical scores to more comprehensive ones that provided a breakdown of the statistics used for certain demographic categories, including age, gender, income level, or occupation. The different styles were presented for scenarios in which a decision had been made about individuals automatically, such as applying for a personal financial loan and where passengers on over-booked

airline flights were selected for rerouting. The results of their experiment showed that some of the participants found that they engaged with the explanations to assess the fairness of the decisions being made, but at times they found them impersonal, and even dehumanizing. What constitutes a fair explanation may need to be more than providing an account of the processes used by the algorithms. From an interaction design perspective, it might help if the explanations were interactive, enabling the user to interrogate and negotiate with the system, especially if a decision that has been made is contrary to what they expected or had hoped.

Jure Leskowec (2018) comments on how the consequences of a system making a decision on behalf of a human can vary. This will determine whether an explanation is needed to support a decision made by a system and what it should include. For example, if a decision is made to pop up an ad for slippers in a user's browser, based on an analysis of their tracked online app usage (a common practice used in targeted advertising), it might be mildly annoying, but it is unlikely to upset them. However, if it means a person is going to be denied a loan or a visa based on the outcome of an automated algorithm, it may have more dire consequences for someone's life, and they would want to know why the particular decision was made. Jure suggests that humans and algorithms need to work together for system decisions that implicate more important societal concerns.

Another reason why ethics and data have become a big concern is that automated systems that rely on existing datasets can sometimes make decisions that are erroneous or biased toward a particular set of criteria. In doing so, they end up being unfair. An example that caused a public outcry was the misidentification of people with dark skin. Traditional AI systems have been found to have much higher error rates for this demographic. In particular, 35 percent of darker-skinned females were misidentified compared with 7 percent of lighter-skinned females (Buolamwini and Gebru, 2018). This difference was exacerbated by the error rate found for lighter-skinned males, which was less than one percent. One of the main reasons for this large discrepancy in misidentification is thought to be due to the make-up of the images in the datasets used. One widely used collection of images was estimated to have more than 80 percent white images of which most were male.

This bias is clearly unacceptable. The challenge facing companies that want to use or provide this data corpora is to develop fairer, more transparent, and accountable facial analysis algorithms that can classify people more accurately regardless of demographics, such as skin color or gender. A number of AI researchers have begun addressing this problem. Some have started developing 3D facial algorithms that continuously learn multiracial characteristics from 2D pictures. Others have introduced new face datasets that are more balanced (see Buolamwini and Gebru, 2018).

BOX 10.5

The Living Room of the Future: An Ethical Approach to Using

## Personal Data

There are now more than 250 smart cities projects throughout the world in nearly 200 cities. Each has different aspirations, but a major goal is to make cities more energy efficient, to make them safer, and to improve the quality of life. Most work in partnership with tech companies, central councils, and local communities to realize the benefits of new economic opportunities. IoT technologies and big data are often a central concern. One aspect has been to develop new approaches and toolkits to empower local individuals with the tools to measure and act upon what they want to find out about their city. For example, a citizen-sensing approach, adopted in the city of Bristol, brought together local citizens, community workers, and volunteers who together developed an innovative and affordable DIY sensing tool that people could use to record and collect data about the level of dampness in their homes (www.bristolapproach.org/).

In addition to the many smart cities projects, there are others that focus on how people adopt, accept, and approach new sensing technologies in a particular building or home. For example, the Living Room of the Future project is investigating how people will live in the future in a home that has been embedded with a range of IoT devices (https://www.bbc.co.uk/rd/projects/living-room-ofthe-future). The project is researching how to make personal data transparent and trustworthy, while at the same time respecting people's privacy. It is also concerned with designing methods that can offer explicit awareness and transparency of those individuals' data.

A particular challenge that they are addressing is how to enable people to be in control of their own personal data while at the same time letting it be used by the home system to adapt their experiences, for example, choosing what media to play and from which device(s). The devices, like sensors and everyday RFID-enabled objects, have the potential of being able to collect a diversity of personal data, including music preferences, history of where everyone is sitting, what they are doing, and how they are feeling. To ensure privacy, the data is collected and stored, not in the cloud but on a home-fenced data server called a databox. The box collates, curates, and mediates access to each person's data. It only uses verified and audited third-party services to ensure that it cannot be accessed by anyone else. As such, the data never leaves the living room and ensures that the IoT services provided can be deemed trustworthy. It also provides a platform that allows personalization to occur without needing to ask the users if they are OK with any suggested changes.

The home of the future project is also investigating how data can be collected and how it is being used in the house, for example, to control home heating and lighting.

## In-Depth Activity

Go to labinthewild.com, and select the test “What is your privacy profile?” This test has been designed to tell you what you think about data privacy and how different you are compared to what others think about this topic. It should take about 10–15 minutes to complete. At the end of the test, it will provide you with your results and classify you in terms of whether you are not concerned, somewhat concerned, or very concerned.

1. Do you consider this to be an accurate reflection of how you view privacy?

2. Did you think the video shown was effective at raising potential problems of what data is collected in a smart building? If not, what other scenario could be used in a video to ask people to consider privacy concerns?

3. What impact do you think the context chosen for the scenario might have on your reactions? For example, if the scenario involved a doctor's surgery, might you have reacted differently and if so, why?

4. What do you think of labinthewild.com as a platform for conducting large-scale online experiments from volunteers?

5. Did you find any other information on the website interesting?

## Summary

This chapter described how data at scale involves bringing together large volumes of data from different sources that is then analyzed to address new questions and provide insights that could not be gained by analyzing data from a single source. The chapter explains techniques and tools for collecting and analyzing large volumes of data. It also raises some concerns about how data at scale is used, particularly as to the need for personal data privacy. UX designers are encouraged to consider the impact of their designs on how data is used and to ensure that it is used ethically. Four core principles are advocated for ethical design: fairness, accountability, transparency, and explainability (FATE).

## Key Points

Data at scale concerns very large volumes of data, which is also known as big data.

A defining feature of data at scale is that it includes different types of data collected from different sources that are analyzed to address particular questions.

Data at scale can be quantitative and qualitative data; it consists of social media messages, sentiment and facial recognition data, documents, sensor, sound and sonic data, and video surveillance data.

Analyzing data from different sources is powerful because it provides different perspectives on people's behavior.

Analyzing data at scale can have positive outcomes, such as understanding

people's health problems, but there are also dangers if personal data is revealed and then misused.

Data at scale is collected and analyzed in many different ways including data scraping, monitoring oneself and others, crowdsourcing, and sentiment and social network analysis.

Data visualization provides tools and techniques for representing, understanding, and exploring data.

Ethical design principles suggest ways that UX designers can create designs and interaction processes that make clear how data is being used.

Ensuring that artificial intelligence systems are transparent is a particularly important ethical design principle.

## Further Reading

HANSEN, D., SHNEIDERMAN, B., SMITH, M. A. AND HIMELBOIN, I., (2019) Analyzing Social Media Networks with NodeXL. Insights from a Connected World (2nd ed.). Morgan Kaufmann. This book provides an introduction to social network analysis. It focuses on NodeXL, but much of the discussion is helpful when using any social network analysis tool.

SCHRAEFEL, M.C. GOMER, R.ALAN, A.GERDING, E., AND MAPLE, C. (2017) The Internet of Things: Interaction Challenges to Meaningful Consent at Scale. Interactions,24, 6 (October 2017), 26–33. This short article discusses how HCI researchers can be involved in helping users manage their privacy and personal data especially in view of IoT.

SZAFIR, D. (2018) The good, the bad, and the biases: Five Ways Visualizations Can Mislead and How to Fix Them. Interactions. xxv.4. As the title suggests, this article discusses some of the well-known problems and design flaws with visualizations and suggests ways to fix them.

SARIKAYA, A., CORELL, M., BARTRAM, L, TOREY, M, FISHER, D. (2018) What Do We Talk About When We Talk About Dashboards? IEEE Trans Vis Comput Graph. This paper characterizes dashboards, and it reviews and critiques their design and how they are used.

SHILTON, K (2018) Values and Ethics in Human-Computer Interaction. Foundations and Trends in Human-Computer Interaction: Vol. 12, No. 2, 107–171. This article provides a good overview of issues being debated in HCI about ethics, data, and HCI.
