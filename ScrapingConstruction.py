import twint
import nest_asyncio
nest_asyncio.apply()

# Configure
c = twint.Config()
#c.Limit = 100
c.Since = '2021-01-01'
a = input("KeyWord:    ")
c.Search = a

c.Pandas = True
c.Filter_retweets = True

# Run
twint.run.Search(c)

#Save to pandas
Tweets_df = twint.storage.panda.Tweets_df

Custom_df = Tweets_df[['date', 'tweet', 'link', 'urls']]
Custom_df.to_excel('/home/basanagoudasomanakatti/ScrapingConstructionProjects/'+a+'.xlsx')