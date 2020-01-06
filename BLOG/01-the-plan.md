#  The Plan, part 1:
## How we're going to get this thing rolling

_January 6, 2020_

### Technological components of the project

Broadly, the first iteration of this is going to be a machine learning model that ranks a set of submissions by similarity to an existing corpus of works. That means I need to build the following components:

**1. A normalized corpus, and a way to update that corpus when changes need to be made.** 

Fortunately, [someone else](https://www.kaggle.com/tgdivy/poetry-foundation-poems) went ahead and did the hard work of scraping and cleaning the entire database of poems from the [Poetry Foundation](https://www.poetryfoundation.org/) website. So this is a pretty good starting point for the first iteration of the software/first issue of the magazine. For this reason the first issue will use a training set of only poetry, but I plan to continue to update the seed corpus with other kinds of works as the project grows. 

As for the second part of this requirement, a way to easily update the corpus, for now it's good old fashioned elbow grease and mouse clicking. Let's consider a programmatic way of doing this my [first feature request](https://github.com/hilarybrennan/ubiquitous-spoon/issues/1) to myself.

**2. A feature extractor to be used on both the training corpus and eventually the submissions.**

For those of you who are unfamiliar with machine learning and how it works at a high level, a _feature_ is essentially an information-having bit of data the model can assign some kind of statistical weight to. For those of us who aren't mathemeticians making vast improvements to core algorithms, _feature Engineering_  is the bulk of most machine learning projects. Which is to say - deciding what to measure and how to measure it. For example, if we're building a model that is intended to identify which records in our data set are cats and which are dogs, we almost certainly want to include infomation about size - this is an important, information-having feature to our data set. Information about whether or not the animal in question has fur is probably not as important for the problem our model is trying to solve. 

I have spent a lot of time brainstorming possible features for categorizing poetry - one interesting problem that I invite the community to weigh in on, for example, is how to represent scansion in a binary vector - but its a rabbit hole and I'd like to get an issue out as soon as possible, so the first iteration of the feature extractor will represent each of the following features in a binary vector:
- Number of words in a record
- Number of lines in a record
- Number of stanzas in a record
- Longest line length
- Shortest line length
- [One-hot](https://jjallaire.github.io/deep-learning-with-r-notebooks/notebooks/6.1-one-hot-encoding-of-words-or-characters.nb.html) representation of words present in a given record.
THIS IS VERY SIMPLE. Overly simple, in fact. That is by design. If you have ideas for features and how to encode them, please, please, please [file a feature request](https://github.com/hilarybrennan/ubiquitous-spoon/issues/new)!

>**A quick note about the inherent problem of a training set:**
>As data scientists we encounter over and over again the problem of choosing a training set. [Every time we decide to measure a thing, we make a judgement.](https://github.com/hilarybrennan/ubiquitous-spoon/issues/2) **Every time.** A really good example of this problem is the phenomenon of [recidivism scores' being inherently racist and awful.](https://www.businessinsider.com/racial-bias-in-criminal-courts-2017-1) Those of us who are interested in using data to discover truths about our world need to constantly confront this problem, and this project is no different.
>
>The whole point of this project is that it is exploratory in nature - we want to _see what happens_ when we try to digitize a general sense of _goodness_ when it comes to an art object. In the case of the first iteration of this project we're using a generally-accepted, English-focused, Academy-accepted established notion of what makes a _good_ poem - the body of work that our friends at the Poetry Foundation have deemed publishable. Obviously, this is a problematic starting point - _and that's the point._ Our hope is to use this project to explore this problem in a way that is interesting and enjoyable for like-minded readers of literature and data.

**3. A Model:**

The model we are going to use will basically be a ranking system to determine which records in a data set (the submissions) are most similar to the records in the training set (the Poetry Foundation Corpus). I will write a more detailed post on the ins and outs of the model itself when I get around to training it, but suffice for now to say that each submission will be given a similarity score in relation to all the other submissions in a given run, and the top X submissions will be selected for publication. 

### The submission and selection process

As I explained above, the first version of this is going to be a simple ranking system. That means that rather than running a single submission through the model and having it classify as either "yes" or "no", we will run the entire set of submission through the system and have the model rank them in camparison to one another. That means we will need to collect a large number of submissions up-front and treat them as their own corpus. 

I have **no idea** how much interest there will be from either the poetry writing or the poetry reading community, so there are a lot of details up in the air about submission, selection, and publication. But for now the plan is to solicit submissions for a set period of time, run then entire submission corpus at the end of that time period, and publish either a specific number of poems or a specific percentage of submissions (depending on how many submissions we receive) in a physical journal as well as online. 
