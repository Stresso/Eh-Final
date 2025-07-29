import json
import sys
import glob
import os
import ollama
import time
import datetime 
def display_discord_messages(data):
    chat_lines = []  # Use a list to collect lines of output

    # Reverse the list to display messages in chronological order
    for message in reversed(data):
        author_info = message.get("author", {})
        author = author_info.get("global_name") or author_info.get("username", "Unknown Author")

        # Format timestamp
        timestamp_str = message.get("timestamp")
        try:
            timestamp = datetime.datetime.fromisoformat(timestamp_str).strftime('%Y-%m-%d %H:%M:%S')
        except (ValueError, TypeError):
            timestamp = "Invalid Time"

        content = message.get("content", "")
        msg_type = message.get("type", 0)

        # Replace user mentions with their global names
        for mention in message.get("mentions", []):
            mention_id = mention.get("id")
            global_name = mention.get("global_name", "Unknown User")
            content = content.replace(f"<@{mention_id}>", f"@{global_name}")

        if message.get("mention_everyone"):
            content = content.replace("@everyone", "@everyone")

        chat_lines.append("=" * 60)
        chat_lines.append(f"Author:    {author}")
        chat_lines.append(f"Timestamp: {timestamp}")

        if msg_type == 6:
            chat_lines.append("\n[System Message]: User pinned a message to this channel.")
        else:
            if content:
                chat_lines.append("\nContent:")
                chat_lines.append(f"  {content}")

        if message.get("embeds"):
            chat_lines.append("\nEmbeds:")
            for embed in message["embeds"]:
                title = embed.get("title", "No Title")
                description = embed.get("description", "No Description")
                url = embed.get("url")
                chat_lines.append(f"  - Title: {title}")
                chat_lines.append(f"    Description: {description}")
                chat_lines.append(f"    URL: {url}")

        if message.get("reactions"):
            chat_lines.append("\nReactions:")
            for reaction in message["reactions"]:
                emoji = reaction["emoji"]["name"]
                count = reaction["count"]
                chat_lines.append(f"  - {emoji} ({count})")

        chat_lines.append("=" * 60 + "\n")

    return "\n".join(chat_lines)  # Join all lines into a single string


def ollama_model(raw_file):
    try:
        with open(raw_file, 'r') as file:
            data = json.load(file)

        output = display_discord_messages(data)
        #print(output)  # Optional: print it
        client= ollama  
        with open(sys.path[0]+"/Response/output2.txt","w",encoding="utf-8") as f:
            f.write(output)
        model=[
        "cogito:8b",              
        #"phi4-reasoning:latest",  
        "starling-lm:latest",     
        "neural-chat:latest",     
        "mistral:latest",
        "deepseek-r1:latest"]  
        main="""Can you classify is this conversation is normal , suspicious or predatory , and mention what parts of the conversation is deemed predatory Jane Doe is out main suspect while John Doe is the victim, Keep in mind that Jane doe is an Adult."""
        prompt=f"{main} {output} "
        
        
        line=["-"]*100
        file_name=raw_file[:-4]+"_log_"+str(datetime.datetime.now()).replace(" ","_").replace(":","_").replace("-","_")[:-10]+".txt"
        for i in model:
            start=time.time()
            print(i+" Started\n" )
            resp=client.generate(model=i,prompt=prompt)
            with open(sys.path[0]+"/Response/"+file_name,"a") as f:
                f.write(i+"\n\n "+ resp.response + " \n\n\n")
                end=time.time()
                total=end-start
                f.write("".join(i for i in line) + "\n"+"completed in:"+str(total)+" seconds"+"\n\n")
            print(i+" Completed")
        print("Saved to "+sys.path[0]+"/Response/"+file_name)
    except json.JSONDecodeError:
        print("Error: Invalid JSON data provided.")

# Extract cache files
def extract_data():
    
    path=sys.path[0]
    print(path)
    os.system(".\extractfiles.bat")
    time.sleep(5)
    print("Extraction Done")
    os.system("mkdir Response")
    os.system("mkdir chat_only")
    files=dict()
    counter=0
    for i in glob.glob(os.path.abspath(f"{os.path.dirname(__file__)}/extracted/50*.json")):
        file_name=i.split("/")
        if file_name[-1] not in files.values():
            files[counter]=file_name[-1]
            os.system(rf'copy "{files[counter]}" "./chat_only"')
            counter+=1
    
    
    for i in files.keys():    
        ollama_model(files[i])

        
if __name__ == "__main__":
    extract_data()