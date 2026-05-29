> 来源：Plans and situated actions the problem of human-machine communication (Suchman, Lucille Alice)
> 原始文件：C:\Users\lenovo\Documents\Codex\2026-05-29\书籍专著\Plans and situated actions the problem of human-machine communication (Suchman, Lucille Alice)\Plans and situated actions the problem of human-machine communication (Suchman, Lucille Alice).md
> 识别方式：强章节标记

# 8 Conclusion

The theme of this book has been in one sense an obvious proposition: namely, that insofar as actions are always situated in particular social and physical circumstances, the situation is crucial to action's interpretation. The very obviousness of this fact about action contributes to the ways in which it has been overlooked. The intellectual tradition of the cognitive sciences, in particular applied logic, has taken abstract structural accounts as the ideal representational form. An adequate account of any phenomenon, according to this tradition, is a formal theory that represents just those aspects of the phenomenon that are true regardless of particular circumstances. This relation of abstract structures to particular instances is exemplified in the relation of plans to situated actions. Plans are taken to be either formal structures that control situated actions, or abstractions over instances of situated action, the instances serving to fill in the abstract structure on particular occasions. The research strategy in cognitive science has been to represent mental constructs, such as goals or plans, then stipulate the procedures by which those constructs are realized as action, or recognized as the actor's intent. The specification of procedures for action, in turn, has presupposed enumeration of the conditions under which a given action is appropriate. These stipulated conditions, ready made and coupled to their associated actions, take the place of a lively, moment-by-moment assessment of the significance of particular circumstances.

In contrast to this cognitivist view, I have proposed an alternative approach drawn from recent developments in the social sciences, principally anthropology and sociology. The aim of research, according to this approach, is not to produce formal models of

## Conclusion

knowlegeandaction,but oexplorethe elationnowlend action to the particular circumstances in which knowing and acting invariably occur. This alternative approach requires corresponding changes in the way in which research on purposeful action proceeds. The first is a fundamental change in perspective, such that the contingence of action on a complex world of objects, artifacts, and other actors, located in space and time, is no longer treated as an extraneous problem with which the individual actor must contend, but rather is seen as the essential resource that makes knowledge possible and gives action its sense. The second change is a renewed commitment to grounding theories of action in empirical evidence: that is, to building generalizations inductively from records of particular, naturally occurring activities, and maintaining the theory's accountability to that evidence. Finally, and perhaps most importantly, this approach assumes that the coherence of action is not adequately explained by either preconceived cognitive schema or institutionalized social norms. Rather, the organization of situated action is an emergent property of moment-by-moment interactions between actors, and between actors and the environments of their action.

The emergent properties of action means that it is not predetermined, but neither is it random. A basic research goal for studies of situated action, therefore, is to explicate the relationship between structures of action and the resources and constraints afforded by physical and social circumstances. Ethnomethodology begins from the premise that we need, and have yet to produce, an adequate base of descriptions of situated human practices. Because there is no stable observational base, the social sciences "are talking sciences, and achieve in texts, not elsewhere, the observability and practical objectivity of their phenomena'' (Garfinkel, Lynch, and Livingston 1981, p. 133). As Heritage has recently stated the problem:

The "boundaries' of specific, located ordinary actions, their "units" or "segments," the determination of adequacy in

## Conclusion

their description or representation  all of these questions and many more pose problems which cannot be resolved "in principle' but which require solution in the context of practical engagement with descriptive tasks. (1984, p. 302)

In this study I have attempted to begin constructing a descriptive foundation for the analysis of human-machine communication. A growing corpus of observations from the analysis of everyday human conversation provides a baseline from which to assess the state of interactivity between people and machines. First, the mutual intelligibility that we achieve in our everyday interactions - sometimes with apparent effortlessness, sometimes with obvious travail  is always the product of in situ, collaborative work. Secondly, the general communicative practices that support that work are designed to maximize sensitivity to particular participants, on particular occasions of interaction. Thirdly, face-to-face communication includes resources for detecting and remedying troubles in understanding as part of its fundamental organization. And fourthly, every occasion of human communication is embedded in, and makes use of, an unarticulated background of experiences and circumstances. Communication in this sense is not a symbolic process that happens to go on in real-word settings, but a real-world activity in which we make use of language to delineate the collective relevance of our shared environment.

The application of insights gained through research on face-toface human interaction, in particular conversation analysis, to the study of human-computer interaction promises to be a productive research path. The initial observation is that interaction between people and machines requires essentially the same interpretive work that characterizes interaction between people, but with fundamentally different resources available to the participants. In particular, people make use of a rich array of linguistic, nonverbal, and inferential resources in finding the intelligibility of actions and events, in making their own actions sensible, and in managing the troubles in understanding that inevitably arise. Today's machines,

## Towards practical solutions

in contrast, rely on a fixed array of sensory inputs, mapped to a predetermined set of internal states and responses. The result is an asymmetry that substantially limits the scope of interaction between people and machines. Taken seriously, this asymmetry poses three outstanding problems for the design of interactive machines. First, the problem of how to lessen the asymmetry by extending the access of the machine to the actions and circumstances of the user. Secondly, the problem of how to make clear to the user the limits on the machine's access to those basic interactional resources. And finally, the problem of how to find ways of compensating for the machine's lack of access to the user's situation with computationally available alternatives.

## 8.1 Toward practical solutions

In the design of interactive machines, the most common substitute for access to the user and her situation has been the incorporation into the machine of a preconceived representation of the user and her situation, or a "user model." User models, constructed in advance as the template against which the user's actual actions re mapped, comprise propositions about the domain, the task, the typical user, and the like. Recently, designers concerned with the provison of situated help, or so-called intelligent tutoring systems, have begun extending such models to support local, or "real-time' assessment of the actions of the computer user (see Burton and Brown 1982, London and Clancey 1982, Woolf and McDonald 1983, Farrell, Anderson, and Reiser 1984, Peachey and McCalla 1986, Shrager and Finin 1982). A primary objective of such systems is to infer the user's knowledge and misconceptions about the system by observing her actions, rather than relying on either error conditions or explicit requests for help. To appreciate the requirements of this objective, one has simply to imagine those occasions where an expert, watching a novice engaged in some activity, would be moved to intercede. The outstanding question with respect to this form of coaching is, Just what does seeing those places where as-

## Conclusion

sistance is called for, and knowing what needs to be said, involve? Researchers pursuing "real-time user modeling" as the basis for a solution to this problem have adopted the following design strategies:

(1) Diagnosis based on differential modeling. A principal strategy for socalled intelligent tutoring systems, or computer-based coaches, has been to work from an ideal model of expert behavior in a given domain, to which the actions of student can be mapped. It is then the difference between expert and student behavior in particular circumstances that serves as the basis for assessing the student's knowledge and skills. The diagnosis works both on manifested errors that arise in the course of the student's actions and, more subtly, on the omisson of actions that, given a particular set of conditions, an idealized expert in those circumstances would take. The rationale for the differential modeling strategy is a combination of predictions based on the model of expert behavior, with techniques for local assessment of the student's actions. The success of the strategy turns on the degree of fit between the actions anticipated by the diagnostic model, and the actions of the student that are detectable by the machine.

)Detection of diagnostic inconsistencies. However felicitous the fit between student actions and diagnostic issues, the design must accommodate the likelihood of misdiagnosis, and provide for its detection and repair. In the best intelligent tutoring systems, the accumulating record of student actions includes both actions that manifest some issue which according to the current diagnosis should not appear, and actions that fail to manifest some issue that the student seems from prior diagnosis to understand. Evidence of misdiagnosis is found in the mount o ear," ste, i cculatig coen c

## Towards practical solutions

between the developing diagnostic model of what the student knows and doesn't know, and the understanding demonstrated in subsequent actions, reaches a certain threshold, the program may invoke alternative strategies that the student might be using. Possible alternative strategies, identified according to local evidence, are then tested for consistency with the global history of the student's actions. Crucially, the domain must be sufficiently closed that the set of possible alternative strategies can be enumerated.

(3) Separation of local and global interpretations. Recent tutoring systems begin to make use of a mechanism basic to everyday human communication, namely the separation, and productive interaction, between local and global interpretations of the other's actions. The diagnosis of student actions in computer-based tutoring systems is accomplished through two independent though interrelated mechanisms: one component which is data-driven from the local context of a given action, and another which runs over an accumulating history of the student's actions with the goal of identifying weaknesses or misunderstandings. As in the interpretation of action in the course of a developing conversation, it is the interaction of these two perspectives that affords the power of the diagnosis. The locality of the data-driven component supports an assessment of each particular action, relatively unconstrained by global preconceptions, while the global perspective of the evaluative component supports the interpretation of that action as a reflection of the student's general strategies and skills.

(4) The constructive use of trouble. In much the way that ordinary conversation relies upon the successful detection, repair, and even exploitation of troubles in understanding, recent tutoring systems adopt a "constructivist position' towards errors, such that the inevitability of student misconceptions or weaknesses is turned to pedagogical advantage.2 The goal of the coach in such systems is

## Conclusion

not to avoid student errors, but to make them accessible to the student, and therefore instructive. If the student has enough information to identify and repair an error, then it is considered a constructive one. If, on the other hand, the error is not manifest in such a way as to be visible, or is perceived but the student lacks the necessary information for its repair, the trouble is non-constructive. One major task of the coach, on this view, is to give the student the information required to transform non-constructive troubles into constructive ones, either by diagnosing the trouble and making it accessible, or by providing the information required for its repair.

This last strategy has recently been generalized as a call to design for the management of trouble (see Brown and Newman 1985). Such an objective implies at least that users are encouraged to use the wider social setting in which a machine is embedded as a resource to remedy the troubles in understanding that inevitably arise. Applied to the design of machines, it recommends incorporating the kind of diagnostic and interactional abilities that characterize the human coach into the machine itself. The problem in applying this later recommendation is that often the "grain size' of machine-readable actions is either too small or too large to constrain the analysis of the user's actions adequately. So, for example, in the case of the help system described in chaper 7, to appreciate the significance of a given user action - say, putting a document into the document handler - may require reference to a history that extends across procedures as the system tracks them. Alternatively, assessing the user's actions may require reference to sub-procedures, such as ordering pages of a document correctly, for which there is no trace. In general, if there is more than one understanding that can produce what appears to be the same action, detecting the action does not serve as unequivocal evidence that the understanding is actually in hand. By the same token, if a given skill can be manifest in some indefinite number of different actions, then the absence of an expected action does not necessarily mean the asenc  the ski While  the cse  thehumn cach th ambiguities are resolved through interaction, in the case of a computer-based coach the limits on the machine's access pose a difficult design problem. The problem is not simply that communicative troubles arise that do not arise in human communication, but rather that when the inevitable troubles do arise, there are not the same resources available for their detection and repair.

## 8.2 Plans as resources for action

Some researchers in human-computer interaction make the claim that cognitive science and computer technologies have advanced to the point where it is now feasible to build instructional computer systems that are as effective as experienced human tutors (see, for example, Anderson, Boyle, and Reiser 1985). In contrast to this optimism, I have argued that there is a profound and persisting asymmetry in interaction between people and machines, due to a disparity in their relative access to the moment-by-moment contingencies that constitute the conditions of situated interaction. Because of the asymmetry of user and machine, interface design is less a project of simulating human communication than of engineering alternatives to interaction's situated properties.

The primary alternative has been to substitute a generalized representation of the situation of action for access to the unique details of the user's particular situation. As in the expert help system analyzed in chapter 7, the representational scheme favored by many designers has been the plan. The problem for designers is that, as common-sense formulations of intent, plans are inherently vague. To the cognitive scientist, this representational vagueness is a fault to be remedied, insofar as a plan is the prerequisite for purposeful action, and the details of action are derived from the completion and modification of the plan. The task of the designer who would model situated action, therefore, is to improve upon, or render more precise and axiomatic, the plan.

For situated action, however, the vagueness of plans is not a fault, but is ideally suited to the fact that the detail of intent and

action must be contingent on the circumstantial and interactional particulars of actual situations. Given this view of plans, namely as resources for action rather than as controlling structures, the outstanding problem is not to improve upon them, but to understand what kind of resource they are. The most promising approach is to begin from the observation that plans are representations, or abstractions over action. In one sense, this simply joins the problem of plans to the more general, and no less difficult, question of representation. But in another sense, viewing plans as representations is suggestive of what their relation to unrepresented actions might be. Chapter 4 introduced a view, developed recently by Barwise and Perry (1985), that language can be characterized in terms of its efficiency and indexicality. By efficiency is meant simply the ways in which "expressions used by different people, in different spacetime locations, with different connections to the world around them, can have different interpretations, even though they retain the same linguistic meaning" (p. 5). In its efficiency, language provides us with a shareable resource for talk about the world. At the same time, the efficiency of language requires that our utterances always be anchored to the unique and particular occasions of their use. In this respect, language is indexical: that is, dependent for its significance on connections to particular occasions, and to the concrete circumstances in which an utterance is spoken. This view of language is taken as foundational by Garfinkel (1967), and by Garfinkel and Sacks (1970) with respect to the intelligibility and significance of action. Like other essentially linguistic representations, plans are efficient formulations of situated actions. By abstracting uniformities across situations, plans allow us to bring past experience and projected outcomes to bear on our present actions. As efficient formulations, however, the significance of plans turns on their relation back to the unique circumstances and unarticulated practices of situated activities. A problem for an account of situated action, on this view, is to describe the processes by which efficient

## Plans as resources for action

representations are brought into productive interaction with particular actions in particular environments. A rich description of this process comes, for example, from research on Micronesian navigation reported by Edwin Hutchins (1983). The natives of the Caroline Islands routinely embark on ocean-going canoe voyages that take them several days out of the sight of land. Western researchers travelling with them have found that, at any time during the voyage, the navigators can indicate the bearings of the port of departure, the target island, and other islands off to the side of the course they are steering, even though these may all be over the horizon and out of sight. They are able to do this and other feats of navigation that are simply impossible for a Western navigator without instruments. What Hutchins reports is that they maintain their course by substituting other environmental referents, that are accessible, for the inaccessible land. In particular, they follow a star path, selected with reference to a sidereal compass or star chart that forms a map between pairs of islands. To maintain their orientation to the star path at any given point in their voyage requires that they consult not only the stars, but a rich set of changing environmental circumstances - the color of the water, the waves, winds and clouds, birds, and so forth - which through experience become interpretable for information about the relative position of the canoe. What is notable about Hutchins's account of the resources of the Micronesian navigator is that nowhere is a preconceived plan in evidence. The basis for navigation seems to be, instead, local interactions with the environment. In this way, navigators maintain their orientation to the star path, which in turn is fixed to the islands of origin and destination.

The Micronesian example demonstrates how the nature of an activity can be missed unless one views purposeful action as an interaction between a representation and the particular contingent details of the environment. With respect to plans and actions, Feitelson and Stefik (1977) found this same relation present in the work of geneticists planning scientific experiments. Specifically, they found that geneticists elaborated their plans only far enough

## Conclusion

to act as a framework in which to organize the constraints of the laboratory. Rather than planning the experiment through an a priori analysis, the experimenters decided what to do next by relating each current observation to their research goals. The experimenters' expertise lay not in completing the plan, but in the ability to generate hypotheses continually, and to exploit serendipity in the course of the experiment. The experimental process, being what Feitelson and Stefik call "event driven," allowed the experimenter to "fish for interesting possibilities"; that is, to follow up on unanticipated observations and opportunities provided by a particular experimental set-up. From these and other examples, we can begin to draw an alternative account of the relation of plans to situated actions. The foundation of actions by this account is not plans, but local interactions with our environment, more and less informed by reference to abstract representations of situations and of actions, and more and less available to representation themselves. The function of abstract representations is not to serve as specifications for the local interactions, but rather to orient or position us in a way that will allow us, through local interactions, to exploit some contingencies of our environment, and to avoid others. While plans can be elaborated indefinitely, they elaborate actions just to the level that elaboration is useful; they are vague with respect to the details of action precisely at the level at which it makes sense to forego abstract representation, and rely on the availability of a particular, embodied response. The interesting problem for an account of action, finally, is not to improve upon common-sense plans, but to describe how it is that we are able to bring efficient descriptions (such as plans) and particular circumstances into productive interaction. The assumption in planning research in cognitive science has been that this process consists in filling in the details of the plan to some operational level. But when we look at actual studies of situated action, it seems that situated action turns on local interactions between the actor and contingencies that, while they are made accountable to a plan,

remain essentially outside of the plan's scope. Just as it would seem absurd to claim that a map in some strong sense controlled the traveler's movements through the world, it is wrong to imagine plans as controlling actions. On the other hand, the question of how a map is produced for specific purposes, how in any actual instance it is interpreted vis-à-vis the world, and how its use is a resource for traversing the world, is a reasonable and productive one. In the last analysis, it is in the interaction of representation and represented where, so to speak, the action is. To get at the action in situ requires accounts not only of efficient symbolic representations but of their productive interaction with the unique, unrepresented circumstances in which action in every instance and invariably occurs.

A starting premise of this book was that the project of building interactive machines has more to gain by understanding the differences between human interaction and machine operation, than by simply assuming their similarity. My argument has been that as long as machine actions are determined by stipulated conditions, machine interaction with the world, and with people in particular, will be limited to the intentions of designers and their ability to anticipate and constrain the user's actions. The generality of various representations of situations and actions is the principle resource for this task, while the context insensitivity of such representational schemes is the principle limitation. The question, finally, is: What are the consequences of that limitation? The answer will differ according to whether our concern is with practical or with theoretical consequences. Practically, ingenious design combined with testing may do much to extend the range of useful machine behavior. Theoretically, understanding the limits of machine behavior challenges our understanding of the resources of human action. Just as the project of building intelligent artifacts has been enlisted in the service of a theory of mind, the attempt to build interactive artifacts, taken seriously, could contribute much to an account of situated human action and shared understanding.

## References

Allen, J. 1983. Recognizing intentions from natural language utterances. In Computational Models of Discourse, M. Brady and R. Berwick, eds., ch. 2. Cambridge, MA: MIT Press.

1984. Towards a general theory of action and time. Artificial Intelligence 23:123-54.

Amerine, R. and Bilmes, J. 1979. Following instruction. Unpublished manuscript, University of California, Santa Barbara.

Anderson, J., Boyle, C., and Reiser, B. 1985. Intelligent tutoring systems. Science 228: 45662.

Anscombe, G. E. M. 1957. Intentions. Oxford: Basil Blackwell.

Appelt, D. 1985. Planning English referring expressions. Artificial Intelligence 26: 133.

Atkinson, J. M. and Drew, P. 1979. Order in Court: The Organization of Verbal Interaction in Judicial Settings. Atlantic Highlands, NJ: Humanities Press.

Austin, J. L. 1962. How to do Things with Words. Oxford: Clarendon Press.

Barwise, J. and Perry, J. 1985. Situations and Attitudes. Cambridge, MA: MIT Press.

Lauge nConx:TheAcqusi PrN York, NY: Academic Press.

Beckman, H. and Frankel, R. 1983. Who hides the agenda: the impact of physician behavior on the collection of data. Presented to the Fourth Annual SREPCIM Task Force on Interviewing, Washington, DC, April 1983. [Address reprint requests to Howard Beckman, MD, POD 5C, University Health Center, 4201 St Antoine, Detroit, MI 48201.]

Berreman, G. 16. Anemic andemetic analyses in socialanthropy. American Anthropologist 68(2)1:34654.

whie .nc anContex:Ess n Bo oictio.hiladelphia, A:Univrsyensvani

Bluer, H. 1969. Symbolic Interactionism. Englewood Cliffs, NJ Prentice-Hall.

Bobrow, D.G., Kaplan, R. M. Kay, M., Norman, D. A., Thompson, H., and Winograd, T. 1977. GUS: a frame-driven dialogue system. Artificial Intelligence 8: 15573.

e u l  Teo Behavior 3:23-46.

y .anBerwck, R.oaM Discourse. Cambridge, MA: MIT Press.

Brown, J. S. and Newman, S. 1985. Issues in cognitive and social ergonomics: from our house to Bauhaus. HumanComputer Interaction 1:35991.

Brown, J. S. Rubenstein, R., and Burton, R. 1976. Reactive Learning Environment for Computer Assisted Electronics Instruction. BBN Report 3314, Bolt Beranek and Newman, Inc., Cambridge, MA.

Bruce, B. 1981. Natural communication between person and computer. In Strategies for Natural Language Processing, W. Lehnert and M. Ringle, eds. Hillsdale, NJ: Erlbaum.

Bruner, J. 1986. Actual Minds, Possible Worlds. Cambridge, MA: Harvard University Press.

Bu J.al elgliin  ial. Unpublished Ph.D. dissertation, University of llinois at Urbana-Champaign.

Burton, R. and Brown, J. S. 1982. An investigation of computer coaching for informal learning activities. In Intelligent Tutoring Systems, D. Sleeman and J. S. Brown, eds. London: Academic Press.

Carbonell, J. R. 1971. Mixed-Initiative Man-Computer Dialogues. Technical Report 1970, Bolt Beranek and Newman, Inc., Cambridge, MA.

Carey, S. 1985. Conceptual Change in Childhood. Cambridge, MA: MIT Press.

Churchland, P. 1984. Matter and Consciousness. Cambridge, MA: MIT Press.

Cohen, J. 1966. Human Robots in Myth and Science. London: Allen and Unwin.

Cohen, P. [n.d.] Pragmatics, speaker-reference, and the modality of communication. Unpublished manuscript, Laboratory for Artificial Intelligence, Fairchild Camera and Instrument Corp., Palo Alto, CA.

Cohen, P. and Perrault, C. R. 1979. Elements of a plan-based theory of speech acts. Cognitive Science 3:177212.

Colby, K. M. et al. 1972. Turing-like indistinguishability tests for the validation of a computer simulation of paranoid processes. Artificial Intelligence 3:199221.

Coombs, M. and Alty, J. 1984. Expert systems: an alternative paradigm. International Journal of Man-Machine Studies 20:2143.

Coulter, J. 1979. The Social Construction of Mind. Totowa, NJ: Rowman and Littlefield.

1983. Rethinking Cognitive Theory. New York, NY: St. Martin's Press.

Dennett, D. 1978. Brainstorms. Cambridge, MA: MIT Press.

Dreyfus, H. 1979. What Computers Can't Do: The Limits of Artificial Intelligence, revised edition. New York, NY: Harper and Row.

ed.1982.Husserl Intentionality and Cognitive Science.Cambridge, MA: MIT Press.

In press. Being-in-the-world: A Commentary on Heidegger's Being and Time, Division I. Cambridge, MA: MIT Press.

Duncan, S. Jr. 1974. On the structure of speaker-auditor interaction during speaking turns. Language in Society 3:16180.

Durkheim, E. 1938. The Rules of Sociological Method. New York, NY: The Free Press.

Erickson, F. 1982. Money tree, lasagna bush, salt and pepper: social construction of topical cohesion in a conversation among Italian-Americans. In Georgetown University Round Table on Language and Linguistics: Analyzing Discourse: Text and Talk, D. Tannen, ed. Washington, DC: Georgetown University Press.

Erickson, F. and Shultz, J. 19.The Counselor as Gatekeeper. New York, NY: Academic Press.

Farrell, R., Anderson, J., and Reiser, B. 1984. An interactive computerbased tutor for LISP. Proceedings ofthe American Association for Artificial Intelligence, pp. 106-9. Austin, TX.

Feitelson, J. and Stefik, M. 197. A case study of the reasoning ina genetics experiment. Heuristic Programming Project, Working Paper 778, Stanford, CA: Stanford University.

Fikes, R. and Nilsson, N. 1971. STRIPS: a new approach to the application of theorem proving to problem solving. Artificial Intelligence 2: 189205.

Fier, .Tar moreaturactive sy. International JournalManMachine Stud11:339.

Fodor, J. 1983. The Modularity of Mind. Cambridge, MA: MIT Press.

Frankel, R. 1984. From sentence to sequence: understanding the medical encounter through microinteractional analysis. Discourse Processes 7:13570.

Galaty, J. 1981. Models and metaphors: on the semiotic explanation of aryyems. InThe r oMe, LHo Stuchlik, eds. New York: Academic Press.

## References

Gardner, H. 1985. The Mind's New Science. New York: Basic Books.

Garfinkel, H. 196. Studies in Ethnomethodology. Englewood Cliffs, NJ Prentice-Hall.

. Remarks on ethnomethodology. In Directions in Sociolinguistics: The Ethnography of Communication, J. Gumperz and D. Hymes, eds. New York, NY: Holt, Rinehart and Winston.

Garfinkel, H. and Sacks, H. 1970. On formal structures of practical actions. In Theoretical Sociology, J. McKinney andE. Tiryakian, eds. New York, NY: Appleton-Century-Crofts.

Garfinkel, H., Lynch, M., and Livingston, E. 1981. The work ofa discovering science construed with materials from the optically discovered pulsar. Philosophy of the Social Sciences 11:13158.

Geertz, C. 19. The Interpretation ofCultures. New York, NY: Basic Books.

Gladwin, T. 1964. Culture and logical process. In Explorations in Cultural Anthropology: Essays Presented to George Peter Murdock, W. Goodenough, ed. New York, NY: McGraw-Hill.

Goffman, E.975.Repliesand responses. Language in Society 5:257.

Goodwin, C. 1981. Conversational Organization: Interaction Between Speakers and Hearers. New York, NY: Academic Press.

Goodwin, M. 1980. Processes of mutual monitoring implicated in the pcetSclnqu:

Grice, H. P. 1975. Logic and conversation. In Syntax and Semantics, vol. 3: Speech Acts, P. Cole and J. Morgan, eds. New York, NY: Academic Press.

Grosz, B. 1981. Focusing and description in natural language dialogues. In Elements of Discourse Understanding, Joshi, A., Webber, B., and Sag, I., eds. Cambridge University Press.

Gumperz, J. 1982a Discourse Strategies. Cambridge: Cambridge University Press.

1982b. The linguistic bases of communicative competence. In Georgetown University Round Table on Language and Linguistics: Analyzing Discourse: Text and Talk, D. Tannen, ed. Washington, DC: Georgetown University Press.

Gumperz, J. and Tannen, D. 1979. Individual and social differences in language use. In Individual Differences in Language Ability and Language Behavior, C. Fillmore et al., eds. New York: Academic Press.

Hayes, P. 1981. A construction-specific approach to focused interaction in flexible parsing. Proceedings of Nineteenth Annual Meeting of the Association for Computational Linguistics, pp. 149-52. Stanford, CA: Stanford University.

Hayes, P. and Reddy, D. R. 1983. Steps toward graceful interaction in spoken and written man-machine communication. International Journal of Man-Machine Studies 19:23184.

Heap, J. 198o. Description in ethnomethodology. Human Studies 3:87106.

Hendrix, G. G. 1977. Human engineering for applied natural language processing. Proceedings of the Fifth International Joint Conference on Artificial Intelligence, pp. 183-91. Cambridge MA: MIT.

Heritage, J. 1984. Garfinkel and Ethnomethodology.Cambridge, England: Polity Press.

1985. Recent developments in conversation analysis. Sociolinguistics 15:1-1

Hutchins, E. 1983. Understanding Micronesian navigation. In Mental Models, D. Gentner, and A. Stevens, eds. Hillsdale, NJ: Erlbaum.

.Issues in the transcription of naturally occurring talk: caricature versus capturing pronunciational particulars. Tilburg Papers in Language and Literature, no. 34, Tilburg University, Tilburg, The Netherlands.

Jordan, B. and Fuller, N. 1975. On the non-fatal nature of trouble: sense-making and trouble-managing in Lingua Franca talk. Semiotica 13:131.

Joshi A. Webber, B., anSag, I. s9.Eleme oDis Understanding. Cambridge University Press.

Levinson, S. 1983. Pragmatics. Cambridge University Press.

London, B. and Clancey, W. 1982. Plan recognition strategies in student modeling: prediction and description. Proceedings of the American Association for Artificial Intelligence, pp. 8. Pittsburg, PA.

Lynch, M.98.Art and Artifact in Laboratory Science. Lon: Routledge and Kegan Paul.

Lynch, M., Livingston, E., and Garfinkel, H. 1983. Temporal order in laboratory work. In Science Observed, K. Knorrand M. Mulkay, eds. London: Sage.

McCorduck, P. 1979. Machines Who Think. San Francisco, CA: W. H. Freeman.

McDermott, R. 1976. Kids make sense: an ethnographic account of the interactionalmanagemen uccss anilurenersd classroom. Unpublished Ph.D. dissertation, Stanford University.

MacKay, D. M. 1962. The use of behavioral language to refer to mchanical prcese.Briti JournalPhilohicalScience, 13:89.

Mead, G. H. 1934. Mind, Self, and Society. University of Chicago Press.

Merritt, M. 1977. On questions following questions in service encuntrs. Languagn Socty 5:157

l . Gl . ,Pl he Behavior. New York, NY: Holt, Rinehart and Winston.

ll A.andSimon, H.Hun roblm Solvin. Eng Cliffs, NJ: Prentice-Hall.

Nickerson, R. 1976. On conversational interaction with computers. In Proceedings of ACM/SIGGRAPH workshop, October 1415, p. 10113. Pittsburgh, PA.

Nilsson, N. 1973. A hierarchical robot planning and execution system. In Technical Note 76, SRI Artificial Intelligence Center, Stanford Research Institute, April. Menlo Park, CA.

Oberquelle, H., Kupka, I., and Maass, S. 1983. A view of human— machine communication and cooperation. International Journal of Man Machine Studies 19:30933.

Ochs, E. 1979. Planned and unplanned discourse. In Syntax and Semantics, vol. 12: Discourse and Syntax, T. Givon, ed. New York, NY: Academic Press.

Peachey, D. and McCalla, G. 1986. Using planning techniques in intelligent tutoring systems. International Journal of Man—Machine Studies 24:7798.

Peirce, C. 1933. Collected Papers, vol 11, C. Hartshorne and P. Weiss, eds. Cambridge, MA: Harvard University Press.

Pylyshyn, Z. 1974. Minds, machines and phenomenology: some relections on Dreyfus' What Computers Can' Do. Cognition 3:5777. 1984. Computation and Cognition. Cambridge, MA: MIT Press.

Rubin, A. 198o. A theoretical taxonomy of the differences between oral and written language. In Theoretical Issues in Reading Comprehension, R. Spiro et al. eds. Hillsdale, NJ: Erlbaum.

Sacerdoti, E. 1975. The nonlinear nature of plans. Proceedings of the Fourth International Joint Conference on Artificial Intelligence. Tbilisi, USSR.

1977. A Structure for Plans and Behavior. New York, NY: Elsevier.

Sacks, H. 1963.Sociological description. Berkeley Journal of Sociology 8:1-16.

1974. An analysis of the course of a joke's telling in conversation. In Explorations in the Ethnography of Speaking, R. Bauman and J. Scherzer, eds. Cambridge University Press.

Sacks, H., Schegloff, E., and Jefferson, G. 1978. A simplest systematics for the organization of turn-taking in conversation. In Studies in the

OrgnizationConvrtioal Interacion,JSchenkein e. NewYork, NY: Academic Press.

Schank, R. and Abelson, R. 1977. Scripts, plans and knowledge. In Thinking: Readings in Cognitive Science, P. Johnson-Laird and P. Wason, eds. Cambridge University Press.

Scheflen, A. E. 1974. How Behavior Means. Garden City, NY.: Anchor Press.

Schegloff, E. 1972. Sequencing in conversational openings. In Directions in Sociolinguistics: The Ethnography of Communication, J. Gumperz and D. Hymes, eds. New York, NY: Academic Press.

1982. Discourse as an interactional achievement: some uses of "uh huh'" and other things that come between sentences. In Georgetown University Round Table on Language and Linguistics: Analyzing Discourse: Text and Talk, D. Tannen, ed. Washington, DC: Georgetown University Press.

Schegloff, E. and Sachs, H. 1973. Opening up closings. Semiotica 7:289327.

Schmidt, C. F., Sridharan, N., and Goodson, J. 1978. The plan recognition problem. Artificial Inteligence 11:4583.

Schutz, A. 9. Collected Papers I: The Problem of Social Reality. The Hague: Martinus Nijhoff.

J Cambridge University Press.

1979. Expression and Meaning. Cambridge University Press.

Theelinon ctivec 4:4

Shrager, J. and Finin, T. 1982. An expert system that volunteers advice. tial pp. 339-40. Pittsburgh, PA.

Sidner, C. L. 1979. Towards a computational theory of definite anaphora comprehension in English discourse. Technical Report TR-537, MIT AI Laboratory. Cambridge, MA.

ich, S..FroFolksychology tConitiveScience.CmriA: MIT Press.

J.c i: Processes 3: 13354.

Suchman, L. 1982. Toward a sociology of human-machine interaction: CA: Xerox Palo Alto Research Center.

Turing, A.M. 190.Computing machinery and intelligence. Mind 59(236):43361.

Turkle, S. 1984. The Second Self. New York, NY: Simon and Schuster.

Turner, R. 96.Words, utterances andactivits. In Ethnmethodoy: Selected readings, ed. Turner. Harmondsworth, Middlesex: Penguin.

Watt, W. C. 1968. Habitability. American Documentation 19(3):33851. Weizenbaum, J. 1983. ELIZA: a computer program for the study of natural language communication between man and machine. Communications of the ACM, 25th Anniversary Iss1:°, 26(1):237. (Reprinted from Communications of the ACM, 29(1):3645, January 1966.)

Wilson, T. 1970. Conceptions of interaction and forms of sociological explanation. American Sociological Review 35:697709.

Woolf, B. and McDonald, D. 1983. Human-computer discourse in the design of a PASCAL tutor. Proceedings of the Computer—Human Interaction Conference, pp. 230-4. Boston, MA.

Zimmerman, D. 1970. The practicalities of rule use. In Understanding Everyday Life, J. Douglas, ed. Chicago, II: Aldine.

## Author index

Abelson, R. 43, 44   
Allen, J. 3,   
Alty, J. 19n, 2on   
Amerine, R. 101, 103   
Anderson, J. 181, 185   
Anscombe, G.E.M.110n   
Appelt, D.40   
tinon, J. M. 84, 85,86, 88,89   
Barwise, J. 58n, 186   
aBats E.59   
Beckman, H. 91,92   
Berreman, G. vii   
erwik, R.39   
Bilmes, J. 101, 103   
Birdwhistell, R. 72   
Blumer, H. 55, 56   
Bobrow, D. G. 12   
Boden, M. 36, 38,45   
Bole,C. 185   
Bray, M.39   
Brown, J.S.19,20n, 115n, 181, 182n, 18n, 184   
Bruce, B.39   
Bruner, J. 119n   
Burke, J.105, 106, 141, 142   
Burton, R. 19, 20n, 115n, 181, 182n, 183n   
Carbonell, J. R. 12   
ary, S. 5n   
Churchland, P.7n   
Clancey, W. 181   
ohen J.7n   
Cohen, P.40, 106   
Colby, K. M. 24n   
Coombs, M. 19n, 20n

Davis, L. K. 38n Dre, P.84, 85, 86, 88,89

Dreyfus, H. vii, 6, 9n, 3,   
Dreyfus, S. viii   
Duncan, S. Jr. 76   
Durkheim, E. 5,55,5,79

Erickson, F. 6,1,,99

Farrell, R. 181   
Feitelson, J. 187, 188   
Fikes, R. 29, 98n, 10n   
FinT. 181   
Fi Fiter, M. 14   
Fodor, J.9   
Franel R.87 89,91,   
uller, N. 87, 157, 70   
Galanter, E. 36, 37   
Galaty . 112n   
Gardner, H.7n   
Garfinkel, H. 2, 46, 5, 5,5, 6, 101, 104, 179, 186   
Geertz, C. 1   
Gladwin, T. vii, 27, 49   
Goffman, E. 68, 80, 82   
Goodson, J. 35   
Goodwin, C.1,72,74,7,77   
Goodwin, M. 72   
Grice, . P.41   
GroSz, B. 13, 105   
Gumperz, J.41,42,7,87,115

Hayes, P. 12, 13, 14, 25   
Hep, J.113   
Heidegger, M. 39n, 53, 54   
Henderson, A. 110n   
Hendrix, G. G. 12   
Heritage, J. 5, 67, 69, 97   
Hutchins, E. 187

Jefferson, G. 69,73, 74, 76, 83, 84, 87

## Author index

Jordan, B. 87, 157, 170   
Joshi, A. 39   
Kaplan, R. M. 12   
Kay,M. 12   
Upa, I. 10   
Levinson, S. 78, 80, 81   
Livingston, E. 101, 104, 179   
London, B.181   
Lynch, M. 9, 101, 10, 9   
Maass, S. 10   
McCalla, G. 181   
McCorduck, P. 7, 8n, 30   
McDermott, R.68   
McDonald, D. 181   
MacKay, D. M. 16   
Mannheim, K. 23   
Mead, G. H. 51, 53, 56, 57   
Merleau-Ponty, M. 53   
de la Mettrie, J.8   
Miller, G. 10, 36, 37   
Newell, A. 28n   
Newman, S. 184   
Nickerson, R. 15   
Nilsson, N. 29, 30   
Norman, D. A. 12   
Oberquelle, H. 10   
OchE. 105   
Peachey, D. 181   
Peirce, C. S. 58, 62   
Perrault C. R.40   
Perry, J. 98n, 186   
Prbram, K. 36,37   
Pylyshyn, Z. 9, 10   
Raphael, B. 30   
Redy, D. R. 12, 13, 14, 25

Reiser, B. 181, 185 Rubenstein, R. 115n Rubin, A. 105

Sacerdoti, E. 29n, 30, 31, 32, 33, 34n, 104   
Sacks, H. 5,60, 61, 69,73-6,78,83, 186   
Sag, I. 399   
Schank, R. 43,44   
Scheflen, A. E.72   
Shegoff, E.69,71,73,74,76,78,79,83   
84,91,94,98,156   
Shmidt C. F. 35   
Schultz, J. 68,71,72,91,93,94   
Schutz, A.58,60,68   
Searle, J. 38n, 40, 41, 61,110   
Shrager, J. 181   
Sidner, C. R. 13   
Simon, H. 28n   
Sridharan, N. 35   
Stefik, M. 187, 188   
Sttih S.8, 9   
treek, J. 70   
Suchman, L. 110n   
Tannen, D. 72, 87   
Thompson, H. 12   
Trigg, R. 52n   
Turing, A. M. 21, 22   
Turkle, S.5, 6, 8n, 10, 16   
Turner,R.118

de Vaucanson, J.7

Watt, W. C. 14   
Webber, B.   
Weizenbaum, J. 2, 2, ,,6   
Wilson, T. 63, 112   
Winograd, T. 12   
Wittgenstein, L. 53   
Woolf, B.  181

Zimmerman, D. 101

adjacency pairs, 7882, 155

agenda, 88, 915

anticipation of designer, 132, 1345, 1379, 166, 169, 189; see also design of interactive machines

artifacts, 4, ch. 2, 132, 189

artificial intelligence research, 6n, , 7, 30, 33,35, 35n, 36, 40, 45, 104, 115n

automata and cognitive science, 710

background knowledge, 28, 428, 61, 180

batch processing, 11

behaviorism, 89, 50, 55

coaching: computer based, 1921, 19n, 181-4; human, 17, 1820, 19n, 1056, 142, 1845; see also expert help systems; instructions to user

cognition, 5, 6n, 8, 9; as computation, 9

cognitive science, ix, 2, 710, 27, 37, 43, 47, 48, 61, 67, 70, 101, 178, 185, 188

common sense: knowledge, 43, 45; plans, 49, 188; psychology, 16; view of world,578

communication, 3, 6, 6n, 1213, 18, 19, 336, 40, 456, 57, 612, 63, 66, 6971, 86,95,115,118, 11921, 1224, 127, 144, 1468, 1558, 16970, 180, 189; situated communication, 4, 33, 701, 77; see also human-machine communication

communicative economy, 45

communicative resources, ch.5, 104f.

Computer-Based Consultant project, 104-5

computer model of intelligent behavior, 2-3,9

conditional relevance, 78, 80, 823, 143-69

contextualization cues, 72

conversation analysis, 69, 7283; notation for, 967

cooperation, 41

"cultural dope," 55

deixis, 58, 60, 168

design ofinteractive machines, 12, 4, 56, 7, 17, 17n, 18, 19, 21, 98, 99, 100n, 11, 119, 120, 121, 122, 127, 1324, 1434, 1512, 165, 1689, 170, 1814, 185,189; see also anticipation of designer   
DOCTOR, 23-4, 24n, 656   
documentary method of interpretation,   
23, 63-7

ELIZA, 225, 64

ensemble work, 702, 180

environment of action, 9, 30, 323, 546, 68, 179, 180, 1878; see also world model

error response, 32, 102

ethnographic anthropology, see social sciences

ethnomethodology, 4950, 57-8, 627, 179

execution monitoring, 2933

expectations, user's, 12, 13, 148, 1634, 165, 16970

expert behavior, vii, 18, 20, 31, 91, 103, 182

expert help systems, 54, 98, 99101, 1069, 110n, 111, 114, ch.7, 185; see also instructions to user; coaching

expert systems, 10, 98

"failure and surprise," 30

false alarm, 121, 1635, 170

feedback, 11, 30, 32

felicity conditions, 41   
garden path situation, 87, 121, 152, 163,   
169, 170   
GUUS, 12   
"habitability," 14   
human-machine communication, 1, 2, 3 4, 67, 1016, 19n, 225, 39, 70, 95, 100, 1045, 114-15, ch.7, 1801   
illocutionary force, 401   
implicature, 41, 80, 1467, 155   
dex, 6;see ounder anag   
indirectness, 412   
instruction manuals, 19, 62, 132   
instructions, 54, 612, 1012, 1046, 11012; to user, 1721, 31, 98101, 104, 1056, 107-9, ch.7; see also expert help systems; coaching   
iellence, vii, 5,8,10,21,39,,4 656; see also under machines   
intelligent tutoring systems, 1814   
ntelligibility  action,18 119,1689,180,186   
, , 6, , 113, 120, 121, 127, 128, 132, 136, 165, 169, 178; intent-in-action, 38, 38n; prior intent, 38, 38n   
intentional causation, 5n   
intentional explanation of machines, 15-16   
interaction, see communication   
interactive computing," 10-11   
interface, 17, 17n, 116, 120, 185   
interpretation of action, 1, 23, 6, 69 99, 109, 112, 116, 178   
introspection, 8,35n   
job specification, 100, 126, 133, 136, 171   
language, 50, 57,586,70; indexicality 0 5862, 132 168, 186   
language setting, 602, 88-95; medical   
ection8alon 8891   
LIFER, 12   
local management, 69, 738, 889, 94   
machines, ix, 1,5,6,6, 10, 11,1,7,

216, 119, 189; machine intelligence, 39, 43; machine response, 11921, 122, 14363, 181; machine situation, 119, 12132, 133-4, 143, 180-1; see also opacity of machines; reactivity of machines

"manipulation,"53

mechanical causation, 5n

methodology, 109-17; event-driven, 188

mind,7,8,9,56, 189

motivation response, 31

mutual intelligibility, 1, 2, 3, 4, 6, 1415, 2,28,33, 42,49, 501, 578,59,61, ,6,72,87, 115,117, 118,121, 180, 189

navigation plans, viii, x, 27, 49, 2, 187

NOAH, 30-2

noise, 1023

novice users, 4, 18, 19, 19n, 54, 114,1323, 169, 14852

opacity of machines, 7, 15, 16, 18

parsing, 12   
pauses, see silence   
people: children's conceptions of, 56; as machines, 6n, 910; as physical structure, 8   
PLANEX, 30, 32   
plans, ix, x, 3, 4, 8, ch.3, 4950, 523, 63, 92, 94,99, 100, 105, 119, 120, 169, 178, 185   
preconditions, 401, 1089,150n   
problem-solving, 8, 2831, 53, 142; see also troubles in human-machine communication   
procedural net, 31   
PROOG, 20n   
purposeful action, viix, 2, 3, 4, 27, 35, 379, 38n, 42, 47, 48, 4950, 51, 56, 623, 689, 148, 163, 179, 187   
reactivity of machines, 5, 7, 1011, 16   
recipient design, 1819, 132   
robots, 10, 30,3; Shakey, 2930, 32   
robust communication, 12, 256   
SCHOLAR, 12

turn-taking, 73-9, 836, 889o; with machines, 108, 1467, 14950

scripts, 434

Shakey, see under robots

significance of action, 1, 423, 50, 69, 113,114,118,169, 186

silence, 70,767, 78, 8990, 1467; in human-machine communication, 129, 1467, 149, 1613

simulation, 23, 7, 11n, 24n, 369, 105, 185

situated actions, ix, x, 3, 4, 278, 389, 39n, 42, 478, ch.4, 68, 101, 104, 109, 11112, 113, 114, 118, 120, 1789, 185-9

situated inquiries, 121, 13243, 162, 169-70

"social fact," 79, 82

social sciences, 12, 4, 49, 578, 69, 101, 11213,112n, 1789; see also ethnomethodology

social world, 1, 546, 57, 98, 112n, 113; stability of, 63-7

speech acts, 28, 3942, 92n

speech synthesis, 11n

Stanford Research Institute, 29, 31, 104

STRIPS, 2930

tear," 182

thought, see cognition

troubles in communication, 12, 14, 25, 26, 44, 534, 69, 72, 73, 838, 89, 94, 95, 1558, 180, 1835

troubles in human-machine communication, 25,54,87, 11415, 121, 12832, 13343, 14870

Trukese navigators, vi-vii, ix, 49

truth conditions, 61

Turing test, 212, 64

unordered actions, 34n user's situation, 11819, 120, 1324, 143, 1812, 185

WEST, 1920, 182n

This lively and original book offers a provocative critique of the dominant assumptions regarding human action and communication which underlie recent research in machine intelligence. Lucy Suchman argues that the planning model of interaction favoured by the majority of AI researchers does not take sufficient account of the situatedness of most human social behaviour. The problems that can arise as a result are pertinently, and often amusingly, illustrated by the careful analysis of a recorded interaction between novice users and an intelligent machine, whose design has failed to accommodate essential resources of successful human communication.

Plans and situated actions presents a compelling case for the reexamination of current models underlying interface design. Lucy Suchman's proposals for a fresh characterization of human-computer interaction which also incorporates recent insights from the social sciences provides a challenge that everyone interested in machine intelligence will need seriously to consider.

This book should be required reading for every serious student of computer system design.'

TERRY wINoGRAD (Professor of Computer Science, Stanford University)

'Lucy Suchman's book is a uniquely creative anthropological approach to human and machine intelligence. Her book poses a closely argued challenge to central assumptions in the cognitive sciences.'

JEAN LAvE (Professor of Anthropology, University of California, Irvine)

Th booul q l who w the human action, whether they be cognitive scientists interested in how people work or practitioners who wish to make systems for people to use . . . A most important work.'

L.R irecor, Institue or Cognitive Science, Univeiy of California, San Diego)

ISBN 0-521-33739-9
