> 来源：Analysing Design Activity -- edited by Nigel Cross, Henri Christiaans, Kees Dorst -- Chichester, New York, England, 1996 -- John Wiley  Sons, -- isbn13 9780471960607 -- 8e770c44116b8564e0def685642b1a
> 原始文件：C:\Users\lenovo\Documents\Codex\2026-05-29\书籍专著\Analysing Design Activity -- edited by Nigel Cross, Henri Christiaans, Kees Dorst -- Chichester, New York, England, 1996 -- John Wiley  Sons, -- isbn13 9780471960607 -- 8e770c44116b8564e0def685642b1a.md
> 识别方式：强章节标记

## 3 Analysis Procedure

The flow chart in Figure 7.2 lays out the different steps in the analysis procedure. The objective of the analysis was to reduce the audio and video data collected in the experiment into a form where the information handling behaviour could be quantitatively observed. We received the data after the completion of steps 1-3. This data were then segmented into information fragments and classified in the information framework described above.

The purpose of segmentation was to reduce the data into smaller chunks which would be easier to handle and could be analysed from an informational perspective. The challenge in segmenting is in objectively identifying the transitions in the protocol.Some transition points are easier to spot than others. We developed rules and guidelines for segmentation as we went along so as to maintain consistency in identifying the transition points. Typical points of transition were when there is a noticeable change in the designer's train of thought, or the designer changes his attention from one concept to another, or pauses in the protocol, or change in the informational activity, or utterance of certain phrases by the designer (such as 'and', 'OK', 'alright', 'emm'). Each segment is called an information fragment.

Table 7. Framework for informational activity classification
<table><tr><td>Information activity</td><td>Descriptor</td><td>Subject class</td><td>Medium</td><td>Level of abstraction</td><td>Level of detail</td></tr><tr><td>Generate Access Analyse</td><td>Alternative Assumption Comparison Construction Location Operation Performance Rationale Relation</td><td>Assembly Component Connection Feature/ Attribute Recruitment Design-concept Other</td><td>Text Graphic Audio Video LIst Simulation Gesture</td><td>Unlabelled Labelled Associative Qualitative Quantitative</td><td>Conceptual Configurational Detail</td></tr></table>

![](../../images/10e41892caa7cd8552f920f41fc5672de523ad25bf51df057bb0f633fa117b8f.jpg)

The next stage in the analysis is to classify each of the information fragments using the template shown in Figure 7.1. This was a very time consuming process as will be evident from the example in the next section. This also required some amount of training before we were consistent in our interpretation of the fragment. The next section shows the analysis of about one minute of the protocol data.

Here is an example of segmentation and classification from about one minute of verbal protocol data. The data are shown in three different stages: after transcription, after segmentation and after classification.

## After transcription:

OK I have spent er fortyfive minutes or so now forty minutes doing that er so em ... (mutter) going to check every possible location here

00:56:56:20

alright so we do have one that comes up front em really a little bit wary about backpacks on em fronts of bikes em let's see if we can em and there is that issue of it being off the side . . . you know from the aesthetics standpoint everybody likes things symmetric and er this is not that big a pack em my initial tests indicated I probably couldn't have one right like that certainly I would not do it this way I would do it that way em in fact I would em maybe do it this way

em . .. and em er so we have that as an option here em there would be a standard carrier

alright so we do have one that comes up front 00:56:59:24

em really a little bit wary about backpacks on em fronts of bikes   
em   
00:57:10:06 let's see if we can em and there is that issue of it being off the side...   
00:57:23:26   
you know from the aesthetics standpoint everybody likes   
things symmetric   
00:57:30:05

and er this is not that big a pack 00:57:36:00

em my initial tests indicated I probably couldn't have oneriht   
like that [horizontal on the back]   
00:57:42:14 certainly I would not do it this way [vertical in the back] I would do it that way [horizontal in the back] em in fact I would em maybe do it this way [horizontal in the back with opening on the outside]   
00:57:51:24

After classification:

alright so we do have one that comes up front (info-fragment :activity ACCESS :time (00565620 00565924) :descriptor ALTERNATIVE

:subjclass DESIGN-CONCEPT   
:subjects (front-position)   
:medium VIDEO   
:levels (CONCEPTUAL LABELLED)   
:measures (1))

em really a little bit wary about backpacks on em fronts of bikes em

(info-fragment :activity ANALYSE :time (00565924 00571006) :descriptor ALTERNATIVE :subjclass DESIGN-CONCEPT :subjects (front-position) :medium AUDIO :levels (CONCEPTUAL LABELLED) :measures (1))

let's see if we can em and there ithat issue of it being off the side..

(info-fragment :activity ACCESS :time (00571006 00572326) :descriptor ALTERNATIVE :subjclass DESIGN-CONCEPT :subjects (side-position) :medium VIDEO :levels (CONCEPTUAL LABELLED) :measures (1))

you know from the aesthetics standpoint everybody likes things symmetric

(info-fragment :activity GENERATE :time (00572326 00573005) :descriptor REQUIREMENT :subjclass ASSEMBLY :subjects (symmetry-for-looks) :medium AUDIO :levels (CONCEPTUAL LABELLED) :measures (1))

and er this is not that big a pack (info-fragment :activity ACCESS :time (00573005 00573600) :descriptor CONSTRUCTION :subjclass FEATURE :subjects (size-of-pack) :medium AUDIO

em my initial tests indicated I probably couldn't have one right   
like that [horizontal on the back] (info-fragment :activity ACCESS :time (00573600 00574214) :descriptor ALTERNATIVE :subjclass DESIGN-CONCEPT :subjects (back-horizontal) :medium VIDEO :levels (CONCEPTUAL UNLABELLED) :measures (1) )

certainly I would not do it this way [vertical in the back] (info-fragment :activity ANALYZE :time (00574214 00574822) :descriptor ALTERNATIVE :subjclass DESIGN-CONCEPT :subjects (back-vertical) :medium VIDEO :levels (CONCEPTUAL UNLABELLED) :measures (1))

I would do it that way [horizontal in the back] em in fact I   
would em maybe do it this way [horizontal in the back with   
opening on the outside] (info-fragment :activity GENERATE :time (00574822 00575124) :descriptor COMPARISON :subjclass DESIGN-CONCEPT :subjects (back-horizontal back-horizontal-2) :medium VIDEO :levels (CONCEPTUAL UNLABELLED) :measures (2))
