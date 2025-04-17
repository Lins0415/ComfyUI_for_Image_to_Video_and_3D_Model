This project is for image generate into video and 3d model by using ComfyUI. 

Requirement:

Recommended: PLEASE CREATE A NEW DISK DRIVE THAT CONTAIN AT LEAST 200GB TO DOWNLOAD THE COMFYUI FOLDER! (Don't save this inside your C drive.)

Notes: Of course, you don't have to follow my recommend if you have enough capacity on your C drive.
 
~~~The image to video only supports any GPU that has 8GB VRAM above.~~~
~~~The image to 3d model requires any GPU that has 4GB VRAM above.~~~

~~~Also, it supports Intel and AMD. ~~~
~~~You can use CUDA Environment if you have NVIDIA graphic card. (Run the environment on your powershell/cmd before you run the "python main.py" inside of the ComfyUI folder) ~~~

~~~If you do not have a "Git", please download it by using this link: https://git-scm.com/downloads

1. Please use powershell/cmd to download the ComfyUI folder that I posted, and make sure you save that ComfyUI folder in your new disk drive that you created.
2. Follow the instruction to download all the setup on the ComfyUI github link below.
3. Then download all the package inside of the requirements text file in ComfyUI folder.
4. After you complete, go to "custom_nodes" folder and download all the requirement package by using "pip install [package_name]" inside of each folder in "custom_nodes" folder.
5. After you done, go back to the main ComfyUI folder and run "python main.py" on your powershell/command.
6. While the coding script is running, you probably will see some packages haven't been install like "ModuleNotFoundError: No module named **'[package_name]'**". You can download the package inside of the ComfyUI folder by using "pip install [package name]".
7. After all the packages are downloaded, check the coding process to make sure there are no error occur.
8. Then, run the "python main.py" and it should be provided you a server link "http://127.0.0.1:8188".
9. Copy the server link and paste it on the browser, you should be able to see the ComfyUI platform.




Reference for ComfyUI: https://github.com/comfyanonymous/ComfyUI

Reference for image to video: 

1. https://github.com/Doubiiu/DynamiCrafter
2. https://github.com/kijai/ComfyUI-DynamiCrafterWrapper
3. https://huggingface.co/Doubiiu/DynamiCrafter_512_Interp

Reference for image to 3d model:

1. https://github.com/flowtyone/ComfyUI-Flowty-TripoSR
2. https://github.com/nsdtcloud3d/ComfyUI-3D-Convert
