> 来源：Analysing Design Activity -- edited by Nigel Cross, Henri Christiaans, Kees Dorst -- Chichester, New York, England, 1996 -- John Wiley  Sons, -- isbn13 9780471960607 -- 8e770c44116b8564e0def685642b1a
> 原始文件：C:\Users\lenovo\Documents\Codex\2026-05-29\书籍专著\Analysing Design Activity -- edited by Nigel Cross, Henri Christiaans, Kees Dorst -- Chichester, New York, England, 1996 -- John Wiley  Sons, -- isbn13 9780471960607 -- 8e770c44116b8564e0def685642b1a.md
> 识别方式：强章节标记

## 3 Analysis of the Protocol Data

We used the protocol data of the team design up to time 1:49. Our reason for choosing the team design is that it is relatively easy to understand because verbalization is clearer. We believe that protocol analysis on design should be done with more than two designers3.

We extract FBS elements in design processes, i.e. functions, functional modifiers, behaviours, and structures. In this design, the objects are usually recognized statically because it has few actions when it is used. Therefore we are concerned with structure instead of state to model the designed object. Extraction here is not a pure grammatical operation but a heuristic operation that depends on the contexts. We use grammatical information as hints to find these types of information (for example, verb words for functions).

In this paper we use Lisp-like forms (function-body subjective objective1 .. .) to represent functions for our convenience. For example, a function description such as 'A device can carry/ fasten a backpack to a bicycle' is represented as (carry/fasten device backpack bicycle). The criteria for extracting these types of information are as follows:

Function We regard verbs used to explain objects as a functional description. In addition, some special words like feature also indicate functions of objects. We pick up a verb with a subjective word and objective words as a function.

Functional modifier We interpret adverbial phrases related to verbs as functional modifiers. We also interpret additional conditions or additional explanations to function as modifiers.

Behaviour Behaviour appears when designers invoke simulations. The problem is that such simulation is often done by nonverbal actions. For example, designers simulate some motion by operating physical objects or by a picture, or even mentally. We try to detect their simulation by observing their actions and pictures, and represent the behaviours used in this.

Structure Since structures are what is designed, they mainly appear as noun phrases. But parts of some structures are also non-verbal, because they are expressed in figures. We gather verbal and non-verbal information to describe structures. As we restrict ourselves to symbolic representation in this analysis, we represent a structure as a set of concepts, relations among concepts, and attribute of concepts.

After the extraction of information on FBS elements, we construct descriptions of the FBS model at each step of the design process, which we call the FBS state model. An FBS state model should consist of the three elements of FBS, that is, function, behaviour, and structure. Since we focus our attention on transition of function and structure, we make state models in the following two ways.

First we model functions and functional modifiers at each step of the design process. Each time functions or functional modifiers are added or changed, we gather all functions and functional modifiers that are under consideration up to that time. A function state model or function model consists of these functions and functional modifiers. Function models are linearly ordered according to their time of designing.

![](../../images/001e8aee785d390946cb27e86fc668672b76bd715e3e9e45c61d50fbb921a88a.jpg)  
Figure 9.8 Combination of function and structure models

Second, we focus on structures and behaviours that the designers propose in design. Each time structures are added or changed, we gather descriptions of the structure under consideration up to that time, and construct a structure state model or structure model that consists of these structures. Since a new structure model may be based on earlier structure models, structure models can be partially ordered according to this relationship.

We can get an FBS state model at certain time by combining a function model and a structure model that is used at that time (see Figure 9.8).

Figure 9.9 Function and structure state models  
![](../../images/f37d53676d2cf1c71a49d17989c69ff15171d7fcc45dcd09b1d7881f82a96880.jpg)

Figure 9.9 shows examples of relations among function and structure state models. A symbol starting with f indicates a function model; a symbol starting with s indicates a structure model. An arrowed line indicates relation between structure models. We made 42 function models and 73 structure models5.

There were three main types of information for objects, before the design was made. The first one is the assignment with its specifications, each of which the designed product should satisfy. The second type is the market research and users' trials and evaluation of the prototype; these describe the criteria the product also could satisfy, but not necessarily. These two types of information are directly related to the product itself. The third type is details of environments of the product, i.e. details of the bicycle and the backpack that define the environment where the product is used.

Figure 9.10 shows the FBS model of the assignment. The righthand side gives explanations of the symbols used in figures for FBS models. In this figure, we identify three independent functions, i.e.

1. (carry/fasten device backpack bicycle)

2. (stack-away device)

3. (fold-down device)

A thin black line indicates a relationship between a function body and an objective or subjective word. Function (carry/fasten device backpack bicycle) is decomposed into these two functions:

. (attach device backpack)

. (attach device bicycle)

A thick black arrow indicates decomposition of a function. There are four functional modifiers in the FBS model of the assignment i.e.

(easy-of-use (carry/fasten device backpack bicycle))

.(a-sporty-appealing-form (carry/fasten device backpack bicycle)

.for-most-bicycles (carry/fasten device backpack bicycle)

reasonable-price-rangecarryfastendevicebackpackbicycle

of-use:

5. (easily (stack-away device))

6. (easily (fold-down device))

![](../../images/461a30c8fd0720bc3499f986538e6c6c3a88dcbdedb7d8b90342d61928759395.jpg)

In Figure 9.10, a box indicates a modifier, a faint line indicates relationship between a modifier and a function body, and a faint arrow indicates decomposition of a modifier.

This representation is good enough to understand what are the required functions of this device. However, it is too vague for design because this representation covers a huge number of candidates, i.e. a huge design space. Therefore the designers need to reduce the possible design space. To reduce the possible design space in this design session, they can consult the information from the users' trial and evaluation on the prototype design.

Figure 9.11 shows the FBS model of the assignment and users' trials and evaluation. Functions appearing in this figure are the same as those in Figure 9.10, but 13 modifiers are added to the FBS model of assignment. As we discussed in the previous section, adding modifiers is setting criteria to evaluate how functions are achieved. So these newly added modifiers are good information for designers to realize how the design space should be reduced. Since these modifiers are not mandatory, designers picked up some of them to consider in design session and they left others untouched. Modifiers marked with a ? did not appear in the design session.

Figure 9.12 shows the final FBS model in our analysis of the design session. A shaded oval box indicates a function added to the assignment FBS model. Sixteen new functions are added to the initial FBS model, i.e.

(ride person bicycle)

(steer person bicycle)

3.(pedal person bicycle)

(attach bicycle attaching-device)

5.(attach attaching-device device)

6.(put-in device backpack)

7.(be-extensible attaching-device)

8. (hold device backpack)

(lock device backpack)

10. (lock device bicycle)

11.(keep-away-straps-from-wheel device)

12.(support device backpack bicycle)

.(stand-up device bicycle)

14. (stand-up device)

15. (rack-function device)

16.(fender-function device)

![](../../images/03ed3992c40ce0dcbbd560ce180003767fecbc5a8b7908ef8e5eb53ebec6ba12.jpg)

![](../../images/5a41a77c86cf6113c2a7ee117c8bb8181ca5ea8405c540e9e42afdebbb27d856.jpg)

The first five functions are added by decomposition of functions, the next six functions are added as reinforcing functions, the next function is added by causal simulation, and the last four functions are added independently from the other functions.

This does not mean that all those functions have to be satisfied, but they are potential functions that the device may have. For example, the design solution at 1:49 will not satisfy (put-in device backpack) (stand-up device bicycle) (stand-up device) (fender-function device) functions. But the 'tray, net, and drawstring' design that is one of the abandoned design solutions would satisfy the function (put-in device backpack).

Thirty-three modifiers are added to the assignment FBS model. Since nine modifiers appear in the Users' Trial FBS model among these modifiers, 24 modifiers are newly found in the design session. In Figure 9.12, a shaded rectangular box indicates a new modifier.

We focus our attention on function (attach device bicycle) here to see how functional representation is changed in the design process. Function (attach device bicycle) finally has two decomposed functions and three reinforcing functions. For example, a reinforcing function (be-extensible device) is suggested as a realization of modifier (adjustable for various bikes). There are no modifiers for (attach device bicycle) in the Assignment FBS model. The modifiers for (attach device bicycle) in the Users' Trial FBS model are:

1. easily

2. centre-of-gravity-is-low

3. stably

4permanent-fixing-point-is-eyesore

Modifiers for (attach device bicycle) in the final FBS model are as follows:

1. easily

centre-of-gravity-is-low

3. stably

4.adjustable-for-most-bikes

5. reduce-the-number-of-parts

6.good-side-balance

7. not-heary-to-steer

8not-too-low-to-fit-things

9.not-too-difficult-to-pedal

The first three modifiers are inherited from the Users' Trial FBS model, and the other six modifiers are new ones. Two of them are added by modifier decomposition: (adjustable-for-most-bikes(attach device bicycle)) is modifier decomposition from (for-most-bikes (carry/fasten device backpack bicycle)) by function decomposition; (reduce-the-number-of-parts (attach device bicycle)) is modifier decomposition from (reasonable-price-range (carry/fasten device backpack bicycle)) by function decomposition. Others are found in the construction and evaluation of new structures. Thus, the function attach is developed into a functional structure that consists of six functions and nine modifiers.

In this section, we investigate how each function or functional modifier is developed in the design process. Table 9.1 shows number of appearances of each evolution type.

A new function can be added in the following four ways.

Adding functions by structures A new function is added by examining a newly suggested structure model. This is similar to decomposing functions, but the added functions are auxiliary or unexpected functions; they are not relevant to existing functions. In the design session, we found six functions in this category. New functions can be found either by positive examples or by negative examples. The former means that the proposed structure has satisfied the designers' intention. In this case, a newly found function itself is added to the function model. The latter means that the proposed structure did not satisfy the intention. In this case, the negation of the newly found function is added to the function model.

Table 9.1 Number of appearances of evolutionary steps
<table><tr><td>Addition of function</td><td>6</td><td></td></tr><tr><td>by positive examples (FAS+) by negative examples (FAS)</td><td></td><td>5</td></tr><tr><td>by other reasons (FDX)</td><td></td><td>1 0</td></tr><tr><td></td><td></td><td></td></tr><tr><td>Addition of &#x27;decompose&#x27; relation</td><td>3</td><td></td></tr><tr><td>by positive examples (FDS+)</td><td></td><td>3</td></tr><tr><td>by negative examples (FDS)</td><td></td><td>0</td></tr><tr><td>by other reasons (FDX)</td><td></td><td>0</td></tr><tr><td>Addition of &#x27;cause&#x27; relation (FC)</td><td>1</td><td></td></tr><tr><td>Addition of &#x27;reinforced-by&#x27; relation (FR)</td><td>6</td><td></td></tr><tr><td>Addition of modifier</td><td></td><td></td></tr><tr><td>by positive examples (MAS+) by negative examples (MAS-)</td><td></td><td>N ∞ N</td></tr><tr><td>by other reasons (MAX)</td><td></td><td></td></tr><tr><td>Addition of &#x27;decompose modifiers&#x27; relation</td><td>12</td><td></td></tr><tr><td>by positive examples (MDS+)</td><td></td><td>5</td></tr><tr><td>by negative examples (MDS)</td><td></td><td>0</td></tr><tr><td>by other reasons (MDX)</td><td></td><td>7</td></tr><tr><td>Total</td><td></td><td></td></tr><tr><td></td><td>45</td><td></td></tr></table>

For example, one of the designers suggested a propylene popup-book-like design at time 1:07. The advantage of this design, he claimed, is that it would work as a mudguard (see Figure 9.13). Although he retracted this idea immediately because of strength problems, this mudguard function is used again later as the 'fender' function when they discuss the function of the vacuumedformed tray (at time 1:22). This tells that the fender-function (or mud-guard-function) is recognized as a function of the device.

Decomposing functions It is claimed that decomposition of functions is the most basic procedure for handling functions in design6. Unless the designing domain is well investigated or well known, as in routine design, it is not easy to find a decomposition of functions. Actually in this design, decomposition of function is found only three times.

For example, at time 0:56 the designers found that attaching the carrying device to the bicycle can be realized easily by attaching an attaching device to the bicycle and attaching this attaching device to the carrying device. This process is the creation of two new functions (attach bicycle attaching-device) and (attach attachingdevice device) and additions of 'decompose' relations between (attach bicycle device) and (attach bicycle attaching-device) and between (attach bicycle device) and (attach attaching-device device).

Adding 'be-caused-by' relation This is the procedure for making causal relations between functions. We see at time 1:06 that the designers discussed the strength issue of attaching the device to the bicycle. They simulated the dynamics of the bicycle with the device and the backpack in order to know how strength of parts would affect the behaviour. Using this simulation, they realized the function (support device backpack) is needed as a sub-function of function carry/fasten because behaviour support is needed for the behaviour attach to be realized. Since most behaviour is implicit or non-verbal, it is difficult to find such causal relations. We could find only one example.

![](../../images/49f640f61a62464a69f78e490658d8c0a0e47ba363f2105ceae5b8a534442732.jpg)

![](../../images/a6ebb636434070f4abc8470ff7b85517a0d0bd13aacf00303ae877a0b94b2b81.jpg)

Adding 'be-reinforced-by' relation The Assignment model and the Users' Trial model have relatively few functions and many modifiers. This implies that interpretation of those modifiers plays an important role in this design. In our model, converting modifiers into functions is achieved by adding be-reinforced-by' relations. A reinforcing function is found by evaluating the functionality of the proposed structure with the modifier.

For example, at time 01:30 the designers try to satisfy modifier safe-from-theft (this modifier is already suggested at time 00:38). In order to realize modifier (safe-from-theft (fasten/carry device backpack)), the designers decomposed it into (safe-from-theft (attach device backpack)). Then they suggested that function lock performed by lockable-knob is a realization of this modifier. This function lock is a reinforcing function of the function attach (see Figure 9.14). We could find six examples for this reinforcing evolution.

As mentioned above, there are relatively few functions and many modifiers in this design. It means that operating modifiers is an important process for evolving function models. Adding modifiers is achieved in two ways, i.e. by structures and by decomposing modifiers.

Adding modifiers by structures A typical procedure observed in the design process is adding modifiers by examining new suggested structures. We found 17 examples.

Figure 9.15 shows how addition of modifiers is achieved. First a function model and a structure model are taken as the current model of the object (Figure 9.15(a)). Comparing the function model and the structure model, the designers suggest a new structure model (Figure 9.15(b)). Behaviours are produced by simulation on this structure model, and the function model for this structure model is created (Figure 9.15(c)). If the new function model is considered to be better than the previous one, modifiers representing the difference are to be included in the descriptions of functionality. If the new function model is considered to be worse, a negation of modifiers representing the difference has to be included (Figure 9.15(d)).

Figure 9.15 Adding modifiers by res  
![](../../images/1d6c2eb5f2a05d80ca0df17c071b82ba5037236b5775e67d622bf021d43988bb.jpg)

![](../../images/50bb4e9895a60089605a62717cc1a15467f83254bf843cea456ea17d69017f35.jpg)

Around time 28:00, the designers suggested using panniers to attach the device to the bicycle (see Figure 9.16). Then they found that to attach the backpack on one side of the bike would be bad for the rider's balance. They decided that the pannier structure was not desirable because of this. In order to find the balancing problem, they might simulate the behaviour of the device with some aspect. The behaviour aspect of this state is the dynamics of riding a bicycle. The simulation of the dynamics of riding a bicycle with the device and the backpack tells them that weights of both sides would be not in balance. Then the designers decided that this is not good. At this moment, they discovered that riding a bike involves having a good side balance, i.e., they found a new specification to function ride. Thus good-side-balance is a new modifier to function ride, and is added to the functional model. The same procedure happened just after this state. They proposed a new structure, i.e. separation of the backpack, which is to satisfy good-side-balance modifier. Then they found that altering the backpack is not desirable. Thus not-alter-backpack is also added to the function model.

It is interesting that adding modifiers by a negative example appears more frequently than adding modifiers by a positive example. It suggests that contradiction or inconsistency are important for design (we discussed and modelled use of inconsistency in design elsewhere ).

Decomposition of modifiers The other way to add modifiers is to decompose modifiers. We found 12 examples in this design session. Decomposition of modifiers happens along with the decomposition of functions, but to decompose modifiers needs another eort.At time 01:1, the designers suggested usinalu minium for the device. The big advantage would be the colouring possibilities. Since they thought that to-have-colours is an idea to realize a-sporty-appealing-form, to-have-colours is a decomposition of modifier a-sporty-appealing-form, and can be added to the functional model as a modifier to function carry/fasten.

In this report, we showed our primary results of a protocol analysis by our functional modelling scheme. Although it is a tentative report, we can draw some remarks from these results.

Function changing and structure changing are important for tracing design processes. We have been absorbed in structure changing when we wanted to know what happened in design processes. Functional descriptions are also changing in design processes. Both changes are important, but it is impossible to model them separately. Our approach is suitable for this purpose because function and structure are represented in a single scheme.

Functional evolution is not magic, but rational in most cases. Designers often make design criteria by themselves in order to converge their design processes. Designers seem to have such criteria a priori. But such criteria (functional modifiers in our terms) have arisen as results of the interaction between structure and function. In our scheme we can explain why they adopt new criteria.

Function modelling is also important as a result of design. Not only the designed structure but also its intended functionality are important as the result of design, because we can evaluate how well the designed structure matches the intention of the designers. The functionality they intended is not the function given by requirements, but the function model they made during the design process.

## References

1 Takeda, H., P. Veerkamp, T. Tomiyama, and H. Yoshikawa, Modeling design processes, AI Magazine, 11(4) (1990) 3748

2 Umeda, Y., H. Takeda, T. Tomiyama, and Y. Yoshikawa, Function, behaviour, and structure, in J.S. Gero (Ed.), Applications of Artificial 177-194

3 Takeda, H., S. Hamada, T. Tomiyama, and H. Yoshikawa, A cognitive approach of the analysis of design processes, in Design Theory and Methodology - DTM '90, ASME (1990), pp. 153-160

4 Forbus, K.D., Qualitative process theory, Artificial Intelligence, 24 (1984) 85168

5 FBS models in Delft protocol analysis, http://ai-www.aistnara.ac.jp/\~takeda/DPW

6 Pahl, G. and W. Beitz, Engineering Design, The Design Council, London (1984)

Takeda, H., T. Tomiyama, and H. Yoshikawa, A logical and computerable framework for reasoning in design, in D.L. Taylor and L.A. Stauffer (Eds), Design Theory and Methodology - DTM '92, ASME (1992), pp. 167174
