This project is for image generate into video and 3d model by using ComfyUI. 

Requirement:

Recommended: PLEASE CREATE A NEW DISK DRIVE THAT CONTAIN AT LEAST 200GB TO DOWNLOAD THE COMFYUI FOLDER! (Don't save this inside your C drive.)

Notes: Of course, you don't have to follow my recommend if you have enough capacity on your C drive.
 
~~~The image to video only supports any GPU that has 8GB VRAM above.~~~
~~~The image to 3d model requires any GPU that has 4GB VRAM above.~~~

~~~Also, it supports Intel and AMD. ~~~
~~~You can use CUDA Environment if you have NVIDIA graphic card. (Run the environment on your powershell/cmd before you run the "python main.py" inside of the ComfyUI folder) ~~~



1. Please use powershell/cmd to download the ComfyUI folder that I posted, and make sure you save that ComfyUI folder in your new disk drive that you created.
    a. "git clone https://github.com/Lins0415/ComfyUI_for_Image_to_Video_and_3D_Model.git"
2. Follow the instruction to download all the setup on the ComfyUI github link below.

3. Then download all the package inside of the requirements text file in ComfyUI folder.

4. After you complete, go to "custom_nodes" folder and download all the requirement package by using "pip install [package_name]" inside of each folder in "custom_nodes" folder.

5. After you done, go back to the main ComfyUI folder and run "python main.py" on your powershell/command.

6. While the coding script is running, you probably will see some packages haven't been install like "ModuleNotFoundError: No module named **'[package_name]'**". You can download the package inside of the ComfyUI folder by using "pip install [package name]" on powershell command.

7. After all the packages are downloaded, check the coding process to make sure there are no error occur.

8. Then, run the "python main.py" and it should be provide you a server link "http://127.0.0.1:8188".

9. Copy the server link and paste it on the browser, you should be able to see the ComfyUI platform.

10. Download the two Models and save inside "ComfyUI_for_Image_to_Video_and_3D_Model\models\checkpoints".
    a. model.ckpt (This model is for image to 3d. You can download it in "https://github.com/flowtyone/ComfyUI-Flowty-TripoSR")
    b. tooncrafter_512_interp-pruned-fp16.safetensors (This model is for image to video. You can download it in "https://huggingface.co/Doubiiu/DynamiCrafter_512_Interp")

11. The another model that needs to be download and save inside "ComfyUI\models\vae".
    a. vae-ft-mse-840000-ema-pruned.ckpt (Here is the link: https://huggingface.co/stabilityai/sd-vae-ft-mse-original/blob/main/vae-ft-mse-840000-ema-pruned.ckpt)
    b. vae-ft-mse-840000-ema-pruned.safetensors (Here is the link: https://huggingface.co/stabilityai/sd-vae-ft-mse-original/blob/main/vae-ft-mse-840000-ema-pruned.safetensors)

12. Then go to "ComfyUI_for_Image_to_Video_and_3D_Model\allworkflow". You can see 3 workflows in there and you can open it on top left corner on the ComfyUI platform.
    a. tooncrafter_example_low_vram_01 (This workflow is for image to video.)
    b. imageto3dworkflow_simple (This workflow is for image to 3d.)
    c. stl3dformat (This workflow is for any 3d format convert into STL 3d format.)


~Please Review the ComfyUI References

Reference for ComfyUI: https://github.com/comfyanonymous/ComfyUI

Reference for image to video: 

1. https://github.com/Doubiiu/DynamiCrafter
2. https://github.com/kijai/ComfyUI-DynamiCrafterWrapper
3. https://huggingface.co/Doubiiu/DynamiCrafter_512_Interp

Reference for image to 3d model:

1. https://github.com/flowtyone/ComfyUI-Flowty-TripoSR
2. https://github.com/nsdtcloud3d/ComfyUI-3D-Convert
