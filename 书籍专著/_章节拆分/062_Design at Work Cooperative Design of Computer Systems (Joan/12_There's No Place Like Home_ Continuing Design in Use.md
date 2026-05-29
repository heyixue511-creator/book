> 来源：Design at Work Cooperative Design of Computer Systems (Joan Greenbaum (editor) etc.)
> 原始文件：C:\Users\lenovo\Documents\Codex\2026-05-29\书籍专著\Design at Work Cooperative Design of Computer Systems (Joan Greenbaum (editor) etc.)\Design at Work Cooperative Design of Computer Systems (Joan Greenbaum (editor) etc.).md
> 识别方式：一级标题

# There's No Place Like Home: Continuing Design in Use

Austin Henderson and Morten Kyng

... effective design involves a co-evolution of artifacts with practice. Where artifacts can be designed by their users, this development goes on over the course of their use.

Suchman and Trigg, Chapter 4, p. 72

One of our primary goals in this book is to contribute to the creation of systems that better fit work situations, as well as the aims and intentions of the people using the systems. This implies a view of design as a process that is tightly coupled to use and that continues during the use of a system.

The preceding chapters in this part of the book have focused on the first of these aspects, showing how to incorporate use experience in the initial design process. This chapter will show what may be involved in continuing design in use, and how we, in the initial design process, may create systems are tailorable.

## Case I: Tailoring?—Never Thought About It!

At Aarhus University, personnel in the payroll office were accustomed to helping people who had difficulty understanding their payslips. Because each person in the office handled only a few types of contracts, they understood the contracts thoroughly and could explain any peculiarities. However, due to the introduction of a new computer system, mandated for all state-owned Danish enterprises, the work was reorganized. As a result, each person at the payroll office handled employees according to their date of birth. This may have been the standard way of doing things at many public payroll offices, and thus an acceptable choice for the computer system, but at Aarhus University it resulted in a dramatic decline in the service provided to the employees; each person at the payroll office now handled so many different kinds of contracts that they no longer knew the details.

Although the change necessary to remedy the situation—to return to the "contract way" of working—seems conceptually simple in terms of the work being done, it was in fact infeasible. First of all, there was no support for "local variations" in the initial design of the system. Secondly, the process of maintaining the system didn't incorporate any notion of modification beyond the fixing of bugs.

## Case II: Handling Modifications

As our second case, consider the Danish hospital that recently installed a new computer-based heating and ventilation control system built from a dozen standard components. The boilerman in charge of the daily operation of the system handled it quite easily. However, the personnel on duty outside normal working hours were not boilermen, and they had difficulty understanding the messages from the system and reacting appropriately. The problem was solved by having some of the "personnel on duty," together with the boilerman, redesign all messages from the system, rephrasing them in language they all understand. This second set of messages was then added to the system as the new default. As the personnel actually encounter the messages in their use of the system, those that still create problems are noted and usually modified.

In this case the system in question was prepared to accept messages in different languages, and this, in combination with a design process that deals with a number of modifications to the standard components, made the change quite feasible.

## Case I: Preparing the System for Change by Its Users

As our last case we consider workers at three cooperating research facilities who are using the Xerox Common Lisp environment (XCL) for electronic paperwork, e. g. handling documents and electronic mail (cf. Sheil, 1983, for information on Lisp environments). These workers include members of the research staff, secretaries, and administrators, only some of whom can program in LISP. Although XCL is a very flexible environment for those who can program in LISP, it can be quite unfriendly to those who can't.

The researchers created Buttons to help (MacLean, Carter, Lövstrand, & Moran, 1990). A button is a screen object (actually a small window) that can be easily moved around, copied, and sent to others in documents and electronic mail. Each button contains an "action," an arbitrary piece of LISP code that is executed when the button is "pushed" by clicking on it with the mouse. Buttons are used to add to the behavior of the XCL environment.

Consider, for example, what happened when users noticed that considerable effort was being expended on remembering and typing addresses for people being sent electronic mail. A local supporter created a button, labelled with a (usually short version of) person's name, that simply typed in that person's address. Soon these address buttons" were being copied and shared with others. Initial ly, users either got help in modifying buttons to capture the addresses of new people or learned how to do it themselves. The buttons were subsequently modified to make changing labels and addresses much easier. XCL was tailored by means of Buttons to meet the needs of electronic mail in ways not anticipated by its designers.

Ideal tailorable systems are those in which there are means for the users, or supporters near the users, to make them fit different work situations. The system we call Buttons is a very general tailoring mechanism which is, with varying degrees of ease, usable by workers to augment XCL behavior.

Professional system designers can match systems to users, because they have the skills to modify them. Creating systems where nonprofessional designers can do the same thing is not nearly as easy. So it is not surprising that program-literate researchers created the first address buttons. However, it should be noted that the nonprogrammers have a big advantage, in that they, as users, know the work the system is supporting, and are therefore in a much better position to determine when the system matches the work.

## Why Do We Need to Continue Design in Use?

There are three main reasons why system behavior may need to change after its initial design is implemented. They are:

•As designers of technology we are usually confronted with the task of designing systems that will be used for long periods of time. And no matter how well they may have fitted the situation initially, circumstances of the situation of use changes: the needs change, the uses change, the users change, the organization changes. Therefore the computer systems may well have to change to match the changed circumstances. In the case of Buttons, an increase in the complexity and number of mail addresses changed the users' needs.

The complexity of the world makes it difficult to anticipate all the issues that will eventually be of importance in the final situation. There are bound to be things we overlook, misunderstand, etc. The creator of the XCL electronic mail system, for example, did not provide a means for aliasing addresses (as is provided in other mail software); the address buttons were created to meet the need.

When we are creating a product which will be purchased by many people, the need to design for many different situations of use is particularly clear, and in fact some of the techniques for allowing users to adjust systems in use have been motivated by market considerations; for example, producers of "plastic" software who want to satisfy as many users as possible with a single product.

## Why Is It Difficult to Continue Design in Use?

Most of this book is about designing systems that fit the work of the users, and the difficulties involved in the quest of concepts and understanding that further such a task. When we want to support continued design in use, we face the same difficulties, magnified by the additional requirements that:

the system include tools for doing this continued design;

the continuing design be feasible for nonprofessional designers (the users);

the "sub-system" for tailoring matches the users' work, just as required of the rest of the system.

But as with traditional systems, tailoring is more often based on concepts from the computer field than from the application domain.

First of all, the need for providing possibilities for tailoring has to be recognized in the development of a system. Otherwise such possibilities will be missing, or tailorable only in the implementation environment. In the development of "plastic" software this need to provide for tailoring is usually recognized. However, it seldom goes beyond the setting of software-switches (parameters), as discussed later. In custom development there is a tendency to try to provide "the right system," without regard for possible future changes. In this respect custom development may learn from plastic software design.

Recognizing the need, however, is only the beginning. Even simple capabilities such as being able to choose a default font for a word processor presuppose that there exist possibilities to choose from. To design such a space of possibilities, which is meaningful in terms of the work of the users, is no easy task; to make it possible for the users to explore this space is even more difficult.

One major problem is the lack of suitable concepts and "parts" at the levels between a full-fledged application and the programming language. With the older technologies there is usually a gradual movement from the understandable to the incomprehensible. Thus to almost any car driver, "motors" make perfect sense, most understand "spark plugs," and quite a few will even attempt to adjust the distance the spark has to travel. When trying to dig into computer applications, users are almost immediately confronted with concepts and parts that do not make sense in terms of their work. This chapter attempts to begin remedying this situation, trying to set the stage for moving from the computer bound concepts to the work otheusers.But there is a long way to go, and the chapter is in some places more technical than the rest of the book.

The rest of the chapter is organized as follows: first we discuss the relationship between use and designing in use and take a brief look at the people doing the tailoring. Then in the main section of the chapter we highlight the practice of designing in use. We look first at how users change the behavior of systems, and then at how to support these activities. Following this is a section on the "down side" of tailoring, on the difficulties that may arise. The chapter concludes with a section summarizing how to support tailoring in the initial design of systems.

## Tailoring and Use

Tailoring a system, continuing designing in use, is an activity different from initial design. The activity is related to specific use situations and the result is not a new system, but a modifed system; that is, a system with a history which relates it to the earlier version and problems with its use.

Whilel des andue tus ay eats cearyent activities, the distinction between use and tailoring—designing in use—is somewhat blurred. For a particular system a distinction may be made, but in general it is no easy matter, because computer systems, their use and tailoring, differ as much as cars, clocks, and computers differ.

The intuition behind our presentation is coupled to the notion of change, and implicitly coupled to the related concept of stability. The distinction between tailoring and use thus rests on the understood and intended variability of artifacts and their patterns of use. Certain aspects of these artifacts we, as users, regard as stable; others we regard as more or less constantly changing. This relative stability of certain aspects is exactly what allows us to consider tailoring as an activity in itself: we tailor when we change stable aspects of an artifact.

But this stability/change dichotomy is not that crisp, as illustrated by the following examples. I may change the font of a piece of text in a text editor. Is it tailoring? Or how about modifying a spreadsheet? Or moving windows around on the screen to make working on a particular task easier?

Are these tailoring? Or are they "just" use? The text editor is designed for the creation of text in different fonts, so to take advantage of that capability seems like using the text editor, not tailoring it. Similarly, moving windows around on the screen feels more like using the window system for what it is intended than it feels like tailoring it.

We offer two more distinctions to improve understanding of the concepts of tailoring and use. The first of these rests on the view of technology as a tool for addressing certain subject matter, often conceived of as manipulating certain objects. A text editor's subject matter is text (or documents); it manipulates text. A window systems manipulates windows. The distinction then is: if the modifications that are being made are to the subject matter of the tool then we think of it as use; if the modifications are to the tool itself, then it is tailoring. So changing a font on a word in your document is use, while changing the default font-modifying the tool—is tailoring. It should be noted once again that this does not necessarily create a crisp distinction: What is it when you create a new style in your document? That act (at least in Microsoft Word) both creates a style and changes the selected paragraph; so in this distinction, creating a new style can be both use and tailoring. Note also that one person's tool is another person's subject matter, and hence, what is tailoring for one person can be use for another. For the Pascal programmer, changing the compiler is certainly tailoring, but for the team developing or maintaining the compiler, it is use.

The last distinction concerns the duration of the effect of the change. If the modification is so that an effect can be achieved later, then it is tailoring. If the modification is made so that the effect is immediate only, without any impact later, it is use. Thus, if I need a window which is buried and I move windows around on the screen so that I can access it, that is use; if I rearrange windows so that when I next want a project folder it will be easy to find, that is tailoring.

These three distinctions align fairly well in the sense that they seem to get the same answers. Usually, changing the tools is for later effect, and usually, the tools are more stable than the "material" they are used to transform. However, not all these distinctions are meaningful in all cases. The windows of the second example are the subject matter of the window system in both usages; one isn't affecting the window system (the tool) by rearranging windows. (Note that one can affect some window systems: change the layout algorithm from overlapping to tiled, or set it so that it grays out windows which have not been touched for a while.) For this reason, all three distinctions are offered as a set, complementing one another, and jointly informing the concept.

## Who Are the Tailors?

After having discussed the activity of tailoring, let us briefly consider the people doing it. Who are they? The simple answer to this question is: those who design in use. "In a paper by Trigg, Moran, and Halasz (1987), the discussion is restricted to activities carried out by users. However, the hospital example discussed previously illustrates what we consider to be succesful tailoring of a sysem, but not one done by the users directly. It was done by people from the company that delivered the system in cooperation with one of the users, because the users did not have the programming skills to make such changes on their own.

![](../../Design at Work Cooperative Design of Computer Systems (Joan Greenbaum (editor) etc.)/images/5f983b87b8858c6562ad6004dfcc544d8ed921ab3e893f1e0fb335c6fc9d38ca.jpg)

From our perspective the decisive point is not whether the users actually do it all themselves. We don't assign tailoring to one specific group. The central view is that the change is being made in response to local needs. Obviously a number of changes will be tailored by the users themselves, or not tailored at all, simply because they involve such small details that it makes no sense to involve people outside the use situation. A few examples of this kind were already illustrated. But most cases of more comprehensive tailoring involve some local expert or supporters or application specialists, because the users don't have the competence.

## The Practice of Designing in Use

In this section we discuss the various activities involved in modifying computer systems. The viewpoint is that of a user turned designer who is trying to change the way in which technology behaves. It may require that a user brings in others with special skills to help achieve those changes.

We address the practice of designing in use in two parts. First, we present three kinds of activity that change the behavior of the technology. These activities are the normal focus of discussions of modifying technology. Second, we discuss the social and cognitive needs of people engaged in making such changes. These activities are often overlooked, because they do not directly change the technology.

## Changing Behavior

## Choosing between Alternative Anticipated Behaviors

Many systems allow the users to choose between alternative behaviors that the developers have anticipated will be needed in particular situations of use. The standard mechanism for doing this is through software switches or parameters. An electronic mail system may have multiple delivery services that it can use to deliver mail; a switch is provided to allow the user to choose the one that is appropriate for the local site. Word processors must use some font to display text when the user does not designate one; a parameter is provided which the user can set to indicate which, of all the fonts available locally, is the default font to use.

With this kind of tailoring we utilize a predetermined set of dimensions from which we choose among the different options provided in the same way as we may adjust the front seat of a car. In well-designed systems the possibilities make sense to the users and are easily identified, for example, via menus. For these reasons the users are able to adjust a system by these means. On the other hand, the possible adjustments are limited to those which have been explicitly anticipated by the designers.

In the early use of Buttons, it quickly became clear that for any particular button, the points of change were usually fixed: on the address button, people would change the label and the address (but not the font, look, size, help message, etc.). A mechanism was added to Buttons which permitted button designers to pick out these points of change; that is, parameters were added. These parameters were used to replace general editing with a simpler process of choosing as the means for altering commonly changed aspects of buttons.

Sometimes the range of choices for any particular dimension of variability can be extended by a user through simply adding new material to the environment in which the system runs. Thus, new default font choices are provided by buying and installing additional font definitions.

A limiting case of achieving different behavior from technology is to replace "the whole thing" with a different one. One word processor may provide the footnote format required by a particular journal;

when writing for that journal, a user can achieve the behavior desired by choosing that word processor. In the case of buttons which failed, or failed to meet new challenges, requests to fellow workers and supporters were a common way of getting a new button to simply replace the unsatisfactory one.

Where parameters are concerned, the major lesson for designers is that parameters themselves must be seen as elements of the resulting tailorable system. Thus parameters must be definable, and manipulable in uniform ways. Computer users must be able to find what parameters are there, what behavior they affect, what values are legitimate, etc. The supporters and designers (including, ultimately, the users) must have tools to add new parameters to the collection. This viewing of parameters as tailorable elements in their own right is the direct consequence of our requirement that the tools for tailoring be tailorable themselves.

## Constructing New Behaviors from Existing Pieces

Some systems are created as configurations of smaller parts. Construction sets of all kinds exist in non-computer based technologies: office furnishings are composed of pieces of furniture; book shelves are composed of shelving and brackets; Lego and Erector sets create wonderful arrays of toys. In computer systems, file systems and folders mimic the physical world; spreadsheets are composed of linked cells; accounting structures are built of linked spreadsheets.

![](../../Design at Work Cooperative Design of Computer Systems (Joan Greenbaum (editor) etc.)/images/ccc13f7be94af6a635befd25986a9bda39d8290ba6de2730fa3029eef5f3ccb0.jpg)

The behavior of such systems can be changed by changing the configuration. Sometimes the change can be simple rearrangement: in offices we push around the furniture; with desktop computers, we push around the windows. In other cases, more elaborate constructions are required to meet the changing needs of the situation.

Rooms, a Xerox system for constructing separate "screen work spaces," has one such mechanism for constructing rooms from other rooms: It was discovered in making and using rooms that many rooms would share a collection of common tools—the clock, your calendar, an application window for alerting one to the arrival of new mail, a door to get to the mailroom. To accommodate this commonality, rooms were provided with the ability to "include" other rooms, with the idea that the common tools would be put in a single "control panel" room that would be included in all relevant rooms. Subsequently, inclusion was used for other purposes too, suggesting that it is an appropriate mechanism for tailoring (cf. Henderson & Card, 1986, and Card & Henderson, 1987, for information on Rooms).

A special case of construction is that of "accelerators." A system is augmented by constructing a new operator from a sequence of operations grouped together. Ideally, the new operation may be treated in the same way as the original operations, and in particular can be used in the construction of yet larger and more powerful operators. The address buttons discussed above are accelerators. A prime factor in the success of the Unix operating system is the incorporation of such a construction philosophy for commands in the various "shell" command languages.

Another special case of construction as a way of adapting technology is "going outside the system." Here, the system is modified not by rearranging its internal parts, but by using it as a component of a larger constructed system which does what is desired. Thus, to take an example from non-computer based technology, if the range of settings for the driver's seat in our car isn't good enough, we may add a pillow to the seat.

Another argument for using a software "component" in multiple constructions is that the interface need only be learned once. For example, the task of identifying a file on the Macintosh is supported by a single dialogue which is used by most applications. However, the quality of the integration is crucial. Consider the case of spellchecking: When the first spell-checkers arrived for the Macintosh they were separate programs that could process a number of different file formats, including those used by MacWrite and Word. The spell-checkers solved the problem of spell-checking on the Mac in a uniform way, but the integration was so poor that Word users quickly abandoned them when Microsoft offered spell-checking as an integrated part of Word.

A special case of commonality is that involved in the common use of an object (with behavior) as the base for many specializations. Thus, for example, the fact that the generic button supplies a common set of interactions for moving, copying, editing, deleting, inserting in a document, etc., means that all buttons inherit these interactions and need only be learned once. Designing good specialization, in both the mechanisms and the concepts expressed using them, is hard to do well. System designers can provide good mechanisms. They can also provide good examples of how to break up concepts so that specialization is easy and productive. However, at the center of the creation of good conceptual structures is good design and good taste; teaching it may be hard.

The lesson for designers of systems that can be tailored through construction is that the elements and mechanisms which support construction must form a coherent assemblage and support a coherent tailoring activity. This lesson is present but hidden in the term "construction set," which appeals to our sense that sets are the results, not of chance, but of conscious focused design. That is, construction must be designed.

## Altering the Artifact

As the most radical kind of tailoring, a last resort when other simpler means fail, we consider altering the artifact itself. (In the case of constructed systems, we consider not the reconstruction, but only the alteration of the smallest nonconstructed pieces.) If we look at the alteration of non-computer based artifacts, we may consider such examples as cutting 25 cm off the legs of the old dining table and painting it, to turn it into a coffee table for a child. Turning to computers, such alteration involves a potential alteration of all parts of a system, particularly the source code.

Changing the source code directly is in most cases infeasible. The code is usually only understandable to the designers; there is no obvious relation between the appearance and behavior of a system and the code. Consequences of specific changes are not detectable in any comprehensive way. Updating and maintenance get extremely complicated. And finally copyright concerns will in most cases make it impossible to get or provide the source code, at least at a reasonable price. Despite these difficulties, changing the source code must be retained as an option to consider.

But means of altering code other than direct change of the source are available. The most powerful of these are code architectures that make it possible to add to the behavior of code without modifying it. A number of such possibilities are found in object-oriented programming; inheritance or specialization, for example. The invocation mechanisms for functions on objects in object-oriented code make it possible to define new classes that specialize the behaviors of existing classes that one cannot examine for the reasons just mentioned." An "event hook" in LISP is another feature that allows users of a system to write LISP functions and install them on objects, to be executed whenever the corresponding event occurs for that object. For example, when the user clicks on a button, the LISP expression which is the value of the "ACTION-hook" is evaluated.

These ways of extending the behavior of code, however, require programming skills. This is the point then at which users may call on supporters for help. It should be noted that there is plenty of precedent in the non-computer world for obtaining such expert help: as the very existence of the profession of tailors makes clear, "users" of clothes do not all possess the skills needed to alter them. When dealing with computers, however, lack of knowledge about possibilities for tailoring may severely limit the users' initiative.

The preceding characterization of tailorable systems is heavily informed by the formative paper on the adapting and tailoring of the NoteCards hypertext system (Trigg et al., 1987). That paper focuses on the characteristics of technology in order to define properties of systems. Here, we focus on the activities that the tailors must do. Our understanding of the relationship between these two different perspectives is as follows. The four properties of adaptable systems are that they should be: 1. Flexible: a system with objects that the user can interpret in different ways. We regard such adaptability as addressing not the system but its use—-a crucial capability, but not one that we are discussing here. 2. Parameterized: offering a range of behaviors from which to choose. We see this as focusing on a particular means of choosing. 3. Integratable: a system that can be used in a construction set. Using a system in a construction is only one of the activities associated with construction. 4. Tailorable: a system that allows the user to change the behavior of its parts through accelerators, specialization, and adding functionality. We see accelerators as construction, while adding functionality and specializing behavior are altering the artifact. In summary, these characterizations are similar and should be seen as carving up the same space according to different perspectives.

## Supporting People in Changing Behavior

We now turn to supporting people engaged in the activities of designing in use. A simple view of these activities is: Some people "author" changes to the technology and make them available; others, perhaps including those authors, make use of the changes. Changes, like the technology itself, become objects to be trafficked in by users. Not only is improved behavior to be had, but membership in the "community of users" may depend on taking part in usage discussions concerning them. The interaction of people with changes becomes merely another case of involvement with design of the system; but, of course, in the case of tailoring, the design will take place locally, motivated by local needs, and often driven or implemented by the users. We can think, then, of a "life cycle" of changes, and look at the support needed to maintain its activities: creating, protecting, perpetuating, sharing, inspecting, learning, and providing feedback.

## Creating

The first job is to make authoring as easy as possible. The easiest way of creating something is to copy it from someone else (see Sharing). This was the usual way for workers to get a button to do something they wanted. If borrowing fails, the next best move is to copy something you have that is like what you want and modify it. This was the second most common way for workers to acquire buttons. Sharing and copying require finding out what is out there, or nearby; so support for this means of creation is the support of information access: finding, negotiating, making available.

Authoring should require as little new mechanism as possible. That is, provide modification using familiar means. What particular means are already familiar to the user (turned designer/author)? Most immediately, there are the objects and mechanisms of the system being changed. If the changes can be expressed using the system itself, then mastering new mechanisms is not required. For example, a macro in Microsoft Excel is made up of commands. Commands are expressed as cell formulae. Thus, the language of commands in Microsoft Excel is an extension of the language of cell formulae that the user already knows. In contrast, the most general means for changing Buttons is the LISP expression editor, something not required in using Buttons.

Another related source of familiarity is that which a user has with the use of the system itself. This resource can be directly tapped through various means of "construction by demonstration." For example, consider creating composite commands: the user enters a demonstration mode and carries out the sequence that is to be captured; the system watches and creates a new command encapsulating the sequence. Most UNIX shells have this capability.

A third way to tap familiarity is to use the same tailoring tools in many applications. Once a user has learned how to author a change in one part of the system (e.g., in one application), authoring changes in other places will be already understood. For example, the fact that Buttons uses the LISP expression editor means that it is familiar to many LISP users because many applications appeal to this tool. And in contrast, the creation of macros in Microsoft Excel as discussed is completely idiosyncratic, working only in Excel.

Finally, familiarity with the objects of a system can be harnessed to capture regularities by letting the system extract an abstraction from a set of constructed objects, all of which are examples of the pattern (abstraction) sought (cf. Myers (Ed.), 1988).

## Protecting

Ease of authoring is not an author's only need. In addition, there is the concern that in changing the system for personal use, a user may mess it up for someone else. This is not a problem if all changes affect only the local author and remain with the local author. But most authors want to share good things, which leverages the effort expended in authoring the change. Thus, for example, when making variable something that had been fixed, one can run the danger of forcing all existing users to learn about and make a new choice. To avoid this problem, an author can insure that the system default to the old behavior. Under this scheme, users need learn nothing about the new choice until they really have a need for it.

And finally, the author must make the change easy for a user to learn about, to learn, and to use. This requires documentation. Further, it is desirable that a user (who may be the author) be able to continue to evolve the change. To aid this continuing design, the history of the design can be a great help, either in conveying the thinking behind the design, or in putting a subsequent author and the original author in contact.

## Perpetuating

Changes become a central part of the definition of a system, because they must be added and deleted, set and manipulated, talked about and shared, by the members of the community of users. Thus it is important that means be provided to support changes as objects (objectification of changes) that will be perpetuated while the system remains in use.

First, a change must become an object. Sometimes a change is captured as a procedure to apply to a system (e.g., adjust the timezone to your local site). These are quickly objectified by creating an object that when applied in some way to the system will carry out this change.

Changes must be objectified for the users, too. A key activity is giving them names or other short descriptions so that they may be referred to verbally and searched for in storage structures. For example, choices in programming environments are often named by the variable in which the value for the choice is held.

Means for storing and applying the changes must be provided. "Initialization files" are often used, either to encapsulate a single change, or to hold a collection of changes. An important requirement for these storage mechanisms is that they support not only individual changes, but the means of assembling them into structures.

One view of buttons is that they are objectified actions. A crucial part of their becoming a powerful mechanism for tailoring in the research communities that use them is the provision for perpetuating them. A means was provided to automatically save buttons such that when a new system was loaded, the buttons in the old one would magically (without user knowledge or action) be restored. This made it worthwhile spending effort on crafting and adjusting buttons.

## Sharing

First the news must be published that a change is available. Any or all means of communication can be used. Most interesting are mechanisms that are themselves part of the system. For example, Xerox ViewPoint has a Loader mechanism that can find all enhancements and applications that have been published locally. UNIX has the MAN (manual pages) mechanism that organizes on-line documentation. Buttons were included in documents and thereby passed around as e-mail, and appeared in documentation.

Next, means must be available for acquiring the change. Here again, system-based mechanisms can organize the work, providing uniform strategies for acquiring changes. Finally, taking advantage of changes sometimes must be coordinated among collaborators. For example, if a user unilaterally acquires a new font and employs it in documents, collaborators who lack that font may have difficulty reading the documents. Such coordination requires a user to be able to know who is affected by the change being contemplated and to interact with them. When people do not want to change, it may also require more complex mechanisms for supporting out-of-sync evolution of systems, in which systems with different modifications can "inter-operate" together. For example, most document editors can upgrade a file written by an older version of the editor; fewer— but some—are prepared to read the newer (and non-understood) objects in a file created by a newer version, preserve them across editing, and write a newer version file.

The other side of this requirement is the need to help users stay current. As colleagues evolve their use of shared systems, they may find that they are operating in a way that is regarded as obsolete and outdated. Keeping completely current may be very time consuming. Knowledge of what others are doing is needed to support achieving the necessary balance between change and stability. Thus, sharing must include knowledge not only of available changes, but also of current usage patterns and understandings of acceptable practice in the local community.

A special case of coordinating with others is the establishment of the necessary assumptions upon which a change depends. Buttons created severe problems for workers on more than one occasion when e-mail containing buttons was not even readable because the receiver's environment lacked something required for the button to display itself. Eventually, button mechanisms were designed so that a failure did not disrupt the receiver's system. The lesson for the designers of tailorable systems is that the architecture of the mechanisms must be robust enough to handle errors in the practice of tailoring. Handling errors means not only minimizing failures, but also providing enough information to diagnose and report failures that do occur.

## Inspecting

A user wanting to change a system will want to know what changes are already there and their history. This history includes the changes that have been made, who made them, and for what purpose, including the work practices that the users had in mind when modifying the system. All of this is needed for people to be able to continue to evolve the system coherently. For example, my Macintosh may be set up to mount certain directories automatically on the local fileservers; some directories are mounted to support working on certain projects, others are a function of people, others of social conventions of the working groups; others using my system casually may find those arrangements quite unclear.

## Learning

Reading documentation and talking to people about using a system change is one thing; learning to actually use the system in its modified state is quite another. Real learning requires much additional work, both to find out how the technology actually works in detail and, more importantly, to learn how to use those capabilities in their work. This involves the mapping of task needs to system capabilities and the development of practices of work to support the use of the system. For example, making copies of large documents on certain copiers requires that there be a flat working surface to hold intermediate stacks of paper, and a large stapler, with a desk strong enough to take the pressures of using it. Buttons are easy to use (just push them), but the effect is not always so easy to predict. The central Buttons mechanism includes a means of giving a user simple help. In addition, conventions have developed encouraging the publishing of buttons in documentation, preferably in e-mail. These conventions support an important pattern (see Feedback) in which trouble with use can be reported by simply replying to the e-mail that brought the button to you. However, once received and put onto the desktop (put to work), buttons lose their ability to lead the user to documentation or the author.

Such learning must inevitably take place in an exploratory mode. Some attempts will fail badly. Users will therefore want an environment for supporting this learning with two important properties:

First, it must be possible to experiment in a safe way, in a way that guarantees that no damage will result from misunderstood changes to "real" information. For example, users experimenting with Excel often open a new worksheet to try out new formulae and macros, knowing that changes usually happen to the sheet in which the formula is located. Second, after exploration has settled down, "real" work may have been done in that safe but "unreal" environment which one would then like to preserve. For example, copying the newly debugged formula from a trial Excel spreadsheet to the real one is quite easy.

## Providing Feedback

The final step, closing the development cycle, is to provide feedback to the creator(s) of changes, based on experience with using the modified system. This is essential for the continued tracking of user needs by the authors of changes. When a user is the author, this activity amounts to the user reflecting, on occasion, on experiences with the changes that have been created. Interestingly, the detection and reporting is often considerably easier in the case of difficulties than for success. Difficulties make themselves known by their negative results, to which the user is usually forced to attend; successes are often very much harder to see; something going right is usually the result of many things going right. And, there is the human question of motivation: "If it ain't broke, don't fix it" is the death of much feedback.

To provide feedback requires knowing what information would be useful, who to feed it back to, and how to get it there. This is the other half of sharing, and the considerations on information dissemination apply here just as they did there. Mechanisms for providing feedback can be built into the system itself. For example, the installation procedures on the Hermes message system ensured that any user with a comment could simply use the "comment" command and Hermes would get the comment to the developers (Henderson & Myers, 1977; Myers & Mooers, 1976). The user needed to know nothing at all about who the developer was. And with buttons, particularly those that came in e-mail, when they didn't work, one could reply to the e-mail (thereby getting it back to the sender without thought), including a few well-chosen words about what had gone wrong--a very easy exchange indeed. The lesson here is that tailoring should not be considered independently of the communication mechanisms that will support sharing and feedback.

More important than the mechanisms for delivering experiences of use to the authors of change is the establishment of a climate of collaboration among users and authors that fosters the learning that all use makes possible. There is a cost even to sending a comment, and more cost if the system has been very difficult to use and the user can't characterize what happened or went wrong. The investment in feedback, however, can be seen—if the larger social system is correctly constituted-as not only a duty, but as a likely source of a better tomorrow.

## Some Problems with Tailoring—Why Not Tailor?

Before we conclude by summing up how to design for tailoring, we look at the down side of tailoring, at some of the major pressures against changing the behavior of a system.

## Tailorability Is Hard to Provide

As discussed previously, to make tailoring possible may require implementing lots of switches, construction sets, mechanisms for adding behavior to code, and integrating into communication systems and social systems. This is not always a large job, but it always adds to the work and in some cases is a great deal of work indeed.

Second, the mechanisms for allowing design in use must be provided. An interface (or interfaces) must be designed and built. It is interesting to note that while buttons have been in use for a number of years, the mechanisms for editing them are still under development.

Third, mechanisms for saving and reestablishing the state of the system must be built. The mechanisms for appropriately saving and reestablishing can be difficult to construct. No current system does this in a principled way, the problem being to untangle the tailoring done by the possibly many authors who have provided changes to an environment, once it is in place. There is research needed on this issue; the principles have not yet been worked out. In Buttons, this difficulty manifests itself in not knowing, for a button which has passed through many hands, whom to give feedback to; or when a new version arrives in the mail, whether the new one should be used in place of one the receiver already has and is happily using.

Finally, there is the very pragmatic fact that all these additional mechanisms add to the resources necessary to use the system. Effort must be expended to create them, adding to the cost of acquisition (construction expense or price). And the system is normally larger, requiring more machine resources to run it (memory and disk space).

## Learning

Turning to the user side, a system with more "stuff" in it requires more learning. A user must learn about the various design possibilities and what aspects of the system's behavior they affect. When the means for design are programming language expressions, the language, its forms and their meanings, must be learned. The interface(s) to the tailoring mechanisms must be learned too, including, where relevant, editors for creating and manipulating linguistic expressions.

Beyond learning the details of the technology of tailoring, a user will need to understand why a particular possibility has been provided by a designer. That is, what applications are better supported by the system if it behaves in one fashion or another. Consider, for example, what happened when word processors were upgraded to permit user control over the fonts in which their text appeared. People usually had no training, skills, or even taste in the arena of typographic design. In many places there was a severe outbreak of ont-itis," the inappropriate use of fonts in documents.

Finally, systems used together often must have their tailoring coordinated. Consequently, a user may well have to learn how colleagues and correspondents tailor their systems for the collaboration to work. For example, if one user employs a package of macros for the spreadsheet program Excel, those sharing these spreadsheets will have to do the same.

A variant of the learning task is the remembering task. Once committed to using certain features of a system, there can be a continuing difficulty in making use of that capability. One forgets how to use it and has to turn to manuals, examples, and colleagues to reproduce the knowledge.

## Using

If one wants to or is forced to tailor, a lot of time may be required. In particular, a changed system will inevitably require changing one's practices of use. It is a very common feeling that one may never regain in time saved, the time spent learning to save it. When the mechanisms to protect against unsuccessful tailoring (breaks, wrong function) themselves are unsuccessful, this can be doubly annoying and time-consuming. Difficulties in saving and restoring buttons have on more than one occasion severely endangered their continued use in one research lab.

Tailorability produces an explosion in configurations in single systems, and when systems interact (when don't they?) the possibilities are endless. A plethora of configurations increases the likelihood of interactions that have to be dealt with by tinkering until things work. Careful factoring of effects can help manage this complexity, but trying out a new configuration may waste a great deal of time and try a lot of patience. So the users will bear the cost of possible tailoring while they are using their systems, whether they tailor them or not.

Finally, but often foremost, is the possibility that the variability provided is just not of any interest to the users. The fact that multiple fonts are available may not be of interest when writing a book which will be typeset by the editors or publishers. The provision of many features, so called "creeping feature-itis," is an ever-present source of unlooked-for and unwanted tailorability, for which users pay a price.

## Babel

A common experience with tailorable systems is to sit down at a colleague's machine that runs systems that you use on your machine and discover that you can't use them because they have been tailored in ways that you are unfamiliar with. Keyboard "wirings" and macros are particularly difficult to adjust to because one's patterns of usage get "built into one's synapses"—backspace is in a certain place (the delete key, or control a, or leftarrow) and the impulse to backspace produces finger motion faster than one can easily control. In Buttons, the unavailability of buttons familiar on your own machine may make it impossible to do things you very commonly do at home."

In some situations, it would be useful if one could install one's own personal "style," including packages, "over the top of" your colleagues' behavior. This is not usually easy to do, because the "saving technology" is not sophisticated enough to save the personal style separately from everything else. For all these reasons, people are loathe to adjust other peoples' systems to their own styles. This makes sharing machines harder when tailoring is common.

Of course, there are cases where you would not want to change to your personal style anyway. When you are trying to help figure out a problem, particularly concerning the behavior affected by personal tailoring, or when you are working collaboratively with a colleague with both of you seated at her machine, you are depending on her style being in force. However, with extensive tailoring, the unfamiliarity of styles—indeed, the languages of interaction—can greatly increase the difficulty of even talking with one another about the things that happen in the system. It becomes harder to help or debug, and collaboration can be reduced to content, not implementation. Other familiar cases are naming files or arranging directories: when collaborating using files, personal styles conflict, and compromises or decisions to live with incompatibility and inconsistency must be made.

## The Missing Designers

Finally, in those cases where professional designers are absent from the "tailoring loop," tailoring may even decrease the usefulness of a system. The subtitle of this book emphasizes the cooperative nature of good design, and just as we have argued for the need to include users in the design process, the competence of designers will often be needed. Particularly in cases where the professional competence of the users does not otherwise include tailoring, it may be wise to seek assistance before modifying a system. An example of this kind is described in Grudin and Barnard (1985), in which command names tailored by naive text editing users were much less effective than those supplied by skilled designers.

## Designing for Tailorability

Tailorability is no panacea, as the preceding discussion illustrates. And what is more, possibilities for tailoring will in many cases be application specific, requiring genuine design work by the creators of a system. However, the reasons for tailoring remain, and experience indicates that the resources saved in the initial development by ignoring tailorability issues will be spent several times over during the use of a system, either by the people doing the maintenance, or by the users who have to take still more elaborate action to bend the system to changing circumstances.

The lesson is desin and arhitecture.If an artifact is ceate with change in mind, even if the specific change is not anticipated by the designer, the creation of change can be greatly simplified, regularized, and most importantly, supported. A simple example of this was given early in this chapter, in which new help messages were added to a system.

An important step in providing more user-accessible tailoring will be to develop new high level, or application-oriented, building blocks together with application-oriented ways of manipulating them. In terms of our characterizations in this chapter, altering of artifacts will be transformed into construction by finding decompositions of those artifacts that align with the understanding of users. The third case described in this chapter, Buttons, is a first step in this direction.

Object oriented design and implementation are a promising basis for this kind of work, since they may allow us to shorten or even bridge the gap between the structure of computer systems and their code on the one hand, and the structure of the work and concepts of the application area on the other.

## Acknowledgments

Thanks to Jonathan Grudin for tailoring our language and to him and many of the authors of this book for helpful comments.

## References

Brad A. M. (Ed.). (1988). Creating user interfaces by demonstration. San Diego, CA: Academic Press.

Card, S. K. & Henderson, A. (1987). A multiple, virtualworkspace interface to support user task switching. Proceedings of CHI+GI '87, (pp. 53-59). New York: ACM Press.

Grudin, J. & Barnard, P. (1985, April). When does an abbreviation become a word? and related questions. In Proceedings CHI '85, Human factors in computing systems (San Francisco), (pp. 121- 125). New York: ACM Press.

Henderson, A. & Card, S. K. (1986). Rooms: The use of multiple virtual workspaces to reduce space contention in a window-based graphical user interface. ACM Transactions on Graphics, 5 (3), 211-243.

Henderson, D. A. & Myers, T. H. (1977). Issues in message technology. In Proceedings of the Fifth ACMiIEEE Data Communications Symposium, September 27-29, 1977 (pp. 6/1-9). New York: Snowbird, UT, IEEE.

MacLean, A., Carter, K., Lövstrand, L., & Moran, T. (1990). User-tailorable systems: Pressing the issue with Buttons. In Proceedings of CHI '90 (pp. 175-182). New York: ACM Press.

Myers, T. H. & Mooers, C. D. (1976). HERMES user's guide. Cambridge, MA: Bolt Beranek and Newman Inc.

Sheil, B. (1983, February). Power tools for programmers. Datamation, 29 (2), 131-144.

Trigg, R. H., Moran, T. P., & Halasz, F. G. (1987, September). Adaptability and tailorability in NoteCards. In Proceedings of INTERACT '87. Stuttgart, Germany.
