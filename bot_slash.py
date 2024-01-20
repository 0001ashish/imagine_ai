import discord
# from config import TOKEN
from discord import app_commands
from discord.ext import commands
import requests
import os
import time
import json
import threading
import csv

bat_directory = "D:\\new_ComfyUI_windows_portable_nvidia_cu121_or_cpu\\ComfyUI_windows_portable"
bat_file_path = "D:\\new_ComfyUI_windows_portable_nvidia_cu121_or_cpu\\ComfyUI_windows_portable\\run_nvidia_gpu.bat"
workflow_directory = "E:\\discord_bot\\workflows\\"
workflow_file = "workflow_api.json"
workflow_path = workflow_directory+workflow_file

def run_bat_file():
    # Change the working directory to the .bat file location
    os.chdir(bat_directory)
    # Execute the .bat file
    os.system(bat_file_path)

URL = "http://127.0.0.1:8188/prompt"
OUTPUT_DIR = "E:\\discord_bot\\output"

def get_latest_image(folder):
    files = os.listdir(folder)
    image_files = [f for f in files if f.lower().endswith(('.png','.jpg','.jpeg'))]
    image_files.sort(key=lambda x:os.path.getmtime(os.path.join(folder,x)))
    latest_image =  os.path.join(folder, image_files[-1]) if image_files else None
    print(latest_image)
    return latest_image
def start_queue(prompt_workflow):
    p = {"prompt":prompt_workflow}
    data = json.dumps(p).encode("utf-8")
    requests.post(URL,data=data)
thread = threading.Thread(target=run_bat_file)
thread.start()

with open("E:\discord_bot\credentials\credentials.json", 'r') as file:
    # Load the JSON data
    data = json.load(file)
TOKEN = data["token"]

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())
@bot.event
async def on_ready():
    print("Bot is up and ready!")
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} command(s)")
    
    except Exception as e:
        print(e)

# @bot.tree.command(name="imagineai")
# async def imagineai(interaction: discord.Interaction):
#     await interaction.response.send_message(f"Hey {interaction.user.mention} ! this is imagineai",ephemeral=True)
#     print("Interaction:", interaction)
@bot.tree.command(name="imagineai")
# @app_commands.describe(arg="What should I say?")
async def imagineai(interaction: discord.Interaction, arg: str):
    prompt = interaction.data['options'][0]['value'] if 'options' in interaction.data and interaction.data['options'] else None
    with open("E:\discord_bot\prompts.csv", 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([prompt])
    # await interaction.response.send_message(f"{interaction.user.name} said: {arg}")
    # print("Interaction:", interaction)
    # print("Argument Value:", argument_value)
    # print("Interaction type:", interaction.type)
    # print("Interaction ID:", interaction.id)
    # print("User ID:", interaction.user.id)
    # print("User Name:", interaction.user.name)
    # print("Guild ID (if applicable):", interaction.guild.id if interaction.guild else None)
    # print("Attributes and methods of the Interaction object:", dir(interaction))
    print("PROMPT:",prompt,"prompttype:",type(prompt))
    # Add more attributes as needed
    workflow=''
    with open(workflow_path, "r") as file_json:
        workflow = json.load(file_json)
        workflow["6"]["inputs"]["text"] = prompt
        
        with open(workflow_path,"w") as json_file:
            json.dump(workflow,json_file, indent=2)

    previous_image = get_latest_image(OUTPUT_DIR)
    start_queue(workflow)
    while get_latest_image(OUTPUT_DIR)==previous_image:
        try:
            time.sleep(3)
        except Exception as e:
            print(e)
        continue
    
    image_path = get_latest_image(OUTPUT_DIR) 
    
    # Send the image to the Discord channel
    channel = bot.get_channel(interaction.channel_id)
    if channel:
        with open(image_path, 'rb') as image_file:
            image_data = discord.File(image_file)
            await channel.send(file=image_data)
    else:
        print("Error: Channel not found.")


bot.run(TOKEN)