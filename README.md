# Udacity Data Science Nano Degree - Starbuck's Capstone Challenge

The Starbucks Udacity Data Scientist Nanodegree Capstone challenge data set is a simulation of customer behavior on the Starbucks rewards mobile application. Periodically, Starbucks sends offers to users that may be an advertisement, discount, or buy one get on free (BOGO). An important characteristic regarding this dataset is that not all users receive the same offer.

**Link to the blog post @ [vasthav.com](https://vasthav.com/posts/udacity-dsnd-starbucks-capstone-project/)**

# Starbuck's Capstone Challenge

## Dataset overview
The data spread across three different files. It is a dummy data, on the Starbuck mobile app, to simulate how different promotional offers impact user interaction and decisions. There are three types of offers as per the data set: buy-one-get-one (BOGO), discount, and informational - all of which are delivered over multiple channels. The main task is to identify different segments of users based on their identifiable feature (like age, income, transaction patterns etc) to offer better targeted promotional offers. Also finding other patterns and trends like the impact of each offers on the different segments of users etc.

### Data Dictionary
 - profile.json - Rewards program users (17000 users x 5 fields)
   - gender: (categorical) M, F, O, or null
   - age: (numeric) missing value encoded as 118
   - id: (string/hash)
   - became_member_on: (date) format YYYYMMDD
   - income: (numeric)
  
 - portfolio.json - Offers sent during 30-day test period (10 offers x 6 fields)
   - reward: (numeric) money awarded for the amount spent
   - channels: (list) web, email, mobile, social
   - difficulty: (numeric) money required to be spent to receive reward
   - duration: (numeric) time for offer to be open, in days
   - offer_type: (string) bogo, discount, informational
   - id: (string/hash)

 - transcript.json - Event log (306648 events x 4 fields)
   - person: (string/hash)
   - event: (string) offer received, offer viewed, transaction, offer completed
   - value: (dictionary) different values depending on event type
   - offer id: (string/hash) not associated with any "transaction"
   - amount: (numeric) money spent in "transaction"
   - reward: (numeric) money gained from "offer completed"
   - time: (numeric) hours after start of test
   
# Motivation 
The problem that I chose to solve was to build a set of heuristics to help decide what offers works best for certain age and gender demographics. I chose a simple approach where the users who converted (completed offer) were analysed based on gender, age, and income bracket. 

At the end we create two user list, one of top user's user id list and the second user id list of potential customers based on transaction behavior, which can be used in re-marketing different products. And given the marketing cost these lists are helpful to target other products to true fans (First list) and use more offers to capture more revenue from the potential users (second list).

# Observations
Based on the analysis we observed that
- Average user transactions count is 8.38
- Average user age 62 years
- Average user income 57000 unit.

Top three two age brackets and gender groups that result in highest number of transactions and in turn revenue are:
- 60+ Male, 60+ Female
- 50-59 Male, 50-59 Female
- 40-49 Male, 40-49 Female

There is not much difference in income gap between the users who transact based on their age, and gender groups.

Highest offer completion rate is for the offer: fafdcd668e3743c1bb461111dcafc2a4 (~82%).

We should send this offer more.
Top Three offers -
1. fafdcd668e3743c1bb461111dcafc2a4
2. 2298d6c36e964ae4a3e7e9706d1fb8c2
3. f19421c1d4aa40978ebb69ca19b0e20d 

We should send these more in general.

The below mentioned offers didn't result in any conversion. We should stop sending these particular offer.
- 5a8bc65990b245e5a138643cd4eb9837
- 3f207df678b143eea3cee63160fa8bed

See the offer-wise metrics and observations in the iPython Notebook.

NOTE:
- We have also created top converting user list (total Ids 3941). 
  - These users are like 1000 true fans. 
  - They enjoy the product & we need not send offers to them.
- We have also created least converting user list (total Ids 4037). 
  - These users have converted but has potential to convert more. 
  - These user ids can be used for re-marketing by offering better offers so that they convert more.

_Next steps include building a simple machine learning model to predict the users who has high chance of conversion (completing the offers) based on offer viewed and completed data._

# Libraries Used
- pandas v0.23.3 
- numpy v1.12.1 
- matplotlib v2.1.0

# Licensing and Acknowledgements
This data set used for training is provided by Udacity and Starbucks. This repository is given under the MIT license. A copy of the license can be found at [here](https://raw.githubusercontent.com/vasthav/Udacity-DSND-Capstone_project-Starbucks/master/LICENSE).
