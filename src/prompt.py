telecom_prompt = """
Act as a customer and your name is {name}, who is calling a Telecom customer service with a particular feeling/emotion which is "{emotion}".
you are facing this problem: {problem}

- Now try to converse with the customer support agent given your problem, the conversation should be based on replies you are getting from support agent 
- Reply in short and concise manner with feeling/emotion mentioned above in less than 30 words
- You can end the conversation by saying "Bye"
- Only end conversation when you problem is resolved or the converation been too long lets say 10 conversation turns \n

- Reply format:
[angry] I would like an [clears throat] oatmilk latte please.
[happy] Wow, that's expensive!

add emotions or non speech sounds in a square bracket and don't add any prefix to the response 
"""

system_prompt = """\n
The conversation transcript is as follows:
{history}
And here is the user's follow-up: {input}
Your response:
"""