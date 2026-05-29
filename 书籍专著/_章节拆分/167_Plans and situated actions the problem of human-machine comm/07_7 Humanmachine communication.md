> 来源：Plans and situated actions the problem of human-machine communication (Suchman, Lucille Alice)
> 原始文件：C:\Users\lenovo\Documents\Codex\2026-05-29\书籍专著\Plans and situated actions the problem of human-machine communication (Suchman, Lucille Alice)\Plans and situated actions the problem of human-machine communication (Suchman, Lucille Alice).md
> 识别方式：强章节标记

# 7 Humanmachine communication

Interaction is always a tentative process, a process of continuously testing the conception one has of . . . the other. (Turner 1962, p. 23, original emphasis)

In chapter 4, I outlined the view that the significance of actions, and their intelligibility, resides neither in what is strictly observable about behavior, nor in a prior mental state of the actor, but in a contingently constructed relationship between observable behavior, embedding circumstances and intent. Rather than enumerating an a priori system of normative rules for meaningful behavior, chapter 5 described resources for constructing shared understanding, collaboratively and in situ. Face-to-face interaction was presented as the most fundamental and highly developed system for accomplishing mutual intelligibility, exploiting a range of linguistic, demonstrative and inferential resources.

Given this view of the basis for action's intelligibility, the situation of action can be defined as the full range of resources that the actor has available to convey the significance of his or her own actions, and to interpret the actions of others. Taking that preliminary definition of the situation as a point of departure, my interest in this chapter is to consider "communication'" between a person and a machine in terms of the nature of their respective situations. For purposes of the analysis, and without ascribing intent in any way, I will assume that the machine is behaving on the basis of resources provided by "its" situation, the user in accord with the resources of hers. The aim of the analysis then is to view the organization of human-machine communication, including its troubles, in terms of constraints posed by asymmetries in the respective situation resources of human and machine.

## Engineering an appropriate response

In the case considered here, we can assume that the situation of the user comprises preconceptions about the nature of the machine and the operations required to use it, combined with moment by moment interpretations of evidence found in and through the actual course of its use. The situation of the machine or expert help system, in contrast, is constituted by a plan for the use of the machine, written by the designer and implemented as the program that determines the machine's behavior, and sensors that register changes to the machine's state, including some changes produced by the user's actions. The design plan defines what constitutes intelligible action by the user insofar as the machine is concerned, and determines what stands as an appropriate machine response. The intersection of the situations of user and machine is the locus both for successful exploitation of mutually available resources, and for problems of understanding that arise out of the disparity of their respective situations.

## 7.1 Engineering an appropriate response

The practical problem with which the designer of an interactive machine must contend is how to ensure that the machine responds appropriately to the user's actions. As in human communication, an appropriate response implies an adequate interpretation of the prior action's significance. And as in human communication, the interpretation of any action's significance is only weakly determined by the action as such. Every action assumes not only the intent of the actor, but the interpretive work of the other in determining its significance.1 That work, in turn, is available only through the other's response. The significance of any action and the adequacy of its interpretation is judged indirectly, by responses to actions taken, and by an interpretation's usefulness in understanding subsequent actions. It is just this highly contingent process that we call interaction.

## Human—machine communication

For purposes of analysis, we can begin by considering two alternative perspectives on face to face interaction, with commensurately different implications for the project of designing interactive machines. The first perspective ties successful interaction to each participant's success at anticipating the actions of the other, and recommends an interactive interface based on a preconceived model of the user that supports the prediction of actions, the specification of recognition criteria for the actions predicted, and the prescription of an appropriate response. The second view focuses on the ways in which interactional success comprises responses that are occasioned by, and responsive to, unanticipated actions of the other. This focus recommends an interactive interface that maximizes sensitivity to actions actually taken, by minimizing predetermined sequences of machine behavior. The former recommendation is constrained by limitations on the designer's ability to predict any user's actions, the latter by limitations on the system's access to and ability to make sense out of the actions that a particular user takes.

The design strategy in the expert help system is to try to provide the effect of an occasioned response, through the use of a predictive model. That is to say, the designer predicts that the user will have one of a set of possible goals, of the form "use the machine to accomplish outcome x." Given that statement of intent, the machine displays a set of instructions that prescribe the actions to be taken, at a level of generality designed to ensure their relevance to any user, whatever the details of her particular situation. Ideally, the instructions tell the user what aspects of her particular situation are relevant or the execution of this plan, and or the machine's - eration. By finding or producing the objects and actions described, the user anchors the general instructions to her unique circumstances.

This chapter looks at some of the consequences of taking a statement of intent and an ascribed plan as grounds for the interpretation of situated action. To anticipate, that strategy involves an insensitivity to particular circumstances that is both the system's

## The system's situation: plans and detectable states

central resource, and its fundamental problem. I look first at the system's resources for construing the actions of the user; namely, plans and states. I then consider the problems posed for the designer by the user's principal resource, organized under the general rubric of situated inquiries, and by the user's ability to find the relevance of the system's response to those inquiries. Finally, I look at two classes of communicative breakdown, the false alarm and the garden path. Chapter 8 concludes with implications of the analysis for a general account of mutual intelligibility, and for the particular requirements on the design of artifacts that would interact with their users.

## 7.2 The system's situation: plans and detectable states

The resources of the expert help system include a program that controls its behavior, and sensors that register certain changes to its state effected by actions of the user. Initially, the user's response to a series of questions about her original documents and desired copies is taken as a statement of her intent, that statement in turn determining the selection by the machine of one from a set of possible plans (see display 0, p. 171). The plan is then presented to the user in the form of a step-wise set of procedural instructions. The designer assumes that the plan matches the user's intent, and that in following the procedural instructions, the user effectively is engaged in carrying out the plan.

The design premise is further that as the user takes the actions prescribed by the instructions, those actions will change the state of the machine in predictable ways. By taking those changes to the machine's state as traces of the user's actions, the designer can effectively specify how the user's actions are to be recognized by the system, and how the system is to respond. The instructions are grouped in a series of displays such that the last action prescribed by each display produces an effect that is detectable by the system, thereby initiating the process that produces the next display. The design assumption is that by detecting certain of the user's actions, the system can follow her course in the procedure and provide instructions as needed along the way.2

The strategy of tying certain machine states to the presentation of particular next instructions enables the appearance of machine responses occasioned by the user's actions. So, in this light, we can view the interaction between A and B in sequence I as the adept

Sequence 1. A and B are proceeding from a display that established their goal as making two-sided copies of a bound document. (Two-sided copying requires an unbound document, so they must begin by making a master unbound copy of their document, using the "Bound Document Aid," or BDA.)
<table><tr><td colspan="2">THE USER</td><td colspan="2">THE MACHINE</td></tr><tr><td>Not available to the machine</td><td>Available to the machine</td><td>Available to the user</td><td>Design rationale</td></tr><tr><td rowspan="6">A: &quot;To access the BDA, pull the latch labelled Bound Document Aid&quot;&quot;:: (Both A and B turn to</td><td></td><td>DISPLAY 1</td><td>Selecting the procedure</td></tr><tr><td>DISPLAY 2</td><td></td><td>Instructions</td></tr><tr><td rowspan="6"></td><td></td><td>for copying a bound</td></tr><tr><td></td><td></td></tr><tr><td></td><td>document:</td></tr><tr><td></td><td>Accessing the Bound</td></tr><tr><td></td><td>Document</td></tr><tr><td colspan="2">(Points) Right there.</td><td>Aid.</td></tr></table>

The system's situation: plans and detectable states
<table><tr><td colspan="2">THE USERS</td><td colspan="2">THE MACHINE</td></tr><tr><td>Not available to</td><td>Available</td><td>Available</td><td>Design</td></tr><tr><td>the machine</td><td>to the machine</td><td>to the user</td><td>rationale</td></tr></table>

B:(Hands on latch)

A:And lift up to the leeft." (Looks to B, who struggles with the atch) Lift up and to the left."

B: (Still struggling)

A: Okay:

B: Pu:ll, and lift up to the left. (Looks at picture) Oh, the whole thing

![](../../Plans and situated actions the problem of human-machine communication (Suchman, Lucille Alice)/images/7d9d4ddda72736bb8d9507cc8e6bc132c731875ef3dffa398fe025598d29d9c5.jpg)

:Lift up and to the left.

A:Place your original face down (Passes journal to B) on the glass, centered over the registration guide." (Looks to machine) Got that? (pause) Want me to read it again?

DISPLAY 3

B: Um.: I'm just trying to figure out what a registration guide is, but I guess that's this, um:

Human-machine communication
<table><tr><td colspan="2">THE USERS</td><td colspan="2">THE MACHINE</td></tr><tr><td>Not available to the machine</td><td>Available to the machine</td><td>Available to the user</td><td>Design rationale</td></tr><tr><td colspan="2">A: (Looking over her shoulder) Yea:</td><td></td><td></td></tr><tr><td>B: centered over this line thingy here. A: Okay, let me read it</td><td></td><td></td><td></td></tr><tr><td>again. &quot;Place your original face down on the glass, centered over the registration guide, to position it for the copier lens.&quot; Okay?</td><td></td><td></td><td></td></tr><tr><td>B: &#x27;Kay. A: Okay. &quot;Slide the</td><td></td><td></td><td></td></tr><tr><td>document cover: left over your original until it latches.&quot;</td><td></td><td></td><td></td></tr><tr><td colspan="2">[Portion omitted in which users first mis-locate, then locate, the document cover.] CLOSES COVER</td><td>DISPLAY 4</td><td></td></tr><tr><td colspan="2">B:Okay, now, [</td><td></td><td>Instructions to start printing</td></tr><tr><td colspan="2">A: All right: &quot;Press the Start button</td><td></td><td></td></tr></table>

completion of what the design attempts. Specifically, A decomposes and re-presents the instructions provided by the system, such that they are fit more precisely to B's actions in carrying them out. A is able to do this because of her sensitivity to what B is doing, including B's troubles. ;

The system's situation: plans and detectable states

Below is the procedure from sequence I, as represented in the program that controls the display of instructions to the user:

Step 1: Set Panel   
[DISPLAy 1]   
Step 2: Tell User "You need to use the Bound Document   
Aid..."   
[DISPLAY 2]   
Step 3: Tell User "Place your original face down . . . Slide the   
document cover left . . ."   
[DISPLAY 3]   
Step 4: Make Ready.   
Step 5: Tell User "Press Start." Requirements:   
Panel Set (If not, try Step 1)   
RDH raised (if not, try Step 2)   
Document cover closed (If not, try Step 3)   
Ready State (If not, try Step )   
[DISPLAy 4]   
Step 6: Complete printing Step   
Requirements:   
Printing State (f not, try Step

Rather than proceeding through the steps of the procedure consecutively, the system starts with the last step of the procedure, Step 6 in this case, and checks to see whether it is completed. A step is completed if a check of the machine's state confirms that the conditions represented by that step's requirements have been met. The requirements in this sense represent features of the system's situation (or, more accurately, of the system's own state) that are resources in determining an appropriate next instruction or action. When a requirement is found that is not met, a further set of specifications, tied to that requirement, sends the system back to an earlier step in the procedural sequence. The system then displays the instructions tied to that earlier step to the user, until another change in state begins the same process again. Each time the user

## Human-machine communication

takes an action that changes the machine's state, the system compares the resulting state with the end state, returns to the first unfinished step in the sequence, and presents the user with the instructions for that and any subsequent step.

Through this simple device of working backward through the procedure, the presentation of redundant instructions can be avoided. In sequence 11, having discovered that their original document is larger than standard paper, A and B decide to re-do the job. They return to the job specification display to select the reduction feature, and then direct the machine to proceed.

Sequence 11. Again A and B are making two-sided copies of a bound t glass, the document cover is closed.)
<table><tr><td colspan="2">THE USERS</td><td colspan="2">THE MACHINE</td></tr><tr><td>Not available to the machine</td><td>Available to the machine</td><td>Available to the user</td><td>Design rationale</td></tr><tr><td>B: It&#x27;s supposed to</td><td></td><td></td><td>Selecting the proceedure</td></tr><tr><td>it&#x27;ll tell &quot;Start,&quot; in a minute. A: Oh. It will?</td><td></td><td></td><td></td></tr><tr><td>B: Well it did: in the past.</td><td></td><td></td><td></td></tr><tr><td>(pause) Á little start: box will:</td><td></td><td>DISPLAY 4</td><td>Ready to</td></tr><tr><td>B:There it goes.</td><td></td><td></td><td>print</td></tr><tr><td>A&quot;Press the Start button&quot;</td><td></td><td></td><td></td></tr><tr><td></td><td>SELECTS START</td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td>STARTS</td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td>PRINTING</td><td></td></tr><tr><td>Okay.</td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td></table>

## The system's situation: plans and detectable states

On this occasion the system bypasses the instructions to raise the document handler, place the documen' on the glass, and close the document cover, al of which are irrelevant in that the actions they prescribe have already been taken. The system is able to act appropriately because a detectable machine state (the closed document cover) can be linked by the designer to an a priori assumption about the user's intent with respect to a next action (ready to press start). As a result, the system can be engineered to provide the appropriate next instruction in spite of the fact that it does not actually have access to the history of the user's actions, or even to the presence or absence now of a document on the glass. The result is that while B predicts the system's behavior  specifically, that it will provide them with a "Start button'  on her recollection of an occasion (sequence 1) on which the system actually behaved somewhat differently, her prediction holds. That is, just because on this occasion a relevant feature of the user's situation, accessible to the system, causes the system to behave differently, it appears to behave in the "same," i.e. predictable way. In human interaction, this graceful accommodation to changing circumstance is precisely what is expected, and is therefore largely taken for granted. The success of the system's accommodation in this instance is evident in the accommodation's transparency to the users.

On other occasions, however, the mapping from a machine state to an a priori assumption about the user's intent, on which the success of sequence 11 rests, leads to trouble. I have said that given a statement of the user's goal (derived from answers to a series of questions about her originals and desired copies) the system initiates a plan, and then tracks the user's actions by mapping state changes to a step-wise procedure bound to that plan. In sequence 111, A and B have completed the unbound master copy of their document, and have gone on to attempt to make their two-sided copies. They find that the page order in the copies is incorrect (a fault not available to the system, which has no access to the actual markings on the page), so they try again. As in sequence 11, for them this is a second attempt to accomplish the same job, while for the machine it

## Human-machine communication

is just another instance of the procedure. On this occasion, however, that discrepancy turns out to matter.

Sequence I11. Again A and B are making two-sided copies from a bound document (this time having already completed theirunbound master copy).
<table><tr><td colspan="2">THE USERS</td><td colspan="2">THE MACHINE</td></tr><tr><td>Not available to the machine</td><td>Available to the machine</td><td>Available to the user</td><td>Design rationale</td></tr><tr><td rowspan="7">B:Okay, and then it&#x27;ll tell us, okay, and::</td><td rowspan="7"></td><td rowspan="7">DISPLAY I</td><td>Selecting</td></tr><tr><td>the</td></tr><tr><td>procedure</td></tr><tr><td></td></tr><tr><td></td></tr><tr><td></td></tr><tr><td>Instructions</td></tr><tr><td>Okay, we&#x27;ve done all that. We&#x27;ve made our</td><td></td><td>DISPLAY 2</td><td>for copying a bound document:</td></tr><tr><td>bound copies. (pause)</td><td></td><td></td><td>Accessing</td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td>the Bound</td></tr><tr><td>A: It&#x27;ll go on though,</td><td></td><td></td><td>Document</td></tr><tr><td>I think. Won&#x27;tit?</td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td>Aid</td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td>B: I think it&#x27;s gonna</td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td>continue on, after</td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td>it realizes that we&#x27;ve</td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td>done all that.</td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr></table>

In sequence 11, the system's ignorance of the relation between this attempt to make copies and the last did not matter, just because a check of the current state of the machine caused the appropriate behavior. Or, more accurately, the "current state' of the interaction could be read as a local, technical matter independent of the embedding course of events. Here, however, a check of the machine's current state belies the users' intent. To appreciate what they are doing now requires that the relation between this attempt and the last is recognized, and the machine state does not capture that relation.

## The system's situation: plans and detectable states

So while both users and system are, in some sense, doing the job again, there are two different senses of what, at this particular point, it means to do so. As far as the users are concerned, they are still trying to make two-sided copies of a bound document, so they leave their job description as such. For the machine, however, the appropriate description of their current goal, having made their master copy, is two-sided copying from an unbound document. The result is that what they in effect tell the machine they are doing is not what they intend to do, and what they intend to do is not available from the current state of the world as the machine is able to see it.

A and B find evidence of this trouble in an extended silence (sequence iv), which suggests that the system is not going to proceed (see also 7.4.2 below). What A and B discover here is that,

Sequence iv (continued from III).
<table><tr><td colspan="2">THE USERS</td><td colspan="2">THE MACHINE</td></tr><tr><td>Not available to the machine</td><td>Available to the machine</td><td>Available to the user</td><td>Design rationale</td></tr><tr><td>(8-sec. pause) A: Then again, maybe we need</td><td></td><td></td><td>Instructions for copying a bound document document</td></tr><tr><td>B: What do you think?</td><td>SELECTS &quot;Change&quot;</td><td>DISPLAY O</td><td>User may want to</td></tr><tr><td>A: No.</td><td></td><td></td><td>change job description.</td></tr><tr><td>B Okay, &quot;Proceed.&quot;</td><td>SELECTS</td><td></td><td></td></tr><tr><td></td><td>&quot;Proceed&quot;</td><td></td><td></td></tr></table>

Human—machine communication
<table><tr><td colspan="2">THE USERS</td><td colspan="2">THE MACHINE</td></tr><tr><td>Not available to the machine</td><td>Available to the machine</td><td>Available to the user</td><td>Design rationale</td></tr><tr><td></td><td></td><td>DISPLAY 1</td><td>Making two-sided copies from a bound</td></tr><tr><td>A: Maybe I should just lift it up and put it=</td><td></td><td>DISPLAY 2</td><td>Accessing the Bound Document Aid</td></tr><tr><td>B:How do we skip this then?</td><td></td><td></td><td></td></tr><tr><td>A: =down again. Maybe it&#x27;l think</td><td></td><td></td><td></td></tr><tr><td>we&#x27;re done. B(laughs)Oh, Jean.</td><td></td><td></td><td></td></tr><tr><td>A: There.</td><td>OPENS BDA</td><td></td><td></td></tr><tr><td></td><td>Okay, we&#x27;ve done what</td><td>DISPLAY 3</td><td>Instructions for placing document</td></tr><tr><td>we&#x27;re supposed to do. Now let&#x27;s put this down. Let&#x27;s see if</td><td>CLOSES BDA</td><td></td><td></td></tr><tr><td>that makes a difference. (Looks back to display)</td><td></td><td>DISPLAY 2</td><td>Instructions</td></tr><tr><td>(laughs) It did something.</td><td></td><td></td><td>for copying a bound document</td></tr><tr><td>B:(inaudible) Good grief. A:Oh, it&#x27;s still telling us</td><td></td><td></td><td></td></tr></table>

The system's situation: plans and detectable states
<table><tr><td colspan="2">THE USERS</td><td colspan="2">THE MACHINE</td></tr><tr><td>Not available to the machine</td><td>Available to the machine</td><td>Available to the user</td><td>Design rationale</td></tr><tr><td>And we don&#x27;t need to do the bound document because we&#x27;ve done that. You know, maybe we ought to go back to the beginning, and erase that thing about the bound document.</td><td></td><td></td><td></td></tr><tr><td>BOkay, that&#x27;s a good idea.</td><td>SELECTS</td><td></td><td></td></tr><tr><td></td><td>&quot;Change&#x27;</td><td>DISPLAY O</td><td>User may want to</td></tr><tr><td>just put no.</td><td>A: Then say, &quot;Is it bound?&quot;</td><td></td><td>change job description</td></tr><tr><td>B: Notanymore.</td><td>SELECTS &#x27;No&quot;</td><td></td><td></td></tr><tr><td>A: And then everything else is constant, isn&#x27;t it?</td><td>It&#x27;s on standard paper::</td><td></td><td></td></tr><tr><td>[ B: so we&#x27;ll proceed.</td><td>SELECTS</td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td>&quot;Proceed&quot;</td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td>A: So let&#x27;s just proceed.</td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td>New job;</td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td>two-sided</td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td>from</td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td>unbound</td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td>document</td></tr><tr><td></td></table>

from the system's "point of view," their intent is determined by their initial statement: that is, to make two-sided copies from a bound document. Statements of intent, however, are inevitably relative to larger purposes, and entail smaller ones, and while A

## Human—machine communication

and B's initial statement still accurately describes their global purpose, it belies their local one. Nor in this instance is their current situation (having failed successfully to produce the two-sided copies from their unbound master) reflected in the system's current state (ready to do two-sided copying from a bound original). Their current situation is available only through a history of which the system has no record, or through their reports and assertions about their situation, to which the system has no access. Their attempt to make their situation accessible to the system by exploiting its insensitivity to their actual circumstances and "faking" the required action fails, but the failure is a failure in performance not in principle. Specifically, if they had opened and closed the document cover, rather than only the Bound Document Aid, they would in fact have achieved the desired effect.

## 7.3 The user's resource: the situated inquiry

The premise of a self-explanatory machine is that users will discover its intended use through information found in and on the machine itself, with no need for further instruction. In physical design, for example, the designer anticipates certain questions such that, in the event, an answer is there ready at hand. So the user's question, "Where do I grab?" is answered by a handle fitted to the action of grabbing. In the traditional instruction manual, some further classes of inquiry are anticipated, and answers provided. The step-wise instruction set addresses the question "What do I do next?", and the diagram the question "Where?" In all cases, however, the questions anticipated and answered must be those that any user of the system might ask, and the occasion for both questions and answers is found by the user. It is this lack of "recpi-derite nstuiaual that te p system is designed to redress.

For the novice engaged in a procedural task, the guiding inquiry is some form of the question What next?" The question is an essen tially indexical one, relying for its significance on the embedin

## The user's resource: the situated inquiry

situation. In the case at hand, the system effectively checks its own state to anticipate the user's question, and then presents the next outstanding requirement of the selected procedure in response. This design strategy assumes that the job specification represents the user's intent, that the intent so represented determines the appropriate plan, and that user and system are engaged in carrying out the procedure for that plan.

The design assumption, in other words, is that the situation of the question "What next?" is just the procedure, and that the question is a request for the next step. As long as that assumption holds, the presentation of a next instruction constitutes an appropriate response (see, for example, sequence 1). The design assumption fails, however, in cases such as sequence v, where the question What extis o a atter  ring with he crrent pau of its abandonment or repair. This sequence is discussed further

Sequence v. C and D are making 5 two-sided copies of a bound document. The are usinghe Bound Docent Aidtomake asingleud master copy of their original.)
<table><tr><td colspan="2">THE USERS</td><td colspan="2">THE MACHINE</td></tr><tr><td>Not available to the machine</td><td>Available to the machine</td><td>Available to the user</td><td>Design rationale</td></tr><tr><td>C: &quot;Instructions. Slide the document cover to the right.&quot;</td><td></td><td>DISPLAY 5</td><td>Instructions for copying a bound document: removing</td></tr><tr><td>D: (Noting output) Okay, it gave us one copy here.</td><td></td><td></td><td>the docuinent from the glass.</td></tr><tr><td>C: cover right to remove the origina.&quot;</td><td>Okay, &quot;Slide the document</td><td></td><td></td></tr><tr><td>D: 5 copies and we only gotone.</td><td>We&#x27;re supposed to have</td><td></td><td></td></tr></table>

Human-machine communication
<table><tr><td colspan="2">THE USERS</td><td colspan="2">THE MACHINE</td></tr><tr><td>Not available to the machine</td><td>Available to the machine</td><td>Available to the user</td><td>Design rationale</td></tr><tr><td>C: (Looks to output) Oh. (Looks to display) We only got one?</td><td></td><td></td><td></td></tr><tr><td>D: Yea.</td><td></td><td></td><td></td></tr><tr><td>(long pause) C: What do we do then?</td><td></td><td></td><td></td></tr><tr><td>(Long pause, both study display)</td><td></td><td></td><td></td></tr></table>

below (see 7.5.1), but, for the moment, the observation is simply that the question "What do we do then?" is not, in this instance, a simple request for a "next' in the sense of a next step in the procedure, but rather is a request for a remedy to the current trouble. The situation of the inquiry (indicated anaphorically by the "then," viz. "given that we were supposed to have 5 copies and we only got one') is not the procedure itself, but the conflict between the apparent outcome of the procedure (a single copy), and their stated intent (five copies). That situation,-while clearly described by D, is unavailable in the current state of the machine, which shows no evidence of their trouble. That is, the current state of the machine indicates just that a copy has been made, the design rationale being that they have copied the first page of an unbound master copy of their bound document, and are ready to go on to the second page.

As a cnsequenc  the c that he situation  the iqu not that which the design anticipates, and is not otherwise accessible to the system, the answer that the system offers  do the next step in this procedure  is inappropriate. Even in cases where the designer anticipates the need to remedy some trouble in the procedure rather than to go on to a next action, however, the context of a request for help may be problematic (sequence vI).

The selection of "Change task description," in the context of a

Sequence v1. E and F and making two-sided copies of a bound document. In  thn he cv they have mistakenly closed the entire BDA instead, and as a consequence have returned to the previous instruction to open the BDA (display 2).)
<table><tr><td colspan="2">THE USERS</td><td colspan="2">THE MACHINE</td></tr><tr><td>Not available to the machine</td><td>Available to the machine</td><td>Available to the user</td><td>Design rationale</td></tr><tr><td>E:&quot;Pull the latch labelled&quot; We did that. &quot;Raise&quot; We did that. (Studying display) Okay. Okay.</td><td></td><td>DISPLAY 2</td><td>Instructions for copying a bound document</td></tr><tr><td>latch,&#x27; We did that. E: Now let&#x27;s change::</td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td>F:</td><td>&quot;Change task description?&quot;</td><td></td><td></td></tr><tr><td>E: Yes. F:</td><td>SELECTS</td><td></td><td>User may</td></tr><tr><td>&quot;Describe the document to be copied&quot; Oh, we already did:</td><td>&quot;Change&#x27;</td><td>DISPLAY O</td><td>want to change job specification</td></tr><tr><td>No, we don&#x27;t want to do that. E:Maybe we have to do it to copy that. [i.e. the next page]</td><td></td><td></td><td></td></tr></table>

Human-machine communication
<table><tr><td colspan="2">THE USERS</td><td colspan="2">THE MACHINE</td></tr><tr><td>Not available to the machine</td><td>Available to the machine</td><td>Available to the user</td><td>Design rationale</td></tr><tr><td>F: (Looks around machine) (laugh)I don&#x27;tknow.</td><td></td><td></td><td></td></tr><tr><td>E: Well:</td><td></td><td></td><td></td></tr><tr><td>F: “Help (laugh)</td><td></td><td></td><td></td></tr><tr><td>&quot;Select the question</td><td></td><td>SELECTS &quot;Help&quot;</td><td>User needs clarification</td></tr><tr><td>you would like help with.&quot; E: I guess we still do have to=</td><td></td><td></td><td>of display</td></tr><tr><td>{ F: Westill ha-</td><td></td><td></td><td></td></tr><tr><td>E: =answer this.</td><td></td><td></td><td></td></tr><tr><td>F:</td><td>Oh. okay,</td><td></td><td></td></tr><tr><td>Alright.</td><td></td><td></td><td></td></tr><tr><td>E: Okay.</td><td>F: We sti-but we did</td><td></td><td></td></tr><tr><td></td><td>all that, didn&#x27;t we?</td><td></td><td></td></tr><tr><td>E: Well, maybe not for this page.</td><td></td><td></td><td></td></tr></table>

loop between display 2 and display 3, and their subsequent surprise at the re-appearance of display 0 in response, suggests that the intent of their action was not to return to the job specification, but to find a next instruction. The inherent ambiguity between any next instruction as either a continuation, or as the initiator of a repair, is discussed at length in 7.4. Our interest here is in the situ-

## The user's resource: the situated inquiry

ation of the request for help that follows the return to display 0. Specifically, the selection of the "Help' option constitutes a question about that return to display 0, and the larger problem of the loop in which it is embedded. The design, however, takes the situation of the request to be a local one: that is, as having to do with interpreting the contents of display 0 itself.

Tied to the guiding inquiry "What next?" is a set of embedded questions about the prescribed actions  questions that look for clarification of the forms "How," "Where," or "To what," and WhyThe system' responsiveness  requests or elaboration turns again on whether or not the designer successfully predicts the inquiry. In sequence v1 C's question is actually interrupted by the change to display 2, which anticipates that very question. In this

Sequence vi. C and D are making two-sided copies of a bound document. (They first must make a single, unbound master copy using the BDA.)
<table><tr><td colspan="2">THE USERS</td><td colspan="2">THE MACHINE</td></tr><tr><td>Not available to the machine</td><td>Available to the machine</td><td>Available to the user</td><td>Design rationale</td></tr><tr><td>C: &quot;You need to use the Bound Document Aid to make an unbound copy of</td><td></td><td>DISPLAY 1</td><td>Overview</td></tr><tr><td>your original.&#x27; Where is</td><td></td><td>DISPLAY 2</td><td>Instructions</td></tr><tr><td>Oh, here it is.</td><td></td><td></td><td>for copying a bound document: picture of</td></tr></table>

## Human-machine communication

instance, it happens that the display change is timed to the mechanism that sets the machine's control panel, rather than being conditional on any action of the user's. Ironically, in part because on this occasion the system's behavior is determined not by the user's actions, but by the internal processing of the system, it appears that the system's behavior is occasioned by the user's question.

The fact that the question anticipated turns out to be the user's question in this instance marks the success of the design. In

Sequence vII1. C and D are making two-sided copies from a bound document, using the BDA. (They have placed their document on the document glass.)
<table><tr><td colspan="2">THE USERS</td><td colspan="2">THE MACHINE</td></tr><tr><td>Not available to the machine</td><td>Available to the machine</td><td>Available to the user</td><td>Design rationale</td></tr><tr><td>C: Okay, wait a minute. &quot;Slide the document cover left over your original until it latches.&quot; (Looks to machine)</td><td></td><td></td><td>Copying a bound document: Closing the document cover</td></tr><tr><td>D: (Grasps BDA)</td><td></td><td></td><td></td></tr><tr><td>BDA)</td><td>C: The document cover- (leans over to look in</td><td></td><td></td></tr><tr><td>(Pulls on document feeder belt, which gives a little) No, no, no.</td><td>(indicating entire BDA) This would be the</td><td></td><td></td></tr><tr><td>C: &quot;To provide an eyeshield for the copier (inaudible).&quot;</td><td>document cover, isn&#x27;t it?</td><td></td><td></td></tr></table>

## The user's resource: the situated inquiry

sequence v1, however, the designer's prediction fails. In this case, the designer anticipates a question regarding the motivation for the action, while the user's problem is with the action's object. In sequence ix, the question what is the object is anticipated, while B's question actually concerns how to do the action. The answer to B's

Seqc. unbound document.
<table><tr><td colspan="2">THE USERS</td><td colspan="2">THE MACHINE</td></tr><tr><td>Not available to the machine</td><td>Available to the machine</td><td>Available to the user</td><td>Design rationale</td></tr><tr><td colspan="2">A:Place the copies::&quot; on the top paper tray.&quot;</td><td></td><td>Beginning second pass of two- sided copies</td></tr><tr><td colspan="2">[Portion omitted in which they locate the tray.]</td><td></td><td></td></tr><tr><td colspan="2">A: Okay.</td><td></td><td></td></tr><tr><td colspan="2">B: But,</td><td></td><td></td></tr><tr><td colspan="2">(Turning back to display</td><td></td><td></td></tr><tr><td colspan="2">How do you do that?</td><td></td><td></td></tr><tr><td colspan="2">A: (Looking at diagram) The top paper tray is to the right of the</td><td></td><td></td></tr></table>

inquiry is found not in the instruction, which locates the object, but in the object itself. In sequence x, similarly, a problem in interpreting an instruction is solved through a picture of the object on which the action is to be performed.

## Human-machine communication

Sequence x. A and B are making two-sided copies of a bound document.
<table><tr><td colspan="2">THE USERS</td><td colspan="2">THE MACHINE</td></tr><tr><td>Not available to the machine</td><td>Available to the machine</td><td>Available to the user</td><td>Design rationale</td></tr><tr><td>A: &quot;To access the BDA, pull the latch labelled Bound Document Aid&quot;</td><td></td><td>DISPLAY 2</td><td>Instructions for copying a bound</td></tr><tr><td>(A and B turn to</td><td></td><td></td><td>document: Accessing the bound</td></tr><tr><td>machine) (Points) Right there.</td><td></td><td></td><td>document aid.</td></tr><tr><td>B: (Hands on latch)</td><td></td><td></td><td></td></tr><tr><td>A:&quot;And lift up to the left.&quot;</td><td></td><td></td><td></td></tr><tr><td>(Looks to B, who struggles with the latch) &quot;Lift up and to the left.&quot;</td><td></td><td></td><td></td></tr><tr><td>B: (Still struggling)</td><td></td><td></td><td></td></tr><tr><td>A: Okay::</td><td></td><td></td><td></td></tr><tr><td>B:Pu:ll, and lift up to the left.</td><td></td><td></td><td></td></tr><tr><td>(Looks at picture) Oh, the whole thing- [</td><td></td><td></td><td></td></tr><tr><td>A: Yea.</td><td></td><td></td><td></td></tr><tr><td>B: =lift up and to the</td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td>left.</td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td>Opens BDA</td><td></td><td></td></tr></table>

When the object that B first takes to be implicated in the action description 'lift up and to the let' resists her attepts to perform he action described, and the description suggests no other interpretation of the action, he finds in the picture a different object. That re-interpretation of the object, in its turn, revises the significancef

## Theuser's resource: the situated inquiy

the action description. In this way a conflict between the action on an object described by an instruction, and the action required by the object itself, can be a resource for identifying trouble in the interpretation of an instruction, and its resolution, as in sequence x1.

Sequence x1. Cand Dhavemistaken the entire BDA for the "docment p sequence VI).
<table><tr><td colspan="2">THE USERS</td><td colspan="2">THE MACHINE</td></tr><tr><td>Not available to the machine</td><td>Available to the machine</td><td>Available to the user</td><td>Design rationale</td></tr><tr><td>D: Okay. &quot;Slide the document cover— left over your original, until it latches.&quot; (Turns to machine)</td><td></td><td></td><td>for closing document cover</td></tr><tr><td>Okay. C: Ohh.</td><td></td><td></td><td></td></tr><tr><td>D: (laughs) Ohh, isn&#x27;t that hilarious?</td><td></td><td></td><td></td></tr><tr><td>Oky 1 C: Okay.</td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td>Closes cover</td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td>DISPLAY 4</td><td></td></tr><tr><td>It was something</td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td>else that was supposed</td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td>to go over that.</td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr></table>

In general, the referential relationship between instructions and the actions and objects they describe is a reciprocal, rather than directional one. Burke (1982), for example, describes a pump as-

## Human—machine communication

sembly task in which to some extent all of the necessary information for assembling the pump is discoverable in requirements of the materials themselves, specifically the "fit and stay' bindings of one component of the pump to another. In spite of the constraints provided by the bindings, Burke noted a difference in confidence between those students who had additional linguistic instruction and those who did not, the former using the instructions, on the one hand, and the task actions and materials, on the other, as mutually informative, such that "both the instructions and the task actions are treated by the apprentice as problems to be solved. But each is used as a resource to solve the other as a problem' (p. 178). That is to say, while instructions answer questions about objects and actions, they also pose problems of interpretation that are solved in and through the objects and actions to which the instructions refer.

A nice example of this reciprocity of description and action described is shown in sequence x1. In this case, rather than the interpretation of the instruction "Pul the latch, etc. being prerequisite to the action's execution, the action, after the fact, clarifies what the instruction intends.

Sequence xI1. E and F are making two-sided copies of a bound document.
<table><tr><td colspan="2">THE USERS *</td><td colspan="2">THE MACHINE</td></tr><tr><td>Not available to the machine</td><td>Available to the machine</td><td>Available to the user</td><td>Design rationale</td></tr><tr><td>F&quot;To access the BDA, pull the latch labelled Bound Document Aid.&quot; (Both turn to machine)</td><td></td><td></td><td>Instructions for copying a bound document:</td></tr><tr><td>E:</td><td>(Takes hold of latch)</td><td></td><td>Accessing the bound document</td></tr><tr><td></td><td>F: Pull it down: just push it down.</td><td></td><td>aid. :</td></tr></table>

Conditional relevance of response
<table><tr><td colspan="2">THE USERS</td><td colspan="2">THE MACHINE</td></tr><tr><td>Not available to the machine</td><td>Available to the machine</td><td>Available to the user</td><td>Design rationale</td></tr><tr><td>E: (Does, BDA starts to open)</td><td rowspan="3">Opens BDA</td><td rowspan="3">DISPLAY 3</td><td rowspan="3">Placing the document on the glass</td></tr><tr><td>F:(startled) Oh, alright.</td></tr><tr><td>This is what you do. E: Is this what you do?</td></tr></table>

Given the requests for clarification that are potential responses to any directive, one can easily predict that any one or more of them might occur, but not with any certainty which. The design of the expert help system attempts to deal with the problem exhaustively, and frequently succeeds. Questions of "How," "Where," and "Why' are answered by a diagram and supplementary description, provided with each next instruction. In all of these instances, however, the user brings the descriptions that the system provides to bear on the material circumstances of her situation, and brings those circumstances to bear on her interpretation of the descriptions. In other words, the user exploits the meaning of object and action descriptions to find their referents, and uses the objects and actions picked out as resources for finding the significance of the description. Through access to these resources the user not only asks, but also effectively answers her own situated inquiries.

## 7.4 Conditional relevance of response

We have seen how the responsiveness of the system is limited to those occasions where the users' actions effect some change in the machine's state, which ties the actions to the requirements of the underlying design plan. In principle, the design plan serves as the

## Humanmachine communication

measure of what constitutes an adequate and appropriate action by the user: namely, one that satisfies the current procedural requirement. The requirements that the system imposes, in this procrustean sense, serve as prescriptions for successful use of the machine. The success assumes, however, that the user interprets the instructions and the system's responses in the way that the designer intended.

In the interest of conveying the intent of the design to the user, and in doing so interactively, the designer tacitly relies upon certain conventions of human conversation. Most generally, designer and user share the expectation that the relevance of each utterance is conditional on the last; that given an action by one party that calls for a response, for example, the other's next action will be a response. The expectation does not ensure that any next action in fact will be a response to the last, but it does mean that, wherever possible, the user will look for an interpretation of the next action that makes it so.

The user's expectation, in other words, is that each system response conveys, either implicitly or explicitly, an assessment of the last action she has taken and a recommendation for what to do next. More specifically, given some instruction to which the user responds with an action, the user has the following expectations with respect to the system's response:

(a) The system's response should be a new instruction, which stands as implicit confirmation of the adequacy of the user's previous action.

(b) If the system does not respond the user's previous action is somehow incomplete.

etition implies that the user's previous action should be repeated (i.e. that the procedure is iterative) or that there is some trouble in the previous action that should be repaired.

## Conditional relevance of response

## 7.4.1 A new instruction confirms the previous action

We have a general expectation, in carrying out a step-wise procedure, that completion of one action allows progress to a new instruction, and a next action. The correlate of the expectation that a completed action indicates readiness for a new instruction is the fact that the appearance of a new instruction is taken, at least initially, as confirmation of the previous action. In sequence xII, B's evidence for the adequacy of A's action is simply the fact that it generates a response, which is assumed to be a next instruction. The apparent change to a new instruction confirms the preceding action in spite of the fact that the action description, "Slide the document cover," does not actually seem to fit the action taken.

Sequence xIII. A and B are making two-sided copies of a bound document. (They first must make a single, unbound master copy using the BDA.)
<table><tr><td colspan="2">THE USERS</td><td colspan="2">THE MACHINE</td></tr><tr><td>Not available to the machine</td><td>Available to the machine</td><td>Available to the user</td><td>Design rationale</td></tr><tr><td>B:Okay. &quot;Slide the document cover: left over your original, until it latches.&quot;</td><td></td><td>DISPLAY 3</td><td>Instructions for closing document cover</td></tr><tr><td>A: (Moves hand to BDA)</td><td></td><td></td><td></td></tr><tr><td>B: (Turns to machine) &quot;Slide the document cover, (Looks back to diagram)</td><td></td><td></td><td></td></tr><tr><td>that&#x27;s this [i.e. BDA]. Right? A: (Starts to close)</td><td></td><td></td><td></td></tr><tr><td>We- it said left, though. (Looks to display)</td><td></td><td></td><td></td></tr><tr><td>B: &quot;To close the document cover, grasp the cover,</td><td></td><td></td><td></td></tr></table>

Human-machine communication
<table><tr><td colspan="2">THE USERS</td><td colspan="2">THE MACHINE</td></tr><tr><td>Not available to the machine</td><td>Available to the machine</td><td>Available to the user</td><td>Design rationale</td></tr><tr><td>A:</td><td>CLOSES BOUND DOCUMENT AID</td><td></td><td></td></tr><tr><td>B: slide it firmly to the left.&quot;</td><td></td><td>DISPLAY 2</td><td>Instructions</td></tr><tr><td>(You must) have done that.</td><td></td><td></td><td>for opening Bound Document Aid</td></tr></table>

The action taken in fact is not closing the document cover, which is located inside the Bound Document Aid, but instead closing the Bound Document Aid itself. The assumption that display 2 must be a "next"' to display 3, however, masks the fact that they are entering into a loop between those two displays (see also sequence vI).

## 7.4.2 No response indicates that the previous action is incomplete

In conversation, slences are more than just theabsenctlk; they are generally owned by one party or another, and they invariably acquire significance (see chapter 5). The significance of silence lies in its relationship to the talk that it follows and, retrospectively, the talk that it can be seen to precede. In particular, the convention that certain utterance types (questions and answers being the canonical example) sequentially implicate the appropriate next utterance produces "noticeable absences' when the next is not forthcoming. An extended silence following a question, for example, will be seen as a non-response. In the case of the expert help system, there is no response until the user completes the action prescribed by the final instruction of a given display. This design constraint, combined with the user's expectation from human interaction regarding sequential implicature and silence, means that the unresponsive-

## Conditional relevance of response

ness of the system carries information. Specifically, when an action that is intended to satisfy a final instruction fails to elicit aresponse, the user takes the unresponsiveness as evidence for trouble in her performance of the action. In sequence xiv, for example, what C and D initially see as a pause comes to be seen, in virtue of its length, as a non-response. The non-response, in turn, carries information with respect to their last action. Specifically, the nonresponse indicates that this is still, in effect, their turn: that the last action was not, somehow, the action prescribed by this instruction. The evidence that the non-response provides  that there is some problem in the action taken  initiates a re-inspection of the instruction, a re-identification of the instruction's object, and the action's repair.

Sequence xiv. C and D are making two-sided copies using the "Recirculating Document Handler" or RDH.
<table><tr><td colspan="2">THE USERS</td><td colspan="2">THE MACHINE</td></tr><tr><td>Not available to the machine</td><td>Available to the machine</td><td>Available to the user</td><td>Design rationale</td></tr><tr><td rowspan="8">C: Okay, &#x27;Remove the copies from the output tray.&quot; (Takes documents handler)</td><td></td><td>DISPLAY 10 [see p. 176]</td><td>Copies complete</td></tr><tr><td></td><td></td><td></td></tr><tr><td>from document</td><td></td><td></td></tr><tr><td>Okay. Now:</td><td></td><td></td></tr><tr><td>(15-second pause) (Turns to output)</td><td></td><td></td></tr><tr><td>Oh,</td><td></td><td></td></tr><tr><td>(Looks back to display)</td><td></td><td></td></tr><tr><td>D: The output tray:</td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td>C: This is the output tray.</td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td>D:(Points to picture)</td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td>That&#x27;s the output</td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td>tray, okay.</td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr></table>

## Human—machine communication

7.4.3 Repetition is ambiguous between iteration and repair There are two conditions on which the system may repeat a prior instruction:

(a) The action taken in response to the instruction should be repeated (the common case, for example, in a procedure that is iterative);

(b) The action taken in response to the instruction is in error in just such a way as to return the system to a state prior to the instruction: in effect, to undo a previous action. This produces a loop.

In human interaction, (b) does not occur. On the other hand, in human interaction repetition is used in a way that does not occur between user and machine, namely to indicate that:

(c) The action taken in response to the instruction in some way fails to satisfy the intent of the instruction, and needs to be remedied.

Consistent with the observation that users import expectations from human interaction to construe the system's responses, users fail to recognize the occurrence of (b), and instead read all cases of repetition as either (a) or as (c).

Repetition as iteration. In procedural instructions, there are occasions, illustrated in sequence xv, on which the repeat of an instruction is to be taken at face value, as an explicit directive to do the previous action again.

Purposeful action is characterized by the fact that its projected outcome is a resource for assessing the action's course. Where the procedure is a composite one, this function is complicated, however. For one thing, success at a composite procedure depends on reliable ways of discriminating between the procedure's outcome and its intermediate states. Particularly for the novice, the expectation that an embedded procedure (in this case, making fhe unbound master copy of the document) will produce the finished product leads to confusion like that of B in sequence xv, and to more complex misunderstandings, as shown in sequence xVI.

Seqncev. Aand Breaki two-siop A.
<table><tr><td colspan="2">THE USERS</td><td colspan="2">THE MACHINE</td></tr><tr><td>Not available to the machine</td><td>Available to the machine</td><td>Available to the user</td><td>Design rationale</td></tr><tr><td>B: &quot;If more pages are to be copied, then place the next page face down on the glass.&quot;</td><td></td><td>DISPLAY 6</td><td>Iterative procedure for using the BDA</td></tr><tr><td>A: Just keep it up until we&#x27;re finished with the, with the, uh:</td><td></td><td></td><td></td></tr><tr><td>B: Oh, well how do you- she was— she said on both sides, right? A: Well that&#x27;s after we</td><td></td><td></td><td></td></tr><tr><td>finish getting this (indicating document). We&#x27;re just getting the originals to stick up here [i.e. RDH]. B: Oh, you&#x27;re right,</td><td></td><td></td><td></td></tr></table>

Coming to what they take to be the end of the iterative procedure described in display 6, C and D hypothesize that their part in the procedure is finished, that the next turn is the system's. That hypothesis is challenged by the system's inaction (a silence of eleven seconds), which suggests some incompleteness in their own action, and something further for them to do. Their problem, then, is to

## Human—machine communication

Sequence xv1. C and D are making 5 two-sided copies of a bound document. (They have completed the master copy using the BDA. Unaware of the composite structure of the procedure, and seeking to explain the fact that this procedure has produced only one copy, they have adopted the hypothesis that the remaining four copies are produced automatically, by the machine, and they are waiting for them to appear.)

<table><tr><td colspan="2">THE USERS</td><td colspan="2">THE MACHINE</td></tr><tr><td>Not available to the machine</td><td>Available to the machine</td><td>Avaliable to the user</td><td>Design rationale</td></tr><tr><td rowspan="9">D: &quot;Place the next page face down on the glass. Slide the document cover (inaudible). Lower the RDH until it latches.&quot;</td><td rowspan="9"></td><td>DISPLAY 6</td><td>Iterative</td></tr><tr><td></td><td>procedure</td></tr><tr><td></td><td>for using</td></tr><tr><td></td><td>the BDA:</td></tr><tr><td></td><td>when</td></tr><tr><td></td><td>RDH is</td></tr><tr><td></td><td>lowered,</td></tr><tr><td></td><td></td></tr><tr><td></td><td>user is</td></tr><tr><td>(11-second pause)</td><td></td><td>ready to</td></tr><tr><td>So we start over for five?</td><td></td><td>go on to</td></tr><tr><td>It doesn&#x27;t do it (inaudible)?</td><td></td><td>make</td></tr><tr><td></td><td></td><td>multiple</td></tr><tr><td>C: I guess we just have to do it five times, and then it&#x27;ll:</td><td></td><td>copies</td></tr><tr><td></td><td></td><td></td></tr><tr><td>(pause)</td><td></td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td>Do what it says, I guess.</td><td></td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td></tr></table>

find a "next": that is, some action prescribed by the instructions iigGi ha l inherently ambiguous context of a procedure that is both recursive and composite (copying each page once until the end of the document, in order that the document can be copied five times), one possible solution is to see the persistence of this instruction as a repeat rather than a non-response, and therefore as a directive to do the procedure again.

## Conditional relevance of response

In another case, sequence xv1, the option "Change task description," intended by the designer to enable a repair, but noticed in the context of the search for a next turn, suggests iteration where the designer did not intend it. If E and s objective in seleting "Change task description' is to find a next action, one way that they can make the system's response a relevant one is to interpret the return to display o iteratively, as telling them to specify their job again. The possibility, if not plausibility, of that interpretation arises from the fact that the difference between going "backward' to something already done in a procedure, and going "forward" to repeat the action, is inherently problematical. The difference does not lie in any features of the instruction or action itself, but just in whether the instruction's re-appearance at a given time is read as a misunderstanding, or as intended by the design. (See sequence vI above for the development of the problem.)

S . En  n spl
<table><tr><td colspan="2">THE USERS</td><td colspan="2">THE MACHINE</td></tr><tr><td>Not available to the machine</td><td>Available to the machine</td><td>Available to the user</td><td>Design rationale Instructions</td></tr><tr><td>E: &quot;Pull the latch labelled-&quot; We did that. &quot;Raise&quot; We did that. (Studying display) Okay. Okay.</td><td></td><td>DISPLAY 2</td><td>for copying a bound document: Raising the document handler.</td></tr><tr><td>F: &quot;Lift up on the latch,&quot; We did that.</td><td></td><td></td><td></td></tr><tr><td></td><td>E: Now let&#x27;s change::</td><td></td><td></td></tr><tr><td></td><td>F: &quot;Change task description?&quot;</td><td></td><td></td></tr><tr><td>E: Yes.</td><td></td><td></td><td></td></tr><tr><td>Fi:</td><td>SELECTS &quot;Change&quot;</td><td>DISPLAY O</td><td>User may want to</td></tr><tr><td>&quot;Describe the document to be copied—&quot; Oh, we already did: No, we don&#x27;t want to do that.</td><td></td><td></td><td>change job specification</td></tr><tr><td>E: Maybe we have to do it to copy that [i.e. the next page].</td><td></td><td></td><td></td></tr><tr><td>F: (Looks around machine) (laugh) I don&#x27;t know.</td><td></td><td></td><td></td></tr></table>

Finally, the novice user may expect iteration in what is by design a one-pass procedure. C's action in sequence xv111 of removing the first page of the document and replacing it with a second assumes that this procedure is iterative, viz. copy each page one at a time, until finished. While taken as a next, however, her action restores a state that from the system's "point of view' appears identical to the state before the action was taken - a document in the document handler  thereby cancelling the action's effect. For C, logically, the last page has been removed from the document handler, and putting the next page in is pre-requisite to going on; for the system there is just a document in the document handler, and its removal is required to go on.

Seen as an instruction to undo their last action, the instruction to "remove the original' would stand as evidence of trouble. But by paraphrasing "remove' as "move the first page to make a place for the second," C makes this response relevant by turning it into a next, iterative instruction, and therefore a confirmation of her last action. (For discussion of this sequence as a "garden path," see section 7.5 below.)

Repetition as repair. The inclination to see each next instruction as a new instruction means that a repetition might not initially even be recognized as such. Recall that this was the case in sequence xI11. In fact, this is another instance of the loop described for sequence v1.

## Conditional relevance of response

qe akic document, using the RDH.
<table><tr><td colspan="2">THE USERS</td><td colspan="2">THE MACHINE</td></tr><tr><td>Not available to the machine</td><td>Available to the machine</td><td>Available to the user</td><td>Design rationale</td></tr><tr><td>C: Okay, and face up, Right? First page?</td><td></td><td>DISPLAY 7</td><td>Instructions for copying an unbound document: Place all originals in RDH.</td></tr><tr><td>&quot;Press the Start</td><td>PLACED IN DOCUMENT HANDLER</td><td>DISPLAY 8</td><td>Ready to print</td></tr><tr><td>button.&quot; Where&#x27;s the Start button? (Looks around machine, then to display)</td><td></td><td></td><td></td></tr><tr><td>D: (Points to display) Start? Right there it is.</td><td></td><td></td><td></td></tr><tr><td>C: There. (laughs)</td><td></td><td></td><td></td></tr><tr><td>D: Okay.</td><td>SELECTS START</td><td></td><td></td></tr><tr><td>C:</td><td></td><td>STARTS</td><td>Document is being copied</td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td>Removing</td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td>DELIVERS</td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td>Job</td></tr><tr><td></td><td></td><td>COPIES</td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td>Ta:: Oh, it comes</td><td></td><td></td><td>complete</td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td>right back out.</td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td>DISPLAY 9</td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td>originals</td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td></table>

Human—machine communication
<table><tr><td colspan="2">THE USERS</td><td colspan="2">THE MACHINE</td></tr><tr><td>Not available to the machine</td><td>Available to the machine</td><td>Available to the user</td><td>Design rationale</td></tr><tr><td>So it made four of the first? (Looks at display) Okay.</td><td></td><td>DISPLAY 10</td><td>Removing copies from the output tray.</td></tr><tr><td>(Holding second page over the document handler, looks to display)</td><td></td><td></td><td></td></tr><tr><td>Does it say to put it in yet?</td><td></td><td></td><td></td></tr><tr><td>D: (inaudible) &quot;Remove the copies from the output tray.&quot;</td><td></td><td></td><td></td></tr><tr><td>C: (inaudible) number two. (Puts second page into document handler)</td><td>DOCUMENT</td><td></td><td></td></tr><tr><td>&quot;Remove the original&quot;</td><td>PLACED IN DOCUMENT HANDLER</td><td>DISPLAY 9</td><td>Removing</td></tr></table>

Specifically, in sequence xI1 mislocation of the object referred to as the "document cover' leads B to close the entire Bound Document Aid, an action that returns the system to its initial state and causes it to re-display the first instruction, namely, to open the BDA.5 The

## Conditional relevance of response

design rationale that produces this system response is simple: (i) the user must use the BDA to copy bound documents; (i) in order to use the BDA, it must be opened; (ii) if the BDA is closed, the user should be presented with instructions for opening it. However, rather than taking the return to the previous instruction as evidence for some problem in their last action, A and B see it as a next instruction, and as confirmation.

The inclination to mistake a return to a previous instruction for a next can be appreciated by considering the anomalous character of this particular problem in terms of any parallels in human interaction. While repetition of the first part of an adjacency pair is justified in cases where there is no response, when a response does occur it terminates the sequence and provides for the relevance of a next. Insofar as the user believes her action constitutes a response to the current instruction, then, she has every reason to view the system's next turn as a next instruction. The closest situation that one finds in human interaction to the loop in human-machine communication occurs when a response to a sequentially implicative utterance  the answer to a summons, for example  is not recognized as such:

As noted, upon the completion of the SA [summons— answer] sequence, the original summoner cannot summon again. The operation of this terminating rule, however, depends upon the clear recognition that an A has occurred. This recognition normally is untroubled. However, trouble sometimes occurs by virtue of the fact that some lexical items, e.g., "Hello," may be used both as summonses and as answers. Under some circumstances it may be impossible to tell whether such a term has been used as summons or as answer. Thus, for example, when acoustic difficulties arise in a telephone conversation, both parties may attempt to confirm their mutual availability to one another. Each one may them employ the term "Hello?" as a summons to the

## Human—machine communication

other. For each of them, however, it may be unclear whether what he hears in the earpiece is an answer to his check, or the other's summons for him to answer. One may, under such circumstances, hear a conversation in which a sequence of some length is constituted by nothing but alternatively and simultaneously offered "hellos." Such "verbal dodging" is typically resolved by the use, by one party, of an item on which a second is conditionally relevant, where that second is unambiguously a second part of a two-part sequence. Most typically this is a question, and the question "Can you hear me?" or one of its common lexical variants, regularly occurs. (Schegloff 1972, p. 366)

Recognized as such, a return to a previous instruction that cannot be construed as iterative is evidence for trouble. In sequence xx is another instance of the same misunderstanding that we saw in sequence xIII.

In human interaction, when the response to an action is either incoherent or inappropriate, the producer of the original action has recourse to two possible interpretations. She can treat the troublesome response as the product of an error on the listener's part (not hearing or mishearing, not understanding or misunderstanding), or as intended. If the troublesome response is seen as the product of some failure of hearing or understanding, the repair may be just to repeat the original action (see Coulter 1979, p. 30). Unless the trouble is one of hearing, however, we rarely repeat a directive verbatim if there appears to be some problem of understanding the first time around. Instead, we try some reformulation, or elaboration. If one formulation fails to convey our intended meaning, we try another. Frequently, it is not simply that we try an alternative formulation of what we intended before, but that what we intend is conditional on the others' response. In that sense, our own intentions are clarified for us by the response of the other.

In every case, to the extent that we are heard to be repeating ourselves, the repeat is heard as an attempt to correct some problem in

## Conditional relevance of response

Seqc x. Enkocp. chBDA
<table><tr><td colspan="2">THE USERS</td><td colspan="2">THE MACHINE</td></tr><tr><td>Not available to the machine</td><td>Available to the machine</td><td>Available to the user</td><td>Design rationale</td></tr><tr><td>F: &quot;Slide the document cover over your original until it latches.&quot;</td><td></td><td>DISPLAY 3</td><td></td></tr><tr><td>E: (Hand on BDA) F: Just push it down. E:</td><td>CLOSES BDA</td><td></td><td></td></tr><tr><td>Okay, here we go. (turns to display)</td><td></td><td>DISPLAY 2</td><td></td></tr><tr><td>Pull the latch la Oh, we already did that.</td><td></td><td></td><td></td></tr><tr><td>(pause. They study display)</td><td></td><td></td><td></td></tr><tr><td>E: Okay.</td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td>F: Okay.</td><td></td><td></td><td></td></tr><tr><td>(7-second pause)</td><td></td><td></td><td></td></tr><tr><td>Now what do we do?</td><td></td><td></td><td></td></tr></table>

understanding the first time around (see Jordan and Fuller 1974). Seen in this light, as a repair-initiator, repetition initiates a review of the repeated instruction. In sequence xx, a review of the instruction confirms that the actions it prescribes have been done. The two alternative responses to the repeat, in that case, are either to assert that the action is complete, or to do it again. In face-to-face interaction these alternatives appear to be ordered; that is, we first assert that we have heard a prior utterance and responded to it and then, if the assertion does not suffice, we provide a demonstration. Realizing that in communication with the machine assertions never

## Human—machine communication

suffice, that the system has access only to demonstrations or actions, is part of acquiring proficiency in its use.

Sequence xx (continued from XIX).

<table><tr><td colspan="2">THE USERS</td><td colspan="2">THE MACHINE</td></tr><tr><td>Not available to the machine</td><td>Available to the machine</td><td>Available to the user</td><td>Design rationale</td></tr><tr><td>E: &quot;Pull the latch labelled-&quot; We did that. &quot;Raise&quot; We did that. (Studying display)</td><td></td><td></td><td></td></tr><tr><td>F: &quot;Lift up on the latch,&quot; We did that.</td><td></td><td></td><td></td></tr></table>

Actually re-doing an action frequently uncovers problems of understanding, not just because the same terrain is considered again, but because, considered again, the terrain is seen differently, as in sequence xx1. On the other hand, when a review fails to reveal any

<table><tr><td colspan="2">THE USERS</td><td colspan="2">THE MACHINE</td></tr><tr><td colspan="2">Not available to Available the machine to the machine</td><td>Available to the user</td><td>Design rationale</td></tr><tr><td colspan="2">B:&quot;Pull the latch labelled bound,&quot; &quot;Raise the RDH.&quot; &quot;To access the BDA, pull the latch labelled Bound Document Aid,&quot; Okay, (Gesture to latch, then back to display) we did.</td><td>DISPLAY 2</td></tr></table>

Conditional relevance of response
<table><tr><td>THE USERS</td><td></td><td colspan="2">THE MACHINE</td></tr><tr><td>Not available to the machine</td><td>Available to the machine</td><td>Available to the user</td><td>Design rationale</td></tr></table>

And lift up to the left," do it again.

## A:

There. (To display) I'm up to the left.

OPENS TO BDA

B:Okay. Place your original face down on the glass, centered over the registration=   
A:"guide," Okay. [

DISPLAY 3

B: =guide."

A: Did that.

B:"Slide the document co"

A: cover left over=

B:Wait a minute.

A: =your originals," Well:

B:Here's the document glass, (Indicating BDA) is that what they mean?

A: (Looking at BDA) Document cover.

Human—machine communication
<table><tr><td colspan="2">THE USERS</td><td colspan="2"></td><td colspan="2">THE MACHINE</td></tr><tr><td>Not available to the machine</td><td></td><td>Available to the machine</td><td>Available to the user</td><td></td><td>Design rationale</td></tr><tr><td></td><td>B: &quot;To close the document cover, grasp the cover and slide it firmly to the left.&quot;</td><td></td><td></td><td></td><td></td></tr><tr><td>A: (Finding it)</td><td>Oh, here&#x27;s the document cover!</td><td>CLOSES</td><td></td><td></td><td></td></tr><tr><td></td><td>B: Oh, Jean, good girl!</td><td></td><td>DOCUMENT COVER</td><td></td><td></td></tr><tr><td></td><td>A: There&#x27;s the document—</td><td></td><td></td><td></td><td></td></tr><tr><td></td><td>(Both turn back</td><td></td><td></td><td>DISPLAY 4</td><td></td></tr><tr><td></td><td>toto display) Okay, now:</td><td></td><td></td><td></td><td></td></tr><tr><td>B: All right:</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td>Press: the Start button. Jean, you&#x27;re doin&#x27; great.</td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td>SELECTS &quot;Start</td><td></td><td></td><td></td></tr><tr><td></td><td>(Both look to BDA)</td><td></td><td></td><td>MACHINE</td><td></td></tr><tr><td>A: Oh, I see,</td><td></td><td></td><td></td><td>STARTS</td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>B: Alright.</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>A: We don&#x27;t have to close this</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>big thing.</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>B: No, we were-</td><td>we were lookin&#x27; at the</td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>wrong thing.</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td>We were closing the bound</td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>document aid, instead of the:</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>A: instead of the document</td><td></td><td></td></table>

## Conditional relevance of response

new actions, a reasonable inference is that the next action must be the other's. In sequence xx11, C's review indicates that the actions prescribed by the instructions have all been completed; the sense of her ready'here is as in ready to goThere appears to be not further for them to do. Since the logical next is for the machine to

Sqc 1. or se te  ispla display 3.
<table><tr><td colspan="2">THE USERS</td><td colspan="2">THE MACHINE</td></tr><tr><td>Not available to the machine</td><td>Available to the machine</td><td>Available to the user</td><td>Design rationale</td></tr><tr><td>C: (inaudible, rereads instructions) Okay, are we ready? &quot;Pull the latch labelled bound— to release.&#x27; and then you release:: the, uh, RDH (inaudible.)</td><td></td><td>DISPLAY 2</td><td></td></tr><tr><td>Okay, are we ready?</td><td></td><td></td><td></td></tr><tr><td>(pause)</td><td></td><td></td><td></td></tr><tr><td>Oh, it&#x27;s supposed to do</td><td></td><td></td><td></td></tr><tr><td>it by itself.</td><td></td><td></td><td></td></tr><tr><td>(pause)</td><td></td><td></td><td></td></tr></table>

copy the document, C concludes that it must do so without further action on their part. Concluding that it is the system's turn offers an alternative to the original interpretation of the repeat as an indication that their action is somehow incomplete. If the system is in fact responding to their last action, that both confirms the action's adequacy, and accounts for the system's failure to provide a next instruction.

The length of time that passes with no apparent activity, however, casts doubt on that conclusion, as the system's silence takes hhe

## Human-machine communication

there must be some further action for them to take. In sequence xx1, they again attempt to read the repetition as a directive to repair some problem in the action as it was done the first time through. C's "why' here is a locally situated one; that is, she is not

Sequence xxII1 (continued from XXII).
<table><tr><td colspan="2">THE USERS</td><td colspan="2">THE MACHINE</td></tr><tr><td>Not available to the machine</td><td>Available to the machine</td><td>Available to the user</td><td>Design rationale</td></tr><tr><td>C: &quot;Pull the latch labelled bound copy aid to release the— RDH&quot;</td><td></td><td>DISPLAY 2</td><td></td></tr><tr><td>D: (Points) This is the RDH. This [i.e. the latch] is the release.</td><td>But why does it</td><td></td><td></td></tr><tr><td>C: want it to release it? (To display) &quot;Release (inaudible) to enable placement of the bound document on the glass,&quot; so we don&#x27;t have that on the glass like it&#x27;s supposed to be.</td><td></td><td></td><td></td></tr></table>

koalhu ticular about its intent now, given their history and present circumstances. While the answer provided is intended to justify the instruction on any occasion, she attributes to it a significance particular to this occasion. Because their inquiry is situated in their particular circumstances, the answer is taken as an answer to that situateinquiry. Specifically, reads theo enableclause as ele vant to the directive that they release the RDH again, to allow a repair of some fault in the document's placement. This attributes to

## Communicative breakdowns

the system substantially greater sensitivity than it has: namely, the ability to tell how the document is sitting on the glass, and to notice that it is faulted in some way. Under this interpretation of the design, the directive to re-place the document would be conveyed by re-presenting this instruction to the user until the document is placed correctly. This interpretation not only accounts for the loop in which they've found themselves, but also suggests the way out of it.

## 7.5 Communicative breakdowns

Users of the expert help system encounter two forms of communicative breakdown: the false alarm and the garden path. In the first case, a misconception on the user's part leads her to find evidence of an error in her actions where none exists; in the second, a misconception on the user's part produces an error in her action with respect to the prescribed procedure, the presence of which is masked. In neither case is the breakdown available as such to the system.

## 7.5.1 The false alarm

I noted earlier that purposeful action is characterized by the fact that projected outcomes of action are a resource for producing the action's course. In particular, the effects of actions taken are compared against expected outcomes, in order to judge the action's adequacy. Expectations with respect to the effect of actions taken often are not articulated, but are discovered only in the breach. In sequence xxiv the machine offers the users two competing pieces of evidence regarding the adequacy of their last action. The display offers a next instruction, which makes sense as a confirmation of their previous action. The output, however, indicates that the action has failed, in which case the next instruction is irrelevant. From the system's "point of view," nonetheless, there is no problem. And because the system detects no problem here, it offers no

## Human-machine communication

Sequence xxiv. Cand D are making two-sided copies of a bound document. (They have copied the first page.)
<table><tr><td colspan="2">THE USERS</td><td colspan="2">THE MACHINE</td></tr><tr><td>Not available to the machine</td><td>Available to the machine</td><td>Available to the user</td><td>Design rationale Copying</td></tr><tr><td>C: &quot;Instructions. Slide the document cover to the right.&quot;</td><td></td><td>DISPLAY 5</td><td>a bound document: Opening the</td></tr><tr><td>D: (Noting output) Okay, it gave us one copy here.</td><td></td><td></td><td>document cover</td></tr><tr><td>C: cover right to remove the origina.&quot;</td><td>Okay, &quot;Slide the document</td><td></td><td></td></tr><tr><td>D: got one.</td><td>: We&#x27;re supposed to have 5 copies and we only</td><td></td><td></td></tr><tr><td>C: (Looks to output) Oh. (Looks to display)</td><td>We only got one?</td><td></td><td></td></tr><tr><td>D: Yea. (long pause)</td><td></td><td></td><td></td></tr><tr><td>C: What do we do then? (long pause,</td><td></td><td></td><td></td></tr><tr><td>Both study display)</td><td></td><td></td><td></td></tr></table>

prescription for a remedy. The result is an interactional impasse, where the question "What do we do then?" finds no answer. Or rather, the answer that the system provides makes sense only if what the users intend to do is to continue making a single copy from a bound document.6

## Communicative breakdowns

While from the point of view of the design that is precisely what they want to do, that intent is not a feature of their situation. Their situation, meanwhile  that they intended to produce five copies of the document, and have produced only one  is unavailable to the system. The consequence is that the users ascribe a (spurious) misunderstanding of their intent to the machine, while the machine fails to detect the (genuine) misunderstanding on their part with respect to the structure of the procedure. The result is their effort to repair a line of action that is in no way faulty.

## 7.5.2 Garden path

To the extent that different assumptions of users and designers produce evidence of misunderstanding, there is at least some hope that the trouble might be located and resolved. In 7.4 we looked at two events taken by users as evidence of trouble: namely, the nonresponse and the repeat. As in sequence xxiv, false expectations with respect to an action's effect may lead the user to find evidence for trouble in her performance where, in design terms, none exists. Because in such cases the problem lies in the user's expectations rather than her actions, and because the evidence for her expectations that the user provides is unavailable to the machine, the problem itself is unavailable to the machine.

While the user is uncertain of her action in such cases, the action she takes is in fact the action that the design prescribes. Deeper problems arise when the user takes an action other than that prescribed by the design, but one that satisfies the procedural requirement. As a result of the ambiguity of the action's effect, the incorrect action is actually 'mistaken' by the system for some other, correct action, from which it is indistinguishable by the system's sensors. As in xxiv, the problem in such cases is inaccessible to the system. But whereas in xxiv the misconception leads the user to find evidence of trouble where, by design, none exists, in these other cases trouble is masked by the fact that the user sees the action as non-problematic, and by the fact that because the action appears non-problematic to the system as well, the system's response appears to the user to confirm the action.

Take the example in sequence xv111 (above, p. 153). From the system's "point of view," this sequence produces no evidence of trouble. Display 7 instructs the users to place their documents in the Recirculating Document Handler and the system's sensors "see' them do so; display 8 instructs them to press Start; they do, and the machine produces four copies of their document.

To a human observer with any knowledge of this machine, however, C's question "So it made four of the first?" indicates a misunderstanding. Specifically, her question conveys the information that this in fact is not a single-page document, but the first page of several. And in contrast to other machines that require the placement of pages on the glass one at a time, copying an unbound document of multiple pages with this machine requires loading the pages all at once. The problem here is not simply a failure of anticipation on the designer's part. On the contrary, in anticipation of this very situation, the instruction for loading documents explicitly states that all of the pages should be placed in the document handler. There is no evidence, however, that the instruction is consulted by these users.

One basic premise of instructions is that they explicate a problem of action: if there is no problem, there is logically no need for instruction. We can infer from the users' failure to consult the instructions at this point that they have a preconception about what to do, based on past experience. Such preconceptions probably account in large part for the common complaint from designers that people "ignore' instructions; they ignore them because they believe that they already know how to proceed. But given the fact of the users' misconception, the further problem arises when the faul-I

## Communicative breakdowns

because what is available to the system is only the action's effect, and that effect satisfies the requirements for the next instruction. As an assertion in the form of a question, C's statement not only formulates her view of the system's last operation, but requests confirmation of that formulation. Interactionally, her statement provides an occasion for the discovery of the misunderstanding. She even looks to the display for a response. The information provided there is efficient enough, however - it simply says, "The copies have been made" - to support her assertion, rather than challenge it. As a consequence, the misunderstanding displayed in C's question is unavailable to the system, while the efficiency of the system's response masks the trouble for the user.

C's action of placing the document in the document handler appears, in other words, to be a perfectly adequate response to display 7. The system treats the action as satisfying the directive to place all of the documents in the document handler (where "all" in this case comprises one), and therefore provides a next instruction, while C and D take the appearance of the next instruction as confirmation that their last action, placing the first page of their document in the document feeder, satisfied the design intent. The start-up of the machine, with no complaint about their prior action, reflects the fact that the directive to "Start' has two different, but compatible interpretations. For the users, the significance of the directive is "make 4 copies of page 1," while for the system it is just "make 4 copies of the document in the document handler." There is nothing in either display 9 or display 1o to indicate the discrepancy. Each is efficient enough to be read under either interpretation.

So at the point where the machine starts to print, C is making four copies of page 1 of her document, while the machine is just making four copies of the document in the document handler. This seems, on the face of it, a minor discrepancy. If the machine copies the document, why should it matter that it fails to appreciate more finely the document's status as one in a set of three?

The problem lies in the consequences of this continuing misunderstanding for the next exchange. The strength of C's concep-

## Human—machine communication

tion of what is going on (repeating the procedure for each page) provides her with a logical next action (loading her second page into the document handler) in advance of any instruction. The instruction is looked to for confirmation of her action, rather than for direction. Her certainty is evident in the terms of the question: "Does it say to put it in yet?" The deictic pronoun "it" with respect to the system as "next speaker," and to the second page as the object of the instruction, the "in" with respect to the location of the action, and the "yet"' with respect to the time of the action, all imply a shared situation that would make the interpretation of those indexical terms non-problematic. For C, that the instruction will appear and what it will say is not in question - only when. While C is going on to the next run of the procedure, however, the system is still engaged in the completion of the last. What remains is the removal of originals and copies from their respective trays.

The "misunderstanding" between users and system at this point turns on just what the document in the document handler is, and how it got there. For C, a first page has been replaced by a second, a necessary step for the next pass of what she takes to be an iterative procedure. For the system, there just is a document in the documeni handler, and its removal is required for the procedure's completion. The result is an impasse wherein both user and system are "waiting for each other," on the assumption that their own turn is complete, that their next action waits on an action by the other.

The instruction to "Place all of your originals in the RDH" must be designed for any user who might come along, on any occasion. The designer assumes that on some actual occasion the instruction, in particular the relative quantifier "all," will be anchored by the particular user to a particular document with a definite number of pages. Under the assumption that theuser will do that anchoring, the system just takes the evidence that something has been put into the RDH as an appropriate response, and takes whatever is put there as satisfying the description. On the one hand, this means that the system can provide the relevant instruction in spite of the fact that it does not have access to the particular identities of this

## Summary

user, or this document. On the other hand, the system's insensitivity to particularsof this users ituation is the limiting factor ts ability to assess the significance of her actions.

## 7.6 Summary

This analysis has tied the particular problem of designing a machine that responds appropriately to the actions of a user, to the general problem of deciding the significance of purposeful action. The ascriptions of intent that make purposeful action intelligible, and define a relevant response, are the result of inferences based on linguistic, demonstrative, and circumstantial evidence. I have argued that one way to characterize machines is by the severe constraints on their access to the evidential resources on which human communication of intent routinely relies. In the particular case considered here, the designer of the expert help system attempts to circumvent those constraints through prediction of the user's actions, and detection of the effects of actions taken. When the actual course of action that the user constructs proceeds in the way that the design anticipates, effects of the user's actions can be mapped to the projected plan, and the system can be engineered to provide an appropriate response.

The new user of a system, however, is engaged in ongoing, situated inquiries regarding an appropriate next action. While the instructions of the expert help system are designed in anticipation of the user's inquiries, problems arise from the user's ability to move easily between a simple request for a next action, "meta' inquiries about the appropriateness of the procedure itself, and embedded requests for clarification of the actions described within a procedure. In reading the machine's response to her situated inquiries and taking the actions prescribed, the user imports certain expectations from human communication: specifically, that a new instruction in response to an action effectively confirms the adequacy of that action, while a non-response is evidence that the action is incomplete. In the case of repeated instructions, an ambi-

## Human-machine communication

guity arises between interpreting the repetition as a straightforward directive to repeat the action, or as a directive for its repair. A further problem arises when the action that the user takes in response to an instruction is in error in just such a way as to return the system to a state prior to that instruction. Because this trouble does not arise in human interaction, new users initially fail to recognize the occurrence of such a loop.

Due to the constraints on the machine's access to the situation of the user's inquiry, breaches in understanding that for face-to-face interaction would be trivial in terms of detection and repair become "fatal" for human-machine communication (see Jordan and Fuller 1974). In particular, misconceptions with regard to the structure of the procedure lead users to take intermediate states of the procedure as faulted outcomes. Because the intermediate state is nonproblematic from the system's point of view, the system offers no remedy. The result is an interactional impasse, with the user finding evidence of trouble in her actions where none in fact exists. In the case of the garden path, in contrast, the user takes an action that is in some way faulted, which nonetheless satisfies the requirements of the design under a different but compatible interpretation. As a result, the faulty action goes by unnoticed at the point where it occurs. At the point where the trouble is discovered by the user, its source is difficult or impossible to reconstruct.

![](../../Plans and situated actions the problem of human-machine communication (Suchman, Lucille Alice)/images/be042a33b97bd18ef71555e10592e3d544b89593f8eb9ec16f1a6f4c96688e8d.jpg)

THE COPIER

## OVERVIEW:

You need to use the Bound Document Aid (BDA) to make an unbound copy of your original. That copy can then be put into the Recirculating Document Handler (RDH) to make your collated two-sided copies.

## INSTRUCTION:

Please wait.

Change Task Description

## OVERVIEW:

You need to use the   
Bound Document Aid (BDA) to make an unbound copy of your original.   
That copy can then be   
put into the Recirculating   
Document Handler (RDH)   
to make your collated   
two-sided copies.

## INSTRUCTION:

Pull the latch labelled Bound Document Aid. (to release the RDH).

Raise the RDH (to enable placement of the bound document on the glass).

Change Task Description

![](../../Plans and situated actions the problem of human-machine communication (Suchman, Lucille Alice)/images/dad1118a78b78825595061c9472f36b11ce238c6fb5a5209b16416c7bf759002.jpg)

## How to access the BDA:

## To access the BDA, pull the latch labelled Bound Document Aid,

![](../../Plans and situated actions the problem of human-machine communication (Suchman, Lucille Alice)/images/7d02052fe766f4bfd8b33af9a513837330373e53a9ca78e87acd60d7c6fb6b7c.jpg)

and lift up and to the left.

![](../../Plans and situated actions the problem of human-machine communication (Suchman, Lucille Alice)/images/574e68498bc45e08cee7e502272772b1921085c010684dafcf8cfcdb692e9d06.jpg)

![](../../Plans and situated actions the problem of human-machine communication (Suchman, Lucille Alice)/images/75cadda5c2667d41a9bc67fcd913f6343d1537fd99917b98bc58fc2aad45c454.jpg)

## INSTRUCTION:

Place your original   
face down on the glass,   
centered over the   
registration guide   
(to position it for the copier lens).

Slide the document cover left over your original until it latches (to provide an eye shield from the copier lights).

## ASSUMPTION:

The first page to be copied is on the glass.

## INSTRUCTION:

Press the Start button (to produce a copy in the output tray).

## How to close the document cover:

To close the document cover, grasp the cover and slide it firmly to the left.

![](../../Plans and situated actions the problem of human-machine communication (Suchman, Lucille Alice)/images/8af89ad83c93da3b91ba7dfb7db44e41c0201015cbd2f2e1cfe59d995a72ac52.jpg)  
Display 3

THE COPIER  
![](../../Plans and situated actions the problem of human-machine communication (Suchman, Lucille Alice)/images/c750f4f4a679f2f25ac86e6599b5397bb3018871c91110d48402848c3d434ad2.jpg)  
Display 4

![](../../Plans and situated actions the problem of human-machine communication (Suchman, Lucille Alice)/images/88461b1b65d175c829873175d6caffc8d7e274efebc0e214dcc771c3963962c8.jpg)

## ASSUMPTION:

The copy of your original on the glass has been made.

## INSTRUCTION:

Slide the document cover right (to remove the original).

Task Description

## INSTRUCTION:

Remove the original from the glass.   
If more pages are to be   
copied, then: Place the next page face down on the glass. Slide the document cover left until it latches.   
Otherwise, lower the RDH   
until it latches.

Change Task Description

## How to open the document cover:

![](../../Plans and situated actions the problem of human-machine communication (Suchman, Lucille Alice)/images/af3ef08c94c3d948bdbd532c7e04c9da83009122b24aebef35e65f90d57607b8.jpg)

Help

Display 5  
THE COPIER  
![](../../Plans and situated actions the problem of human-machine communication (Suchman, Lucille Alice)/images/281179f5e59a746bd6d59706d4d88349c905d2b519f6e8e6ec6671af8fd3e1f2.jpg)  
Display6

![](../../Plans and situated actions the problem of human-machine communication (Suchman, Lucille Alice)/images/394dec7560bb36fde1ae9cb9d4427506f67e8c6263f5d962a9aee9176b362f6c.jpg)

## OVERVIEW:

You can use the Recirculating Document Handler (RDH) to make your copies.

## INSTRUCTION:

Place all of your originals in the RDH, first page on top (so that the RDH can automatically feed each sheet into the copier).

Change

Task Description

## OVERVIEW:

You can use the Recirculating Document Handler (RDH) to make your copies.

## ASSUMPTION:

The document to be copied is in the RDH.

## INSTRUCTION:

Press the Start button (to produce 4 copies in the output tray).

Task Description

THE COPIER  
![](../../Plans and situated actions the problem of human-machine communication (Suchman, Lucille Alice)/images/f624c1d409915b9dcdc3aae5be598e4c84c3f05690fd44ef0f9975fa5350ea86.jpg)  
Display7  
THE COPIER  
Display 8

The copies have been made.

INSTRUCTION:

Task Description

## ASSUMPTION:

Remove the copies from the output tray.

Task Description

![](../../Plans and situated actions the problem of human-machine communication (Suchman, Lucille Alice)/images/a92411e41681329991b70ac46211cc0669f8ea382b19c41cee0f27d2b40f4471.jpg)

Display 9  
![](../../Plans and situated actions the problem of human-machine communication (Suchman, Lucille Alice)/images/d399a90fed05640fc9b62789c74c284d1a46228a4ea994b27b6d74743bb53a54.jpg)

## ASSUMPTION:

A copy of your document is being used as the original to make the final copies.

The back sides of the copies have been made.

## INSTRUCTION:

Place the copies in the top paper tray.

Change Task Description

The COPIER

The top paper tray is to the right of the output paper tray.

![](../../Plans and situated actions the problem of human-machine communication (Suchman, Lucille Alice)/images/172a508849e0774b399c2cd0859e868bbbcd1cb29ca1ea34790af52538492d54.jpg)

Help

Display 11
