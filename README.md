I have created a discord bot which uses stable diffusion running on your local computer to generate images in discord. 

Pre requisites:
  1.1 : Installing confyUI
  You need to have python 3.10 and git isntalled on your device before you can use above stable diffusion confyUI suite(NOTE: it is important that you have python 3.10 and not any other version)
  Download confyUI suite here https://github.com/comfyanonymous/ComfyUI/releases/download/latest/ComfyUI_windows_portable_nvidia_cu121_or_cpu.7z 
  Once you download the zip file and extract, you will see directory structure like following(I have omitted some directories in following structure as those are not required at the moment):

                                                        -------------------------DIRECTORY STRUCTURE 1-------------------------

                                                          CondyUI_windows_portable/
                                                                              - ConfyUI/
                                                                                        - custom_nodes/
                                                                                        - models/
                                                                                              - checkpoints/
                                                                              - run_cpu.bat
                                                                              - run_nvidia_gpu.bat
                                                                              
  Download stable diffusion checkpoint(s) from civitai or huggingface and put them in checkpoints/ directory. The path to 'checkpoints' directory is shown in DIRECTORY STRUCTURE 1
            Here are some good checkpoints that I prefer:
            
                                                a. animerge_v24.safetensors
                                                b. realcartoon3d_v11.safetensors
                                                c. majicmixLux_v2.safetensors
                                                d. majicmixRealistic_v7.safetensors
                                                e. visualnovel_v1.safetensors
                                                
  Download confyUI manager as it will help you to automatically install missing custom nodes. Here is the link to confyUI manager: https://github.com/ltdrdata/ComfyUI-Manager
      Instructions to download confyUI manager:
      
                                  a. cd custom_nodes       #It is equivalent to going to the custom_nodes directory and opening cmd or terminal there (relative path to custom_nodes is shown in DIRECTORY STRUCTURE 1)
                                  b. git clone https://github.com/ltdrdata/ComfyUI-Manager.git   #paste this command in terminal and hit enter
  
  Now click on run_nvidia_gpu.bat and if everything goes according to plan, which it should, then you will find yourself using confyUI( it will take few minutes in the beginning to open up, so wait patiently)
  There are many tutorials on youtube as to how to generate images. I won't explain it all here as my point is to help you se up a bot for discord. But keep the confyUI running
  
Cloning my repo & configuring confyUI:
  Clone my repo anywhere outside the confyUI directories. Just open some drive on your PC/laptop and open up a terminal/cmd. then, paste following link and hit enter: git clone https://github.com/0001ashish/imagine_ai.git
  Once you clone my repo, you will see following directory structure:


                                             ------------------------DIRECTORY STRUCTURE 2-----------------------
                                                                     
                                                                      workflows/
                                                                              - workflow_api.json
                                                                      output/
                                                                      credentials/
                                                                              - credentials.json
                                                                      prompts.csv
                                                                      bot_slash.py
                                                                      main.py
                                                                      requirements.txt
                                                                      .gitignore

Once again, go to the confyUI and do the following:
            1. You should see a load button there in confyUI. Click on it and upload workflow_api.json. The 'workflow_api.json' is present in my repo as shown in above DIRECTORY STRUCTURE 2.
            2. You will see some red nodes, but don't worry, that's what confyUI manager was installed for ! just click on confyUI manager and then click on install missing custom nodes
            NOTE: It may take some time as it would download dependencies and all for all the nodes required in my workflow that were previously missing. Once done, it will show a restart button at bottom, Don't forget to hit it
            3. Once restarted, try creating one image. click on queue button and wait for the image. If you see an image there, then we are ready to go !

            
    

  
