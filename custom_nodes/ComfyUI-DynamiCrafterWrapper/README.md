## DynamiCrafter wrapper nodes for ComfyUI

## Update2: Refactor

Changed lots of things to better integrate this to ComfyUI, you can (and have to) use clip_vision and clip models, but memory usage is much better and I was able to do 512x320 under 10GB VRAM.
New example workflows are included, all old workflows will have to be updated.

## Update: ToonCrafter
Initial ToonCrafter support with it's own node. 

VRAM required for 512x320 seems to be slightly under 15GB for sampling, and peaks to ~17GB at decoding. Dropping the resolution a bit can reduce the memory use a lot.

Decoding is the most memory hungry operation in all this, and currently REQUIRES XFORMERS for full quality results, however it is possible to use the standard Comfy VAE decoder for bit less quality but far less memory used.
The ToonCrafter model can also be used with the old Dynamicrafter I2V -node, quality then suffers a lot more, memory usage is halved, fitting under 8GB at best.

Fp8 option can also further reduce memory use by 1-2GB.

https://github.com/kijai/ComfyUI-DynamiCrafterWrapper/assets/40791699/96bf0902-40e6-42ad-beb9-a092f26c0458

# Installing
Either manager and install from git, or clone this repo to custom_nodes and run:

`pip install -r requirements.txt`

or if you use portable (run this in ComfyUI_windows_portable -folder):

`python_embeded\python.exe -m pip install -r ComfyUI\custom_nodes\ComfyUI-DynamiCrafterWrapper\requirements.txt`

Currently even if this can run without xformers, the memory usage is huge. Recommended to use xformers if possible:

`pip install xformers --no-deps`

or with portable:

`python_embeded\python.exe -m pip install xformers --no-deps`

UPDATE:
Converted the models to bf16 and .safetensors format here:
https://huggingface.co/Kijai/DynamiCrafter_pruned/tree/main

Models go to `ComfyUI/models/checkpoints` (can also be in subfolder, up to you)

If you want to use the original models, they are available here, they do need to be renamed to be used with the node:
Name this: `dynamicrafter_1024_v1.ckpt`
https://huggingface.co/Doubiiu/DynamiCrafter_1024

Interpolation model should be named: `dynamicrafter_512_interp_v1.ckpt`
https://huggingface.co/Doubiiu/DynamiCrafter_512_Interp/

With fp16 1024x576 uses bit under 10GB VRAM, and interpolation at 512p can be done with 8GB

Looping example:

https://github.com/kijai/ComfyUI-DynamiCrafterWrapper/assets/40791699/d1a83fac-d654-487f-a02e-be00509d38d5



Interpolation example:


https://github.com/kijai/ComfyUI-DynamiCrafterWrapper/assets/40791699/96251573-4b15-4d51-becd-daf8a1e5eab5


https://github.com/kijai/ComfyUI-DynamiCrafterWrapper/assets/40791699/156aeb21-4936-4e9a-a9b4-1767a8f6bbee






# ORIGINAL REPO:
https://github.com/Doubiiu/DynamiCrafter

## ___***DynamiCrafter: Animating Open-domain Images with Video Diffusion Priors***___
<!-- ![](./assets/logo_long.png#gh-light-mode-only){: width="50%"} -->
<!-- ![](./assets/logo_long_dark.png#gh-dark-mode-only=100x20) -->
<div align="center">
<img src='assets/logo_long.png' style="height:100px"></img>




 <a href='https://arxiv.org/abs/2310.12190'><img src='https://img.shields.io/badge/arXiv-2310.12190-b31b1b.svg'></a> &nbsp;
 <a href='https://doubiiu.github.io/projects/DynamiCrafter/'><img src='https://img.shields.io/badge/Project-Page-Green'></a> &nbsp;
<a href='https://huggingface.co/spaces/Doubiiu/DynamiCrafter'><img src='https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Demo-blue'></a> &nbsp;
<a href='https://youtu.be/0NfmIsNAg-g'><img src='https://img.shields.io/badge/Youtube-Video-b31b1b.svg'></a><br>
[![Open in OpenXLab](https://cdn-static.openxlab.org.cn/app-center/openxlab_app.svg)](https://openxlab.org.cn/apps/detail/JinboXING/DynamiCrafter)&nbsp;&nbsp;
<a href='https://replicate.com/camenduru/dynami-crafter-576x1024'><img src='https://img.shields.io/badge/replicate-Demo-blue'></a>&nbsp;&nbsp;
<a href='https://github.com/camenduru/DynamiCrafter-colab'><img src='https://img.shields.io/badge/Colab-Demo-Green'></a>&nbsp;<a href='https://huggingface.co/papers/2310.12190'><img src='https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Page-blue'></a>

_**[Jinbo Xing](https://doubiiu.github.io/), [Menghan Xia*](https://menghanxia.github.io), [Yong Zhang](https://yzhang2016.github.io), [Haoxin Chen](), [Wangbo Yu](), <br>[Hanyuan Liu](https://github.com/hyliu), [Xintao Wang](https://xinntao.github.io/), [Tien-Tsin Wong*](https://www.cse.cuhk.edu.hk/~ttwong/myself.html), [Ying Shan](https://scholar.google.com/citations?hl=en&user=4oXBp9UAAAAJ&view_op=list_works&sortby=pubdate)**_
<br><br>
(* corresponding authors)

From CUHK and Tencent AI Lab.

</div>
 
## 🔆 Introduction
🔥🔥 Generative frame interpolation / looping video generation model weights (320x512) have been released!

🔥 New Update Rolls Out for DynamiCrafter! Better Dynamic, Higher Resolution, and Stronger Coherence! <br>
🤗 DynamiCrafter can animate open-domain still images based on <strong>text prompt</strong> by leveraging the pre-trained video diffusion priors. Please check our project page and paper for more information. <br>
😀 We will continue to improve the model's performance.

👀 Seeking comparisons with [Stable Video Diffusion](https://stability.ai/news/stable-video-diffusion-open-ai-video-model) and [PikaLabs](https://pika.art/)? Click the image below.
[![](https://img.youtube.com/vi/0NfmIsNAg-g/0.jpg)](https://www.youtube.com/watch?v=0NfmIsNAg-g)


### 1.1. Showcases (576x1024)
<table class="center">
  <!-- <tr>
    <td colspan="1">"fireworks display"</td>
    <td colspan="1">"a robot is walking through a destroyed city"</td>
  </tr> -->
  <tr>
  <td>
    <img src=assets/showcase/firework03.gif width="340">
  </td>
  <td>
    <img src=assets/showcase/robot01.gif width="340">
  </td>
  </tr>

  <!-- <tr>
    <td colspan="1">"riding a bike under a bridge"</td>
    <td colspan="1">""</td>
  </tr> -->
  <tr>
  <td>
    <img src=assets/showcase/bike_chineseink.gif width="340">
  </td>
  <td>
    <img src=assets/showcase/girl07.gif width="340">
  </td>
  </tr>
</table>


### 1.2. Showcases (320x512)
<table class="center">
  <!-- <tr>
    <td colspan="1">"fireworks display"</td>
    <td colspan="1">"a robot is walking through a destroyed city"</td>
  </tr> -->
  <tr>
  <td>
    <img src=assets/showcase/bloom2.gif width="340">
  </td>
  <td>
    <img src=assets/showcase/train_anime02.gif width="340">
  </td>
  </tr>

  <!-- <tr>
    <td colspan="1">"riding a bike under a bridge"</td>
    <td colspan="1">""</td>
  </tr> -->
  <tr>
  <td>
    <img src=assets/showcase/pour_honey.gif width="340">
  </td>
  <td>
    <img src=assets/showcase/lighthouse.gif width="340">
  </td>
  </tr>
</table>




### 1.3. Showcases (256x256)

<table class="center">
  <tr>
    <td colspan="2">"bear playing guitar happily, snowing"</td>
    <td colspan="2">"boy walking on the street"</td>
  </tr>
  <tr>
  <td>
    <img src=assets/showcase/guitar0.jpeg_00.png width="170">
  </td>
  <td>
    <img src=assets/showcase/guitar0.gif width="170">
  </td>
  <td>
    <img src=assets/showcase/walk0.png_00.png width="170">
  </td>
  <td>
    <img src=assets/showcase/walk0.gif width="170">
  </td>
  </tr>


  <!-- <tr>
    <td colspan="2">"two people dancing"</td>
    <td colspan="2">"girl talking and blinking"</td>
  </tr>
  <tr>
  <td>
    <img src=assets/showcase/dance1.jpeg_00.png width="170">
  </td>
  <td>
    <img src=assets/showcase/dance1.gif width="170">
  </td>

  <td>
    <img src=assets/showcase/girl3.jpeg_00.png width="170">
  </td>
  <td>
    <img src=assets/showcase/girl3.gif width="170">
  </td>
  </tr> -->


  <!-- <tr>
    <td colspan="2">"zoom-in, a landscape, springtime"</td>
    <td colspan="2">"A blonde woman rides on top of a moving <br>washing machine into the sunset."</td>
  </tr>
  <tr>
  <td>
    <img src=assets/showcase/Upscaled_Aime_Tribolet_springtime_landscape_golden_hour_morning_pale_yel_e6946f8d-37c1-4ce8-bf62-6ba90d23bd93.mp4_00.png width="170">
  </td>
  <td>
    <img src=assets/showcase/Upscaled_Aime_Tribolet_springtime_landscape_golden_hour_morning_pale_yel_e6946f8d-37c1-4ce8-bf62-6ba90d23bd93.gif width="170">
  </td>

  <td>
    <img src=assets/showcase/Upscaled_Alex__State_Blonde_woman_riding_on_top_of_a_moving_washing_mach_c31acaa3-dd30-459f-a109-2d2eb4c00fe2.mp4_00.png width="170">
  </td>
  <td>
    <img src=assets/showcase/Upscaled_Alex__State_Blonde_woman_riding_on_top_of_a_moving_washing_mach_c31acaa3-dd30-459f-a109-2d2eb4c00fe2.gif width="170">
  </td>
  </tr>

  <tr>
    <td colspan="2">"explode colorful smoke coming out"</td>
    <td colspan="2">"a bird on the tree branch"</td>
  </tr>
  <tr>
  <td>
    <img src=assets/showcase/explode0.jpeg_00.png width="170">
  </td>
  <td>
    <img src=assets/showcase/explode0.gif width="170">
  </td>

  <td>
    <img src=assets/showcase/bird000.jpeg width="170">
  </td>
  <td>
    <img src=assets/showcase/bird000.gif width="170">
  </td>
  </tr> -->
</table >

### 2. Applications
#### 2.1 Storytelling video generation (see project page for more details)
<table class="center">
    <!-- <tr style="font-weight: bolder;text-align:center;">
        <td>Input</td>
        <td>Output</td>
        <td>Input</td>
        <td>Output</td>
    </tr> -->
  <tr>
    <td colspan="4"><img src=assets/application/storytellingvideo.gif width="250"></td>
  </tr>
</table >

#### 2.2 Generative frame interpolation

<table class="center">
    <tr style="font-weight: bolder;text-align:center;">
        <td>Input starting frame</td>
        <td>Input ending frame</td>
        <td>Generated video</td>
    </tr>
  <tr>
  <td>
    <img src=assets/application/gkxX0kb8mE8_input_start.png width="250">
  </td>
  <td>
    <img src=assets/application/gkxX0kb8mE8_input_end.png width="250">
  </td>
  <td>
    <img src=assets/application/gkxX0kb8mE8.gif width="250">
  </td>
  </tr>


   <tr>
  <td>
    <img src=assets/application/smile_start.png width="250">
  </td>
  <td>
    <img src=assets/application/smile_end.png width="250">
  </td>
  <td>
    <img src=assets/application/smile.gif width="250">
  </td>
  </tr>
  <tr>
  <td>
    <img src=assets/application/stone01_start.png width="250">
  </td>
  <td>
    <img src=assets/application/stone01_end.png width="250">
  </td>
  <td>
    <img src=assets/application/stone01.gif width="250">
  </td>
  </tr> 
</table >

#### 2.3 Looping video generation
<table class="center">

  <tr>
  <td>
    <img src=assets/application/60.gif width="300">
  </td>
  <td>
    <img src=assets/application/35.gif width="300">
  </td>
  <td>
    <img src=assets/application/36.gif width="300">
  </td>
  </tr>
  <!-- <tr>
  <td>
    <img src=assets/application/05.gif width="300">
  </td>
  <td>
    <img src=assets/application/25.gif width="300">
  </td>
  <td>
    <img src=assets/application/34.gif width="300">
  </td>
  </tr> -->
</table >





## 📝 Changelog
- __[2024.03.14]__: 🔥🔥 Release generative frame interpolation and looping video models (320x512).
- __[2024.02.05]__: Release high-resolution models (320x512 & 576x1024).
- __[2023.12.02]__: Launch the local Gradio demo.
- __[2023.11.29]__: Release the main model at a resolution of 256x256.
- __[2023.11.27]__: Launch the project page and update the arXiv preprint.
<br>


## 🧰 Models

|Model|Resolution|GPU Mem. & Inference Time (A100, ddim 50steps)|Checkpoint|
|:---------|:---------|:--------|:--------|
|DynamiCrafter1024|576x1024|18.3GB & 75s (`perframe_ae=True`)|[Hugging Face](https://huggingface.co/Doubiiu/DynamiCrafter_1024/blob/main/model.ckpt)|
|DynamiCrafter512|320x512|12.8GB & 20s (`perframe_ae=True`)|[Hugging Face](https://huggingface.co/Doubiiu/DynamiCrafter_512/blob/main/model.ckpt)|
|DynamiCrafter256|256x256|11.9GB  & 10s (`perframe_ae=False`)|[Hugging Face](https://huggingface.co/Doubiiu/DynamiCrafter/blob/main/model.ckpt)|
|DynamiCrafter512_interp|320x512|12.8GB & 20s (`perframe_ae=True`)|[Hugging Face](https://huggingface.co/Doubiiu/DynamiCrafter_512_Interp/blob/main/model.ckpt)|


Currently, our DynamiCrafter can support generating videos of up to 16 frames with a resolution of 576x1024. The inference time can be reduced by using fewer DDIM steps.

GPU memory consumed on RTX 4090 reported by @noguchis in [Twitter](https://x.com/noguchis/status/1754488826016432341?s=20): 18.3GB (576x1024), 12.8GB (320x512), 11.9GB (256x256).
<!-- It takes approximately 10 seconds and requires a peak GPU memory of 20 GB to animate an image using a single NVIDIA A100 (40G) GPU. -->

## ⚙️ Setup

### Install Environment via Anaconda (Recommended)
```bash
conda create -n dynamicrafter python=3.8.5
conda activate dynamicrafter
pip install -r requirements.txt
```


## 💫 Inference
### 1. Command line
### Image-to-Video Generation
1) Download pretrained models via Hugging Face, and put the `model.ckpt` with the required resolution in `checkpoints/dynamicrafter_[1024|512|256]_v1/model.ckpt`.
2) Run the commands based on your devices and needs in terminal.
```bash
  # Run on a single GPU:
  # Select the model based on required resolutions: i.e., 1024|512|320:
  sh scripts/run.sh 1024
  # Run on multiple GPUs for parallel inference:
  sh scripts/run_mp.sh 1024
```

### Generative Frame Interpolation / Looping Video Generation
Download pretrained model DynamiCrafter512_interp and put the `model.ckpt` in `checkpoints/dynamicrafter_512_interp_v1/model.ckpt`.
```bash
  sh scripts/run_application.sh interp # Generate frame interpolation
  sh scripts/run_application.sh loop   # Looping video generation
```


### 2. Local Gradio demo
### Image-to-Video Generation
1. Download the pretrained models and put them in the corresponding directory according to the previous guidelines.
2. Input the following commands in terminal (choose a model based on the required resolution: 1024, 512 or 256).
```bash
  python gradio_app.py --res 1024
```

### Generative Frame Interpolation / Looping Video Generation
Download the pretrained model and put it in the corresponding directory according to the previous guidelines.
```bash
  python gradio_app_interp_and_loop.py 
```

Community Extensions for Image-to-Video: [ComfyUI](https://github.com/chaojie/ComfyUI-DynamiCrafter) (Thanks to [chaojie](https://github.com/chaojie)).


## 👨‍👩‍👧‍👦 Crafter Family
[VideoCrafter1](https://github.com/AILab-CVC/VideoCrafter): Framework for high-quality video generation.

[ScaleCrafter](https://github.com/YingqingHe/ScaleCrafter): Tuning-free method for high-resolution image/video generation.

[TaleCrafter](https://github.com/AILab-CVC/TaleCrafter): An interactive story visualization tool that supports multiple characters.  

[LongerCrafter](https://github.com/arthur-qiu/LongerCrafter): Tuning-free method for longer high-quality video generation.  

[MakeYourVideo, might be a Crafter:)](https://doubiiu.github.io/projects/Make-Your-Video/): Video generation/editing with textual and structural guidance.

[StyleCrafter](https://gongyeliu.github.io/StyleCrafter.github.io/): Stylized-image-guided text-to-image and text-to-video generation.
## 😉 Citation
```bib
@article{xing2023dynamicrafter,
  title={DynamiCrafter: Animating Open-domain Images with Video Diffusion Priors},
  author={Xing, Jinbo and Xia, Menghan and Zhang, Yong and Chen, Haoxin and Yu, Wangbo and Liu, Hanyuan and Wang, Xintao and Wong, Tien-Tsin and Shan, Ying},
  journal={arXiv preprint arXiv:2310.12190},
  year={2023}
}
```

## 🙏 Acknowledgements
We would like to thank [AK(@_akhaliq)](https://twitter.com/_akhaliq?lang=en) for the help of setting up hugging face online demo, and [camenduru](https://twitter.com/camenduru) for providing the replicate & colab online demo.

## 📢 Disclaimer
We develop this repository for RESEARCH purposes, so it can only be used for personal/research/non-commercial purposes.
****
