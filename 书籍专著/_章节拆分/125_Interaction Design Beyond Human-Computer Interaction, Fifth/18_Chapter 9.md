> 来源：Interaction Design Beyond Human-Computer Interaction, Fifth Edition (Helen Sharp, Jenny Preece, Yvonne Rogers)
> 原始文件：C:\Users\lenovo\Documents\Codex\2026-05-29\书籍专著\Interaction Design Beyond Human-Computer Interaction, Fifth Edition (Helen Sharp, Jenny Preece, Yvonne Rogers)\Interaction Design Beyond Human-Computer Interaction, Fifth Edition (Helen Sharp, Jenny Preece, Yvonne Rogers).md
> 识别方式：强章节标记

## Chapter 9

# DATA ANALYSIS, INTERPRETATION, AND PRESENTATION

9.1 Introduction

9.2 Qualitative and Quantitative

9.3 Basic Quantitative Analysis

9.4 Basic Qualitative Analysis

9.5 What Kind of Analytic Framework to Use

9.6 Tools to Support Data Analysis

9.7 Interpreting and Presenting the Findings

## Objectives

The main goals of this chapter are to accomplish the following:

Discuss the difference between qualitative and quantitative data and analysis.

Enable you to analyze data gathered from questionnaires.

Enable you to analyze data gathered from interviews.

Enable you to analyze data gathered from observation studies.

Make you aware of software packages that are available to help your analysis.

Identify some of the common pitfalls in data analysis, interpretation, and presentation.

Enable you to interpret and present your findings in a meaningful and appropriate manner.

## 9.1 Introduction

The kind of analysis that can be performed on a set of data will be influenced by the goals identified at the outset and the data gathered. Broadly speaking, a qualitative analysis approach, a quantitative analysis approach, or a combination of qualitative and quantitative approaches may be taken. The last of these is very common, as it provides a more comprehensive account of the behavior being observed or the performance being measured.

Most analysis, whether it is quantitative or qualitative, begins with the initial reactions or observations from the data. This may involve identifying patterns or calculating simple numerical values such as ratios, averages, or percentages. For all data, but especially when dealing with large volumes of data (that is, Big Data), it is useful to look over the data to check for any anomalies that might be erroneous. For example, people who are 999 years old. This process is known as data cleansing, and there are often digital tools to help with the process. This initial analysis is followed by more detailed work using structured frameworks or theories to support the investigation.

Interpretation of the findings often proceeds in parallel with analysis, but there are different ways to interpret results, and it is important to make sure that the data supports any conclusions. A common mistake is for the investigator's existing beliefs or biases to influence the interpretation of results. Imagine that an initial analysis of the data has revealed a pattern of responses to customer care questionnaires that indicates that inquiries from customers routed through the Sydney office of an organization take longer to process than those routed through the Moscow office. This result can be interpreted in many different ways. For example, the customer care operatives in Sydney are less efficient, they provide more detailed responses, the technology supporting the inquiry process in Sydney needs to be updated, customers reaching the Sydney office demand a higher level of service, and so on. Which one is correct? To determine whether any of these potential interpretations is accurate, it would be appropriate to look at other data such as customer inquiry details and maybe to interview staff.

Another common mistake is to make claims that go beyond what the data can support. This is a matter of interpretation and of presentation. Using words such as many or often or all when reporting conclusions needs to be carefully considered. An investigator needs to remain as impartial and objective as possible if the conclusions are to be trusted. Showing that the conclusions are supported by the results is an important skill to develop.

Finally, finding the best way to present findings is equally skilled, and it depends on the goals but also on the audience for whom the study was performed. For example, a formal notation may be used to report the results for the requirements activity, while a summary of problems found, supported by video clips of users experiencing those problems, may be better for presentation to the team of developers.

This chapter introduces a variety of methods, and it describes in more detail how to approach data analysis and presentation using some of the common approaches taken in interaction design.

## 9.2 Quantitative and Qualitative

Quantitative data is in the form of numbers, or data that can easily be translated into numbers. Examples are the number of years' experience the interviewees have, the number of projects a department handles at a time, or the number of minutes it takes to perform a task. Qualitative data is in the form of words and images, and it includes descriptions, quotes from interviewees, vignettes of activity, and photos. It is possible to express qualitative data in numerical form, but it is not always meaningful to do so (see

Box 9.1).

It is sometimes assumed that certain forms of data gathering can only result in quantitative data and that others can only result in qualitative data. However, this is a fallacy. All forms of data gathering discussed in the previous chapter may result in qualitative and quantitative data. For example, on a questionnaire, questions about the participant's age or number of software apps they use in a day will result in quantitative data, while any comments will result in qualitative data. In an observation, quantitative data that may be recorded includes the number of people involved in a project or how many hours someone spends sorting out a problem, while notes about feelings of frustration, or the nature of interactions between team members, are qualitative data.

Quantitative analysis uses numerical methods to ascertain the magnitude, amount, or size of something; for example, the attributes, behavior, or strength of opinion of the participants. For example, in describing a population, a quantitative analysis might conclude that the average person is 5 feet 11 inches tall, weighs 180 pounds, and is 45 years old. Qualitative analysis focuses on the nature of something and can be represented by themes, patterns, and stories. For example, in describing the same population, a qualitative analysis might conclude that the average person is tall, thin, and middle-aged.

## BOX 9.1

## Use and Abuse of Numbers

Numbers are infinitely malleable and can make a convincing argument, but it is important to justify the manipulation of quantitative data and what the implications will be. Before adding a set of numbers together, finding an average, calculating a percentage, or performing any other kind of numerical translation, consider whether the operation is meaningful in the specific context.

Qualitative data can also be turned into a set of numbers. Translating nonnumerical data into a numerical or ordered scale is appropriate at times, and this is a common approach in interaction design. However, this kind of translation also needs to be justified to ensure that it is meaningful in the given context. For example, assume you have collected a set of interviews from sales representatives about their use of a new mobile app for reporting sales queries. One way of turning this data into a numerical form would be to count the number of words uttered by each interviewee. Conclusions might then be drawn about how strongly the sales representatives feel about the app; for example, the more they had to say about the product, the stronger they felt about it. But do you think this is a wise way to analyze the data? Does it help to answer the study questions?

Other, less obvious, abuses include translating small population sizes into percentages. For example, saying that 50 percent of users take longer than 30 minutes to place an order through an e-commerce website carries a different meaning than saying that two out of four users had the same problem. It is better not to use percentages unless the number of data points is at least 10, and even then it is appropriate to use both percentages and raw numbers to make sure that the claim is not misunderstood.

It is possible to perform legitimate statistical calculations on a set of data and still present misleading results by not making the context clear or by choosing the particular calculation that gives the most favorable result (Huff, 1991). In addition, choosing and applying the best statistical test requires careful thinking (Cairns, 2019), as using an inappropriate test can unintentionally misrepresent the data.

## 9.2.1 First Steps in Analyzing Data

Having collected the data, some initial processing is normally required before data analysis can begin in earnest. For example, audio data may be transcribed by hand or by using an automated tool, such as Dragon; quantitative data, such as time taken or errors made, is usually entered into a spreadsheet, like Excel. Initial analysis steps for data typically collected through interviews, questionnaires, and observation are summarized in Table 9.1.

Table 9.1 Data gathered and typical initial processing steps for interviews, questionnaires, and observation
<table><tr><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">Usual rawdata</td><td colspan="1" rowspan="1">Examplequalitativedata</td><td colspan="1" rowspan="1">Examplequantitativedata</td><td colspan="1" rowspan="1">Initial processingsteps</td></tr><tr><td colspan="1" rowspan="1">Interviews</td><td colspan="1" rowspan="1">Audiorecordings.Interviewernotes.Videorecordings.</td><td colspan="1" rowspan="1">Responses toopen-endedquestions.Videopictures.Respondent'sopinions.</td><td colspan="1" rowspan="1">Age, job role, yearsof experience.Responses toclose-endedquestions.</td><td colspan="1" rowspan="1">Transcription ofrecordings.Expansion of notes.Entry of answers toclose-ended questionsinto a spreadsheet</td></tr><tr><td colspan="1" rowspan="1">Questionnaires</td><td colspan="1" rowspan="1">Writtenresponses.Onlinedatabase.</td><td colspan="1" rowspan="1">Responses toopen-endedquestions.Responses infurthercomments"fields.Respondent'sopinions.</td><td colspan="1" rowspan="1">Age, job role, yearsof experience.Responses toclose-endedquestions.</td><td colspan="1" rowspan="1">Clean up data.Filter into differentdata sets.Synchronizationbetween datarecordings.</td></tr><tr><td colspan="1" rowspan="1">Observation</td><td colspan="1" rowspan="1">Observer'snotes.Photographs.Audio andvideorecordings.</td><td colspan="1" rowspan="1">Records ofbehavior.Description ofa task as it isundertaken.Copies of</td><td colspan="1" rowspan="1">Demographics ofparticipants.Time spent on atask.The number ofpeople involved in</td><td colspan="1" rowspan="1">Expansion of notes.Transcription ofrecordings.</td></tr><tr><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">Data logs.Think-aloudDiaries.</td><td colspan="1" rowspan="1">informalprocedures.</td><td colspan="1" rowspan="1">an activity.How manydifferent types ofactivity areundertaken.</td><td colspan="1" rowspan="1"></td></tr></table>

## Interviews

Interviewer notes need to be written up and expanded as soon as possible after the interview has taken place so that the interviewer's memory is clear and fresh. An audio or video recording may be used to help in this process, or it may be transcribed for more detailed analysis. Transcription takes significant effort, as people talk more quickly than most people can type (or write), and the recording is not always clear. It is worth considering whether to transcribe the whole interview or just sections of it that are relevant. Deciding what is relevant, however, can be difficult. Revisiting the goals of the study to see which passages address the research questions can guide this process.

Close-ended questions are usually treated as quantitative data and analyzed using basic quantitative analysis (see Section 9.3 “Basic Quantitative Analysis”). For example, a question that asks for the respondent's age range can easily be analyzed to find out the percentage of respondents in each. More complicated statistical techniques are needed to identify relationships between responses that can be generalized, such as whether there is an interaction between the condition being tested and a demographic. For example, do people of different ages use Facebook for different lengths of time when first logging on in the morning or at night before they go to bed? Open-ended questions typically result in qualitative data that might be searched for categories or patterns of response.

## Questionnaires

Increasingly, questionnaire responses are provided using online surveys, and the data is automatically stored in a database. The data can be filtered according to respondent subpopulations (for instance, everyone under 16) or according to a particular question (for example, to understand respondents' reactions to one kind of robot personality rather than another). This allows analyses to be conducted on subsets of the data and hence to draw specific conclusions for more targeted goals. To conduct this kind of analysis requires sufficient data from a large enough sample of participants.

## Observation

Observation can result in a wide variety of data including notes, photographs, data logs, think-aloud recordings (often called protocols), video, and audio recordings. Taken together, these different types of data can provide a rich picture of the observed activity. The difficult part is working out how to combine the different sources to create a coherent narrative of what has been recorded; analytic frameworks, discussed in section 9.5, can help with this. Initial data processing includes writing up and expanding notes and transcribing elements of the audio and video recordings and the think-aloud protocols. For observation in a controlled environment, initial processing might also include synchronizing different data recordings.

Transcriptions and the observer's notes are most likely to be analyzed using qualitative approaches, while photographs provide contextual information. Data logs and some elements of the observer's notes would probably be analyzed quantitatively.

## 9.3 Basic Quantitative Analysis

Explaining statistical analysis requires a whole book on its own (for example, see Cairns, 2019). Here, we introduce two basic quantitative analysis techniques that can be used effectively in interaction design: averages and percentages. Percentages are useful for standardizing the data, particularly to compare two or more large sets of responses.

Averages and percentages are fairly well-known numerical measures. However, there are three different types of average, and using the wrong one can lead to the misinterpretation of the results. These three are: mean, median, and mode. Mean refers to the commonly understood interpretation of average; that is, add together all the figures and divide by the number of figures with which you started. Median and mode averages are less well-known but are very useful. The median is the middle value of the data when the numbers are ranked. The mode is the most commonly occurring number. For example, in a set of data (2, 3, 4, 6, 6, 7, 7, 7, 8), the median is 6 and the mode is 7, while the mean is $5 0 / 9 = 5 . 5 6$ . In this case, the difference between the different averages is not that great. However, consider the set (2, 2, 2, 2, 450). Now the median is 2, the mode is 2, and the mean is $4 5 8 / 5 = 9 1 . 6 !$

![](../../Interaction Design Beyond Human-Computer Interaction, Fifth Edition (Helen Sharp, Jenny Preece, Yvonne Rogers)/images/abd324a48135b32d0afba666274d26ddf364e02a9e17cf631038f9de795d5daa.jpg)  
Source: Mike Baldwin / Cartoon Stock

Use of simple averages can provide useful overview information, but they need to be used with caution. Evangelos Karapanos et al. (2009) go further and suggest that averaging treats diversity among participants as error and proposes the use of a multidimensional scaling approach instead.

Before any analysis can take place, the data needs to be collated into analyzable data sets. Quantitative data can usually be translated into rows and columns, where one row equals one record, such as respondent or interviewee. If these are entered into a spreadsheet such as Excel, this makes simple manipulations and data set filtering easier. Before entering data in this way, it is important to decide how to represent the different possible answers. For example, “don't know” represents a different response from no answer at all, and they need to be distinguished, for instance, with separate columns in the spreadsheet. Also, if dealing with options from a close-ended question, such as job role, there are two different possible approaches that affect the analysis. One approach is to have a column headed “Job role” and to enter the job role as it is given by the respondent or interviewee. The alternative approach is to have a column for each possible answer. The latter approach lends itself more easily to automatic summaries. Note, however, that this option will be open only if the original question was designed to collect the appropriate data (see Box 9.2).

## BOX 9.2

## How Question Design Affects Data Analysis

Different question designs affect the kinds of analyses that can be performed and the kinds of conclusions that can be drawn. To illustrate this, assume that some interviews have been conducted to evaluate a new app that lets you try on virtual clothes and see yourself in real time as a 3D holograph. This is an extension of the Memory Mirror described at http://memorymirror.com.

Assume that one of the questions asked is: “How do you feel about this new app?” Responses to this will be varied and may include that it is cool, impressive, realistic, clunky, technically complex, and so on. There are many possibilities, and the responses would need to be treated qualitatively. This means that analysis of the data must consider each individual response. If there are only 10 or so responses, then this may not be too bad, but if there are many more, it becomes harder to process the information and harder to summarize the findings. This is typical of open-ended questions; that is, answers are not likely to be homogeneous and so they will need to be treated individually. In contrast, answers to a close-ended question, which gives respondents a fixed set of alternatives from which to choose, can be treated quantitatively. So, for example, instead of asking “How do you feel about the virtual try-on holograph?” assume that you have asked “In your experience, are virtual try-on holographs realistic, clunky, or distorted?” This clearly reduces the number of options and the responses would be recorded as “realistic,” “clunky,” or “distorted.”

When entered in a spreadsheet, or a simple table, initial analysis of this data might look like the following:

<table><tr><td colspan="1" rowspan="1">Respondent R</td><td colspan="1" rowspan="1">ealistic</td><td colspan="1" rowspan="1">ClunkyD</td><td colspan="1" rowspan="1">istorted</td></tr><tr><td colspan="1" rowspan="1">A</td><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">B</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">C</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Z</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">1</td></tr><tr><td colspan="1" rowspan="1">Total</td><td colspan="1" rowspan="1">14</td><td colspan="1" rowspan="1">5</td><td colspan="1" rowspan="1">7</td></tr></table>

Based on this, we can then say that 14 out of 26 (54 percent) of the respondents think virtual try-on holographs are realistic, 5 out of 26 (19 percent) think they are clunky, and 7 out of 26 (27 percent) think they are distorted. Note also that in the table, respondents' names are replaced by letters so that they are identifiable but anonymous to any onlookers. This strategy is important for protecting participants' privacy.

Another alternative that might be used in a questionnaire is to phrase the question in terms of a Likert scale, such as the following one. This again alters the kind of data and hence the kind of conclusions that can be drawn.

Virtual try-on holographs are realistic:

strongly agree agree neither disagree strongly disagree

The data could then be analyzed using a simple spreadsheet or table:

<table><tr><td rowspan=1 colspan=1>Respondent S</td><td rowspan=1 colspan=1>trongly agree A</td><td rowspan=1 colspan=1>gree N</td><td rowspan=1 colspan=1>eitherD</td><td rowspan=1 colspan=1>isagree S</td><td rowspan=1 colspan=1>trongly disagree</td></tr><tr><td rowspan=1 colspan=1>A</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>B</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>C</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>…</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Z</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>1</td></tr><tr><td rowspan=1 colspan=1>Total</td><td rowspan=1 colspan=1>5</td><td rowspan=1 colspan=1>7</td><td rowspan=1 colspan=1>10</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>3</td></tr></table>

In this case, the kind of data being collected has changed. Based on this second set, nothing can be said about whether respondents think the virtual try-on holographs are clunky or distorted, as that question has not been asked. We can only say that, for example, 4 out of 26 (15 percent) disagreed with the statement that virtual tryon holographs are realistic, and of those, 3 (11.5 percent) strongly disagreed.

For simple collation and analysis, spreadsheet software such as Excel or Google Sheets is often used as it is commonly available, is well understood, and offers a variety of numerical manipulations and graphical representations. Basic analysis might involve finding out averages and identifying outliers, in other words, values that are significantly different from the majority, and hence not common. Producing a graphical representation provides an overall view of the data and any patterns it contains. Other tools are available for performing specific statistical tests, such as online t-tests and A/B testing tools. Data visualization tools can create more sophisticated representations of the data such as heatmaps.

For example, consider the set of data shown in Table 9.2, which was collected during an evaluation of a new photo sharing app. This data shows the users' experience of social media and the number of errors made while trying to complete a controlled task with the new app. It was captured automatically and recorded in a spreadsheet; then the totals and averages were calculated. The graphs in Figure 9.1 were generated using the spreadsheet package. They show an overall view of the data set. In particular, it is easy to see that there are no significant outliers in the error rate data.

Table 9.2 Data gathered during a study of a photo sharing app
<table><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=6>Social media use</td></tr><tr><td rowspan=1 colspan=1>User</td><td rowspan=1 colspan=1>More thanonce a day</td><td rowspan=1 colspan=1>Oncea day</td><td rowspan=1 colspan=1>Once aweek</td><td rowspan=1 colspan=1>Two or threetimes a week</td><td rowspan=1 colspan=1>Once amonth</td><td rowspan=1 colspan=1>Number oferrors made</td></tr><tr><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>4</td></tr><tr><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>2</td></tr><tr><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>1</td></tr><tr><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>0</td></tr><tr><td rowspan=1 colspan=1>5</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>2</td></tr><tr><td rowspan=1 colspan=1>6</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>3</td></tr><tr><td rowspan=1 colspan=1>7</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>2</td></tr><tr><td rowspan=1 colspan=1>8</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>0</td></tr><tr><td rowspan=1 colspan=1>9</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>3</td></tr><tr><td rowspan=1 colspan=1>10</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>2</td></tr><tr><td rowspan=1 colspan=1>11</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>1</td></tr><tr><td rowspan=1 colspan=1>12</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>2</td></tr><tr><td rowspan=1 colspan=1>13</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>4</td></tr><tr><td rowspan=1 colspan=1>14</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>2</td></tr><tr><td rowspan=1 colspan=1>15</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>1</td></tr><tr><td rowspan=1 colspan=1>16</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>1</td></tr><tr><td rowspan=1 colspan=1>17</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>0</td></tr><tr><td rowspan=1 colspan=1>18</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>0</td></tr><tr><td rowspan=1 colspan=1>Totals</td><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>7</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>30</td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>Mean</td><td rowspan=1 colspan=1>1.67</td></tr><tr><td rowspan=1 colspan=7>(to 2 decimal places)</td></tr></table>

![](../../Interaction Design Beyond Human-Computer Interaction, Fifth Edition (Helen Sharp, Jenny Preece, Yvonne Rogers)/images/0784075eb27a7b53e23660bc2413e5e36a92abdcfafcc48598e53d6ff5c2f765.jpg)

![](../../Interaction Design Beyond Human-Computer Interaction, Fifth Edition (Helen Sharp, Jenny Preece, Yvonne Rogers)/images/e618a38330deeeee001f4921c885d61726d982d9f6b9f8545eae32a3a21b0503.jpg)  
Figure 9.1 Graphical representations of the data in Table 9.2 (a) The distribution of errors made (take note of the scale used in these graphs, as seemingly large differences may be much smaller in reality). (b) The spread of social media experience within the participant group.

Adding one more user to Table 9.2 with an error rate of 9 and plotting the new data as a scatter graph (see Figure 9.2) illustrates how graphs can help to identify outliers. Outliers are usually removed from the main data set because they distort the general patterns. However, outliers may also be interesting cases to investigate further in case there are special circumstances surrounding those users and their session.

![](../../Interaction Design Beyond Human-Computer Interaction, Fifth Edition (Helen Sharp, Jenny Preece, Yvonne Rogers)/images/be825895ed158b91bedb4714682e291ef42180d3e3dad06ed497bb9bd3431bb9.jpg)  
Figure 9.2 Using a scatter diagram helps to identify outliers in your data quite quickly

These initial investigations also help to identify other areas for further investigation. For example, is there something special about users with error rate 0 or something distinctive about the performance of those who use the social media only once a month?

## ACTIVITY 9.1

The data in the following table represents the time taken for a group of users to select and buy an item from an online shopping website.

Using a spreadsheet application to which you have access, generate a bar graph and a scatter diagram to provide an overall view of the data. From this representation, make two initial observations about the data that might form the basis of further investigation.

Time to complete (mins) 15 10 12 10 14 13 11 18 14 17 20 15 18 24 12 16 18 20 26

## Comment

The bar graph and scatter diagram are shown here.

![](../../Interaction Design Beyond Human-Computer Interaction, Fifth Edition (Helen Sharp, Jenny Preece, Yvonne Rogers)/images/989b53150de48c89acc867325f8fc3b9c0f756b4efb9b7dc5e5772d9b0192a42.jpg)

![](../../Interaction Design Beyond Human-Computer Interaction, Fifth Edition (Helen Sharp, Jenny Preece, Yvonne Rogers)/images/590d641735e65bb7b9fcf18fe7f708f87fa278bd03145616691ceee43339151b.jpg)  
From these two diagrams, there are two areas for further investigation. First, the values for user N (24) and user S (26) are higher than the others and could be looked at in more detail. In addition, there appears to be a trend that the users at the beginning of the testing time (particularly users B, C, D, E, F, and G) performed faster than those toward the end of the testing time. This is not a clear-cut situation, as O also performed well, and I, L, and P were almost as fast, but there may be something about this later testing time that has affected the results, and it is worth investigating further.

It is fairly straightforward to compare two sets of results, for instance from the evaluation of two interactive products, using these kinds of graphical representations of the data. Semantic differential data can also be analyzed in this way and used to identify trends, provided that the format of the question is appropriate. For example, the following question was asked in a questionnaire to evaluate two different smartphone designs:

For each pair of adjectives, place a cross at the point between them that reflects

the extent to which you believe the adjectives describe the smartphone design.   
Please place only one cross between the marks on each line.

<table><tr><td>Annoying</td><td></td><td></td><td>Pleasing</td></tr><tr><td>Easy to use</td><td></td><td></td><td>Difficult to use</td></tr><tr><td>Value-for-money</td><td></td><td></td><td>Expensive</td></tr><tr><td>Attractive</td><td></td><td></td><td>Unattractive</td></tr><tr><td>Secure</td><td></td><td></td><td>Not secure</td></tr><tr><td>Helpful</td><td></td><td></td><td>Unhelpful</td></tr><tr><td>Hi-tech</td><td></td><td></td><td>Lo-tech</td></tr><tr><td>Robust</td><td></td><td></td><td>Fragile</td></tr><tr><td>Inefficient</td><td></td><td></td><td>Efficient</td></tr><tr><td>Modern</td><td></td><td></td><td>Dated</td></tr></table>

Table 9.3 and Table 9.4 show the tabulated results from 100 respondents. Note that the responses have been translated into five categories, numbered from 1 to 5, based on where the respondent marked the line between each pair of adjectives. It is possible that respondents may have intentionally put a cross closer to one side of the box than the other, but it is acceptable to lose this nuance in the data, provided that the original data is not lost, and any further analysis could refer back to it.

## Table 9.3 Phone 1

<table><tr><td></td><td>1 2 3 4 5</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Annoying</td><td></td><td>3520</td><td></td><td></td><td></td><td>18 15 12 Pleasing</td></tr><tr><td>Easy to use</td><td></td><td></td><td></td><td></td><td></td><td>20 28 21 13 18 Difficult to use</td></tr><tr><td>Value-for-money 15 30 22 27 6 Expensive</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Attractive</td><td>37 22 326 3</td><td></td><td></td><td></td><td></td><td>Unattractive</td></tr><tr><td>Secure</td><td></td><td>52 29</td><td>12 4 3</td><td></td><td></td><td>Not secure</td></tr><tr><td>Helpful</td><td></td><td>33213</td><td></td><td></td><td></td><td>32 12 2 Unhelpful</td></tr><tr><td>Hi-tech</td><td></td><td></td><td></td><td></td><td></td><td>12 24 36 12 16 Lo-tech</td></tr><tr><td>Robust</td><td></td><td></td><td></td><td></td><td></td><td>44 13 15 16 12 Fragile</td></tr><tr><td>Inefficient</td><td></td><td></td><td></td><td></td><td></td><td>28 23 25 12 12 Efficient</td></tr><tr><td>Modern</td><td></td><td></td><td></td><td></td><td></td><td>35 27 20 11 7 Dated</td></tr></table>

Table 9.4 Phone 2
<table><tr><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">2</td><td colspan="1" rowspan="1">3</td><td colspan="1" rowspan="1">4 5</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Annoying</td><td colspan="1" rowspan="1">24</td><td colspan="1" rowspan="1">23</td><td colspan="1" rowspan="1">23</td><td colspan="1" rowspan="1">15</td><td colspan="1" rowspan="1">15</td><td colspan="1" rowspan="1">Pleasing</td></tr><tr><td colspan="1" rowspan="1">Easy</td><td colspan="1" rowspan="1">37</td><td colspan="1" rowspan="1">291</td><td colspan="1" rowspan="1">5</td><td colspan="1" rowspan="1">10</td><td colspan="1" rowspan="1">9</td><td colspan="1" rowspan="1">Difficult to use</td></tr><tr><td colspan="1" rowspan="1">Value-for-money</td><td colspan="1" rowspan="1">26</td><td colspan="1" rowspan="1">32 1</td><td colspan="1" rowspan="1">7 1</td><td colspan="1" rowspan="1">3 1</td><td colspan="1" rowspan="1">2 E</td><td colspan="1" rowspan="1">xpensive</td></tr><tr><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td></tr><tr><td>Attractive</td><td></td><td></td><td></td><td></td><td></td><td>38 21 29 8 4 Unattractive</td></tr><tr><td>Secure</td><td></td><td></td><td></td><td></td><td></td><td>43 22 19 12 4 Not secure</td></tr><tr><td>Helpful</td><td></td><td></td><td></td><td></td><td></td><td>51 19 16 12 2 Unhelpful</td></tr><tr><td>Hi-tech</td><td></td><td></td><td></td><td></td><td></td><td>28 12 30 18 12 Lo-tech</td></tr><tr><td>Robust</td><td></td><td></td><td></td><td></td><td></td><td>46 23 10 11 10 Fragile</td></tr><tr><td>Inefficient</td><td></td><td></td><td></td><td></td><td></td><td>10 6 37 29 18 Efficient</td></tr><tr><td>Modern</td><td></td><td></td><td></td><td></td><td></td><td>3 10 45 27 15 Dated</td></tr></table>

The graph in Figure 9.3 shows how the two smartphone designs varied according to the respondents' perceptions of how modern the design is. This graphical notation shows clearly how the two designs compare.

![](../../Interaction Design Beyond Human-Computer Interaction, Fifth Edition (Helen Sharp, Jenny Preece, Yvonne Rogers)/images/3f5661f063c8a0a3787eea0824dd022882a610317f8900de3e301e867a109a54.jpg)  
Figure 9.3 A graphical comparison of two smartphone designs according to whether they are perceived as modern or dated

Data logs that capture users' interactions automatically, such as with a website or smartphone, can also be analyzed and represented graphically, thus helping to identify patterns in behavior. Also, more sophisticated manipulations and graphical images can be used to highlight patterns in collected data.

## 9.4 Basic Qualitative Analysis

Three basic approaches to qualitative analysis are discussed in this section: identifying themes, categorizing data, and analyzing critical incidents. Critical incident analysis is a way to isolate subsets of data for more detailed analysis, perhaps by identifying themes or applying categories. These three basic approaches are not mutually exclusive and are often used in combination, for example, when analyzing video material critical incidents may first be identified and then a thematic analysis undertaken. Video analysis is discussed further in Box 9.3.

As with quantitative analysis, the first step in qualitative analysis is to gain an overall impression of the data and to start looking for interesting features, topics, repeated observations, or things that stands out. Some of these will have emerged during data gathering, and this may already have suggested the kinds of pattern to look for, but it is important to confirm and re-confirm findings to make sure that initial impressions don't bias analysis. For example, you might notice from the logged data of people visiting TripAdviser.com that they often look for reviews for hotels that are rated “terrible” first. Or, you might notice that a lot of respondents all say how frustrating it is to have to answer so many security questions when logging onto an online banking service. During this first pass, it is not necessary to capture all of the findings but instead to highlight common features and record any surprises that arise (Blandford, 2017).

For observations, the guiding framework used in data gathering will give some structure to the data. For example, the practitioner's framework for observation introduced in Chapter 8, “Data Gathering,” will have resulted in a focus on who, where, and what, while using the more detailed framework will result in patterns relating to physical objects, people's goals, sequences of events, and so on.

Qualitative data can be analyzed inductively, that is, extracting concepts from the data, or deductively, in other words using existing theoretical or conceptual ideas to categorize data elements (Robson and McCartan, 2016). Which approach is used depends on the data obtained and the goal of the study, but the underlying principle is to classify elements of the data in order to gain insights toward the study's goal. Identifying themes (thematic analysis) takes an inductive approach, while categorizing data takes a deductive approach. In practice, analysis is often performed iteratively, and it is common for themes identified inductively then to be applied deductively to new data, and for an initial, pre-existing categorization scheme, to be enhanced inductively when applied to a new situation or new data. One of the most challenging aspects of identifying themes or new categories is determining meaningful codes that are orthogonal (that is, codes which do not overlap). Another is deciding on the appropriate granularity for them, for example at the word, phrase, sentence, or paragraph level. This is also dependent on the goal of the study and the data being analyzed.

Whether an inductive or deductive approach is used, an objective is to produce a reliable analysis, that is, one that can be replicated by someone else if they were to use the same type of approach. One way to achieve this is to train another person to do the coding. When training is complete, both researchers analyze a sample of the same data. If there is a large discrepancy between the two analyses, either training was inadequate or the categorization is not working and needs to be refined. When a high level of reliability is reached between the two researchers, it can be quantified by calculating the inter-rater reliability. This is the percentage of agreement between the analyses of the two researchers, defined as the number of items of agreement, for example the number of categories or themes arising from the data that have been identified consistently by both researchers, expressed as a percentage of the total number of items examined. An alternative measure where two researchers have been used is Cohen's kappa, (κ), which considers the possibility that agreement has occurred due to chance (Cohen, 1960).

Using more sophisticated analytical frameworks to structure the analysis of qualitative data can lead to additional insights that go beyond the results of these basic techniques. Section 9.5 introduces frameworks that are commonly used in interaction design.

## BOX 9.3

## Analyzing Video Material

A good way to start a video analysis is to watch what has been recorded all the way through while writing a high-level narrative of what happens, noting down where in the video there are any potentially interesting events. How to decide which is an interesting event will depend on what is being observed. For example, in a study of the interruptions that occur in an open plan office, an event might be each time that a person takes a break from an ongoing activity, for instance, when a phone rings, someone walks into their cubicle, or email arrives. If it is a study of how pairs of students use a collaborative learning tool, then activities such as turn-taking, sharing of input devices, speaking over one another, and fighting over shared objects would be appropriate to record.

Chronological and video times are used to index events. These may not be the same, since recordings can run at different speeds from real time and video can be edited. Labels for certain routine events are also used, for instance lunchtime, coffee break, staff meeting, and doctor's rounds. Spreadsheets are used to record the classification and description of events, together with annotations and notes of how the events began, how they unfolded, and how they ended.

Video can be augmented with captured screens or logged data of people's interactions with a computer display, and sometimes transcription is required. There are various logging and screen capture tools available for this purpose, which enable interactions to be played back as a movie, showing screen objects being opened, moved, selected, and so on. These can then be played in parallel with the video to provide different perspectives on the talk, physical interactions, and the system's responses that occur. Having a combination of data streams can enable more detailed and fine-grained patterns of behavior to be interpreted (Heath et al., 2010).

## 9.4.1 Identifying Themes

Thematic analysis is considered an umbrella term to cover a variety of different approaches to examining qualitative data. It is a widely used analytical technique that aims to identify, analyze, and report patterns in the data (Braun and Clarke, 2006). More formally, a theme is something important about the data in relation to the study goal. A theme represents a pattern of some kind, perhaps a particular topic or feature found in the data set, which is considered to be important, relevant, and even unexpected with respect to the goals driving the study. Themes that are identified may relate to a variety of aspects: behavior, a user group, events, places or situations where those events happen, and so on. Each of these kinds of themes may be relevant to the study goals. For example, descriptions of typical users may be an outcome of data analysis that focuses on participant characteristics. Although thematic analysis is

described in this section on qualitative analysis, themes and patterns may also emerge from quantitative data.

After an initial pass through the data, the next step is to look more systematically for themes across participants' transcripts, seeking further evidence both to confirm and disconfirm initial impressions in all of the data. This more systematic analysis focuses on checking for consistency; in other words, do the themes occur across all participants, or is it only one or two people who mention something? Another focus is on finding further themes that may not have been noticed first time. Sometimes, the refined themes resulting from this systematic analysis form the primary set of findings for the analysis, and sometimes they are just the starting point.

The study's goal provides an orienting focus for the identification and formulation of themes in the first and subsequent passes through the data. For example, consider a survey to evaluate whether the information displayed on a train travel website is appropriate and sufficient. Several of the respondents suggest that the station stops in between the origin and destination stations should be displayed. This is relevant to the study's goal and would be reported as a main theme. In another part of the survey, under further comments you might notice that several respondents say the company's logo is distracting. Although this too is a theme in the data, it is not directly relevant to the study's goals and may be reported only as a minor theme.

Once a number of themes have been identified, it is usual to step back from the set of themes to look at the bigger picture. Is an overall narrative starting to emerge, or are the themes quite disparate? Do some seem to fit together with others? If so, is there an overarching theme? Can you start to formulate a meta-narrative, that is, an overall picture of the data? In doing this, some of the original themes may not seem as relevant and can be removed. Are there some themes that contradict each other? Why might this be the case? This can be done individually, but more often this is applied in a group using brainstorming techniques with sticky notes.

A common technique for exploring data, identifying themes, and looking for an overall narrative is to create an af inity diagram. The approach seeks to organize individual ideas and insights into a hierarchy showing common structures and themes. Notes are grouped together when they are similar in some fashion. The groups are not predefined, but rather they emerge from the data. This process was originally introduced into the software quality community from Japan, where it is regarded as one of the seven quality processes. The affinity diagram is built gradually. One note is put up first, and then the team searches for other notes that are related in some way.

Affinity diagrams are used in Contextual Design (Beyer and Holtzblatt, 1998; Holtzblatt, 2001), but they have also been adopted widely in interaction design (Lucero, 2015). For example, Madeline Smith et al. (2018) conducted interviews to design a web app for cowatching videos across a distance, and they used affinity diagramming to identify requirements from interviewee transcripts (see Figure 9.4). Despite the prevalence of digital collaboration tools, the popularity of physical affinity diagramming using sticky notes drawn by hand, has persisted for many years (Harboe and Huang, 2015).

![](../../Interaction Design Beyond Human-Computer Interaction, Fifth Edition (Helen Sharp, Jenny Preece, Yvonne Rogers)/images/5a4f170d92392f9317137e50b9f07b021bf3b02e9281fb9a5b34b375e15392cc.jpg)  
Figure 9.4 Section of an affinity diagram built during the design of a web application Source: Smith (2018). Used courtesy of Madeline Smith

To read more about the use of affinity diagrams in interaction design, see the following page:

https://uxdict.io/design-thinking-methods-affinity-diagrams-357bd8671ad4

## 9.4.2 Categorizing Data

Inductive analysis is appropriate when the study is exploratory, and it is important to let the themes emerge from the data itself. Sometimes, the analysis frame (the set of categories used) is chosen beforehand, based on the study goal. In that case, analysis proceeds deductively. For example, in a study of novice interaction designer behavior in Botswana, Nicole Lotz et al. (2014) used a set of predetermined categories based on Schön (1983)'s design and reflection cycle: naming, framing, moving, and reflecting. This allowed the researchers to identify detailed patterns in the designers' behavior, which provided implications for education and support.

To illustrate categorization, we present an example derived from a set of studies looking at the use of different navigation aids in an online educational setting (Ursula Armitage, 2004). These studies involved observing users working through some online educational material (about evaluation methods), using the think-aloud technique. The think-aloud protocol was recorded and then transcribed before being analyzed from various perspectives, one of which was to identify usability problems that the participants were having with the online environment known as Nestor Navigator (Zeiliger et al., 1997). An excerpt from the transcription is shown in Figure 9.5.

I'm thinking that it's just a lot of information to absorb from the screen. I just I don't concentrate very well when I'm looking at the screen. I have a very clear idea of what I've read so far … but it's because of the headings I know OK this is another kind of evaluation now and before it was about evaluation which wasn't anyone can test and here it's about experts so it's like it's nice that I'm clicking every now and then coz it just sort of organizes the thoughts. But it would still be nice to see it on a piece of paper because it's a lot of text to read.

Am I supposed to, just one question, am supposed to say something about what I'm reading and what I think about it the conditions as well or how I feel reading it from the screen, what is the best thing really?

Observer: What you think about the information that you are reading on the screen … you don't need to give me comments … if you think this bit fits together.

There's so much reference to all those previously said like I'm like I've already forgotten the name of the other evaluation so it said unlike the other evaluation this one like, there really is not much contrast with the other it just says what it is may be … so I think I think of …

Maybe it would be nice to have other evaluations listed to see other evaluations you know here, to have the names of other evaluations other evaluations just to, because now when I click previous I have to click it several times so it would be nice to have this navigation, extra links.

Figure 9.5 Excerpt from a transcript of a think-aloud protocol when using an online educational environment. Note the prompt from the observer about halfway through.

Source: Armitage (2004). Used courtesy of Ursula Armitage

This excerpt was analyzed using a categorization scheme derived from a set of negative effects of a system on a user (van Rens, 1997) and was iteratively extended to accommodate the specific kinds of interaction observed in these studies. The categorization scheme is shown in Figure 9.6.
