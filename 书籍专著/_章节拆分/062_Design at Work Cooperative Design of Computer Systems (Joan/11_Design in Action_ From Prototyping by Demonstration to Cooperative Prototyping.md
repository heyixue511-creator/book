> 来源：Design at Work Cooperative Design of Computer Systems (Joan Greenbaum (editor) etc.)
> 原始文件：C:\Users\lenovo\Documents\Codex\2026-05-29\书籍专著\Design at Work Cooperative Design of Computer Systems (Joan Greenbaum (editor) etc.)\Design at Work Cooperative Design of Computer Systems (Joan Greenbaum (editor) etc.).md
> 识别方式：一级标题

# Design in Action: From Prototyping by Demonstration to Cooperative Prototyping

Susanne Bødker and Kaj Grønbak

... the development of any computer-based system will have to proceed in a cycle from design to experience and back again. It is impossible to anticipate all of the relevant breakdowns and their domains. They emerge gradually in practice.

Winograd and Flores, 1986, p. 171

Some time ago we worked with a group of dental assstants, esning a prototype case record system to explore the possibility of using computer support in public dental clinics. The application was not intended to be used directly in the treatment sessions, but to help administer the patients' visits. The dental assistants would be the primary users of the application, and they took part in a series of prototyping sessions to specify how they would like to use computers in their work. They knew that some kind of computer application would soon be introduced at their workplace, and it was important for them to be able to influence the choice of system. The following scene is taken from one of the prototyping sessions:

At one point two dental assistants were sitting together in front of the screen with the designer standing just behind them. They switched between screens containing pictures representing patients' teeth. Suddenly one of them said: "The lower jaw is turned upside down—that's quite confusing given how we number the individual teeth." The designer had turned the upper and lower jaws the same way, with the front teeth pointing upwards. The dental assistants did not like this. One of the dental assistants explained: "I want to think of the pictures of the teeth as I'm looking into the mouth of the patient when I look at the screen." The designer took the mouse and used a few menu operations to flip the picture. This gave all patients in the database the new, improved tooth representation. The modification activity lasted only a few minutes, without anyone touching the keyboard. The dental assistants were amazed by the ease of changing the prototype. They were satisfied with the change and one of them took the mouse again and continued using the prototype.

## System Design and User Involvement

We saw that by actually using the prototype, the dental assistants were able to make changes that may not have otherwise surfaced until the users got the final system in their hands. The designer, of course, thought that he had turned the picture right. He had not realized that there was a "mapping" between the drawing and the position of the jaws in the mouth.

In this and similar examples, we find strong arguments for a more direct and active involvement of users in the design of computer systems; to find out how the computer application functions in the use situation the users must somehow be able to experience it. We call this envisionment. To experience is not to read a description of the computer application, nor is it to watch a demonstration. We have found prototyping to be very useful in uncovering unarticulated aspects of users' work and in having them contribute to the design of improved tools. In envisionment, breakdowns may lead to a change in the prototype, and eventually to a change in the future computer application." What we find useful in prototyping, relative the use  mock-ups as desbed in Chapter  hat a rooye better shows dynamic aspects of the future application.

In a  i r that involves users actively and creatively. We will give examples illustrating how to obtain a close coupling between design activities and experimental evaluation of prototypes in work-like situations. Before going into the examples we give a brief overview of current prototyping approaches and point out how the approaches we propose are different.

## Different Approaches to Prototyping

A rich variety of approaches to prototyping has been proposed in recent years. They all provide possibilities for users to gain hands-on experience before the final application is built; and yet, the way they are used today, they are not often applied this way. Grønbak (1989b) gives a critique of three categories of prototyping: prototype becomes the system; executable specification; and exploratory approaches.

The prototype becomes the system approaches dominate current system development practice and literature. They supplement a traditional requirements specification with a prototype of user interface aspects before the implementation begins, primarily for the users to adjust details of the system. From empirical studies (Grønbæk, 1989a) we see that such prototypes are used primarily to demonstrate features, and not to let users try them out actively.

The main purpose of executable specification approaches is to obtain a full, formal specification of what (parts of) the future system should do. The specifications are made in a formal, executable specification language, meaning that a program, and thus a prototype, can be generated automatically from the specification. Although in theory, users and designers can evaluate the specification by evaluating this prototype, in practice this is hardly ever done. The specification languages that serve as basis for generating the prototypes are usually not suitable as a means for communication with users and empirically it has turned out that a full-scale formal specification of a system requires an effort similar to traditional programming of the system. Offsprings of these two approaches are seen in the so-called CASE-tools. Code generating CASE-tools have, however, not been used enough yet to assess their ability to support prototyping.

In exploratory approaches mock-ups, simulations and "throwaway" prototypes are developed employing various tools. The aim of the approaches is to make "quick-and-dirty" sketches of the computer application in order to clarify requirements for a new computer system. A number of cases describing user involvement in the evaluation of prototypes exists, but there are not many examples where users have been actively involved in the design and modification of prototypes and thus have creatively influenced the future system. However, the rapid development of simulated applications can facilitate early hands-on evaluation. The prototypes in these examples serve mainly as substitute specifications for the application and to propagate ideas into detailed design activities (see Bødker, 1987).

## Cooperative Prototyping to Stimulate User Participation and Creativity

The traditional prototyping approaches mainly take the perspective of the designers and software engineers, and pay little attention to user involvement in the design process. We will now introduce a slightly different approach that we call cooperative prototyping. The approach has its roots in the exploratory approaches previously described, but we will demonstrate that prototyping can be a cooperative activity between users and designers, rather than an activity of designers utilizing users' more or less articulated requirements.

The cooperative prototyping approach aims to establish a design process where both users and designers are participating actively and creatively, drawing on their different qualifications. To facilitate such a process, the designers must somehow let the users experience a fluent work-like situation with a future computer application; that is, users' current skills must be brought into contact with new technological possibilities. This can be done in a simulated future work situation as described in the beginning of this chapter, or, even better, in a real use situation. When breakdowns occur in the simulated use situation, users and designers can analyze the situation and discuss whether the breakdown occurred because of the need for training, a bad or incomplete design solution, or for some other reason. Breakdowns caused by bad or incomplete design solutions could be rapidly turned into improved designs, reestablishing the fluent work-like evaluation of the prototype.

To fully experience the prototype, the users need to be in control of its use for some period of time, and to try it out in a use-like setting. The roles of the professional designers include anticipation of the use situation and building/cleaning up the prototypes in between the prototyping sessions. Ideally, cooperative prototyping should be performed by a small group of designers and users with access to flexible computer-based tools for the rapid development and modification of prototypes.

## Examples of Cooperative Prototyping

We will present two examples.One is a cooperative prototyping process in which users participate directly in changing the prototype, using direct manipulation design facilities. This process is primarily a laboratory experiment. The second example of a cooperative prototyping process takes place in a real organizational setting, but without the close cooperation in making changes to prototypes. In the first example, HyperCard on a Macintosh is used, and the focus is on exploring a new graphical user interface for a dentist case record system providing direct representation of teeth on the screen. In the second example, the 4th Generation System, ORACLE, is used, and the focus is on exploring organizational aspects of a new computer system in an office that manages registration of incoming and outgoing mail for a large trade school. The examples illustrate very different cooperative prototyping processes, one focusing on technical issues and one on organizational issues, both of which need attention in a system development project.

## Prototyping of Graphic User Interfaces

This example, mentioned in the introduction, deals with the development of a prototype of a patient record system for municipal dentist clinics (for more details see Bødker & Grønbæk, 1989)." The endusers are mainly dental assistants working in clinics in public schools in Denmark.The purpose of these clinics is to provide regular dental checkups and treatment for school children. These clinics, as well as the work of the individual dental assistants, vary a lot, according to the size of the school and the organization of work at the clinic. All of the dental assistants in these clinics, and thus in the prototyping sessions, were women, most of them with no prior experience using computers.

This prototyping process was carried out by a designer together with a number of dental assistants in an educational setting where the main purpose was to learn about computer technology—about system design in general and design for dental clinics in particular. The topic was to explore problems in and prospects for developing a decentralized patient record system, combining administrative information with treatment-oriented information. The application was not intended primarily for use in the treatment session, but enough medical information was kept to fulfil the demands for statistical information from the Ministry of Health, and to help administer the patient's next visit.

## The Prototyping Process

In order to prepare the prototyping sessions we designed an initial prototype with some modification of a prototype case record system for general practitioners (Bajlum & Nielsen, 1988). Pictures of human teeth and a set of fictitious test data were incorporated into the prototype. Later on, we augmented it with report facilities provided by Reports.1 A few illustrative reports were prepared. "We had some foreknowledge of the application domain, and the preparation activities required only two to three days of design work in order to provide reasonably stable prototypes for the sessions.2

![](../../Design at Work Cooperative Design of Computer Systems (Joan Greenbaum (editor) etc.)/images/dc28430c9dd37fa35648c52ceb83b3b03d635ffa624e20ff8ca29625acc6447c.jpg)  
Figure 1. Direct representation of teeth in a prototype dental patient case record (Lower mouth part).

The dental assistants were on leave from their daily work to participate in the educational activities.3 The prototyping process was introduced and discussed with the dental assistants, and the sessions started with a short demonstration of the prototype. Then the dental assistants worked with the prototype in groups of two to four to get a better understanding of it. The designer, who was one of us, had told the dental assistants that the prototype had been built in a flexible environment that allowed for changes to the design, encouraging the dental assistants to come up with suggestions for improvements. The designer tried to stay at a distance in order to let the dental assistants themselves explore the prototype and imagine that they were performing their daily tasks. There was no intervention by the designer in the process except in breakdown situations in which the dental assistants had problems or suggestions for improvements.

Some groups worked quite enthusiastically with the prototype and came up with constructive suggestions, which were built into the prototype on the spot or after the sessions.

File Edit Go Patientsøgning

7:14:24

![](../../Design at Work Cooperative Design of Computer Systems (Joan Greenbaum (editor) etc.)/images/23051036ca7303d0c8c556675cc721f2aa516dc84762b54cc901ebdc26321765.jpg)  
Figure 2. Direct representation of teeth in a prototype dental patient case record (Lower mouth part).

Examples of improvements that resulted from cooperation with the dental assistants in the prototyping session:

Change of teeth representation: The mouth pictures, which were used to indicate where treatment had been given, were initially turned upside down, as described in the introduction, but HyperCard provided point-and-select tools to turn the pictures around.

Exploring alternative representations of tooth treatment: The dental assistants asked for direct marking of fillings on the mouth pictures as an alternative to our solution, which had each tooth as a button link to a separate card with a verbal treatment description. The visual aspects of this alternative representation could be explored immediately using the freehand painting tool of HyperCard, and thus be compared to the initial proposal.

Report lay-out design: The dental assistants participated in laying out simple reports from scratch and changing existing ones. This was possible because objects such as fields, text and graphics could be instantiated from available menus.

These modifications were done through direct manipulation; many such changes were made. The general experience was that the dental assistants became enthusiastic and creative when they discovered the potential for making these changes. We also made modifications that required modest programming. These included:

Copying buttons and modifying scripts: The dental assistants asked for functionality that was quite similar to functionality already available in an existing button. A few times we copied such a button and made minor modifications. When this programming lasted longer than a couple of minutes, the dental assistants lost their patience, because they could not follow what went on.

"Simple" query forulation and modification: When the dental assistants were participating in the design of reports they also had to participate in the formulation of queries. This soon became a little too hard. Not surprisingly they had to rely totally on the designers' suggestions regarding more complex queries constructed from ANDs and ORs.

A number of suggestions and ideas that came up during the sessions could not be integrated in the prototypes directly. The following are examples of this:

The implementation of a menu to support searching for patients was made after the sessions, because it is rather time-consuming to program global menus. Moreover, the change could not be done via direct manipulation.

•In the sessions we only made reports with data from one type of card. One group realized that they wanted to print out a survey of the treatment of all the teeth of a patient. We had to tell them that while this ought to be done, it was quite a cumbersome process. Since programming reports was time consuming, the dental assistants didn't want it done during the sessions. For this reason many good suggestions for reports were never realized in the prototype.

## Lessons Learned

Together with the dental assistants we came up with a number of conclusions about the prototype:

The idea of cards with direct representation of teeth seemed promising.

The idea of having each tooth on a separate card did not work for the dental assistants. They needed to be able to get a quick overview of all the treatment given to a patient. Such an overview could be provided with direct marking on the teeth combined with links to more detailed information." A similar combination of verbal and direct marking was needed to deal with treatments affecting several teeth. A major restructuring of the prototype seemed to be necessary to fulfil these demands.

Before the sessions we expected that the major challenge would be to keep the unreflected action of the users going in a prototyping process when, at the same time, we often had to stop and make changes to the artifact they were using. In our situation we could not go out into the real setting and have dental assistants use the prototypes there; our environment was not suitable for simulating a real dental clinic. It was the fact that the dental assistants were together that made it possible for them to "be in the situation" by having to demonstrate to each other how they did things "at home." It was possible for the dental assistants to step into the illusion that they could perform realistic work tasks with the prototype. The real challenge was to interrupt the process and modify the prototype, while they were criticizing some aspect of it, and then restart the evaluation process. Using a prototype that provided familiar cards and pictures of teeth made it possible for them to formulate very specific needs and requirements for a future computer application by using their own language and pointing at the prototype.

We expected that using HyperCard and Reports would often allow immediate design solutions to problems encountered with the prototype. As expected, problems arose when major HyperTalk programming was needed." Also, with the present tools, it was clear that cleanup of the prototype versions was needed. There was still quite a lot of work for the computer people to do in between meetings.

We see direct manipulation facilities as provided by HyperCard/- Reports as important for a cooperative prototyping process with insession modifications. The direct representation of the data structure on the screen (the cards, fields, etc.) was valuable in this case. We can easily see situations where the card structure would be a limitation, but in this case the direct mapping of "good old-fashioned" cards on the screen made it relatively easy for the dental assistants to understand what the prototype could do for them and how the direct manipulation changes affected it. We experienced two sources of undesirable breakdowns in the design situation: reaching the limits of direct manipulation possibilities, and making changes that require major restructuring of the prototype.

These experiences show that it is possible for a group of workers, when given the chance, to come up with constructive and creative contributions to the design of their computer applications. The discussions quite easily got focused on the current prototype and rather technical issues, though. But regarding work-oriented issues the users in this case found out by experiencing a prototype that treatment-oriented work could be supported much better than with systems currently in their workplace.

Furthermore, the study illustrates that it is not necessary to aim at a prototype which simulates full functionality. It is possible for users to abstract from knowledge about these matters where necessary when provided with a prototype with some essential functionality. The initial prototype was stable enough to be evaluated in a work-like situation, and flexible enough to allow in-session modification. In the case just described, we made work-like evaluation and in-session changes of prototypes together with users in a laboratory setting. The following section describes a case where prototypes were tested in a real organizational setting.

## Prototyping in an Organizational Setting

In this case, we explored hands-on prototyping utilizing a 4th generation system, ORACLE, taking prototyping out of the laboratory setting and into an actual work setting.It deals with a small group of workers in a large organization. We worked with the administration of a large Danish trade school, spread over a number of locations. This administration takes care of budgets and other financial issues, management of buildings and other facilities, including construction work, registration of students, salaries, and other staff administration, supplies, secretarial work, etc. Many of these functions are located partly centrally and partly locally. This administration carried out a large project with one of us as a consultant. The purpose of the project was to create an integrated office automation system, to provide more efficient administration of the school. The office administration system should be financed not by laying off employees, but by allowing for more efficient use of resources such as classrooms and heating.

The project was initiated by the school management. According to the local technology agreement,4 it was managed by a technology committee with representatives from management and staff. It was the general idea of the project that the employees should, in project groups, take part in designing the computer applications that they are to use themselves. The school hired a number of consultants to work with the employees in the design work. The actual realization of the computer applications was carried out by a computer manufacturer on the basis of the specifications and prototypes created by the users and consultants. The case described here deals with one of these project groups, working with information storage and retrieval. The purpose of the group was to reorganize the files of the school to be more efficient, eventually by means of a computer application.5

The file of all incoming and outgoing documents represents the history or memory of the organization. The information retrieval was rather cumbersome in the then-existing structure. The office where the file is located served the case workers in the administration, who acquired documents on specific issues from the file. The project group consisted of the women working in the filing office, representatives of the case workers who were the users of the file, and consultants competent with respect to both organizational issues and computers. There was a general agreement among the users that the way documents were filed and retrieved was not working well— each group of workers had problems with the system.

## The Prototyping Process

The consultants began by interviewing the participants and observing the work in the filing office. Then the group gathered to start its part of the work. After initial discussions, three alternative ways of filing were proposed. Scenarios were made of how the future would look with each alternative. In addition, different ways of organizing the file and of doing the filing and retrieving were envisioned by the group. This was done through visits to trade shows and other workplaces in which filing technology had been applied. The filing office even borrowed a couple of filing systems from vendors and installed them in the office for a couple of weeks. This allowed the group to focus on what it wanted and what it didn't want from these different applications and the organization of work they required.

After this, an initial paper-based sequence of screen image simulations was discussed in the group. This mock-up illustrated one of the three alternatives: a paper-based file with lists of incoming and outgoing mail kept and distributed via the computer (see Chapter 9 for a discussion on mock-ups).

On the basis of these discussions, the consultants built a first prototype using ORACLE. Some questions to be considered were: What does it mean to have the lists of incoming and outgoing mail computerized? What information needs to be entered, and by whom? Which lists should be available to each caseworker? How should the lists be structured? Who "owns" the lists? At this stage there was a strong emphasis on the cooperation between the filing office and the caseworkers, on the different caseworkers varying needs for information, and on the qualifications of the filing office workers.

As the versions of the prototype stabilized, they were also used in the real use setting—the women in the filing office used the prototype to create mailing lists and make these available to the caseworkers.6

Programming the prototype required a lot of experience because much of what the group wanted, concerning cursor movements and the like, could not be programmed directly in the available version of ORACLE, but had to be programmed in Pascal. The prototype, as it was, illustrated only a limited part of a future new application, a part that was running rather well. "In the next step, when we wanted to expand this prototype, the database had to be completely restructured and the previous prototype, including test data, thrown away. We found that office management, in particular, was reluctant to take this step. Although the prototype was unable to handle the large data sets needed for daily work, management thought of the prototype as something running perfectly well in the setting. They tried to use it for work purposes as it was, and of course it failed. This issue is discussed in more detail later in a subsection on unrealistic expectations.

ORACLE allowed the group to run the prototype on the computer that was used for other purposes in the office. For some weeks the prototype was used daily, under supervision of some of the consultants. They helped each worker get started, they were there when things broke down, and they made observations of the use processes. The aspects that were illustrated had to do with how mailing lists worked. This prototype allowed experiments with a rather limited but essential part of a future filing system in the real setting. What could be experimented with was the communication between the caseworkers and the filing office, which involved a change in the traditional way of making mailing lists. There also came to be a strong focus on the qualifications of the filing office in relation to the work of the caseworkers: How much do the filing office workers have to know about the work that the caseworkers are doing in order to fill in the proper information in the mailing lists?

## Lessons Learned

We learned from this process that using prototypes as well as existing systems as alternative suggestions for the future allows the participating users to formulate their suggestions better. It was not necessary to come to a consensus about the understanding of the problem as long as some solutions could be found that made everybody comfortable with the future use. By integrating the prototypes in the organizational setting it became possible to focus not only on individual use, but also on cooperation among people. And still, to avoid an overly technical focus, it was necessary to shift between techniques, and to bring in other kinds of "prototypes," such as the filing systems from other domains. The prototype's actual use required a robust prototype, running on equipment that could be made available in the use setting. Because the prototype ran on the same computers as other programs that the workers used, it was easier for them to get started, and easier to integrate it into the daily work tasks, than would have been the case with a prototype running on a separate computer. In this case the price paid was that it was difficult to actively involve the users in the actual construction of the prototype, because the programming effort was too large. The 4th generation system used was too limited in the facilities provided, the concepts used were too hard for the users to understand, and a structural change of the prototype was very difficult. Furthermore, in this case, a major restructuring of the prototype was prevented by the inflexibility of the 4th generation system.

It was important for all the participants to keep in mind the status of a prototype—the purpose it is intended to serve and the aspects of the future application it is illustrating in order to avoid giving rise to unrealistic expectations of the sort experienced by management in this case.

We have seen a case in which cooperation issues were important and in which prototypes running in the organization, as well as borrowed computer applications, were important elements in a cooperative design process.

## How to Get Going with Cooperative Prototyping

We have given examples of cooperative prototyping based on the use of existing tools. To get a cooperative prototyping process going it is crucial for the working group to establish a common understanding of the aims of the process, the status of the intermediate products developed in the process, and the role of prototyping in the overall design process. Furthermore, some organizational problems must necessarily be handled to establish a basis for performing cooperative prototyping in a specific project. These problems cannot necessarily be handled within the project; some of them need to be handled before the project is established. In this section we summarize some of our experiences and suggest possible steps for system designers to take in order to get going with cooperative prototyping. We present these suggestions by pointing to a number of issues, or rather, tensions between issues that are worth considering.

## Establishing Project Groups: Making a Workable Group versus Involving a Large User Group

There are a lot of issues involved in selecting a competent group of users to participate in design/prototyping activities. Many are not within the control of the designers, but are determined by power relations, technology agreements (in Scandinavia), and the like. System development literature (Harker, 1988; Pape & Thoresen, 1987; Grønbæk, Grudin, Bødker, & Bannon, 1990) and practice indicate that there are several ways to select participants. For example:

middle managers who have an overview of the task domain;

participants who constitute statistically representative samples;

representatives elected by the users;

employees with experience using computers;

the most skilled workers among the future users;

the most enthusiastic among the future users.

In addition the design can start as a pilot project in one department.

We are unable to point to one of these criteria as the most important, nor do we believe in setting up a single criterion. The appropriate choice in the actual project should be discussed carefully when establishing the group. However, we consider the first criterion mentioned particularly dangerous in relation to our view of design. Middle management, who are only involved in the tasks on an abstract level, cannot be expected to make relevant contributions through hands-on evaluation of prototypes, as they do not have the necessary familiarity with daily work processes. We say this even after encountering, in a previous project, the problem that workers at the shop floor had very little understanding of the planning and coordination of their work processes. In relation to establishing a working group of a reasonable size the second criterion is problematic too, because many computer systems have user groups which are quite big and diverse. Thus a statistically representative sample will result in too big a working group. What we find most important, though, is to establish a working group together with competent user representatives.

![](../../Design at Work Cooperative Design of Computer Systems (Joan Greenbaum (editor) etc.)/images/f37a8f2a73f7e645dde0abed61a96d8f01f2be3907c4519939591cc94363578f.jpg)

It is also important that the participating designers and users get to know each other quite well, because cooperative prototyping is based on the assumption that contributions from all participants are important. Cooperation is crucial to maintain the ongoing mutual learning process between users and system developers. Steps to be taken in establishing a project working group are discussed further in Chapter 7 and in Andersen, Kensing, Lundin, Mathiassen, Munk-Madsen, Rasbech, & Sørgaard (1990).

The product of the prototyping process is more than a computer prototype. Prototyping is a learning process, and much of the new understanding must be spread to workers and managers who are not participating directly in the prototyping process. One way is to use the different prototypes in a process in which all involved personnel are guided through an abbreviated version of the prototyping process (Bisgaard, Mogensen, Nørby, & Thomsen, 1989). In general, the prototypes are valuable means of educating future users, because education can start while the final computer application is being implemented. Similarly, the participants from a prototyping process may be able to act as teachers.

Depending on the size of the organization, a process such as the one described by Pape and Thoresen (1986) may be appropriate. They describe a process in which an intermediate prototype is built in one part of the organizational setting. The designers move on to a new part of the organization, bringing this prototype to be used as a starting point there. A new process with a new group of people is conducted, and the designers move on to yet another part of the organization, where, in this case, the final prototype is developed. As with all prototyping processes this requires mutual learning in each of the settings.

## Setting up Prototyping Sessions: Designers as Conductors versus Users Being in Charge

To users, designing a new computer application is secondary, whereas for designers it is their primary work. This means that the designers must know how to set up the process, and must make sure that they all get something out of their meetings. This involves considering such questions as: What is the purpose of the session? How stable should the prototype be in advance? To what extent should in-session modifications be made? What setting should be chosen? How should the outcome be documented/evaluated? These issues are discussed in more detail elsewhere (Grønbæk, 1989a). A remark on the question of stability and allowing in-session modifications is relevant here. As we saw in the trade school case, cooperative prototyping does not require that a prototype be modified in the session, but, in our experience, using direct manipulation for modifications is a good way to engage the users. However, only some prototype modifications can be done insession, and it is necessary that designers be aware of the constraints and know when to postpone a modification until after the session. In particular, much homework must be done by the designers to prepare for prototyping sessions. Thus, the designers still control much of the decision-making process.

In prototyping sessions, designers often like to demonstrate all the features they believe are wonderful. Our claim, however, is that demonstrations do not necessarily tell the users anything about how the prototype or the final application fulfils their needs. To fully experience the prototype, the users need to be in control of its use for some period of time-to try it out in a work-like setting. If the prototype is not sufficiently stable to let the users work on their own with it, the designer should be prepared to give first aid for breakdowns caused by the prototype. While designers are, initially, the ones who know how the process should be set up, it is important that the process be adjusted to the needs and wishes of the users.

## Providing Prototypes: Showing Fantasy versus Being Limited by the Tools

We have given examples of how we used two quite different tools for prototyping, neither of which was ideal. Getting started, so that the users can experience using some prototype of the future system, is important. We find the experiences of potential problems and possible solutions gained from the early prototyping experiments quite valuable and thus worthwhile. The prototyping activities can always be supplemented with more flexible mock-ups and even traditional description to cover aspects of a future application that cannot easily be covered by the prototypes.

If unstable or poor prototypes are presented to the users there is, of course, a danger of missing the point. If, however, there is no realistic possibility for making better prototypes, the users' handson experiences with imagined parts of the future system are still valuable. In the trade school case we saw that existing but different computer applications can serve as sources of comparison to developed prototypes. Thus we could say that a poor example is better than no example, if the status of the prototype is made clear. We recommend that the shortcomings of a prototype be compensated for by a good explanation of the deficiencies.

Today a number of tools exists that can be utilized for cooperative prototyping (see Grønbak, 1989b). Such tools are often available on PCs or graphic workstations, and they are not necessarily expensive. Smalltalk and various LISP tools can also be bought for PCs at reasonable prices. Some tools are useful for prototyping in certain application domains, although they are not application specific from the outset. For example, in the domain of patient case records, HyperCard, providing an interface based on a card metaphor, supports the prototyping of some aspects quite well, because the case records in that example did consist of cards in folders. To summarize, we find that it is possible to accomplish a lot with existing tools.

Finally, alternatives can stimulate the users' imaginations and thereby encourage the group to discuss different ways of organizing work. Exploring alternatives is not a waste of time, but a necessity to get fantasy into the development process and thereby to improve the users' work through better computer support. A way to stimua prototype, as we did in the dental assistant example. Building a toolbox of elements to make exploration of alternatives easy would also seem to be a good investment in most cases; for example, general elements could support different interaction styles and devices.

## Maintaining Communication: Describing Requirements versus Experiencing Work

Users are not there to annoy the designers or to spoil their "wonderful" design, but to guide them, because the users know the relevant work tasks. Users are not necessarily good designers of computer systems, but even awkward suggestions may be grounded in tacit knowledge related to aspects of the work that the designers do not understand fully. As discussed in Part I, designers will perhaps have to study the work of the users more carefully and discuss it with them further before suggestions can be understood or turned down. Keep in mind that the users are the key to the design of a useful system and the designers are the key to propagating the user demands into the technical design of the system. The delicate balance may well be to design an application that is both useful to the users and of high quality from a technical point of view.

The most fruitful communication of design ideas occurs when problems are explained within language games familiar to the users. Examples of this are seen in the case with the dental assistants. We used a direct representation, a picture of the teeth on the screen, instead of burdening them with explanations of a form or a record data structure. At the trade school we used concepts from the existing file and mailing lists. The principle used for the interaction with the system was similar to the idea of putting information on cards or sheets in a case record folder in the manual case records. In general we have found it useful to have users and designers experience the use of prototypes in work-like situations and to make use of language games that are familiar to the users.

## Users Perception of the Process: Realistic Prototypes versus Unrealistic Expectations

To obtain a work-like evaluation in prototyping sessions, prototypes need to be realistic and stable enough to let the users be in charge of the evaluation. But it is also important from the beginning to create awareness of prototypes as rough drafts that should be thrown away if they are bad. Not every prototype the group comes up with will be a hit, and many times the group will choose a minimal solution when making modifications. The group may know all along that this solution is temporary, but it may still be worth pursuing.

However, prototypes direct the expectations of both designers and users in a way that creates a blindness toward other and maybe better ways of dealing with the issues being considered. The designers may expect that the prototype can be included in the final product. Alternatively, as at the trade school, users may find the prototype so stable that they think of it as the final product when it is not suitable for handling production data. A manager may, for example, demand that production data be entered into the database and treated by the prototype. These observations lead us to stress the need for setting the scene and creating awareness of the objectives of prototyping approaches.

## Maintaining Focus: A Technical versus a Work-oriented Focus

Technical skills have traditionally been considered the important skills in the development of computer applications, so working groups have often consisted of only technically skilled designers and a representative for the "customer." However, as the first part of this book points out, the major problems are not purely technical, but rather grounded in the coupling between technical solutions and work, the organization of work, and political issues at the workplace. Thus, early prototyping experiments should act as catalysts for focusing on this coupling, as illustrated in the trade school example, in which prototypes were evaluated in the use domain and cooperation issues were in focus. To maintain this focus requires more than the purely technical skills needed to build prototypes. Domain knowledge is crucial, as is a certain level of knowledge of organizational issues in general. The question is whether we can realistically have it all. In our experience, the enthusiasm of being actively engaged in design may well be spoiled if the working group grows too big.

Prototyping naturally leads to a technical focus on the computer application, as was seen in the dental assistants case. There is a danger that the designer gets more focused on "hacking" than on discussing problems related to the use situation. Discussion in a prototyping session often focuses on the interaction with the computer more than on how work is organized around the computer. These matters are important (Bødker, 1990), but they are not all. To avoid a too technical focus it is important, as we saw in the trade school case, to shift back and forth to techniques that have different foci. And it is important to use experiments with the prototypes in work-like settings to get to an understanding of changes in work, such as in the qualifications and organization of work around the computer application. In our experience it is important to combine prototyping with other techniques, and not be afraid to step away from the prototype.

## Getting Resources: Adding More Resources to Early Activities versus Lowering Development Costs

By highlighting the benefits of cooperative prototyping early in a development project we also point to the necessity for development projects to allocate more resources for these early activities. What might require the most resources, in contrast to traditional projects, is the participation of more users. To ensure real, active involvement, users have to be freed from part of their daily work to avoid requiring them to do double work." Yet it is also important that the users keep some involvement with everyday work tasks so that they do not become managers or professional user representatives.

A number of authors (among them Boehm, 1981) have pointed out that the most expensive mistakes or shortcomings in system development are those made in the early phases in which the focus is on analysis and design. At the same time, it is pointed out that the resources spent in these phases are traditionally the smallest portion of total expenses. We agree with these authors that there is an imbalance between importance and resources. We believe that cooperative prototyping can help anticipate some of the expensive "mistakes" and most likely reduce development costs (Lantz, 1986).

## Design as an Ongoing Process

We have argued that cooperative prototyping approaches can attack a number of problems traditionally related to lack of user involvement in system development. Of course, they cannot solve all such problems; they will not resolve conflicts in organizations or indicate when prototyping has produced sufficient clarification to implement a system.

But ceativ rooypi an plo e y of computer systems seen from the point of view of the users; that is, users can get a system that is more tailored to their needs and thus improve the quality of their work. However, organizations are not static, and technological innovations increase the number of different interaction styles that can be provided for essentially the same function. Neither designers nor users can gain full knowledge of the possibilities for providing computer support for an application domain; design is an ongoing process. Thus cooperative prototyping should not be viewed as an approach to produce the ultimate computer system for an application domain." It should rather be viewed as one of the initial steps in the ongoing development process in which a computer application is augmented and tailored in conjunction with changing needs. Actually, the possibility for users to create individual interaction styles and augment existing applications based on their own needs may not be that unusual in the future. Such aspects of computer systems are referred to as adaptability or tailorability; these concepts are discussed further in the next chapter.

## Acknowledgments

Thanks to "our real user" John Kammersgaard and to many of the contributors of this book for useful comments.

## References

Andersen, N. E., Kensing, F., Lundin, J., Mathiassen, L., Munk-Madsen, A., Rasbech, M., & Sørgaard, P. (1990). Professional system development—Experience, ideas and action. Englewood Cliffs, NJ: Prentice-Hall.

Bajlum, T. & Nielsen, T. (1988). Edb-støtte til lægepraksis—et eksperiment med udvikling af en brugsmodel og en prototype [Computer support for medical practice—an experiment with the development of a use model and a prototype]. Unpublished master's thesis, Aarhus University, Aarhus, Denmark.

Bisgaard, O., Mogensen, P., Nørby, M., & Thomsen, M. (1989). Systemudvikling som lærevirksomhed, konflikter som basis for organisationel udvikling [Systems development as a learning process, conflicts as the origin of organizational development]. DAIMI IR-88. Aarhus, Denmark: Aarhus University, Computer Science Department.

Boehm, B. W. (1981). Software engineering economics. Englewood Cliffs, NJ: Prentice-Hall.

Bødker, S. (1990). Through the interface—A human activity approach to user interface design. Hillsdale, NJ: Lawrence Erlbaum Associates.

Bødker, S. (1987). Prototyping revisited—design with users in a cooperative setting. In P. Järvinen (Ed.), Report of the 10th IRIS Seminar (pp. 71-92). Vaskievesi, Finland. Tampere, Finland: University of Tampere.

Bødker, S. & Grønbæk, K. (1989). Cooperative prototyping experiments—Users and designers envision a dentist case record system. In J. Bowers & S. Benford (Eds.), Proceedings of the First European Conference on Computer-Supported Cooperative Work, EC-CSCW (pp. 343-357). London.

Grønbak, K. (1989a). Rapid prototyping with fourth generation systems—An empirical study. Office: Technology and People, 5 (2), 105-125.

Grønbak, K. (1989b). Extending the boundaries of prototyping-— Towards cooperative prototyping. In S. Bødker (Ed.), Proceedings of the 12th IRIS conference (pp. 219-239). DAIMI PB-296-I. Aarhus, Denmark: Aarhus University, Computer Science Department.

Grønbæk, K., Grudin, J., Bødker, S., & Bannon, L. (1990). Improving conditions for cooperative design Shifting from

product to process focus. DAIMI PB-331. Aarhus, Denmark: Aarhus University, Computer Science Department.

Harker, S. (1988). The use of prototyping and simulation in the development of large-scale applications. The Computer Journal, 31 (5), 420-425.

Kristensen, B. H., Bollesen, N., & Sørensen, O. L. (1986). Retningslinier for valg af faglige strategier på kontoromrãdet—et case studie over Arhus tekniske Skoles kontorautomatiseringsprojekt [Guidelines for trade union strategies in the office area——A case study of the office automation project of the Aarhus School of Polytechnics]. Unpublished master's thesis, Computer Science Department, Aarhus University, Aarhus, Denmark.

Lantz, K. E. (1986). The prototyping methodology. Englewood Cliffs, NJ: Prentice-Hall.

Mathiassen, L., Rolskov, B., & Vedel, E. (1983). Regulating the use of edp by law and agreements. In U. Briefs, C. Ciborra, & L. Schneider (Eds.), Systems design for, with and by users (pp. 251-264). Amsterdam: North-Holland.

Pape, T. & Thoresen, K. (1987). Development of common systems by prototyping. In G. Bjerknes, P. Ehn, & M. Kyng (Eds.), Computers and democracy — a Scandinavian challenge (pp. 297- 311). Aldershot, UK: Avebury.

Winograd, T. & Flores, C. F. (1986). Understanding computers and cognition: A new foundation for design. Norwood, NJ: Ablex.
