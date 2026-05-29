> 来源：Understanding computers and cognition a new foundation for design (Winograd, Terry, Flores, Fernando)
> 原始文件：C:\Users\lenovo\Documents\Codex\2026-05-29\书籍专著\Understanding computers and cognition a new foundation for design (Winograd, Terry, Flores, Fernando)\Understanding computers and cognition a new foundation for design (Winograd, Terry, Flores, Fernando).md
> 识别方式：强章节标记

## Chapter 9

## Understanding language

There is an intimate connection between intelligence and language. Many of the representation techniques described in the previous chapters were first developed in trying to process natural language1 with computers. Our position, in accord with the preceding chapters, is that computers cannot understand language. Some important observations can be made along the route to that conclusion, and in this chapter we review the existing research work in some detail. We are concerned with the technical details here because natural language research has been the context for many of the efforts within artificial intelligence to deal with the theoretical issues we raise. Mechanisms such as 'frames,' 'scripts,' and 'resource-limited reasoning' have been proposed as ways to build machines that in some sense deal with 'understanding' and 'interpretation.' We need to examine them carefully to evaluate these claims.

## 9.1 Artificial intelligence and language understanding

In the mid 1960s, natural language research with computers proceeded in the wake of widespread disillusionment caused by the failure of the highly touted and heavily funded machine translation projects. There was a feeling that researchers had failed to make good on their early confident claims and that computers might not be able to deal with the complexities of human language at all. Artificial intelligence researchers took a new approach, going beyond the syntactic word-shuffing that dominated machine translation. It was clear that for effective machine processing of language-whether for translation, question answering, or sophisticated information retrieval—an analysis of the syntactic structures and identification of the lexical items was not sufficient. Programs had to deal somehow with what the words and sentences meant.

A number of programs in this new vein were described in the early collections of papers on artificial intelligence.2 Each program worked in some very limited domain (such as baseball scores, family trees, or algebra word problems) within which it was possible to set up formal representation structures corresponding to the meanings of sentences. These structures could be used in a systematic reasoning process as a partial simulation of language comprehension. The model of language understanding implicit in those programs (and most such programs since) rests on some basic assumptions about language and representation that we have elaborated in our earlier accounts of the rationalistic tradition:

1. Sentences in a natural language correspond to facts about the world.

2. It is possible to create a formal representation system such that:

(a) For any relevant fact about the world there can be a corresponding structure in the representation system.

(b) There is a systematic way of correlating sentences in natural language with structures in the representation system, so that the corresponding structure states the same fact as the sentence.

(c) Systematic formal operations on representation structures can be devised to carry out valid reasoning.

This somewhat simplistic formulation needs elaboration to be comprehensive. It is clear, for example, that a question or command does not correspond to facts in the same manner as a statement, and that a reasoning system based on pure logic is unlikely to be sufficient. We will discuss some of these elaborations later, but for a preliminary understanding they do not play a major role.

The critical element in this approach is the systematic manipulation of a formal representation. Operations carried out on the representation structures are justified not by facts about language, but by the correspondence between the representation and the world being described. It is in this sense that such programs are said to 'understand' the words and sentences they deal with, while the earlier machine translation programs (or other programs that deal with text using key-word recognition or statistical methods) only 'manipulate without understanding.'

Many claims have been made that the 'artificial intelligence paradigm' is new and superior to older philosophical approaches to language. But with a few notable exceptions (discussed later), these claims have proved rather empty. Fodor, in "Methodological solipsism considered as a research strategy in cognitive psychology" (1980), has pointed out that to the extent that they are clearly defined, artificial intelligence models are generally equivalent to older philosophical ones in the analytic tradition, drawing on ideas that go back to Aristotle and beyond. Before pursuing the limitations of this tradition, let us look at what has been achieved.

One of the most widely known programs of the kind described here was Winograd's SHRDLU (Understanding Natural Language, 1972). The program carried on a dialog with a person (via teletype) concerning the activity of a simulated robot arm in a tabletop world of toy objects (often referred to as the 'blocks world'). The program could answer questions, carry out commands, and incorporate new facts about its world. It displayed the simulated world on a video screen, showing the activities it carried out as it moved the objects around. The following dialog³ illustrates some of its abilities (lines in lower case are typed by the person, those in upper case by the computer):

pick up a big red block.

OK.

grasp the pyramid.

I DON'T UNDERSTAND WHICH PYRAMID YOU MEAN.

find a block which is taller than the one you are holding and put it into the box.

OK

what does the box contain?

THE BLUE PYRAMID AND THE BLUE BLOCK.

what is the pyramid supported by? THE BOX.

how many blocks are not in the box?

FOUR OF THEM.

is at least one of them narrower than the one which I told you to pick up?

YES, THE RED CUBE.

is it supported?

YES, BY THE TABLE.

can the table pick up blocks?

NO.

had you touched any pyramid before you put the green one on the little cube?

YES, THE GREEN ONE.

when did you pick it up?

WHILE I WAS STACKING UP THE RED CUBE, A LARGE RED BLOCK AND A LARGE GREEN CUBE.

why?

TO GET RID OF IT.

In addition to giving responses that call for reasoning about the domain (the world of toy blocks), the system draws conclusions about the structure of the conversation and about the hypothesized knowledge of the other participant. In order to analyze a phrase like "the pyramid," context must be considered. The command "Grasp the pyramid" near the beginning of the dialog is underspecified since there are several pyramids in the robot's world. But the later question "What is the pyramid supported by?" is understood as referring to the specific pyramid mentioned in a previous response. By keeping a record of the conversation, SHRDLU could often determine the referent of a phrase. It also kept track of part of the knowledge implicit in the person's utterances, for example the fact that a particular block was referred to using its color. It could then use this to help in choosing among alternative interpretations. For example, if a block had been referred to by the person as "the green block," it would not be considered as a likely referent for "it" in a subsequent question What color is it?

In SHRDLU, this reasoning about the conversation did not make use of the same representation formalism as for the blocks world itself, but was done in an ad hoc style. Nevertheless, in essence it was no different from any other reasoning process carried out on representation structures. Later programs have refined and extended the approach, within the same theoretical background.

## 9.2 The problem of background

The rationalistic approach to meaning that underlies systems like SHRDLU is founded on the assumption that the meanings of words and of the sentences and phrases made up of them can be characterized independently of the interpretation given by individuals in a situation. There are, of course, aspects of meaning that call for qualifying this assumption. A sentence may include indexicals (words like "I," "you," and "now") whose referents are elements of the conversation situation, or may have connotative effects (as in the impact of a poetic metaphor) that depend on the full understanding and empathy of the hearer. But these are seen as add-ons to a central core of meaning that is context-independent. Even those who are critical of artificial intelligence are prone to accept this separation of the 'literal meaning' from other linguistic effects. Weizenbaum, for instance, argues against the possibility of computer understanding in this way:

It may be possible... to construct a conceptual structure that corresponds to the meaning of the sentence, "Will you come to dinner with me this evening?" But it is hard to see... how [such] schemes could possibly understand that same sentence to mean a shy young man's desperate longing for love. Weizenbaum, Computer Power and Human Reason (1976), p. 200.

In his review of Weizenbaum's book, McCarthy responds by pointing out that there are different kinds of understanding and by suggesting that we might expect a computer to understand literal meaning even if it were not open to the connotations and emotional subtleties of full meaning:

This good example raises interesting issues and seems to call for some distinctions. Full understanding of the sentence indeed results in knowing about the young man's desire for love, but it would seem that there is a useful lesser level of understanding in which the machine would know only that he would like her to come to dinner. — McCarthy, "An unreasonable book" (1976), p. 86.

But as we saw in Chapters 3 and 5, the concept of literal meaning is inadequate even in dealing with the most mundane examples. The phenomena of background and interpretation pervade our everyday life. Meaning always derives from an interpretation that is rooted in a situation:

relativity to situation and opportunity constitutes the very essence of speaking. For no statement simply has an unambiguous meaning based on its linguistic and logical construction, as such, but on the contrary, each is motivated. A question is behind each statement that first gives it its meaning. Gadamer, Philosophical Hermeneutics (1976), pp. 88-89.

Gadamer, Heidegger, Habermas, and others argue that the goal of reducing even 'literal' meanings to truth conditions is ultimately impossible, and inevitably misleading. It focusses attention on those aspects of language (such as the statement of mathematical truths) that are secondary and derivative, while ignoring the central problems of meaning and communication. When we squeeze out the role of interpretation, we are left not with the essence of meaning, but with the shell. Chapter 5 showed how the meaning of a concrete term like "water" could be understood only relative to purpose and background. Looking at computer programs, we see this kind of problem lurking at every turn. In order for a computer system to draw conclusions from the use of a word or combination of words, meaning must be identified with a finite collection of logical predicates (its truth conditions) or procedures to be applied. Complications arise even in apparently simple cases.

In classical discussions of semantics, the word "bachelor" has been put forth as a word that can be clearly defined in more elementary terms: "adult human male who has never been married."4 But when someone refers to a person as a "bachelor" in an ordinary conversational situation, much more (and less) is conveyed. "Bachelor" is inappropriate if used in describing the Pope or a member of a monogamous homosexual couple, and might well be used in describing an independent career woman. The problem is not that the definition of bachelor is complex and involves more terms than accounted for in the classical definition. There is no coherent 'checklist' of any length such that objects meeting all of its conditions will consistently be called "bachelors" and those failing one or more of them will not.5 The question "Is X a bachelor?" cannot be answered without considering the potential answers to "Why do you want to know?" This is what Gadamer means by "A question is behind each statement that first gives it its meaning." It is possible to create artificial 'stipulative definitions,' as in a mathematics text or in establishing the use of terms in legal documents, but these do not account for the normal use of language.

When we leave philosophical examples and lok at the words appearing in everyday language, the problem becomes even more obvious. Each of the nouns in the sentence "The regime's corruption provoked a crisis of confidence in government" raises a significant problem for definition. It is clear that purpose and context play a major role in determining what will be called a "crisis," "corruption," or a "regime.

Other problems arise in trying to deal with words such as "the" and "and," which seem the closest to logical operators. In SHRDLU, as described above, the program for determining the referent of a definite noun phrase such as "the block" made use of a list of previously mentioned objects. The most recently mentioned thing fitting the description was assumed to be the referent. But this is only a rough approximation. Sometimes it gives a wrong answer, and other times it gives no clue at all. Consider the text: "Tommy had just been given a new set of blocks. He was opening the box when he saw Jimmy coming in."

There is no mention of what is in the box—no clue as to what box it is at all. But a person reading the text makes the immediate assumption that it is the box which contains the set of blocks. We can do this because we know that new items often come in boxes, and that opening the box is a usual thing to do. Most important, we assume that we are receiving a connected message. There is no reason why the box has to be connected with the blocks, but if it weren't, it couldn't be mentioned without further introduction. - Winograd, "When will computers understand people?" (1974), p. 75.

The problem, then, is to account for how the background of knowledge and expectations leads to interpretation. In building artificial intelligence systems, this has led to the addition of 'internal' aspects to the representation. In addition to reasoning about the subject matter, the program attempts to model those aspects of the speaker's and hearer's internal thought processes that are relevant to interpretation. There has been a good deal of work along these lines6 which rests on an extended version of the basic model and a corresponding extension of the assumptions given above:

1. There is a systematic way of correlating sentences in natural language with structures in the representation system.

2. The correlation can be analyzed in terms of:

(a) Fixed basic meanings of the smallest elements (words or morphemes).

) Rules for the composition of these into the meanings of phrases and sentences, where these rules can take into account specific properties of the current state of speaker and hearer (including memory of the preceding text).

3. There is a fixed set of relevant properties that constitute the psychological state of a language user, and there is a well-defined set of rules that describe how this state is modified by any utterance.

The extension allows considerations such as recency, focus, and hearer's knowledge to contribute to the analysis of the meaning of an utterance. The third assumption is necessary or the second becomes vacuous. If we cannot specify the relevant properties and the laws that govern them, then we cannot have a rigorous account of meaning.

Philosophers have generally avoided making this kind of extension because of the diffculty of producing a clear account of psychological state as it relates to language.7 Workers in artificial intelligence, on the other hand, adopt a pragmatic approach with casual introspection as a guide to devising models that seem potentially useful. Objects and properties get added to the representation of the state of the speaker/hearer because the programmer feels they will be relevant. They are kept because with them the system is perceived as in some way performing better than it did without them.

There have been many clever ideas for what should be included in the model of the speaker/hearer and how some of it might be organized, but the overall feeling is of undirected and untested speculation. Experimental psychology provides some suggestive concepts, but little else of direct use. A language comprehension system depends on models of memory, attention, and inference, all dealing with meaningful material, not the well-controlled stimuli of the typical laboratory experiment. Research in cognitive psychology has focussed on tasks that do not generalize to these more complex activities. In fact, much current psychological investigation of how people deal with meaningful material has been guided by research on artificial intelligence rather than the other way around.

## 9.3 Understanding as pattern recognition

The artifcial intelligence literature of the 1970s heralded a move away from the traditional problem-solving orientation towards a new one centered around 'frames' or 'expectations.' Programs based on 'beta structures' (Moore and Newell, 1973), 'frames' (Minsky, 1975), 'scripts' (Schank and Abelson, 1977), 'schemas' (Bobrow and Norman, 1975), and 'prototypes' and 'perspectives' (Bobrow and Winograd, 1977) all deal with how a previously existing structure guides the interpretation of new inputs. The emphasis is on recognition rather than problem solving. It has been claimed that these systems avoid the limitations of earlier approaches to representation and that they support 'non-logical' kinds of reasoning that more closely approximate human intelligence. We will examine these claims in light of our discussion of background.

The overall idea is summarized by Minsky:

Here is the essence of the theory: When one encounters a new situation (or makes a substantial change in one's view of the present problem) one selects from memory a substantial structure called a frame. This is a remembered framework to be adapted to fit reality by changing details as necessary.... Once a frame is proposed to represent a situation, a matching process tries to assign values to the terminals [the detailed features] of each frame, consistent with the markers at each place.... Most of the phenomenological power of the theory hinges on the inclusion of expectations and other kinds of presumptions. A frame's terminals are normally already filled with default assignments. Thus, a frame may contain a great many details whose supposition is not specifically warranted by the situation. These have many uses in representing general information, most-likely cases, techniques for 'bypassing logic' and ways to make useful generalizations. - Minsky, "A framework for representing knowledge" (1975), pp. 212-213.

Minsky's standard example is a frame for the visual appearance of a room. Once we have decided (perhaps on the basis of seeing a doorway) that we are looking at a room, our interpretation of the rest of the scene is biased by assumptions that certain other elements (such as windows) are present. Similar assumptions also apply to the understanding of a sentence, in which previous expectations are matched against the contents. In applying the frame idea to the meaning of words in a natural language, we associate a frame-like 'prototype' with each word. This prototype, like a definition, includes a description of the objects to which the word applies. Unlike a definition, however, this further description is not taken to be sufficient or necessary for determining the applicability of the word. It can include things that are typical (but not always the case) or that are relevant only in some contexts. In deciding whether a word applies to a representation of an object, the reasoning system compares these further descriptions to what is known about the object. In doing so it can preferentially deal with only some of the description, choosing what to do on the basis of context.

It would seem that a process of this type has the potential to treat word meanings in the open-ended way discussed for the "bachelor" example above. Although the "bachelor" prototype includes further descriptions (typical life style, age, etc.), the process of checking is context-dependent. One can devise strategies for deciding which of these to examine, depending on some characterization of context and current purposes.

In addition to using expectations about typical properties, frame systems have also been portrayed as a way to reason and understand by analogy.

One thing that people remember is a particular experience, often in some detail. So, we postulate a level of memory that contains specific remembrances of particular situations.... Understanding is finding the closest higher-level structure available to explain an input and creating a new memory node for that input that is in terms of the old node's closely related higher-level structure. Understanding is a process that has its basis in memory, particularly memory for closely related experiences accessible through reminding and expressible through analogy. — Schank, "Language and memory" (1981), pp. 121, 129.

In a way, frame-based computational systems approach meaning from a hermeneutic direction. They concentrate not on the question "How does the program come to accurately reflect the situation?" but rather "How does the system's preknowledge (collection of frames) affect its interpretation of the situation?" The meaning of a sentence or scene lies in the interaction between its structure and the pre-existing structures in the machine.

The widespread enthusiasm about frames was a response to a shared but unarticulated awareness of the inadequacies of the problem-solving approach. But the solution did not solve the problems. Let us once again consider the task of a programmer trying to create an intelligent program, this time using frames. First there is the characterization of the task environment. This is essentially the same. It is still necessary to distinguish the relevant objects and properties before doing any representation.

The difference comes in the second step—in designing the formal system used to represent the situation. In more traditional programs, whether or not they explicitly use formal logic, there is an assumption that formulas represent propositions of the kind traditionally assigned truth values, such as "Every dog is an animal." A major goal of frame formalisms was to represent 'defaults': the ways things are typically, but not always. For example we might want  iclude the act Ds bark" wihout precd the possibility of a mute dog.

The frame intuition can be implemented only in a system that does informal reasoning-one that comes to conclusions based on partial evidence, makes assumptions about what is relevant and what is to be expected in typical cases, and leaves open the possibility of mistake and contradiction. It can be 'non-monotonic'—it can draw some conclusion, then reverse it on the basis of further information.8

The problem, of course, is to know when something is to be treated as 'typical' and when the various parts of the frame are to be taken as relevant. Here, if we look at the literature on frame systems, we find a mixture of hand waving and silence. Simple rules don't work. If, for example, defaults are used precisely when there is no explicit (previously derived) information to the contrary, then we will assume that one holds even when a straightforward simple deduction might contradict it. If analogies are treated too simply, we attempt to carry over the detailed properties of one object to another for which they are not appropriate.

It should be clear that the answer cannot lie in extending the details of the rules within the subject domain. If the default that rooms have windows is to be applied precisely in the cases of "those rooms that. . . and not those that..." then it is no longer a default. We have simply refined our description of the world to distinguish among more properties that rooms can have.

Another approach has been to postulate 'resource-limited processing' as a basis for reasoning.9 In any act of interpretation or reasoning, a system (biological or computer) has a finite quantity of processing resources to expend. The nature of these resources will be affected by the details of the processor, its environment, and its previous history. The outcome of the process is determined by the interaction between the structure of the task and the allocation of processing. The ability to deal with partial or imprecise information comes from the ability to do a finite amount of processing, then jump to a conclusion on the basis of what has happened so far, even though that conclusion may not be deducible or even true.

This is what Minsky refers to when he talks of the need to "bypass logic."

From one point of view, a resource-limited system is a purely logical formal system—it operates with precise rules on well-defined structures, as does any computer program. From another viewpoint the system is carrying out informal reasoning. The key to this paradox lies in the use of formal rules that are relative to the structure of the computer system that embodies the formalism.10 In reasoning about some task environment, a frame-based system can come to conclusions on the basis not only of statements about the world, but also on the basis of the form of the representation and the processes that manipulate it (for example, concluding something is false because it is represented as typically false, and with some bounded amount of deduction in this case it cannot be proved true).

Once again, the intuition is related to the work we have been presenting. Maturana's account of structure-determined systems deals directly with how the system's structure (rather than an externally observed structure of the environment) determines its space of operation. However, there is a significant difference in that the frame approach assumes a mechanism operating on representations, albeit in a resource-limited way.

Although the general idea of frames with resource-limited reasoning has some plausibility, it has not produced computer systems with any degree of generality. The problem lies in accounting for how the detailed structure of the system leads to the desired results. Only very simplistic examples have been given of what this structure might look like, and those examples cannot be extended in any obvious way. Programs actually written using frame systems tend to fall into two classes. Either the structures are written with a few specific examples in mind and work well only for those examples and minor variations on them,11 or they do not make any essential use of the frame ideas (adopting only a frame-like notation) and are equivalent to more traditional programs.12

Furthermore, even if a system containing frames with an appropriate structure could be constructed, it still does not escape the problems of blindness described in Chapter 8. The programmer is responsible for a characterization of the objects and properties to be dealt with using frames, to exactly the same degree as the programmer of any representation system. The program begins with a characterization of the possible objects and properties. Detailed consideration of its internal structure (both of representations and of processes on them) cannot move beyond this initial articulation. No amount of non-monotonic resource-limited processing in this domain can lead to giving the program a background in the sense of pre-understanding emphasized by Heidegger or the structural coupling described by Maturana.

## 9.4 What does it mean to understand?

In light of this critique, we may be puzzled when Newsweek reports that "Computers can. . . draw analogies among Shakespearean plays and understand tales involving friendship and adultery"13 and Schank and Riesbeck state that their program SAM "was a major advance. .. because its use of pt allowt onderstand rel storis.Arethese caims tr ffalse?

To answer this last question in its own terms would violate our theory of language. If objective truth conditions cannot be defined for "water," how could they possibly be found for "understand"? We need instead to analyze the web of commitments into which we have entered when we seriously utter a sentence of the form "X understands Y." We will begin by illustrating some simple 'language understanding' programs as a basis for comparison.

Program 1 prints out the time of day whenever the precise sequence What time is it?" is typed in. Any other sequence is simply ignored. Such a program might well operate to the satisfaction of those who use it, and they might want to claim that it "understands the question," since it responds appropriately.

Program 2 accepts sequences of the form "What ... is it?" where the ga i flle y e," y,"t,"year. It ty u appropriate answer to each of these and ignores any sequence not matching this pattern.

Program 3 has a collection of patterns that are matched against the input. For each of these there is a corresponding form to be printed out, where that printout may include fragments of the pattern that was entered. The program finds a pattern that matches the input and prints out the associated response. For example if it is provided with the pattern "My name is ..." and corresponding response "Hello, ..., how are you today?" it would respond to the input "My name is Joseph" with "Hello, Joseph, how are you today?"

Those familiar with artificial intelligence will recognize program 3 as ELIZA.15 This program was run (under the name DOCTOR) with a collection o patterns that simulated a non-directive psychiatrist interviewing a patient. For example, it responded to "I am ..." with "How long have you been .. ?" Given "I hope ..." it responded "What would it mean to you if .?" and given ... everybody ..." it responded "Are you thinking of somebody in particular?"

The behavior of the DOCTOR program was strikingly human-like. Weizenbaum reported:

I was startled to see how quickly and how very deeply people conversing with DOCTOR became emotionally involved with the computer and how unequivocally they anthropomorphized it.... Another widespread, and to me surprising, reaction to the ELIZA program was the spread of a belief that it demonstrated a general solution to the problem of computer understanding of natural language. — Weizenbaum, Computer Power and Human Reason (1976), p. 6.

Program 4 has a collection of 'scripts,' each corresponding to a particular kind of event sequence. For example, it might have a script for what happens when a person goes to a restaurant: "The person enters, is seated by a host, is brought a menu by a waiter, orders some food, is brought the food by the waiter, eats the food, is brought a check by the waiter, pays the check, and leaves." When an input is entered that matches the title'of the script (ie., it mentions going to a restaurant), the program then compares each subsequent input with one of the event patterns in the script and fills in values based on the input (as ELIZA filled in the ".." in the examples above). If the input does not match the next event in line, it skips over that event and compares it to the next. Once the input is complete, the program can use the values filled in from the inputs to answer simple questions. For example, given the sequence of inputs "John went to a restaurant. John ate a hamburger," it can use the script to answer the question "What did John order?" with "a hamburger."

Again, this is a description (slightly simplified but not in any essential way) of an existing program-the SAM program that Schank and Riesbeck described as "understanding real stories." It has served as a model for a series of more elaborate programs done by Schank and his group, as described in Schank and Riesbeck, Inside Computer Understanding (1981).

With these examples in mind, let us return to the question of what it would mean for a computer to understand language. We might say that the computer understands when it responds appropriately. The obvious problem lies in determining what constitutes an appropriate response. In one sense, the simple clock program always responds appropriately. Asked What time is it?" it types out the time. But of course we could equally well have designed it to respond with the time when we type in "Why is the sky blue?" or simply "?" The appropriateness of the response is relative to a background of other things that might be said. In the case of the timekeeper (or the more elaborate program 2 that allows some variability in the patterns) this range is too limited to warrant being called understanding.

But as we move up in complexity to ELIZA and SAM, the essential issue doesn't change. The range of patterns grows larger and, as Weizenbaum reports, it may be difficult for a person to recognize the program's limitations. Nonetheless, the program responds on the basis of a fixed set of patterns provided by a programmer who anticipated certain inputs. This anticipation may be clever (as in the DOCTOR's response to sentences mentioning "everybody"), but it still represents a permanent structure of blindness. This limitation is not one of insufficient deductive power. It applies equally to programs like SHRDLU that include routines for reasoning with representations, and holds as well for systems with 'frame-like' reasoning. It lies in the nature of the process by which representations are fixed in a computer program.

It is important to recognize that this limitation is not dependent on the apparent breadth of subject. SHRDLU operates in a microworld in which the set of objects, properties, and relations are fixed and limited in an obvious way. The DOCTOR apparently deals with all aspects of human life, but it is really working with an even more limited set of objects and properties, as specified in its patterns. Given the sentence "I am swallowing poison," it will respond "How long have you been swallowing poison?" rather than responding as a person would to implications that were not anticipated in creating the pattern.

The claim that computers "understand tales involving friendship and adultery" was based on a program called BORIS,16 a more elaborate version of SAM. Instead of dealing with "John went to a restaurant. He ate a hamburger," BORIS works on stories containing sentences like "When Paul walked into the bedroom and found Sarah with another man, he nearly had a heart attack. Then he realized what a blessing it was." It responds to questions like "What happened to Paul at home?" and "How did Paul feel?" with "Paul caught Sarah committing adultery" and "Paul was surprised."

If we examine the workings of BORIS we find a menagerie of scriptlike representations (called MOPS, TOPS, TAUS, and META-MOPS) that were used in preparing the system for the one specific story it could answer questions about. For example, TAU-RED-HANDED is activated "when a goal to violate a norm, which requires secrecy for its success, fails during plan execution due to a witnessing." It characterizes the feeling of the witness as "surprised." In order to apply this to the specific story, there are MOPS such as M-SEX (which is applied whenever two people are in a bedroom together) and M-ADULTERY (which includes the structure needed to match the requirements of TAU-RED-HANDED). The apparent human breadth of the program is like that of ELIZA. A rule that "If two people are in a bedroom together, infer they are having sex" is as much a micro-world inference as "If one block is directly above another, infer that the the lower one supports the upper." The illusions described by Weizenbaum are fueled by subject matter that makes it appear that complex and subtle understanding is taking place.

In a similar vein, the program that can "draw analogies among Shakespearean plays" operates in a micro-world that the programmer fashioned after his reading of Shakespeare.17 The actual input is not a Shakespeare play, or even a formal representation of the lines spoken by the characters, but a structure containing a few objects and relations based on the plot. The complete representation of Macbeth used for drawing analogies consisted of the following:

{Macbeth is a noble} before {Macbeth is a king}.

Macbeth marry Lady-Macbeth.

Lady-Macbeth is a woman-has-property greedy ambitious.

Duncan is a king.

Macduff is a noble-has-property loyal angry.

Weird-sisters is a hag group—has-property old ugly weirdnumber 3.

Weird-sisters predict {Macbeth murder Duncan}.

Macbeth desire {Macbeth kind-of king}

[cause {Macbeth murder Duncan}].

Lady-Macbeth persuade {Macbeth murder Duncan}.

Macbeth murder Duncan {coagent Lady-Macbeth-

instrument knife}.

Lady-Macbeth kill Lady-Macbeth.

Macbeth murder Duncan [cause{Macduff kill Macbeth}].

The program includes simple rules like "whenever a person persuades another to do an action, the action is caused by the persuasion and the persuaded person has 'control' of the action." As with all of the examples so far, the program's claim to understanding is based on the fact that the linguistic and experiential domains the programmer is trying to represent are complex and call for a broad range of human understanding. As with the other examples, however, the program actually operates within a narrowed micro-world that reflects the blindness of that representation.

But, one might argue, aren't people subject to this blindness too? If we don't want to describe these programs as 'understanding language,' how can we coherently ascribe understanding to anyone? To answer this we must return to the theory of language presented in Chapter 5. We argued there that the essence of language as a human activity lies not in its ability to reflect the world, but in its characteristic of creating commitment. When we say that a person understands something, we imply that he or she has entered into the commitment implied by that understanding. But how can a computer enter into a commitment?

As we pointed out in Chapter 8, the use of mental terms like "understand" presupposes an orientation towards an autonomous agent. In spite of this, it is often convenient to use mental terms for animals and machines. It seems natural to say "This program only understands commands asking for the time and date" and to find this way of talking effective in explaining behavior. In this case, "understand a command" means to perform those operations that someone intends to invoke in giving the command. But the computer is not committed to behaving in this way—it is committed to nothing. I do not attribute to it the kind of responsibility that I would to a person who obeyed (or failed to obey) the same words.

Of course there is a commitment, but it is that of the programmer, not the program. If I write something and mail it to you, you are not tempted to see the paper as exhibiting language behavior. It is a medium through which you and I interact. If I write a complex computer program that responds to things you type, the situation is still the same—the program is still a medium through which my commitments to you are conveyed. This intermediation is not trivial, and in Chapter 12 we will describe the roles that computers can play as an 'active structured communication medium.' Nonetheless, it must be stressed that we are engaging in a particularly dangerous form of blindness if we see the computer—rather than the people who program it-as doing the understanding.

This applies equally to systems like TEIRESIAS18 that can respond to queries about the details of the representation itself and the way it has been used in a particular calculation. The 'meta-knowledge' programmed into such a system is a representation of exactly the kind we have been talking about throughout this book. It may play a useful role in the operation of the program, but it reflects a pre-determined choice of objects, properties, and relations and is limited in its description of the program in the same way the program is limited in its description of a domain. Hofstadter argues in Gödel, Escher, Bach (1979) that these limitations might not apply to a system that allows multiple levels of such knowledge, including 'strange loops' in which a level of description applies to itself. However, he admits that this is an unsupported intuition, and is not able to offer explanations of just why we should expect such systems to be really different.

As we have pointed out in earlier chapters, a person is not permanently trapped in the same kind of blindness. We have the potential to respond to breakdown with a shift of domains in which we enter into new commitments. Understanding is not a fixed relationship between a representation and the things represented, but is a commitment to carry out a dialog within the full horizons of both speaker and hearer in a way that permits new distinctions to emerge.

What does all this mean about practical applications of language processing on computers? Our critique is not a condemnation of the technical work that has been done or even of the specific techniques (representations, deductive logic, frames, meta-description, etc.) that have been developed. It challenges the common understanding of how these techniques are related to the human use of language. Chapter 10 describes some practical applications of computer programs in which linguistic structures (e.g., English words and syntax) provide a useful medium for building or accessing formal representations. The deductive techniques developed in artificial intelligence (including the frame-like reasoning discussed in this chapter) may serve well in producing useful responses by such programs.

What is important is that people using the system recognize (as those duped by ELIZA did not) two critical things. First, they are using the structures of their natural language to interact with a system that does not understand the language but is able to manipulate some of those structures. Second, the responses reflect a particular representation that was created by some person or group of people, and embodies a blindness of which even the builders cannot be fully aware.
