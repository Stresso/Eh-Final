import random
import time
import sys
import requests
url_chat="https://discord.com/api/v9/channels/1396802712481566720/messages"

JaneDoe="MTM4MDQ4ODEyNDE1MjY4MDQ1OA.GHkKrU.lTUR52p7hPAKmBTDPlmWCIWsb6N-bCeBXQCXdI"
JohnDoe="MTM4MDQ4MDcyMDc1NzA2MzcxMQ.Gr89Am.5IamAibUDLjQxp_tchxAQGN1BW6wWR6spPeGD0"
payload= {
    "content":"e"
}
Jane_doe_header={
    "Authorization":"MTM4MDQ4ODEyNDE1MjY4MDQ1OA.GHkKrU.lTUR52p7hPAKmBTDPlmWCIWsb6N-bCeBXQCXdI",
}
John_doe_header={
    "Authorization":"MTM4MDQ4MDcyMDc1NzA2MzcxMQ.Gr89Am.5IamAibUDLjQxp_tchxAQGN1BW6wWR6spPeGD0",
}

# A conversation between John and Jane Doe on a Monday morning in July.
# A suspicious conversation between John and Jane Doe.
jane_doe = [
    "Are you absolutely certain no one followed you here?",
    "It just feels exposed. Too many dog walkers. So, is everything ready?",
    "And the client? Have you heard from them again?",
    "That's what worries me. Impatient people make mistakes. What about the route?",
    "The M77 is always busy. So many cameras. It feels like a risk.",
    "And the payment? You're sure it's secure?",
    "What happens if there's a problem? What's the contingency?",
    "That's easy for you to say. You're not the one making the delivery.",
    "Yes... lovely weather for it.",
    "So, what's the final instruction? When does this happen?",
    "And he'll be alone? You're positive?",
    "I don't like it. There are too many variables.",
    "What's the signal? The same as last time?",
    "I need to know you've thought of everything, John.",
    "Alright. I'll be ready."
]

john_doe = [
    "Relax, Jane. I was careful. Just act normal, like we're just enjoying the park.",
    "The package is secure. It's ready for transit tonight, exactly as planned.",
    "They're getting impatient. They want it concluded by midnight.",
    "It's the fastest way. No one expects you to use the main roads. It's hiding in plain sight.",
    "It's a calculated risk. It's better than winding through side streets where we'd stand out.",
    "Half has been transferred to the usual account. The other half arrives on completion. It's all confirmed.",
    "There won't be a problem. You just stick to the plan. Don't deviate.",
    "It has to be you. Your car is clean, nobody knows who you are. Just a normal person out for a drive.",
    "Yes, perfect for a walk. Did you see the roses near the pond?",
    "Tonight. 11:45 PM. You leave the house. You don't stop for anything. You go directly to the arranged spot.",
    "That was the arrangement. He has as much to lose as we do. He'll be alone.",
    "It's happening. It's too late to back out now. Just focus on the task.",
    "Yes. The porch light. If it's on, we're good to go. If it's off, you turn around and come straight back.",
    "I have. Now go home. Act normal. Don't speak to anyone. I'll see you afterwards.",
    "I know you will be."
]

for i in range(len(jane_doe)):
    #send Jane Doe message
    content=jane_doe[i]
    payload= {
    "content":content
}
    res=requests.post(url=url_chat,json=payload,headers=Jane_doe_header)
    time.sleep(1)
    #send John Doe's message
    content=john_doe[i]
    payload= {
    "content":content
}
    res=requests.post(url=url_chat,json=payload,headers=John_doe_header)
