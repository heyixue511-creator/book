> 来源：Design at Work Cooperative Design of Computer Systems (Joan Greenbaum (editor) etc.)
> 原始文件：C:\Users\lenovo\Documents\Codex\2026-05-29\书籍专著\Design at Work Cooperative Design of Computer Systems (Joan Greenbaum (editor) etc.)\Design at Work Cooperative Design of Computer Systems (Joan Greenbaum (editor) etc.).md
> 识别方式：一级标题

# Language, Perspectives and Design

Berit Holmqvist and Peter Bøgh Andersen

The inversion of viewpoints occasioned by Structured Analysis is that we now present the workings of a system as seen by the data, not as seen by the data processors. The advantage of this approach is that the data sees the big picture, while the various people and machines and organizations that work on the data see only a portion of what happens. As you go about doing Structured Analysis, you will find yourself more and more frequently attaching yourself to the data and following it through the operation. I think of this as interviewing "the data."

DeMarco, 1978, p. 49

In opposition to the dominant data flow perspective, expressed in this quotation from Tom DeMarco, this chapter presents a positive understanding of users as sources of information. This does not mean that the data-flow perspective is rejected, but if this perspective is the only one adopted, and if the working of a system is not also "as seen by the data processors," then system development is going to miss crucial information.

This chapter does not present the users' point of view but rather the activities of the workers and the working of the system as seen from a linguistic point of view. We introduce linguistic concepts and methods for analyzing interpretations of work and organizations. The concepts that are part of the stock in trade of traditional structural linguistics include sign, code, perspective, semantic field, syntax, and case, and are successively introduced and explained, so that the reader ultimately should be able to understand system development from a linguist's point of view.1

We view computers as controlled by means of signs, either verbal or pictorial. Like other sign-bearing media such as books, newspapers, film, or video, they should present relevant and understandable information. This is not always the case, as illustrated in the following taperecording, where a worker tries to explain the meaning of the log in the system she uses.2

L: They are different files, it is how much frags there are, how many errors there are, hots, what was it, it was ... do you remember?

X: Yeah.

L: I don't remember shit of what I learned there.

The log is clearly incomprehensible to the worker. It is full of "computerese," and at first sight one is tempted to blame the disfunctionality on that. But as linguists we knew that foreign words could be learned if they occupy a relevant place in a language system. The essential point is that computers present a particular interpretation of the tasks performed on them. If that interpretation is irrelevant to the workers actually performing the task, it prohibits the understanding of the system. In the following quotation, two workers are discussing the same system, the topic now being the control area of the screen where descriptions of the tasks are displayed.

H: Like, if we say, now it says "completion" up here, but then, when I finish the pile, then it says "production," how come?

R: Because then you begin a new "production," then, when you type, when you have typed the first one and the last one, then it says "completion."

H: Yes.

R: It always says here exactly what you're doing.

In this case, H has a different idea of "what she is doing" than the system has. Will H maintain her own interpretation, or will she come to accept that the system in fact "says exactly what she's doing"? In the latter case, whose interpretation of her work is it she adopts when accepting the interpretation given by the system?

To construct computer systems is also to construct and communicate an interpretation of the tasks and the organization in which the system is used. Although we do not believe that a system designer should design the computer-based sign system as a copy of the existing work language, we feel that some knowledge of the latter is a good basis for understanding the part of design that has to do with the users' interpretation of the system. It will give the designer a keener awareness of the design choices in this area. Therefore, we also show how these methods can be included among the techniques for designing computer systems.

## Perspectives Differ With Organizational Roles

In a traditional hierarchical organization, it is possible to distinguish between two fundamental roles in relation to the work: one role that performs the work, and another that describes and organizes the work. Linguistically, this means that one either talks in the work or about the work. In such an organization, there is often a clear distinction between these two. The roles are, of course, not fixed, and their manifestations vary according to the situation. The following is based, however, on the hypothesis that there is a fundamental, visible differentiation of manifestations, and that there is a methodological point in describing people's linguistic manifestations as a product of their varying associations to the work process.

## Describers and Performers

In the following example, (1) has been taken from a recorded interview with a coordinator, (2) from a recorded interview with an instructor who teaches the use of the system at office level, and (3) from a recording of the work language at office level. In (1), the interview takes place in the office of the interviewed, in (2), at a table in the bookkeeping department, and in (3), at a work station.

## (1) The coordinator:

One of the purposes of the Optical Character Recognition is of course that one can read everything optically-directly, that is— for example, our pay-in slips "C"; because they have complete rows of optic codes, so they never have to pass the B 25.

## (2) The instructor:

They code a lot of C-slips that have this optic area—the machines are able to read it, and so they read the slip and we don't have to touch it—when we put it into the frame, the machine reads it and then we lift the blue box, and then they are ready.

## (3) The work situation:

E: Well, I think you should do like this: you take a small piece of paper, and then you attach it to the C-slip to tell that it is a C-slip. Later, when you have got it back, then you put everything in this box.

X: Well, I'll have to leave this till tomorrow morning, then I'l give it to her, because I had one today that I left for her—a slip that was missing something that she had cut out— we'll take that too, and then I'll put back this C-slip when she ... well

E: Because she is bound to see that one too if you leave it for her, she wants to see the C-slip, too.

In the first two examples, the interviews take place outside the work situation and the persons are talking about work. The difference is that the person in (1) does not normally take part in the work process in question, whereas the person in (2) does. In (3), the persons interact with and comment on the process in which they both take part.

When we look at reality, we always concern ourselves with parts. We are interested in one slice of the cake, and we reject the rest. In simple terms, what we are interested in is usually something we want to learn about, or think that the person we are talking to wants to learn about, and what we reject are things we do not need to know, or which we already know. This has direct consequences for how we select things to talk about.

In this case the selection has been done by us; we have picked out bits from long conversations. Furthermore, in the first two cases, the participants' actual selection is determined by the questions asked by the interviewers, the subject being "advantages of the new system"; and in the last case, it is determined by the working process—the persons talk, in a simple manner, about problems as they appear in the course of the work.

## To Be General or Specific

In both (1) and (2), the attitudes toward the work process are of a general nature. Both persons are able to describe the general premises of the process without including specific persons or objects of time and space. This is demonstrated by their choice of indefinite pronouns, for example:

one can read

a lot of C-slips

and in the use of nominalizations:

the Optical Character Recognition

and temporal/causal relations combined with timeless present tense:

because they have .. so they never have to pass

Moving on to (3), we will see that this example is not in the same vein as the others, although it deals with the same working process. The description of the working process is not of a general nature; instead, the language is used for interacting with work and commenting on it. This means that the statements are related to time and space. They talk about specific work objects and specific persons that can be pointed out in the room. This is shown in the use of the definite article:

then I'll put back this C-slip

and personal pronouns:

then you attach

The actions they talk about take place within a certain period of time:

leave this till tomorrow morning

and in a certain sequence of time:

take a small piece of paper, and then..

When they talk about work they adopt a perspective of generality, whereas talking in work implies a perspective of specificity.

To Be Normative or Descriptive

The staff is working at work station B 25. In the first two examples, we find statements about the flow of data and the handling of material that are directly contradicted in the third situation. With regard to the C-slips (paying-in forms that are fully pre-coded), it is said that

they never have to be passed on to B 25

and that

we don't have to touch them any more

but in (3) there are indications that the C-slips are in fact included in the work at the work station:

you take a small piece of paper, and then you attach it to the C-slip to tell that it is a C-slip

then I'll put back this C-slip

This does not mean that (1) and (2) are lying, it simply means that they have both decided not to talk about the concrete reality; instead, they talk about the system as principle and possibility which can be seen in their use of words for purposes and possibilities:

one of the purposes of the Optical Character Recognition we don't have to touch it   
the machines are able to read it.

While the coordinator and the instructor are normative, talking about how the work process "ought to" be, the staff is descriptive, talking about breakdowns in the routine and how the working process "is." The work process "is" such that the C-slips are often not recognized by the machine, and have to be manually registered, but it "ought not to be" this way.

When talking about work it is easy to become normative since the work situation is not present to verify your description. This could be compared to the top down view of traditional system development. When talking in work on the other hand, deviations from the norm often become the main conversational subject. Therefore, revealing a normative perspective presupposes a thorough knowledge about the working situation, including the language that goes with it.

## Participants and Spectators

Although the coordinator and the instructor both adopt an "about" perspective there are differences. These differences are due to their roles as spectator versus participant. The coordinator's job is to establish routines for production and cooperation on an overall level. Therefore he has to adopt what is usually called a bird's eye perspective. The instructor's job is to teach the routines in direct connection to the work situation. She does not perform the work but still she is present in time and space, giving a helping hand and good advice. Therefore she tends to adopt what we will call an ant's perspective.

## Talking about Activities or Processes

The linguistic item that reflects their difference in perspective most clearly is probably the semantic roles appearing in the examples. A semantic role is a relationship between a verb and another constituent of a sentence describing an event. It is characteristic of the common semantics of verbs that they have certain roles attached to them. For instance, a verb like "read" implies that there are readers, agents, and that they read something, an object. They may use a magnifying glass, an instrument, to help them read: "Hanna read the book through a magnifying glass."

It also implies that the reading is done in time and space: "at the kitchen table yesterday." Sometimes there is also a cause built in: "Hanna who has bad eyes read.. ." The semantic role is supposed to be part of the linguistic deep structure. The linguistic deep structure is the abstract system behind our concrete usage of language, whic in turn is calld the surface structure, according to the tey of transformational grammar. The semantic roles can manifest themselves as different grammatical roles (sentence members) in the linguistic surface structure (see Fillmore, 1968).

Now let us look at how the coordinator and the instructor expressed themselves in the example given. The following constructed sentence represents the simplified deep structure:

Workers can read slips by the means of an OCR agent object instrument

It is now possible to vary the grammatical manifestations of the semantic roles on the basis of what one wants to emphasize.

The coordinator expresses himself like this:

everything one can read optically

Neither the agent nor the instrument nor the object is made the grammatical subject; instead a "subject dummy" has been introduced in the form of the indefinite pronoun one. And in the next one

(One of the purposes of) Optical Character Recognition

the event has been turned into a nominalization, that is a thing that can be given a grammatical role in a new sentence. The instructor, however, behaves a bit differently:

## the machine reads it

and makes the instrument the grammatical subject in all three sentences.

The coordinator's perspective is the perspective of a flow, in which the focus is on the paper and information (everything that one can read), and the actions on them viewed as objects (the optical recognition). This is not incidental, but fully in line with the traditional data flow perspective within system development, as DeMarco expressed it in the introduction.

The instructor focuses on machine activities that make paper and information flow. But this does not mean that she only sees a portion of what happens; she just sees more detailed portions. For example, the procedure which the coordinator describes as the optical recognition is described in three stages by the instructor:

we put it into the frame the machine reads it we lift the blue box

Whereas the coordinator rejects people as well as activities, the instructor includes the physical activities before and after the technical processing, with persons as agents. Whereas the coordinator goes on to talk about the work station, through which the "flow" does not pass:

## so they never have to pass the B 25

making the slips the subject of his sentences, the instructor stops at the workers, making them subjects and the slips objects:

## we never have to touch them

The coordinator's job is to establish routines for production and cooperation on an overall level. His work object is processes by means of which information is transmitted. To him, the information plays the main part in the game. The instructor's job is to teach the routines, and her work objects are workers performing concrete activities. To her the workers or their stand-ins performing the activities are playing the main part.

## Semantic Fields in Work Language and System

In the previous section, we contrasted different fragments of the language usage in the organization in order to illustrate the difference in perspective when persons with different functions describe the same phenomenon. In this section we will contrast system design with the work language around it. Our example will be the PGPsystem introduced at the Postal Giro around 1986.

The terms of the PGP-system for the work material are partly taken from the old work language in the bookkeeping department at the Postal Giro. But when the system was built, new terms were introduced; the old terms had to make room for new ones and were therefore given a new content.

The words for the tasks were taken from other sublanguages. In spite of the fact that the content of the new words is almost the same as the content of the words in the old work language, the words for tasks were rejected by the workers and were replaced by other innovations.

To describe this we use the concept of semantic fields. The concept is traditionally used within linguistics to make comparisons among the ways national languages classify phenomena in the world. As an illustration we give the following example of the extension of similar words in Danish, Swedish, and English.

Danish Swedish English
<table><tr><td rowspan=1 colspan=1>skov</td><td rowspan=1 colspan=1>skog</td><td rowspan=1 colspan=1>forest</td></tr><tr><td rowspan=3 colspan=1>træe</td><td rowspan=2 colspan=1>trä</td><td></td></tr><tr><td rowspan=1 colspan=1>wood</td></tr><tr><td rowspan=1 colspan=1>träd</td><td rowspan=1 colspan=1>tree</td></tr></table>

Figure 1. A model of a semantic field.

However, instead of comparing different national languages we just compare different sublanguages within a company.

## Old Words in a New System

First we are going to compare words for work material in the old work language, in the system, and in the new work language.

In the construction of the system at the Postal Giro, linguistic terms for the work material from the old work language have been applied as far as possible, but new words are also introduced. This leads to changes in the semantic fields.

As shown in Figure 2, the term "job" has been introduced into the system; it is taken from the work language of computer professionals, where a "job" is simply a term for a certain amount of data, which the machine processes as a whole. Thus, "job" has come to occupy the place previously possessed by "bunt"' (pile), (i.e., an amount of working material which is relatively easy to handle, but also arbitrary), and this causes "bunt" to be pushed into the location of the old word "BO" (i.e., the current transactions of one client ; a certain number of slips together with a payment order signed by the client). This chain reaction sets the meaning of the word "BÓ" in motion, so that it becomes more limited and now refers to the payment order only. (The corresponding concept is lacking in the old work language, as indicated by the large shaded area.)

This process is copied in the new work language with one exception: the work language version of "job" and "bunt" refers only to the physical cards that are actually in the hands of the workers, while the extension of the words in the computer system is "all slips read by the OCR together with the manually registered ones." This restriction of extension is symbolized by the shaded areas in Figure 2.

<table><tr><td rowspan=1 colspan=3>Old           Computer     Newwork         system         worklanguage                         language</td></tr><tr><td rowspan=1 colspan=1>bunt</td><td rowspan=1 colspan=1>job</td><td rowspan=1 colspan=1>s*    9908job</td></tr><tr><td rowspan=1 colspan=1>BO</td><td rowspan=1 colspan=1>bunt</td><td rowspan=1 colspan=1>80000000008bunt</td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>BO</td><td rowspan=1 colspan=1>BO</td></tr></table>

Figure 2. A semantic field for work material.

The old work language is based on a perception of the work as handling papers and documents, and an imitation of this has been attempted in the computer system. At the same time, the staff has demanded that they keep the ordinary slips in order "to keep at least a part of reality."

The result is that in the bookkeeping department there are now slightly different meanings of these words. One for the old system, one for (the paper slips of) the computer-based system, and one for (the electronic slips of) the computer system. The old system will progressively disappear; the idea behind an electronic system is to gradually render paper superfluous, but the fact remains that the terms are the same for ordinary slips and electronic signals. Our observations, however, indicate that it has been easy for the staff to adopt this linguistic change. We have not noticed any misunderstandings or conflicts as a result of it. For us as observers it was extremely difficult to know if the staff was talking about paperbased or electronic work objects, but for them as performers in time and space the situation resolved any ambiguities.

## New Words in a New System

We have already seen how words from the old work language have been borrowed and readjusted to the new system. In spite of a rather complicated change in the semantic structure, the new language usage is easily accepted by the users. Now we will look at a case where new words have been introduced.

One of the consequences of the electronic system is that several functions that used to be clearly separated in time and space can now be combined and carried out by one person at one work station without being separated in time. The old work system has two functions, "coding" and "correction," that are carried out in separate units and with the staff changing places every half hour; and one function that is carried out in a separate department, and that, in the work language, is called "the Correction." The system designers have introduced a more complicated and hierarchical description of the work organization, but have preserved the old interpretation of different functions in it, just with new wording. The monitor display contains the overall term "activity," divided into four functions on the next level, "production" being one of them and "other competence" another one. These two resemble the old division of labor with routine tasks performed in the department and specialist tasks performed in "the Correction" department.

"Production" has two subordinate functions on the same level: "completion," which equals the old task "coding," and "balance," which equals the old task "correction."

![](../../Design at Work Cooperative Design of Computer Systems (Joan Greenbaum (editor) etc.)/images/f4bc0f7fe071851e583b033abd06c180497c064b143ee19417cbc61fb10aad5b.jpg)  
Figure 3. A hierarchical division of tasks.

What is interesting about this is that the functions that used to be clearly separated—spatially, technically, and with regard to roles— and that the staff used to view as separate, when combined in the new system are viewed by the staff as a single function. In their new work language it is called "registering"; the employees neglect the outdated system description of the work organization and construct a new semantic field for tasks which again is based on time and space. The choice is between working at the terminal "registering" or at the OCR, now called "running" or "standing. The following figure, a rough generalization based on the most frequently used "functions" in connection with the work languages of the old and the new systems, illustrates this.3

<table><tr><td rowspan=1 colspan=3>Old           Computer     Newwork         system         worklanguage                        language</td></tr><tr><td rowspan=2 colspan=1>coding</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>running</td></tr><tr><td rowspan=1 colspan=1>completion</td><td rowspan=4 colspan=1>registering</td></tr><tr><td rowspan=1 colspan=1>correction</td><td rowspan=1 colspan=1>balance</td></tr><tr><td rowspan=2 colspan=1>TheCorrection</td><td></td></tr><tr><td rowspan=1 colspan=1>othercompetence</td></tr></table>

Figure 4. A semantic field for work activities.

Of course, there are technical and historical reasons for introducing this new division of functions into the system, but to the staff, the differences are hardly evident. As far as time and space are concerned, they are in the same work situation when working at the work station, and the terminology is by no means self-explanatory. If the purpose of this terminology has been to create a specificnpretation of the work process, the attempt has not been very successful, as was illustrated in the conversation in the beginning of this chapter.

"It always says here exactly what you're doing," the instructor said there. Does the woman really not know "what she is doing," or does she merely have another perception of it?

The examples in Figure 4 show that the new terms are taken from somewhere other than the work language of the bookkeeping staff The words "production," "completion," and "balance" do not exist in their old work language; they are taken from other work languages or professional languages. "Balance" is indeed a bookkeeping term, but it belongs in a theoretical situation. It is an educational term. Indeed, it was the main function of "correction" in the old system, but there was no word for this. "Production" is a term from economics. The word "completion" can almost be characterized as a common language term.

But as we mentioned in the introduction this is not a main point. The general meaning of the words are not that difficult to understand. Rather, the point is that the words that are chosen reflect a specific view of the work. The word "completion" is particularly interesting. It reflects the fact that the staff only performs parts of the work. They only add something that has been lost in the Optical Reading Recognition process. It goes perfectly well with the coordinator's flow perspective.

It is not unreasonable to expect that the workers should adopt the word. In fact the greatest part of their daily work, and their main task, is to perform this function. But as seen in the following conversation between the researcher (R) and the worker (H), the worker, in spite of the fact that she is obviously very well aware of the meaning of this specific word, is still not willing to adopt it in her work language:

R: Thee words up here, "alane"and pletion,"iyu use them before or are they new words?

H: No, they're new words.

R: Do you use them yourselves?

H: Completion, because when we were coding, we were holding all the slips, even the C-slips.

R: Do you say completion?

H: Yes, because here we only get certain things—if the C-slip is wrong, and then, when there's an error in the ID-section, and maybe it hasn't been able to read one or two digits out of thirty-four, then I simply type these digits he hasn't been able to read, and then I have to complete.

R: You say complete, do you?

H: Well, but we use to say—anyway, we call this registering.

R: Did you also use that word before? Did you say registering before? Or did you say coding?

H: No, comple—coding.

R: Registering is also new then?

H: Yes, that is also new—it was separated, because when they were sitting at "the checks" over there [i.e., a special section in the department, where they have had computer systems for a while], then it was registering, it was a little more posh.

"Registering," which the staff prefers, is an overall term for different types of data collection. And yet, here the term is related to data entry in computers. The reason for the adoption of the word is probably (as the example indicates) that the word is familiar in the department. It has been borrowed from a special section that was not occupied with coding and punching, and therefore needed a specific word for their data collection to mark the difference. Now when computers are introduced it can be used in the whole department as something different from the old techniques.

Two different perspectives meet in the system. One describes work as manipulation of physical objects. This is reflected in the reuse of old words for working material. The other one describes work as information processing, reflected in the introduction of the new abstract words for work organization. The staff chooses to accept the first perspective (as seen in their adoption of the new content for old words) and to reject the second (as seen in their refusal to adopt the new words and instead introduce one of their own).

## Semantic Fields as a Basis for Designing the Objects of the System

In the previous sections we have given examples of divergence between system and work language; a natural question to ask is: How can we use knowledge about the work language in design, and how might the system have looked like, had the work language been used as a basis for design? In this section, we show examples of how semantic fields can be used to get ideas for design.

The first thing to note is that there is no question of copying or translating work language into computer-based signs. There are two reasons for this. First, the computer is a medium other than the verbal language, and this alone prohibits direct copying. Second, system development normally also means organizational change— changes of task structure, of division of labor, of responsibilities and rights, and of values and norms.

The idea is to use work language as the point of departure for inventing new computer-based signs. It is more like making a film version of a novel than translating a book from one language to another.

The second thing to note is that work language can never be used on an isolated basis. However, after having studied and analyzed it, we can use it to build prototypes that can be used as a source for constructive discussions with users.

Our point of departure will be the previous observation that the semantic fields of the system are different from those of the work language, not only on a superficial level, but in the distinctive features that are used to structure them. Many signs in the actual system are related by part-whole relations, but these meanings are not operative in the work language.

We have seen that the workers used space and time as principles for naming their work processes; this same principle can be observed in many other places in their language. The following quotations are from a speaking aloud session. We asked a worker to tell us what she did while she worked. In her speech, work objects can go there, come, come forth;

you know, everything goes there

this one is no good because then all cards come

and she presents her own actions as a journey in a landscape of cards and tasks, describing the surroundings from her present location: come to, go to, go back to, be, sit;

because I came to the last card on this one

when I sit in "comp" then it is "completion"

Her own actions on the work objects either remove them from her: put aside, send back, place there, take out, take away;

then I put aside

then I have to take this signal away

or bring them nearer to her: fetch;

I could have fetched it

In addition to the spatial distinction between here and not here, the worker uses another basic contrast, namely between have and not have. Although the distinction between here and not here is closely related to the distinction between having and not having, with presence often implying possession as in the phrasing now I have the C- cards, cards can be absent but still in possession as in I have the cards in the flier.

These verbs can be arranged in a semantic field structured by three sets of features:

location versus possession

positive versus negative versus modal

(result of) process versus state

where positive location = here, negative location = there, not here.

For example, put aside differs from get by being concerned with location instead of possession, from come by leaving the object there instead of here, and from exist by being a process and not a state.

An analysis like this shows that the worker does not look at the data from a spectator's perspective, but views them from her own position—that of a participant—using mine and here as her points of reference. In addition, her conception of these landmarks seems to be positively charged, whereas there or theirs are negatively charged, since she uses the phrasings doesn't exist, doesn't have, miss about items that are located in other places or possessed by others.

We find this way of organizing the world quite sensible. In design it can be supported by declaring attributes of possession and location in all system objects that designate work objects. The precise value of these attributes represents the status of the work object. To give a few examples:

The card I am working on at the moment will be owned by me and located in a batch that is located in a job that again is located on my desk. When I send a superfluous card to the flier file,4 its properties change: it is no longer owned by me but by the whole department, and any worker is entitled to take it if needed. Also it no longer is located in the current batch but in the flier file.

A job can also be located in different places and owned by different people. The current job is, of course, located at my desk and owned by me, which means that no one else can see it or manipulate its items." If I cannot solve an error in the job, I can abandon it, making it a so-called red job5 as in the actual system. A red job can still be possessed by me because I may want to give it another try later and therefore wish to prevent others from taking it. On the other hand, I may also want to give it up completely and transfer possession of it to my colleagues in my section. When a job is finished it becomes a so-called green job; I lose possession of it, and its location is changed from my desk to the area of the section. Later, after the job has been checked against the paper jobs, it is put into a box and sent to the computer department which also owns it now. It means the section can neither access nor see it any longer.

These examples illustrate how the two attributes can be used to represent important aspects of the system objects denoting work objects. In addition, the attributes have the advantage that they are easy to express visually.

A possile screen layout, shown in Figure 5, could be as follows: The location of the worker is implicitly assumed to be at the bottom of the screen, and the locations of the work objects are symbolized by their distance from the bottom and the color of the surrounding area—the higher up and the darker the background, the longer the distance.

![](../../Design at Work Cooperative Design of Computer Systems (Joan Greenbaum (editor) etc.)/images/0b58d909d03e79672459ab37760e55d6607a936f12a58aabada8fecfc1282553.jpg)  
Figure 5. Screen layout based on the vocabulary of the work language.

The work objects near "me" are placed in the white rectangle in the bottom of the screen. Here is found the current job, batch, and card, together with the red jobs I want to keep for myself. At the opposite end is the computer department, where the boxes sent from the accounting department are now irretrievably outside our jurisdiction.

We have now described some properties of the system objects with a basis in the work language. The sentence structure of the work language can also give inspiration to the structure of the actions.

The sentences of the workers are built according to a limited set of patterns; our design can use at least the patterns relating to locating, transport, and possession. Figure 6 shows three patterns relating to transport, which occur frequently in our tape recordings.

Work Objects or Worker move Somewhere Worker moves Work Object Somewhere Work Objects or Worker is placed Somewhere

Fiure 6.Sentence patterns relating to transport.

The patterns can be used for the administrative part of the work: locating, moving, and taking or losing possession of data. Here are a few examples based on the patterns shown in Figure 6:

Work Objects moving by themselves can be used if the system is to supply the next card or batch after the previous have been finished. "The card or batch will "themselves" move into the work area and make themselves ready for data entry.

Worker moves Work Object will typically be used in problemsolving situations, where the worker and not the system should decide whether to move a superfluous card to the fliers or fetch a missing card from them.

To some degree, the final design will look like the direct manipulation interfaces of the Xerox and Macintosh systems. Our point is that the success of these interfaces can be explained by the fact that they have a conceptual basis in the users' work language. A natural inference is that work language is probably a rich source for ideas for other types of good interfaces.

Although we built a prototype based on the above ideas, the prototype was never tried out, and served only to make the ideas concrete. However, we feel that the design exercises at least show that it is not difficult to use work language systematically as a basis for design ideas. The benefit is that design is built on concepts which workers know, understand, and use in practice.

## Perspective as a Basis for Designing Interaction Styles

## Involvement Is Not Enough

The preceding design proposal is in the direct manipulation interaction style. When it is a question of performing routine tasks on objects, this is preferable, as it goes with a participant's perspective. In this section, however, we will show that this interaction style is not the only one. By studying the language games that arise during the process of work, one can get to the crucial problem of what user needs are, and avoid getting stuck with the (pseudo) problem of what is the superior overall interaction style (there may be none!).

The direct manipulation style is becoming more popular and is advocated by several authors (see Norman & Draper, 1986). Its purpose is to make the interface transparent, so that the users feel their work objects, and not the computer, to be present. The effect is achieved through a coding based on similarity: actions are coded as dependencies between graphical changes and user movements (e.g., clicking the mouse causes an object to invert, or dragging it causes an object to change location), whereas objects are coded as stable icons. Processes are denoted by processes on the screen, stable objects by stable pictures. The hypothesis is that similarities of this kind enhance a feeling of participation and involvement.

At least a part of the work language is suited for being coded with direct manipulation techniques, because—as emphasized in the first section—it is used for acting in the work situation, not for describing it from a vantage point outside. It is concerned with concrete instances, not with examples or classes. The theme of its sentences is persons or work objects, not tasks.

But our data also show that workers are not always involved participants in the work process. Sometimes they stop working, stand back to reflect, and actually adopt a spectator's perspective. On our tapes we identified conversations in which they tried to predict which kind of work processes the system would allow (forecasting), and conversations whose purpose was to explain uninterpretable system behavior (mystery solving). We will argue that a verbal interaction style can be preferable in these situations.

An example of forecasting is a short conversation where two workers try to fix the correct order of the tasks involved in sending a box to the computer department, entering new data into the system, closing the transmission line to the computer department, and processing cards. Mystery solving is illustrated by a long conversation where the workers try to figure out why fliers that have been removed from the flier file one day pop in again the next day.

Our thesis is that workers look at their work from two perspectives and these perspectives should be supported by different styles of interaction.

## The Participant Perspective

In the participant perspective the speakers' focus of attention is on the current goal and the relevant objects; the tense of the utterances is present; their agents are the speakers; pronouns are used instead of nouns; deixis (here, there) is used instead of prepositional phrases (on a table); the context of the utterances is known by the speakers and therefore not verbalized; the utterances often consist of simple sentences or parts of sentences; and they cohere with the work process, not with preceding or subsequent utterances.

The typical sentence in these conversations is a simple sentence (S) with a verb (V) denoting a task, and noun phrases (NP) designating worker and work objects, for example: I must take it away.

![](../../Design at Work Cooperative Design of Computer Systems (Joan Greenbaum (editor) etc.)/images/e4f2c9fdb8b5ac1f7341ac0d9134d864b1dbbc289292a7d56d5dbc262ed4c4d2.jpg)  
Figure 7. Participant sentence structure.

This kind of perspective can be supported with direct manipulation interaction that is intended to make workers experience the work process as a presence. We recode the workers' sentence structure in the following way: the verbs (denoting actions) are recoded as dependencies between user actions and graphical changes on the screen, while the noun phrases (denoting work objects or workers) are recoded as stable icons:

Noun phrases -> stable icons (contents: work objects or workers)

Verbs -> dependencies between graphical changes in the icons and user actions (contents: events or tasks)

Thus: User actions are coded as computer actions, and objects as computer objects.

An additional argument for having some similarity between expression and content in this case is that the computer system itself is built as a mirror image of the paper system, and the users need to determine whether the states of the two systems correspond. For example, if the system asserts that a certain job is unfinished (a "red job"), then the corresponding paper cards should be placed in a certain tray with a red header, and if a data box is sent to the computer department, then the corresponding plastic box should also be on its way. Since the system is built as a mirror image, it is important that users can easily determine whether the image is true. We believe that it will be helpful to them to design the screen as a stylized picture of the physical workplace and its objects.

## The Spectator Perspective

In addition to the participant perspective, we find examples of spectator perspective. The clearest examples are found in mystery solving and forecasting. The speakers' focus of attention is no longer on the current goals of the work but on actions and relations between actions, either past events, as in mystery solving:

But isn't it something we cancelled, cancelled out, we had them from the 6th, before, that stayed there for two days

or possible future events in forecasting:

and then she said that you could reset that one, but if you reset it, then it says that the datacom is closed. Yup, and if it closes, then we can't send off our box.

The tense of the tterances is past (mystery solvingor futue/ndtional (forecasting); their agents may be people other than the speakers or may be indefinite; descriptive phrases are used instead of pronouns and deixis; the context of the utterances is presented and partially described by the speakers; the utterances can consist of complex sentences with subordinate clauses; and they cohere internally, not with the suspended work process.

An example of spectator perspective is found in the coordinator's speech from the section Describers and Performers. He uses complex sentences in which the noun phrases contain nominalizations with a verb kernel. Example: Merge the data input with completion.

![](../../Design at Work Cooperative Design of Computer Systems (Joan Greenbaum (editor) etc.)/images/381c2ffdb2fc87e16d8711c2d0a91c848854425d0b0b75b9043b517aab3ce0af.jpg)  
Figure 8. Spectators' sentence structure.

These sentences are very difficult or impossible to paraphrase in direct manipulation style. In the latter example, it would mean that the verb of the main sentence ("merge") should be coded by graphical changes of the coding of its noun phrases, but they are themselves verbs and should, too, be coded by other graphical changes. So the verb merge would have to be coded by changes of changes!

To us at least, this concept is difficult to envisage—direct manipulation seems to be like first order predicate calculus in that although it allows one to describe properties and relations between objects, it does not allow properties of properties and relations between relations. To support spectator conversation we believe that some kind of textual interaction is the most appropriate, since verbal language has a rich arsenal of devices for expressing relations of relations: subordinate sentences, nominalization, prepositions, and conjunctions.

On the basis of these data and reflections, we propose two major modifications in a redesign.

## Support for Mystery Solving: Logging the Past

First, we propose that the topic of the system should not only include the present state of the thousands of cards as it does now, but also past and future actions. The former could be achieved by letting the system record a selection of the actions performed and by providing facilities for playing this log. Such a log would be helpful in the mystery solving situation mentioned earlier, where the workers cannot understand why fliers that have been removed from the flier file continue to stay in it. By playing the log backward and forward, the workers would have opportunities for discovering patterns in the fliers' behavior. At present, mystery solving conversations consist mostly of guesswork, and much time is spent on them because the workers want to understand the rules, and not just comply with them. Given a log, the conversation about fliers could run as follows. It may start just as in the tapes:

Lisa: Listen Anki, what is this?

Lisa: Two—what is this, it is a flier, I saw it was a flier.

Anki: But it was empty yesterday.

Lisa: Strange, look, 8 fliers.

Lisa: We had them before, but they disappeared.

Eva: We checked yesterday, then we didn't have any fliers left.

Lisa: I do not understand why they jump in.

But given the new facility, at this point the workers can play the log in order to verify their hypothesis about what happened since yesterday, which they could not do in the real conversation:

Lisa: Let us play the log from yesterday morning.

Eva: OK. Look there, now the fliers begin to come.

Lisa: And now they begin to disappear—look, this was mine, remember?

Eva: Four o'clock—all fliers are fetched as we thought.

Lisa: Now the date shifts—hey, look, ll the old fliers jump in again!

Replaying the log has now told them that they have not made any mistakes, such as looking into the file of old fliers as the instructor in the real conversation suggested. The next step for them would be to set up hypotheses about the rules governing the behavior of the fliers:

Eva: Maybe you can only go back a certain number of days to see them.

Anki: Yes, I believe that too—maybe they just stay on for two to three days.

Eva: Let us go three days back and see what happens.

And playing the g may n act show that the ers jump  and sy on for three days.

Eva: It is them.

Lisa: It is those we removed.

Eva: They seem to stay on for approximately three days.

Anki: And then they disappear.

Lisa: The ones from today should have disappeared on Monday.

We recommend this method of rewriting conversations as a good technique for getting new ideas for design. It simply consists of looking at existing conversations, discovering lines of arguments that could be improved, or discovering ideas that were not explored further because the necessary information was lacking. There are two advantages in this technique:

1. It is based on real events, curbing tendencies to design facilities that have no connection with real needs;

It shows concretely the future uses of the facility.

The actual PGP-system does contain logs. However, one log is only for technical events in the machine, such as Checking pool readability, poolsize = 20505600, and is clearly addressed to technicians. Other logs are used for reporting, but although the wording to some degree is taken from the work language, it also contains technical passages, which turn out to be difficult for the users to understand and to use, as the example in the beginning of this chapter illustrates.

It is important that the facility describes the events in terms of the work process, not in terms of system features, since the data shows that workers always interpret the system's behavior in terms of work. Building the system on two perspectives amounts to creating two main subviews, both referring to the same subject, but using different concepts and means of expression.

## Direct Manipulation Style

The direct manipulation style will be used in routine work such as data entry and some problem solving situations. It shows a world of work objects in which the worker can act according to the sentence patterns listed in Figure 6, two of which concern transport of work object and worker:

1. Work Objects or Worker move Somewhere

2. Worker moves Work Object Somewhere

The following figure, taken from the experimental prototype, shows the desk of one worker:

![](../../Design at Work Cooperative Design of Computer Systems (Joan Greenbaum (editor) etc.)/images/422b55b97b9c7547e1792fa881c1dd459b1a7efa9799aa85c5e83a34394cfe37.jpg)  
Figure 9. Screen dump of prototype.

It shows two collections of work objects, the current batch and the fliers. They are denoted by scrollable windows that can be opened and closed. Each text line of the window denotes a work object that the user can move from one collection to another by selecting it and dragging it from one window to the other.

Let us look at the action type (2) where workers move work objects. Now, although the workers distinguish between different tasks when they talk about work, the ideal of uniform interaction advocated in the literature seems sensible enough when they do work. Therefore, we want to make this kind of interaction uniform, expressing all actions in the same way, namely dragging an item from one list to another, thereby making all actions conform to the pattern Worker moves Work Object from Source to Destination. Thus, instead of spelling the commands by means of letters, we can use the mouse and the icons to indicate the more circumstantial Move Document from Current Batch to Removed Documents, for example, in the form of a menu containing Remove Document.

In the direct manipulation style, each "sentence" will be expressed by means of three parts:

1. Selecting: Grasping document in source list.

2. Dragging.

3. Deselecting: Letting go of document in destination list.

## Recoding Direct Manipulation as Textual Style

But, as mentioned, this sentence structure will probably not support the workers when they reflect on work, so in addition to the direct manipulation style, we want the system to be able to paraphrase these actions in a textual style.

In mystery solving, a window can present descriptions of the actions done, for example, "Film number xxxx is sent to the flier file," or "The job is abandoned," or "Batch xxx is taken away."

An important argument for adding such verbal paraphrases to the graphic one is that although we may easily log the "sentences" of graphic interaction and make them available for replay during mystery solving games, the concepts they express are poorly suited for reflective conversations like mystery solving or forecasting, because they only contain a large number of simple analytical statements such as

1. Worker moves Document from Batch to Fliers.

2. Worker moves Document from Fliers to Batch.

3. Worker moves Document from Batch to Removed Documenits.

In discussions, these phrasings are long and circumstantial and lack complex concepts that are good for discussing and thinking. To remedy this, we may introduce the concept take away = move from Batch to Removed Documents, giving (3) the shorter paraphrase

4Worker took away Document.

A short phrase like We took it away is a better aid for the thought than the circumstantial We moved it from the batch to the Removed Document file.

However, still more complex concepts are needed. Consider, for example, the sentence

## 5. But they just disappeared

which a worker uses to describe the behavior of all fliers in the mystery solving example, condensing hundreds of statements of the form Worker moves Document from Fliers to Batch to one.

What is needed is not merely another kind of expression, but also a semantic structure other than that given by the direct manipulation interface. The basic linguistic problem is one of translating from one language to another, but since we want it done automatically and the system can only handle formal units, we must write explicit rules, relating the graphic expression form to one or more verbal expression forms in such a way that the referents of the two are interpreted as identical but their semantic structure as different. In short, we have to present the data from two different perspectives.

Until now, Artificial Intelligence has monopolized formal manipulation of language with the aim of making computers understand natural language. We think that this project is both scientifically and politically misguided, but on the other hand do not see any reason for not exploiting the insights of formal linguistics for other purposes. The present case is a good example of how the linguist can use all the horsepower of his or her science to achieve a different end, namely to program the machine to make paraphrases of the same data suiting different information needs of the user. Thus, the purpose is not to make the machine but the user wiser.

Solving these kinds of problems involves cases (see the beginning of the chapter) and semantic analysis, and is therefore also interesting as a linguistic problem—which we consider a prerequisite for enticing linguists to work within a paradigm other than AI or computational linguistics.

Here is a simple example of a possible rule that will translate the direct manipulation sentences from the previous section to verbal sentences:

the name of the list component of the selection part (part ) is put into the source case

2. the name of the deselection part (part 3) into the destination case

3.if the middle part is dragging, move is put into the verb slot.

Note how cases serve as a common point of reference for both codes since they can be used to analyze both verbal and graphic signs.

This rule will translate graphic actions into sentences such as move BO1234 from batch to fliers.

The shorter and more synthetic phrasings used by the workers can be handled by writing rules of the type used in formal generative semantics.

For example, source = batch is the unmarked case, which is never verbalized, and the system should mirror this by deleting the source case in this situation. In addition, if the destination is the file Removed Cards, the work language has special words such as take away and destroy that allow the destination case also to be deleted. Thus, Move BO1234 from batch to Removed Cards can be shortened to Destroy BO1234.

## Support for Forecasting: Simulating the Future

In addition to enhancing the system with a past tense, we suggest that adding an unreal future to the system would be useful in the language game of forecasting. Here the workers try to set up hypothetical dependencies between actions and exploit the modality (possible/not possible) and mode (conditional/nonconditional) systems of their language. One obvious possibility for supporting this kind of conversation is to enhance the modality of the system by adding a "conditional" to it, for example, as a small toy database, where errors or improper actions would not have fatal consequences. With such a tool, the workers could settle the correct dependencies among sending a box, entering a new date, closing the transmission line, and processing cards by experimenting, rather than by guessing as they do in the real conversation. The conversation may sound like this, given the new facility:

C: Can we close the data valve before we send our box?

D: I think it closes automatically when we have sent the box, but let us try. No—we cannot send the box when we have closed the valve.

D: But can we enter a new date before we are finished? Let us see. No, if I enter the new date, it says that the data valve closes. And when it has closed, we cannot send the last box.

The system should support the workers by shifting between direct manipulation and text style interaction. Although some kinds of situation favor one style—data entry a direct manipulation style, and mystery solving a textual style—other situations exhibit a shift from participant to spectator perspective. If an error is not too difficult to locate, the problem solving conversation can be carried out in a participant perspective, whereas other problems make the workers step back from work and reflect upon the consequences of the solution.

## Conclusion

It has been important for us to show how linguistics can be used for analysis and design of computer systems in a different way than is normally done within the AI-tradition. We could sum up the approach presented in this paper by changing the DeMarco quotation a little:

As you go about doing Linguistic Analysis, you will find yourself more and more frequently attaching yourself to the workers and following them through the work. We think of this as interviewing the workers.

Thus we not only interview workers in the coffee room, but we are more interested in the way they talk during work. The reason for this is that we believe that work language is not fortuitous, but based on collective and partially unconscious knowledge and experience.

The result is our interpretation of these hidden patterns, and can be used as a basis for prototyping and discussions with the users, making them aware of patterns of work practice and conceptual structures they are not paying attention to during daily work.

## References

Andersen, P. Bøgh & Holmqvist, B. (1986). A toolbox for analyzing work language. In J. D. Johansen & H. Sonne in collaboration with H. Haberland (Eds.), Pragmatics and Linguistics. Odense, Denmark: Odense University Press.

Andersen, P. Bøgh. (1990). A theory of computer semiotics. Semiotic approaches to construction and assessment of computer systems. Cambridge, UK: Cambridge University Press.

Fillmore, C. J. (1968). The case for case. In E. Bach & R. T. Harms (Eds.), Universals in linguistic theory (pp. 1-90). London: Holt, Rinehart & Winston.

Fillmore, C. J. (1977). The case for case reopened. In P. Cole & G. M. Sadock (Eds.), Syntax and semantics: 8. Grammatical relations (pp. 59-81). New York: Academic Press.

Holmqvist, B. & Andersen, P. Bøgh. (1987). Work language and information technology. Journal of Pragmatics, 11, 327-357.

Holmqvist, B. (1989). Work language and perspective. In Scandinavian Journal of Information Systems, No.1. Aalborg, Denmark: University of Aalborg.

DeMarco, T. (1978). Structured analysis and systems specification. New York: Yourdon.

Norman, D. A. & Draper, S. W. (1986). User centered design— New perspectives on human computer interaction. Hillsdale, NJ: Lawrence Erlbaum Associates.

Ullman, S. (1962). Semantics. An introduction to the science of meaning. Oxford, UK: Basil Blackwell.

![](../../Design at Work Cooperative Design of Computer Systems (Joan Greenbaum (editor) etc.)/images/ab948e7c352c2c074d15e9ae143ac34fe70254d7a304963918e485f9169e0bef.jpg)

Taylor & Francis

Taylor & Francis Group http://taylorandfrancis.com
