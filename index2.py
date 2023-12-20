
# Import the required module for text  
# to speech conversion 
from gtts import gTTS 
  
# This module is imported so that we can  
# play the converted audio 
import os 
  
# The text that you want to convert to audio 
mytext = 'In the Colorado court’s lengthy ruling on Tuesday, the justices there reversed a Denver district judge’s finding last month that Section 3 did not apply to the presidency. They affirmed the district judge’s other key conclusions: that Mr. Trump’s actions before and on Jan. 6, 2021, constituted engaging in insurrection, and that courts had the authority to enforce Section 3 against a person whom Congress had not specifically designated.A majority of the court holds that President Trump is disqualified from holding the office of president under Section 3 of the 14th Amendment to the United States Constitution,” the justices wrote. “Because he is disqualified, it would be a wrongful act under the Election Code for the Colorado secretary of state to list him as a candidate on the presidential primary ballot.Mr. Trump’s campaign denounced the ruling, which is likely to inflame a Republican base that he has primed to see the array of civil and criminal cases against him as a witch hunt. Politically, his standing among Republican primary voters has only risen in the wake of the dozens of criminal charges against him.“Unsurprisingly, the all-Democrat appointed Colorado Supreme Court has ruled against President Trump, supporting a Soros-funded, left-wing group’s scheme to interfere in an election on behalf of Crooked Joe Biden by removing President Trump’s name from the ballot and eliminating the rights of Colorado voters to vote for the candidate of their choice,” a campaign spokesman, Steven Cheung, said. “We have full confidence that the U.S. Supreme Court will quickly rule in our favor and finally put an end to these un-American lawsuits.”Our politics reporters. Times journalists are not allowed to endorse or campaign for candidates or political causes. That includes participating in rallies and donating money to a candidate or cause.Learn more about our process.Similar lawsuits in Minnesota and New Hampshire were dismissed on procedural grounds. A judge in Michigan ruled last month that the issue was political and not for him to decide, and an appeals court affirmed the decision not to disqualify Mr. Trump there. The plaintiffs have appealed to the Michigan Supreme Court.'
  
# Language in which you want to convert 
language = 'en'
  
# Passing the text and language to the engine,  
# here we have marked slow=False. Which tells  
# the module that the converted audio should  
# have a high speed 
myobj = gTTS(text=mytext, lang=language, slow=False) 
  
# Saving the converted audio in a mp3 file named 
# welcome  
myobj.save("welcome.mp3") 
  
# Playing the converted file 
os.system("mpg321 welcome.mp3") 