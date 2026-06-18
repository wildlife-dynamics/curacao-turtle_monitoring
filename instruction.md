### 1\. Turtle Monitoring Workflow 

Workflow to analyse sea turtle nesting activity, nesting success, turtle-related field events, and fibropapillomatosis (FP) cases across sites. The report should be runnable by month, quarter, year, or any custom date range so it can feed both internal monitoring and the organisation's annual report. This report will use data from the following ER events:

**Dashboard / Report Features**

Headline stats:

* Stat card: total nesting events \- (suspected) Nest V2, Attempt V2, Dry Run V2  
* Stat card: total hatched eggs \- Total nr of hatched/empty egg shells from Hatching Data V2  
* Stat card: hatching success \- Total nr of hatched/empty egg shells ÷ Total numbers of eggs from Hatching Data V2.  
* Stat card: total turtle-related events \- Count of all records in Turtle Data Form V2 regardless of Activity Type value.  
* Stat card: total turtles with FP \- Count of records in Turtle Data Form V2 where Fibropapillomatosis \= Yes.

Nesting:

* Map: nesting activity by location  
  * (suspected)nest\_v2, relocation\_V2, Attempt\_V2  
* Line graph: nesting activity over time  
  * X-axis: Reported at (date) from nesting events. Series: Specie from (suspected) Nest V2.  
* Table: total nesting activity by beach  
  * Beach \- Beach dropdown field from (suspected) Nest V2, Attempt V2, Dry Run V2  
  * Suspected nest \- count of (suspected) Nest V2 events per beach  
  * Attempt \- count of Attempt V2 events per beach ⚠ Clarify if Attempts include Dry Runs  
  * Dry run \- count of Dry Run V2 events per beach  
  * Total \- sum of the above three  
* Table: nesting success by species and beach \- hatching data v2  
  * Species \- Specie dropdown (group-by)  
  * Beach \- Beach dropdown (group-by)  
  * Total eggs \- SUM of Total numbers of eggs  
  * Hatched eggs \- SUM of Total nr of hatched/empty egg shells  
  * Dead eggs \- SUM of Total nr of dead eggs  
  * Hatching success % \- Total nr of hatched/empty egg shells ÷ Total numbers of eggs × 100  
* Table: nesting success by nest manipulation \- hatching data v2  
  * Manipulation type \- Original Activity ID: 11th character \= S (Suspected), C (Confirmed), R (Relocated), or Surprise Nest flag.  
  * Total eggs \- SUM of Total numbers of eggs per manipulation type  
  * Hatched eggs \- SUM of Total nr of hatched/empty egg shells  
  * Dead eggs \- SUM of Total nr of dead eggs  
  * Hatching success % \- Total nr of hatched/empty egg shells ÷ Total numbers of eggs × 100

Turtle related events:

* Map: turtle-related events by location \- turtle data form v2  
* Table: overview of turtle-related events by location and activity  
  * Netting session \- count where Activity Type \= Netting session  
  * Rescue \- count where Activity Type \= Rescue  
  * Stranding \- count where Activity Type \= Stranding  
  * Nesting \- count where Activity Type \= Nesting  
  * Handcatch \- count where Activity Type \= Handcatch  
  * Release \- count where Activity Type \= Release  
  * Total \- sum of all activity types per location

Fibropapillomatosis (FP) Monitoring:

* Table: overview of FP turtles by location and activity \- Turtle Data Form V2 filtered where Fibropapillomatosis \= Yes  
  * Location \- Beach dropdown (group-by)  
  * Handcatch (with FP) \- count where Activity Type \= Handcatch AND Fibropapillomatosis \= Yes  
  * Stranding (with FP) \- count where Activity Type \= Stranding AND Fibropapillomatosis \= Yes  
  * Netting session (with FP) \- count where Activity Type \= Netting session AND Fibropapillomatosis \= Yes  
  * Number of turtles with FP \- unique count using Turtle\_number where Fibropapillomatosis \= Yes
