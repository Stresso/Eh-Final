The following is my Ethical Hacking and Cyber secirity MS Project aimed as a forensic tool to analyze Discord chats.

Once downloaded , running the main.py , assuming Discord is installed on the system will extract all the cache files present on the system and store them in a directory called "extracted"
The program then will copy the chat logs to a new directory called "chat_only" for easy access.

the program will format the extracted chat and then make use of ollama and its models to classify the chats as "predetory" , "suspecious" or "normal" conversations.

Extracted.bat exists only because running chromeCacheView via python caused errors
